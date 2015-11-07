import time
from contextlib import contextmanager

@contextmanager
def list_transaction(orig_list):
    working = list(orig_list) 
    yield working 
    orig_list[:] = working

if __name__ == '__main__':
    from minitest import *

    with test(list_transaction):
        items = [1,2,3]
        with list_transaction(items) as working:
            working.append(4)
            working.append(5)
        items.must_equal([1,2,3,4,5])