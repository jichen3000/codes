import threading, time

class FileWriteThread(threading.Thread):
    def __init__(self, thread_index, output, count):
        threading.Thread.__init__(self)
        self.thread_index = thread_index
        self.output = output
        self.count = count

    def run(self):
        def write_content(index):
            self.output.write(
                "No"+str(self.thread_index)+
                " write : "+str(index)+"\n")
            time.sleep(0.1)
        map(write_content, range(self.count))
        print "thread "+str(self.thread_index)+" ok\n"

if __name__ == '__main__':
    thread_count = 2
    write_count = 3
    with open('simple.log','w') as output:
        def thread_start(thread_index):
            thread = FileWriteThread(
                thread_index, output, write_count)
            thread.start()
            return thread
        threads = map(thread_start, range(thread_count))
        [thread.join() for thread in threads]
    print "ok"
