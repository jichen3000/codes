import threading, time

"""
Locks have 2 states: locked and unlocked. 
2 methods are used to manipulate them: acquire() and release(). 
Those are the rules:
    if the state is unlocked: a call to acquire() changes the state to locked.
    if the state is locked: a call to acquire() blocks until another thread calls release().
    if the state is unlocked: a call to release() raises a RuntimeError exception.
    if the state is locked: a call to release() changes the state to unlocked().
"""

class FileWriteThread(threading.Thread):
    def __init__(self, thread_index, output, count, lock):
        threading.Thread.__init__(self)
        self.thread_index = thread_index
        self.output = output
        self.count = count
        self.lock = lock

    def run(self):
        def write_content(index):
            self.output.write(
                "No"+str(self.thread_index)+
                " write : "+str(index)+"\n")
            time.sleep(0.1)
        # self.lock.acquire()
        with self.lock:
            print "thread %d is locked!\n" % self.thread_index
            map(write_content, range(self.count))
            print "thread %d is unlocked!\n" % self.thread_index
            # self.lock.release()
        print "thread %d is end!\n" % self.thread_index

if __name__ == '__main__':
    thread_count = 2
    write_count = 3
    lock = threading.Lock()
    with open('simple.log','w') as output:
        def thread_start(thread_index):
            thread = FileWriteThread(
                thread_index, output, write_count, lock)
            thread.start()
            return thread
        threads = map(thread_start, range(thread_count))
        [thread.join() for thread in threads]
    print "ok"
