class lazyproperty(object):
    def __init__(self, func):
        self.func = func
    def __get__(self, instance, cls): 
        if instance is None:
            return self 
        else:
            value = self.func(instance) 
            setattr(instance, self.func.__name__, value) 
            return value

import math
class Circle(object):
    def __init__(self, radius):
        self.radius = radius
    @lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2
    @lazyproperty
    def perimeter(self): 
        print('Computing perimeter') 
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    from minitest import *

    with test(lazyproperty):
        c = Circle(4.0)
        c.radius.p()
        c.area.p()
        c.area = 5
        c.area.p()
        pass