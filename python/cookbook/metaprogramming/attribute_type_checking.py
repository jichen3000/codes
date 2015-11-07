def typed_property(name, expected_type): 
    storage_name = '_' + name
    @property
    def prop(self):
        return getattr(self, storage_name)
    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError('{} must be a {}'.format(name, expected_type)) 
        setattr(self, storage_name, value)
        return prop

# Example use
class Person(object):
    name = typed_property('name', str) 
    age = typed_property('age', int) 
    def __init__(self, name, age):
            self.name = name
            self.age = age

from functools import partial
String = partial(typed_property, expected_type=str)
Integer = partial(typed_property, expected_type=int)

class Person1(object):
    name = String('name')
    age = Integer('age')
    def __init__(self, name, age):
        self.name = name
        self.age = age

if __name__ == '__main__':
    from minitest import *

    with test(Person):
        colin = Person("colin", 37)
        colin1 = Person1("colin", 37)