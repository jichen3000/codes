from itertools import chain

if __name__ == '__main__':
    from minitest import *

    with test("add list"):
        a = range(3)
        b = range(20,23)
        (a + b).must_equal([0, 1, 2, 20, 21, 22])
        # more efficent
        list(chain(a,b)).must_equal([0, 1, 2, 20, 21, 22])
        pass