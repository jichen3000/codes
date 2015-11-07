import time
from functools import wraps
def timethis(func): 
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print('{}.{} : {}'.format(func.__module__, func.__name__, end - start)) 
        return r
    return wrapper

def countdown(n):
    while n > 0:
        n -= 1

import timeit

if __name__ == '__main__':
    from minitest import *

    with test(timethis):
        timethis(countdown)(100).pp()

    with test(timeit):
        timeit.timeit('math.sqrt(2)', 'import math').pp()
        timeit.timeit('math.sqrt(2)', 'import math', number=1000).pp()