# the best pratice, is not use inherit at all,
# but using a method to provide this feature.

class Structure(object):
# Class variable that specifies expected fields 
    _fields= []
    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))
        
        # Set the arguments
        for name, value in zip(self._fields, args): 
            setattr(self, name, value)
        
        # Set the additional arguments (if any)
        # extra_args = kwargs.keys() - self._fields 
        extra_args = kwargs.keys()[::]
        for i in self._fields:
            if i in extra_args:
                extra_args.remove(i)

        for name in extra_args:
            setattr(self, name, kwargs.pop(name)) 
        if kwargs:
            raise TypeError('Duplicate values for {}'.format(','.join(kwargs)))

class Stock(Structure):
    _fields = ['name', 'shares', 'price']

if __name__ == '__main__':
    from minitest import *

    with test(Structure):
        s1 = Stock('ACME', 50, 91.1)
        s2 = Stock('ACME', 50, 91.1, date='8/2/2012')
        help(Stock).pp()
        pass