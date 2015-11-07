import weakref
class Cached(type):
    def __init__(self, *args, **kwargs):
        print "in __init__"
        super(Cached, self).__init__(*args, **kwargs)
        self.__cache = weakref.WeakValueDictionary()
    def __call__(self, *args): 
        print "in __call__"
        # args.pp()
        if args not in self.__cache:
            obj = super(Cached, self).__call__(*args)
            self.__cache[args] = obj 
        return self.__cache[args]
        # if args in self.__cache:
        #     return self.__cache[args] 
        # else:
        #     obj = super(Cached, self).__call__(*args) 
        #     self.__cache[args] = obj 
        #     # return obj
        # return self.__cache[args]

# Example
class CachedSpam(object): 
    __metaclass__ = Cached
    def __init__(self, name):
        print('Creating CachedSpam({!r})'.format(name)) 
        self.name = name

if __name__ == '__main__':
    from minitest import *

    with test(Cached):
        a1 = CachedSpam("a")
        a2 = CachedSpam("a")
        pass