from multiprocessing import Process, Pipe
from os import getpid
from datetime import datetime


def local_time(counter):
    return ' (LAMPORT_TIME={}, LOCAL_TIME={})'.format(
            counter, datetime.now())

def calc_recv_timestamp(recv_time_stamp, counter):
    return max(recv_time_stamp, counter) + 1

def event(pid, counter):
    counter += 1
    print('Something happened in {} !'.format(pid) + local_time(counter))
    return counter

def send_message(pipe, pid, counter):
    counter += 1
    pipe.send(('Empty shell', counter))
    print('Message sent from ' + str(pid) +
            local_time(counter))
    return counter

def recv_message(pipe, pid, counter):
    message, timestamp = pipe.recv()
    counter = calc_recv_timestamp(timestamp, counter)
    print('Message received at ' + str(pid)  +
            local_time(counter))
    return counter    

def process_one(pipe12):
    # pid = getpid()
    # print("one is {}".format(pid))
    pid = 1
    counter = 0
    counter = event(pid, counter)
    counter = send_message(pipe12, pid, counter)
    counter  = event(pid, counter)
    counter = recv_message(pipe12, pid, counter)
    counter  = event(pid, counter)
def process_two(pipe21, pipe23):
    # pid = getpid()
    # print("two is {}".format(pid))
    pid = 2
    counter = 0
    counter = recv_message(pipe21, pid, counter)
    counter = send_message(pipe21, pid, counter)
    counter = send_message(pipe23, pid, counter)
    counter = recv_message(pipe23, pid, counter)

def process_three(pipe32):
    # pid = getpid()
    # print("three is {}".format(pid))
    pid = 3
    counter = 0
    counter = recv_message(pipe32, pid, counter)
    counter = send_message(pipe32, pid, counter)



def main():
    pipe12, pipe21 = Pipe()
    pipe23, pipe32 = Pipe()
    process1 = Process(target=process_one,
                       args=(pipe12,))
    process2 = Process(target=process_two,
                       args=(pipe21, pipe23))
    process3 = Process(target=process_three,
                       args=(pipe32,))
    process1.start()
    process2.start()
    process3.start()
    process1.join()
    process2.join()
    process3.join()    

if __name__ == '__main__':
    main()