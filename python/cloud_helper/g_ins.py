#!/usr/bin/python
import sys
import subprocess
import re
import time
from collections import OrderedDict
from tabulate import tabulate
from time import gmtime, strftime
import fileinput
import sys

# table_str like the below
# NAME      ZONE        MACHINE_TYPE   PREEMPTIBLE  INTERNAL_IP  EXTERNAL_IP  STATUS
# g-test    us-east1-d  f1-micro                    10.142.0.4                TERMINATED
# g-test-2  us-east1-d  f1-micro                    10.142.0.5                TERMINATED
def parse_table_str(table_str):
    lines = table_str.split("\n")
    lines = filter(lambda x: x!="", lines)
    if len(lines) == 0:
        return None
    if len(lines) == 1:
        return []
    split_re = re.compile("\s+")
    header_line = lines[0]
    header_fields = split_re.split(header_line)
    pos_list = map(header_line.index, header_fields)
    def handle_record(record_str):
        cur_pos_list = pos_list + [len(record_str)]
        values = [record_str[pos_list[i]:cur_pos_list[i+1]].strip() for i in range(len(pos_list))]
        return OrderedDict(zip(header_fields,values))
    hash_list = map(handle_record, lines[1:])
    return hash_list



class InstanceCommand(object):
    @staticmethod
    def list():
        cmd_str = "gcloud beta compute instances list"
        return subprocess.check_output(cmd_str.split(" "))
    @staticmethod
    def stop(name_list):
        cmd_str = "gcloud beta compute instances stop "+" ".join(name_list)
        # return subprocess.check_output(cmd_str.split(" "))
        # the bug of gcould, the normal output should not put into error
        return subprocess.check_output(cmd_str.split(" "),stderr=subprocess.STDOUT)

    @staticmethod
    def start(name_list):
        cmd_str = "gcloud beta compute instances start "+" ".join(name_list)
        # return subprocess.check_output(cmd_str.split(" "))
        # the bug of gcould, the normal output should not put into error
        return subprocess.check_output(cmd_str.split(" "),stderr=subprocess.STDOUT)

class PackagedInstance(object):
    FIELD_STATUS = "STATUS"
    FIELD_NAME = "NAME"
    FIELD_IP = "EXTERNAL_IP"
    STOP_STATUS = "TERMINATED"
    START_STATUS = "RUNNING"
    @staticmethod
    def list(result_str=None):
        if result_str == None:
            result_str = InstanceCommand.list()
        return parse_table_str(result_str)

    @staticmethod
    def stop(instance_name, result_str=None):
        if result_str == None:
            result_str = InstanceCommand.stop([instance_name])
        # return PackagedInstance.__package_action(result_str, instance_name)
        return result_str

    @staticmethod
    def start(instance_name, result_str=None):
        if result_str == None:
            result_str = InstanceCommand.start([instance_name])
        # return PackagedInstance.__package_action(result_str, instance_name)
        return result_str

    @staticmethod
    def find(instance_name, info_list):
        found_list = filter(lambda x: x[PackagedInstance.FIELD_NAME]==instance_name, info_list)
        return found_list[0]

class InstanceCustomizedCommand(object):
    @staticmethod
    def __action(action_name, check_state, instance_name):
        the_info = getattr(PackagedInstance, action_name)(instance_name)
        # the_info = PackagedInstance.stop(instance_name)
        print("run "+action_name+" command, result:")
        print_as_table(the_info)

        def check_running():
            info_list = PackagedInstance.list()
            last_info = PackagedInstance.find(instance_name, info_list)
            if last_info[PackagedInstance.FIELD_STATUS] == check_state:
                return last_info
            else:
                print("the state is still: "+last_info[PackagedInstance.FIELD_STATUS])
                return None
        last_info = wait_until(check_running, 60)
        print("the instance info:")
        print_as_table(last_info)

        return last_info

    @staticmethod
    def list():
        info_list = PackagedInstance.list()
        print_as_table(info_list)

    @staticmethod
    def stop(instance_name):
        return InstanceCustomizedCommand.__action("stop", 
                PackagedInstance.STOP_STATUS, instance_name)

    @staticmethod
    def start(instance_name):
        last_info = InstanceCustomizedCommand.__action("start", 
                PackagedInstance.START_STATUS, instance_name)

        the_ip = last_info[PackagedInstance.FIELD_IP]
        new_line = change_host_ip(instance_name, the_ip)
        print("ip changed in /etc/hosts:")
        print(new_line)

        print("finished")

        return last_info

    @staticmethod
    def all_methods():
        all_attributes = dir(InstanceCustomizedCommand)
        return filter(lambda x: not x.startswith("__") and not x=="all_methods",
                all_attributes)

