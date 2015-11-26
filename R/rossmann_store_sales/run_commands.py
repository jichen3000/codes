import os
import time
from threading import Thread
from minitest import *

def run_one(cmds):
    for cmd in cmds:
        cmd.p()
        os.system(cmd)
        time.sleep(10)
    return True

def main(cmd_file_path, thread_count=4):
    lines = [line for line in open(cmd_file_path)]
    group_count = int(round(float(len(lines))/thread_count))
    cmd_groups = [ lines[i:i+group_count] for i in xrange(0,len(lines),group_count)]
    cmd_groups.p()
    # threads = [time.sleep(5);Thread(target=run_one, args=(group,)) for group in cmd_groups]
    threads = []
    for group in cmd_groups:
        threads.append(Thread(target=run_one, args=(group,)))
        time.sleep(10)
    # threads.size().p()
    [t.start() for t in threads]
    [t.join() for t in threads]

cmd_file_path = './cmds.txt'

# nohup python run_commands.py >logs/run.log 2>&1 &
main(cmd_file_path)

failed 141, log163.log
