# the values assigned as defaults should always be immutable objects
def spam(a, b=[]):
    return b

if __name__ == '__main__':
    from minitest import *

    with test(spam):
        arr = spam(1)
        arr.must_equal([])
        arr.append(1)
        spam(2).must_equal([1])
        pass
