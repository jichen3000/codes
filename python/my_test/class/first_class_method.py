class Person(object):

    @classmethod
    def p(clz):
        print "class method p:", clz

    # def p(self):
    #     print "instance method p:", self


colin = Person()
colin.p()
print dir(colin)

import functools
class combomethod(object):
    def __init__(self, method):
        self.method = method

    def __get__(self, obj=None, objtype=None):
        @functools.wraps(self.method)
        def _wrapper(*args, **kwargs):
            if obj is not None:
                return self.method(obj, *args, **kwargs)
            else:
                return self.method(objtype, *args, **kwargs)
        return _wrapper

class Person1(object):
    @combomethod
    def p(self_or_clz):
        print "I'm the ", self_or_clz

colin = Person1()
colin.p()
Person1.p()

