class MyQueue(object):
    def __init__(self):
        super(MyQueue, self).__init__()
        self.items = []


    def enqueue(self, item):
        self.items.append(item)
        return self

    def dequeue(self):
        if self.size() <= 0:
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def to_list(self):
        return self.items

    def __eq__(self, the_list):
        return self.to_list() == the_list

    def __repr__(self):
        return repr(self.to_list())
MyQueue.en = MyQueue.enqueue
MyQueue.de = MyQueue.dequeue

if __name__ == '__main__':
    from minitest import *

    with test(MyQueue):
        q = MyQueue().en(1).en(2).en(3)
        q.must_equal([1,2,3])
        q.is_empty().must_equal(False)
        q.size().must_equal(3)
        q.de().must_equal(1)
        q.de().must_equal(2)
        q.de().must_equal(3)
        (lambda : q.de()).must_raise(
                IndexError, "dequeue from empty queue")
        q.is_empty().must_equal(True)
        q.size().must_equal(0)
        pass

