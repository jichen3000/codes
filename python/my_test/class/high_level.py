class Basic(object):
    """it's the basic which handles methods in the basic level."""
    def __init__(self, basic_arg):
        super(Basic, self).__init__()
        self.basic_arg = basic_arg
        
    def basic_func1(self, index):
        # print index
        return index

    def basic_func2(self, index):
        # print index
        return index

class High(Basic):
    """it's the basic which handles methods in the high level."""
    def __init__(self, high_arg):
        super(High, self).__init__(high_arg)
        self.high_arg = high_arg

    def high(self):
        return self.basic_func1(1), self.basic_func2(2), \
            self.basic_arg, self.high_arg
        

if __name__ == '__main__':
    from minitest import *

    with test("high"):
        high = High("jc")
        high.high().must_equal((1, 2, 'jc', 'jc'))