import threading, time, random, Queue

class Producer(threading.Thread):
    """
    Produces random integers to a list
    """

    def __init__(self, queue, count):
        """
        Constructor.

        @param integers list of integers
        @param queue queue synchronization object
        """
        threading.Thread.__init__(self)
        self.queue = queue
        self.count = count
    
    def run(self):
        """
        Thread run method. Append random integers to the integers list at
        random time.
        """
        for i in range(self.count):
            integer = random.randint(0, 256)
            self.queue.put(integer) 
            print '%d put to queue by %s' % (integer, self.name)
            time.sleep(1)

class Consumer(threading.Thread):
    """
    Consumes random integers from a list
    """

    def __init__(self, queue, count):
        """
        Constructor.

        @param integers list of integers
        @param queue queue synchronization object
        """
        threading.Thread.__init__(self)
        self.queue = queue
        self.count = count
    
    def run(self):
        """
        Thread run method. Consumes integers from list
        """
        for i in range(self.count):
            integer = self.queue.get()
            print '%d popped from list by %s' % (integer, self.name)
            self.queue.task_done()

def main():
    count = 6
    integers = []
    queue = Queue.Queue()
    t1 = Producer(queue, count)
    # t2 = Consumer(queue, count)
    t2 = Consumer(queue, count/2)
    t3 = Consumer(queue, count/2)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()

if __name__ == '__main__':
    main()

