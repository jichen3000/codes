# work for python3
def only_keyword(first, *, key1):
    return (first, key1)

if __name__ == '__main__':
    from minitest import *

    with test(only_keyword):
        only_keyword(1,key1=2).must_equal((1,2))
        pass