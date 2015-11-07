
class Person(object):
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self): 
        # print "self"
        return self._first_name
    
    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected a string') 
        self._first_name = value
        
    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Can't delete attribute")


class SubPerson(Person): 
    @property
    def first_name(self): 
        # print('Getting first_name') 
        return super(SubPerson, self).first_name
        # python 3
        # return super(SubPerson, self).first_name

    @first_name.setter
    def first_name(self, value):
        print('Setting first_name to {}'.format(value))
        super(SubPerson, SubPerson).first_name.__set__(self, value)
        
    @first_name.deleter
    def first_name(self):
        print('Deleting first_name')
        super(SubPerson, SubPerson).first_name.__delete__(self)

class Cal(object):
    def __init__(self, size):
        self._size = size
    @property
    def space(self):
        print "cal"
        return self._size*2

if __name__ == '__main__':
    from minitest import *

    with test(Cal):
        c = Cal(3)
        c.space
        c.space

    with test(Person):
        colin = Person('colin')
        colin.first_name.must_equal('colin')
        def set_value():
            colin.first_name = 42
        (lambda : set_value()).must_raise(TypeError, "Expected a string")
        def del_value():
            del colin.first_name
        (lambda : del_value()).must_raise(AttributeError, "Can't delete attribute")
        pass

    with test(SubPerson):
        with capture_output() as output:
            john = SubPerson("john")
            def set_value2():
                john.first_name = 42
            john.first_name.must_equal('john')
            (lambda : set_value2()).must_raise(TypeError, "Expected a string")
        output.must_equal(["Setting first_name to john",
                "Setting first_name to 42"])
        def del_value2():
            del john.first_name
        with capture_output() as output:
            (lambda : del_value2()).must_raise(AttributeError, "Can't delete attribute")
        output.must_equal(["Deleting first_name"])
