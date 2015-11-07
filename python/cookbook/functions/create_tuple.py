# it’s actually the comma that forms a tuple, not the parentheses.
b = 1,2,3

if __name__ == '__main__':
    from minitest import *

    with test(b):
        b.must_equal((1,2,3))
        pass