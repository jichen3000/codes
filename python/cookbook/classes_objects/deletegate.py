class A(object):
    def __init__(self, x):
        self.x = x    
    def spam(self, y):
        return "spam {}".format(y)
    def foo(self): 
        return "foo"


class B(object):
    def __init__(self):
        self._a = A(3)
    def bar(self): 
        pass
    # def spam(self, x):
    #     print "spam"
    #     # Delegate to the internal self._a instance 
    #     return self._a.spam(x)
    # def foo(self):
    #     # Delegate to the internal self._a instance 
    #     return self._a.foo()

    # Expose all of the methods defined on class A
    def __getattr__(self, name): 
        print "__getattr__"
        return getattr(self._a, name)

# cannot handle __len__ which start with two underscore methods
class Proxy(object):
    def __init__(self, obj):
        self._obj = obj
        
    # Delegate attribute lookup to internal obj
    def __getattr__(self, name): 
        print('getattr:', name)
        return getattr(self._obj, name)
    
    # Delegate attribute assignment
    def __setattr__(self, name, value): 
        if name.startswith('_'):
            super(Proxy, self).__setattr__(name, value) 
        else:
            print('setattr:', name, value) 
            setattr(self._obj, name, value)
        
    # Delegate attribute deletion
    def __delattr__(self, name): 
        if name.startswith('_'):
            super(Proxy, self).__delattr__(name) 
        else:
            print('delattr:', name) 
            delattr(self._obj, name)


if __name__ == '__main__':
    from minitest import *

    with test(A):
        b = B()
        b.spam(3).must_equal("spam 3")
        pass

    with test(Proxy):
        a = A(2)
        p = Proxy(a)
        p.x.must_equal(2)
        p.spam(3).must_equal("spam 3")
        pass
