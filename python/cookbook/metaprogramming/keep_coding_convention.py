class NoMixedCaseMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        for name in clsdict:
            if name.lower() != name:
                raise TypeError('Bad attribute name: ' + name) 
        return super(NoMixedCaseMeta,cls).__new__(
                        cls, clsname, bases, clsdict)
class Root(object): 
    __metaclass__=NoMixedCaseMeta
    pass
    
class A(Root):
    def foo_bar(self):
        return "foo_bar"

def define_b():
    class B(Root):
        def fooBar(self):
            pass
def define_class_method():
    class B(Root):
        @classmethod
        def fooBar(self):
            pass            

if __name__ == '__main__':
    from minitest import *

    with test(NoMixedCaseMeta):
        A().foo_bar().must_equal("foo_bar")
        (lambda : define_b()).must_raise(TypeError)
        (lambda : define_class_method()).must_raise(TypeError)
        pass