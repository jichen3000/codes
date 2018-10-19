from time import sleep
from threading import Thread, current_thread

import subprocess

def tail(file_path, interval_sec=1, from_what= 0):
    ''' 
        from_what: 
            0 measures from the beginning of the file,   
            1 uses the current file position, 
            2 uses the end of the file as the reference point.  
    '''
    print("openfile")
    with open(file_path) as file_:
        # Go to the end of file
        file_.seek(0, from_what)
        while True:
            curr_position = file_.tell()
            line = file_.readline()
            if not line:
                file_.seek(curr_position)
                sleep(interval_sec)
            else:
                yield line

def _run_command(cmd_str):
    ''' return is_successful, result '''
    try:
        result = subprocess.check_output(cmd_str,
                stderr=subprocess.STDOUT, shell=True)
        return {"is_successful":True, 
                "output":result.decode("utf-8"), "cmd":cmd_str}
    except subprocess.CalledProcessError as e:
        # return [e.returncode, e.output]
        return {"is_successful":False, 
                "output":e.output.decode("utf-8"), "cmd":cmd_str}


def run_one_testcase(testcase, output_func):
    output_func(".")
    sleep(0.1)
    output_func(".")
    output_func("running {}\n".format(
            testcase))
    for i in range(5):
        output_func("index {}\n".format(i))
        sleep(1)
    output_func("finished {}\n".format(
            testcase))

def run_one_testcase2(testcase, q):
    # q.put(".")
    # # sleep(1)
    # q.put("end")
    print("put 1")
    for i in range(5):
        print("index {}\n".format(i))
        sleep(1)
    q.put(1)
    pass

def nothing(testcase, sleep_func):
    print(".")
    # sleep(1)
    for i in range(5):
        print("index {}\n".format(i))
        sleep_func(1)

    print("end")    

def new_thread(testcase):
    def some():
        print("some")
        sleep(1)
    print("sleep  0.5")
    sleep(0.5)
    print("using a thread")
    t = Thread(target=some)
    t.start()
    t.join()
    

    print("end")   

def func_with_check_stop2(n, result, log_path, end_str):
    '''
        using need_stop to let thread stop
    '''
    assert len(result) > 0, "the result must a list with one element"
    # _run_command("ls -l").p()
    with open(log_path, "w") as file_:
        def output(msg):
            file_.write(msg)
            file_.flush()
        for i in range(n):
            if hasattr(current_thread(),"need_stop") and current_thread().need_stop:
                result[0] = "force stop"
                print("i: {}".format(i))
                output(end_str)
                return
            output("i: {}\n".format(i))
            sleep(0.5)
        result[0] = "finish"
        print("finish")
        output("finish\n")   
        output(end_str)

def func_with_file(n, result, output, end_str):
    '''
        using need_stop to let thread stop
    '''
    assert len(result) > 0, "the result must a list with one element"
    # _run_command("ls -l").p()
    for i in range(n):
        if hasattr(current_thread(),"need_stop") and current_thread().need_stop:
            result[0] = "force stop"
            output(end_str)
            return
        print("i: {}".format(i))
        output("i: {}\n".format(i))
        sleep(0.5)
    result[0] = "finish"
    print("finish")
    output("finish\n")   
    output(end_str)

def func_with_file_for_process(n, result, output, end_str):
    '''
        using need_stop to let thread stop
    '''
    assert len(result) > 0, "the result must a list with one element"
    # _run_command("ls -l").p()
    for i in range(n):
        print("i: {}".format(i))
        output("i: {}\n".format(i))
        sleep(0.5)
    result[0] = "finish"
    print("finish")
    output("finish\n")   
    output(end_str)    