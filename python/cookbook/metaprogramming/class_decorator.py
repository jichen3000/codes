def log_getattribute(cls):
    # Get the original implementation 
    orig_getattribute = cls.__getattribute__
    # Make a new definition
    def new_getattribute(self, name): 
        print('getting:', name)

        return orig_getattribute(self, name)
        
    # Attach to the class and return
    cls.__getattribute__ = new_getattribute 
    return cls

# Example use
@log_getattribute
class A(object):
    def __init__(self,x):
        self.x = x 
    def spam(self):
        return self.x

if __name__ == '__main__':
    from minitest import *

    with test(A):
        a = A(2)
        with capture_output() as output:
            a.x.must_equal(2)
        output.must_equal(["('getting:', 'x')"])