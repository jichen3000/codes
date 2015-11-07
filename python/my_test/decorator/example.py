from functools import wraps

def logged_no_wraps(the_func):
    def internal(*args, **kwargs):
        print "function name: {0}".format(
                the_func.__name__)
        return the_func(*args, **kwargs)
    return internal

def logged(the_func):
    @wraps(the_func)
    def internal(*args, **kwargs):
        print "function name: {0}".format(
                the_func.__name__)
        return the_func(*args, **kwargs)
    return internal

@logged_no_wraps
def bar():
    return "bar"

@logged
def foo():
    return "foo"


if __name__ == '__main__':
        from minitest import *
    
        with test(logged):
            bar().pp()
            foo().pp()
            bar.__name__.pp()
            foo.__name__.pp()
            pass    