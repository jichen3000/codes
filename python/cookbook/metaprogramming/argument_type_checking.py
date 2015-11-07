# from inspect import signature
from funcsigs import signature
from functools import wraps
def typeassert(*ty_args, **ty_kwargs): 
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__: 
            return func
        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments
        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments 
            for name, value in bound_values.arguments.items():
                if name in bound_types:
                    if not isinstance(value, bound_types[name]):
                        raise TypeError(
                                'Argument {} must be {}'.format(
                                name, bound_types[name]) )
            return func(*args, **kwargs) 
        return wrapper
    return decorate

@typeassert(int, int)
def add(x,y):
    return x+y

@typeassert(int, z=int) 
def spam(x, y, z=42): 
    return (x, y, z)

if __name__ == '__main__':
    from minitest import *

    with test(typeassert):
        add(3,4).must_equal(7)
        (lambda : add("",1)).must_raise(
                TypeError,"Argument x must be <type 'int'>")

        spam(1,"",3).must_equal((1,"",3))
        # spam(1,"","").must_equal((1,"",3))
        (lambda : spam(1,"","")).must_raise(
                TypeError,"Argument z must be <type 'int'>")
