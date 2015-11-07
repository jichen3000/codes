# Descriptor attribute for an integer type-checked attribute
class Integer(object):
    def __init__(self, name):
        self.name = name
    def __get__(self, instance, cls):
        print "Integer.__get__"
        # for class call
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]

class Point(object):
    x = Integer('x')
    y = Integer('y')
    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __repr__(self):
        return "Point({}, {})".format(self.x,self.y)


if __name__ == '__main__':
    from minitest import *

    with test(Point):
        p = Point(1,2)
        p.pp()

        pass