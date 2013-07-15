from pprint import pprint as pp

class Person(object):
    def __init__(self, name):
        self.name = name
    def __getattr__(self, name):
        def _missing(*args, **kwargs):
            print "A missing method was called."
            print "The object was %r, the method was %r. " % (self, name)
            print "It was called with %r and %r as arguments" % (args, kwargs)
        return _missing


colin = Person("colin")
pp(colin.name)
pp(colin.nnn())

# pp("other","234")


