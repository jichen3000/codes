# not working in python2
import types
from functools import wraps
class Profiled:
    def __init__(self, func):
        self.o_func = func
        wraps(func)(self)
        self.ncalls = 0
    def __call__(self, *args, **kwargs): 
        args.pp()
        kwargs.pp()
        self.ncalls += 1
        # return self.__wrapped__(*args, **kwargs)
        return self.o_func(*args, **kwargs)
    def __get__(self, instance, cls): 
        "get".pp()
        if instance is None:
            return self 
        else:
            return types.MethodType(self, instance)

@Profiled
def add(x, y): 
    return x + y

class Spam(object): 
    @Profiled
    def bar(self, x): 
        return (self, x)

if __name__ == '__main__':
    from minitest import *

    with test("decorator as class"):
        add(2,3)
        add(2,3)
        add.ncalls.must_equal(2)
        s = Spam()
        s.bar(3)
        s.bar(3)
        s.bar(3)
        s.bar.ncalls.must_equal(3)