from my_queue import *

class MyStack(object):
    def __init__(self):
        super(MyStack, self).__init__()
        self.queue = MyQueue()

    def pop(self):
        tmp_queue = MyQueue()
        while self.queue.size() > 1:
            tmp_queue.en(self.queue.de())
        result = self.queue.de()
        self.queue = tmp_queue
        return result

    def push(self, item):
        self.queue.en(item)
        return self

    def to_list(self):
        return self.queue.to_list()

    def is_empty(self):
        return self.queue.is_empty()

    def size(self):
        return self.queue.size()

    def __repr__(self):
        return repr(self.to_list())

    def __eq__(self, the_list):
        return self.to_list() == the_list

if __name__ == '__main__':
    from minitest import *

    with test(MyStack):
        stack = MyStack().push("1").push(2).push(3)
        stack.must_equal(['1',2,3])
        stack.pop().must_equal(3)
        pass