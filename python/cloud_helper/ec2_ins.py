#!/usr/bin/python
import sys
import json
import subprocess
import time
from collections import OrderedDict
from tabulate import tabulate
from time import gmtime, strftime
import fileinput
import sys

class InstanceCommand(object):
    @staticmethod
    def list():
        return subprocess.check_output(["aws", "ec2", "describe-instances"])
    @staticmethod
    def stop(id_list):
        return subprocess.check_output(["aws", "ec2", "stop-instances", "--instance-ids", ",".join(id_list)])
    @staticmethod
    def start(id_list):
        return subprocess.check_output(["aws", "ec2", "start-instances", "--instance-ids", ",".join(id_list)])

class PackagedInstance(object):
    @staticmethod
    def list(result_str=None):
        if result_str == None:
            result_str = InstanceCommand.list()
        result = json.loads(result_str)
        headers = ['name', 'state', 'ip', 'type', 'id', 'launch_time']
        def get_info_dict(instance):
            inner_instance = instance['Instances'][0]
            name_tags = filter(lambda x: x['Key']=="Name",inner_instance['Tags'])
            name = ""
            if len(name_tags) > 0:
                name = name_tags[0]['Value']

            ip = ""
            public_dns_name = inner_instance['PublicDnsName']
            if public_dns_name != "":
                ip_list = filter(lambda x: x['Association']['PublicDnsName']==public_dns_name,
                        inner_instance['NetworkInterfaces'])
                ip = ip_list[0]['Association']['PublicIp']
            values = (name, 
                    inner_instance['State']['Name'],
                    ip,
                    inner_instance['InstanceType'],
                    inner_instance['InstanceId'],
                    inner_instance['LaunchTime'])
            return OrderedDict(zip(headers,values))

        info_list = map(get_info_dict, result['Reservations'])
        return info_list

    @staticmethod
    def __package_action(json_str, instance_name):
        result = json.loads(json_str)
        the_action = result.keys()[0]
        info_dict = result[the_action][0]
        headers = ('name','id','the_action','current_state','previouse_state')
        values = (instance_name,
                info_dict['InstanceId'],
                the_action,
                info_dict['CurrentState']['Name'],
                info_dict['PreviousState']['Name'])
        return OrderedDict(zip(headers, values))

    @staticmethod
    def stop(instance_name, result_str=None):
        the_id = get_instance_id(instance_name)
        if result_str == None:
            result_str = InstanceCommand.stop([the_id])
        return PackagedInstance.__package_action(result_str, instance_name)

    @staticmethod
    def start(instance_name, result_str=None):
        the_id = get_instance_id(instance_name)
        if result_str == None:
            result_str = InstanceCommand.start([the_id])
        return PackagedInstance.__package_action(result_str, instance_name)

    @staticmethod
    def find(instance_name, info_list):
        found_list = filter(lambda x: x['name']==instance_name, info_list)
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
            if last_info['state'] == check_state:
                return last_info
            else:
                print("the state is still: "+last_info['state'])
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
        return InstanceCustomizedCommand.__action("stop", 'stopped', instance_name)

    @staticmethod
    def start(instance_name):
        last_info = InstanceCustomizedCommand.__action("start", 'running', instance_name)

        the_ip = last_info['ip']
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


def get_instance_id(instance_name):
    # info_list = get_info_list()
    # found_list = filter(lambda x: x['name']==instance_name, info_list)
    # if len(found_list) == 0:
    #     print("Cannot find the instance for "+instance_name)
    #     print_info_list()
    # the_id = found_list[0]['id']
    name_id_map = { 'ec2-gpu':'i-0e3f3f00a86d384cd',
                    'ec2-test':'i-0c7fa3add1ccc7df7'}
    return name_id_map[instance_name]


# def replace_all_in_file(file,search_exp,replace_exp):
#     for line in fileinput.input(file, inplace=True):
#         if re.search(search_exp,line):
#             line = re.sub(search_exp,replace_exp, line)
#         sys.stdout.write(line)


# sudo cp ./ec2_ins.py /usr/bin/ec2_ins.py
# sudo chmod 777 /usr/bin/ec2_ins.py
# cp ~/hosts_back /etc/hosts


if __name__ == '__main__':
    # print sys.argv
    if len(sys.argv) < 2:
        print "Usage: ec2_ins.py start ec2_test"
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
    #     # the_info = PackagedInstance.start('ec2-test')
    #     # print_as_table(the_info)
    #     # start_instance('ec2-test')
    #     # stop_instance('ec2-test')
    #     # start_main('ec2-test')
    #     InstanceCustomizedCommand.start('ec2-test')
    #     pass

