# copy from:
# http://stackoverflow.com/questions/12594148/skipping-execution-of-with-block

import sys
import inspect

class skip(object):
    def __init__(self,mode=0):
        """
        if mode = 0, proceed as normal
        if mode = 1, do not execute block
        """
        self.mode=mode
    def __enter__(self):
        if self.mode==1:
            print 'Met block-skipping criterion ...'
            # Do some magic
            sys.settrace(lambda *args, **keys: None)
            frame = inspect.currentframe(1)

            frame.f_trace = self.trace
            return
        print "some"
    def trace(self, frame, event, arg):
        raise
    def __exit__(self, type, value, traceback):
        print 'Exiting context ...'
        return True

if __name__ == '__main__':
    from minitest import *
    with test("skip block"):
        with skip(mode=1):
            print 'Executing block of code ...'

    with test("skip disable"):
        with skip(mode=0):
            print 'Executing block of code ... '            