# not work in python2

# Base class. Uses a descriptor to set a value
class Descriptor(object):
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value) 
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

# Descriptor for enforcing types
class Typed(Descriptor): 
    expected_type = type(None)
    def __set__(self, instance, value):
        print "Typed"
        if not isinstance(value, self.expected_type):
            raise TypeError('expected ' + str(self.expected_type)) 
        super(Typed, self).__set__(instance, value)
    
# Descriptor for enforcing values
class Unsigned(Descriptor):
    def __set__(self, instance, value):
        print "Unsigned"
        if value < 0:
            raise ValueError('Expected >= 0')
        super(Unsigned, self).__set__(instance, value)

class MaxSized(Descriptor):
    def __init__(self, name=None, **opts):
        if 'size' not in opts:
            raise TypeError('missing size option')
        super(MaxSized, self).__init__(name, **opts)

    def __set__(self, instance, value): 
        if len(value) >= self.size:
            raise ValueError('size must be < ' + str(self.size)) 
        super(MaxSized, self).__set__(instance, value)

class Integer(Typed): 
    expected_type = int

class UnsignedInteger(Integer, Unsigned): 
    pass

class Float(Typed): 
    expected_type = float

class UnsignedFloat(Float, Unsigned): 
    pass

class String(Typed): 
    expected_type = str

class SizedString(String, MaxSized): 
    pass

class Stock:
    # Specify constraints
    name = SizedString('name',size=8)
    shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price    

if __name__ == '__main__':
    from minitest import *

    with test(Stock):
        s = Stock('ACME', 50, 91.1)
        s.name.must_equal('ACME')
        s.shares = 75
        s.shares.must_equal(75)
        s.shares = -10
        # def intern():
        #     s.shares = -10
        # (lambda : intern()).must_raise(ValueError)
