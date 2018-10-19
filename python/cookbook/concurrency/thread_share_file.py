from time import sleep
from threading import Thread, current_thread


def tail(file_path, interval_sec=1, from_what= 2):
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
            # curr_position = file_.tell()
            line = file_.readline()
            if not line:
                # file_.seek(curr_position)
                sleep(interval_sec)
            else:
                yield line

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

if __name__ == '__main__':
    from minitest import *

    with test(func_with_file):
        log_path = "test.log"
        end_str = "###allend"
        file_ = open(log_path, "w")
        try:
            def output(msg):
                file_.write(msg)
                file_.flush()
            result = [0]
            t = Thread(target=func_with_file, args=(5, result, output, end_str))
            t.start()
                # t.join()
            for line in tail(log_path):
                if line == end_str:
                    print("end")
                else:
                    line.p()        
        finally:
            file_.close()
