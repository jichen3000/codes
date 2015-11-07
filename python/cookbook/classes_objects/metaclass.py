# the metaclass will automatically get passed the same argument
# that you usually pass to `type`

# ndeed, metaclasses are especially useful to do black magic, and therefore complicated stuff. 
# But by themselves, they are simple:
# intercept a class creation
# modify the class
# return the modified class
def upper_attr(future_class_name, future_class_parents, future_class_attr):
    """
    Return a class object, with the list of its attribute turned 
    into uppercase.
    """

    # pick up any attribute that doesn't start with '__' and uppercase it
    uppercase_attr = {}
    for name, val in future_class_attr.items():
        if not name.startswith('__'):
            uppercase_attr[name.upper()] = val
        else:
            uppercase_attr[name] = val

    # let `type` do the class creation
    return type(future_class_name, future_class_parents, uppercase_attr)

__metaclass__ = upper_attr # this will affect all classes in the module

class Foo(): # global __metaclass__ won't work with "object" though
    # but we can define __metaclass__ here instead to affect only this class
    # and this will work with "object" children
    bar = 'bip'

class Foo2(object):
    bar = 'bip'

class FooWithMetaclass(object):
    __metaclass__ = upper_attr
    bar = 'bip'

class UpperAttrMetaclass(type): 

    def __new__(cls, clsname, bases, dct):

        uppercase_attr = {}
        for name, val in dct.items():
            if not name.startswith('__'):
                uppercase_attr[name.upper()] = val
            else:
                uppercase_attr[name] = val

        return super(UpperAttrMetaclass, cls).__new__(cls, clsname, bases, uppercase_attr)

if __name__ == '__main__':
    from minitest import *

    with test(upper_attr):
        hasattr(Foo, 'bar').must_false()
        hasattr(Foo, 'BAR').must_true()

        Foo().BAR.must_equal("bip")

        hasattr(Foo2, 'bar').must_true()
        hasattr(Foo2, 'BAR').must_false()

        hasattr(FooWithMetaclass, 'bar').must_false()
        hasattr(FooWithMetaclass, 'BAR').must_true()
        FooWithMetaclass().BAR.must_equal("bip")

    with test(UpperAttrMetaclass):
        ua = UpperAttrMetaclass('Foo3',(object,),{'bar':'bip'})
        hasattr(ua, 'bar').must_false()
        hasattr(ua, 'BAR').must_true()
