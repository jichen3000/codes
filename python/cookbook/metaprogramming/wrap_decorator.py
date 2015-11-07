import time
from functools import wraps

def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print func.__name__, end-start
    return wrapper

@timethis
def count_down(n):
    while n > 0:
        n -= 1

def timethis_without_wraps(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print func.__name__, end-start
    return wrapper

@timethis_without_wraps
def count_down_without_wraps(n):
    while n > 0:
        n -= 1

if __name__ == '__main__':
    from minitest import *

    with test(count_down):
        # count_down(100000)
        # count_down(10000000)
        count_down.__name__.must_equal("count_down")
        dir(count_down).pp()
        # count_down.__annotations__.must_equal("count_down")
        count_down_without_wraps.__name__.must_equal("wrapper")
        # __wrapped__ not for python2
        # count_down.__wrapped__.__name__.must_equal("count_down_without_wraps")