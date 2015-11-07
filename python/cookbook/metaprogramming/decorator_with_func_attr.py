from functools import wraps, partial
import logging
import sys

def attach_wrapper(obj, func=None):
    # print "mm",obj,func
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func

def logged(level, name=None, message=None): 
    '''
    Add logging to a function.  level is the logging
    level, name is the logger name, and message is the
    log message.  If name and message aren't specified,
    they default to the function's module and name.
    '''
    def decorate(func):
        logname = name if name else func.__module__ 
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(wrapper.level, logmsg)
            return func(*args, **kwargs) 

        @attach_wrapper(wrapper)
        def set_level(new_level):
            wrapper.level = new_level

        wrapper.level = level

        return wrapper
    return decorate


# Example use
@logged(logging.INFO) 
def add(x, y):
    return x + y

@logged(logging.CRITICAL, 'example') 
def spam():
    print('Spam!')

if __name__ == '__main__':
    from minitest import *

    with test(logged):
        with capture_output() as output:
            logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
            result = add(1,2)
            spam()
            add.set_level(logging.WARNING)
            add(3,5)
        output.must_equal([
                'INFO:__main__:add', 
                'CRITICAL:example:spam', 
                'Spam!',
                'WARNING:__main__:add'])
