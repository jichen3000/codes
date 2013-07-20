import types
def getId(self): 
    return self.__id
def patch_method(target, method):
    #def method(target,x):
        # print "x=",x
        # print "called from", target
    setattr(target, method.func_name, types.MethodType(method,target))

def addID(original_class):
    orig_init = original_class.__init__
    # make copy of original __init__, so we can call it without recursion

    def __init__(self, id, *args, **kws):
        self.__id = id
        patch_method(self, getId)
        orig_init(self, *args, **kws) # call the original __init__

    original_class.__init__ = __init__ # set the class' __init__ to the new one
    return original_class

@addID
class Foo:
    def __init__(self, value1):
        self.value1 = value1

foo1 = Foo(5,1)
print foo1.value1
print Foo.__dict__
print foo1.getId()
# foo1.getId = getId
# print foo1.getId()
from pprint import pprint as pp
pp(dir(foo1))
