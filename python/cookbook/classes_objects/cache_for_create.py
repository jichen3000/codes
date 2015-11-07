import weakref

_cache = weakref.WeakValueDictionary()
class Spam(object):
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Please use factory method Spam.create()")

    @classmethod
    def create(cls, name):
        if name not in _cache:
            self = cls.__new__(cls)
            self.name = name
            _cache[name] = self
            return self
        else:
            return _cache[name]

if __name__ == '__main__':
    from minitest import *

    with test(Spam):
        s1 = Spam.create("s1")
        s11 = Spam.create("s1")
        s1.must_equal(s11)
        (lambda : Spam("mm")).must_raise(RuntimeError, 
                "Please use factory method Spam.create()")
        pass
