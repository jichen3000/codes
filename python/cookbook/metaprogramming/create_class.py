# cannot work in python2
import types
import operator
import sys

def __init__(self, name, shares, price): 
    self.name = name
    self.shares = shares
    self.price = price

def cost(self):
    return self.shares * self.price

type_dict = {
    '__init__' : __init__,
    'cost' : cost,
}

Stock = types.new_class('Stock', (), {}, lambda ns: ns.update(type_dict))
Stock.__module__ = __name__


# just like collections.namedtuple
# def named_tuple(classname, fieldnames):
#     # Populate a dictionary of field property accessors 
#     cls_dict = { name: property(operator.itemgetter(n))
#             for n, name in enumerate(fieldnames) }
#     # Make a __new__ function and add to the class dict
#     def __new__(cls, *args):
#         if len(args) != len(fieldnames):
#             raise TypeError('Expected {} arguments'.format(len(fieldnames))) 
#         return tuple.__new__(cls, args)

#     cls_dict['__new__'] = __new__
#     # Make the class
#     cls = types.new_class(classname, (tuple,), {},
#             lambda ns: ns.update(cls_dict))
#     # Set the module to that of the caller
#     cls.__module__ = sys._getframe(1).f_globals['__name__'] 
#     return cls

if __name__ == '__main__':
    from minitest import *

    with test("create a class"):
        s = Stock('ACME', 50, 91.1)
        s.cost().must_equal(30)

    # with test(named_tuple):
    #     Point = named_tuple('Point', ['x', 'y'])
    #     Point['Point']