import threading, time, random


class Producer(threading.Thread):
    """
    Produces random integers to a list
    """

    def __init__(self, integers, event, count):
        """
        Constructor.

        @param integers list of integers
        @param event event synchronization object
        """
        threading.Thread.__init__(self)
        self.integers = integers
        self.event = event
        self.count = count
    
    def run(self):
        """
        Thread run method. Append random integers to the integers list
        at random time.
        """
        for i in range(self.count):
            integer = random.randint(0, 256)
            self.integers.append(integer) 
            print '%d appended to list by %s' % (integer, self.name)
            print 'event set by %s' % self.name
            self.event.set()
            self.event.clear()
            print 'event cleared by %s' % self.name
            time.sleep(1)


class Consumer(threading.Thread):
    """
    Consumes random integers from a list
    """

    def __init__(self, integers, event, count):
        """
        Constructor.

        @param integers list of integers
        @param event event synchronization object
        """
        threading.Thread.__init__(self)
        self.integers = integers
        self.event = event
        self.count = count
    
    def run(self):
        """
        Thread run method. Consumes integers from list
        """
        for i in range(self.count):
            self.event.wait()
            try:
                integer = self.integers.pop()
                print '%d popped from list by %s' % (integer, self.name)
            except IndexError:
                # catch pop on empty list
                time.sleep(1)

def main():
    count = 6
    integers = []
    event = threading.Event()
    t1 = Producer(integers, event, count)
    # t2 = Consumer(integers, event, count)
    t2 = Consumer(integers, event, count/2)
    t3 = Consumer(integers, event, count/2)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()

if __name__ == '__main__':
    main()

