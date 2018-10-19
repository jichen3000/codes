from flask_socketio import SocketIO, emit, send, disconnect
from threading import Thread
from multiprocessing import Process



def run_one_testcase(testcase, output_func, sleep_func):
    # in_socketio = SocketIO(async_mode="eventlet", log_output=True, message_queue='redis://redis-test:6379/12')
    # ss = SocketIO(message_queue='redis://redis-test:6379/12')
    # def output_func(msg):
    #     msg.p()
    #     in_socketio.emit('result_event', {"msg":msg}, namespace='/execution')

    output_func(".")
    sleep_func(0.1)
    output_func(".")
    output_func("running {}\n".format(
            testcase))
    for i in range(8):
        output_func("index {}\n".format(i))
        sleep_func(1)
    output_func("finished {}\n".format(
            testcase))

def run_one_testcase_with_process(testcase, output_func, sleep_func):
    # in_socketio = SocketIO(async_mode="eventlet", log_output=True, message_queue='redis://redis-test:6379/12')
    # def output_func(msg):
    #     msg.p()
    #     in_socketio.emit('result_event', {"msg":msg}, namespace='/execution')

    output_func(".")
    sleep_func(0.1)
    output_func(".")
    output_func("running {}\n".format(
            testcase))
    def target_func(n):
        for i in range(n):
            output_func("index {}\n".format(i))
            sleep_func(1)

    output_func("start a process\n")
    t = Process(target=target_func, args=(5,))
    t.start()
    t.join()
    output_func("finish the process\n")
    output_func("finished {}\n".format(
            testcase))

def run_one_testcase_with_thread(testcase, output_func, sleep_func):
    # in_socketio = SocketIO(async_mode="eventlet", log_output=True, message_queue='redis://redis-test:6379/12')
    # def output_func(msg):
    #     msg.p()
    #     in_socketio.emit('result_event', {"msg":msg}, namespace='/execution')

    output_func(".")
    sleep_func(0.1)
    output_func(".")
    output_func("running {}\n".format(
            testcase))
    def target_func(n):
        for i in range(n):
            output_func("index {}\n".format(i))
            sleep_func(1)

    output_func("start a thread\n")
    t = Thread(target=target_func, args=(5,))
    t.start()
    t.join()
    output_func("finish the thread\n")
    output_func("finished {}\n".format(
            testcase))

def run_one_testcase_new_socketio(testcase, some, sleep_func):
    in_socketio = SocketIO(message_queue='redis://redis-test:6379/12')
    def output_func(msg):
        msg.p()
        in_socketio.emit('result_event', {"msg":msg}, namespace='/execution')

    output_func(".")
    sleep_func(0.1)
    output_func(".")
    output_func("running {}\n".format(
            testcase))
    for i in range(5):
        output_func("index {}\n".format(i))
        sleep_func(1)
    output_func("finished {}\n".format(
            testcase))

# def run_one_testcase2(testcase, q):
#     q.put(".")
#     sleep_func(1)
#     q.put("end")