class TimeoutError(Exception):
    pass

def wait_until(the_func, timeout_seconds, interval_seconds=2):
    start_time = time.time()
    while time.time() - start_time < timeout_seconds:
        result = the_func()
        if result:
            return result
        print("time: "+time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())+
                " sleep "+str(interval_seconds))
        time.sleep(interval_seconds)
    raise TimeoutError("timeout "+str(timeout_seconds) +" seconds.")

def print_as_table(the_object):
    if isinstance(the_object,str):
        print(the_object)
        print("")
        return

    headers = None
    if isinstance(the_object, list):
        headers = the_object[0].keys()
        values_list = [item.values() for item in the_object]
    else:
        headers = the_object.keys()
        values_list = [the_object.values()]
    result = tabulate(values_list, headers=headers)
    print(result)
    print("")


def change_host_ip(the_name, the_ip):
    hosts_path = '/etc/hosts'

    # search_exp = '(?:[0-9]{1,3}\.){3}[0-9]{1,3}\s+'+the_name
    # replace_exp = the_ip+"\t"+the_name
    # replace_all_in_file(file,search_exp,replace_exp)
    # return replace_exp

    new_line = the_ip+"\t"+the_name+"\n"
    def change_line(the_line):
        if the_line.find(the_name) > 0:
            return new_line
        else:
            return the_line
    with open(hosts_path,'r') as the_file:
        lines = the_file.readlines()
        new_lines = map(change_line, lines)
    with open(hosts_path,'w') as the_file:
        # new_lines[11:20].pp()
        the_file.write("".join(new_lines))
    return new_line



# sudo cp ./g_ins.py /usr/bin/g_ins.py
# sudo chmod 777 /usr/bin/g_ins.py
# cp ~/hosts_back /etc/hosts


if __name__ == '__main__':
    print sys.argv
    if len(sys.argv) < 2:
        print "Usage: g_ins.py start instance_name"
        print "    now support commands: "+", ".join(InstanceCustomizedCommand.all_methods())
        exit()
    else:
        if sys.argv[1] not in InstanceCustomizedCommand.all_methods():
            print "    now support commands: "+", ".join(InstanceCustomizedCommand.all_methods())
            exit()
    getattr(InstanceCustomizedCommand, sys.argv[1])(*sys.argv[2:])

    # import print_helper
    # from minitest import *

    # with test("print_info_list"):
    #     # info_list = PackagedInstance.list()
    #     # print_as_table(info_list)
    #     pass

    # with test("start_instance"):
        # the_info = PackagedInstance.start('ec2-test')
        # print_as_table(the_info)
        # start_instance('ec2-test')
        # stop_instance('ec2-test')
        # start_main('ec2-test')
        # InstanceCustomizedCommand.stop('g-test-2')

    # with test("InstanceCommand.stop"):
    #     InstanceCommand.stop(['g-test-2']).p()
    #     pass

    # with test(InstanceCustomizedCommand.list):
    #     InstanceCustomizedCommand.list()

    # with test(InstanceCustomizedCommand.stop):
    #     InstanceCustomizedCommand.stop('g-test')

    # with test(InstanceCustomizedCommand.start):
    #     InstanceCustomizedCommand.start('g-test-2')


