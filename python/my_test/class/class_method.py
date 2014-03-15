class A(object):
    CONSTANTS = {1:'JC'}

    @classmethod
    def my_class_method(cls):
        return 'my_class_method', cls.CONSTANTS

    def normal_method(self):
        return 'normal_method', self.CONSTANTS, self.my_class_method()


if __name__ == '__main__':
    from minitest import *

    with test("classmethod"):
        A.my_class_method().must_equal(
            ('my_class_method', {1: 'JC'})) 

        a = A()
        a.normal_method().must_equal(
            ('normal_method', {1: 'JC'}, ('my_class_method', {1: 'JC'})))