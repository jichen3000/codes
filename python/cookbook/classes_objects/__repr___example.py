class Pair(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        # !r means repr
        return 'Pair({0.x!r}, {0.y!r})'.format(self) 
    def __str__(self):
        return '({0.x!s}, {0.y!s})'.format(self)
    def __eq__(self,other):
        return repr(self) == repr(other)

if __name__ == '__main__':
    from minitest import *

    with test(Pair):
        pair = Pair(3,4)
        print pair
        str(pair).must_equal('(3, 4)')
        repr(pair).must_equal('Pair(3, 4)')
        eval(repr(pair)).must_equal(pair)