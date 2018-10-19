# https://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work
# remove @property, t.lr will return a function
class MyTest(object):
    def __init__(self, lr):
        self._lr = lr

    @property
    def lr(self):
        return self._lr

    mm = 0

if __name__ == '__main__':
    from minitest import *

    with test(MyTest):
        t = MyTest(2)
        t.lr.must_equal(2)
        t.mm.must_equal(0)
        t.mm = 3
        t.mm.must_equal(3)
        # t.lr = 5
        (lambda: [ None for t.lr in [5]]).must_raise(AttributeError,"can't set attribute")
