import time
def timing(f):
    def wrap(*args):
        time1 = time.time()
        ret = f(*args)
        time2 = time.time()
        print('%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0))
        return ret
    return wrap

@timing
def do_work():
  b = 2 ^ 30


if __name__ == '__main__':
        from minitest import *
    
        with test(timing):
            do_work()