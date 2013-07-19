import threading, time

"""
RLock is a reentrant lock. acquire() can be called multiple times 
by the same thread without blocking. Keep in mind that release() 
needs to be called the same number of times to unlock the resource.

"""

class FileWriteThread(threading.Thread):
    def __init__(self, thread_index, output, count, rlock):
        threading.Thread.__init__(self)
        self.thread_index = thread_index
        self.output = output
        self.count = count
        self.rlock = rlock

    def run(self):
        def write_content(index):
            self.rlock.acquire()
            print "thread %d is rlocked!\n" % self.thread_index
            self.output.write(
                "No"+str(self.thread_index)+
                " write : "+str(index)+"\n")
            time.sleep(0.1)
        map(write_content, range(self.count))
        def release(index):
            print "thread %d is unrlocked!\n" % self.thread_index
            self.rlock.release()
        map(release, range(self.count))
        print "thread %d is end!\n" % self.thread_index

if __name__ == '__main__':
    thread_count = 2
    write_count = 3
    rlock = threading.RLock()
    with open('simple.log','w') as output:
        def thread_start(thread_index):
            thread = FileWriteThread(
                thread_index, output, write_count, rlock)
            thread.start()
            return thread
        threads = map(thread_start, range(thread_count))
        [thread.join() for thread in threads]
    print "ok"
