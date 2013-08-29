class Person(object):
    def __init__(self, name):
        self.name = name

    def new_no(self):
        return self.name + "1"

    @staticmethod
    def no():
        return 0


colin = Person("jc")
print colin.name

print Person.no()

def new_no():
    return 1
# def new_no(self):
#     return 1
print Person.__class__
Person.new_no = staticmethod(new_no)
print Person.new_no()


def the_class_metho(clz):
    return "clz method"

Person.the_class_metho = classmethod(the_class_metho)
print Person.the_class_metho()

import types
print types.NoneType

# None.new_no = classmethod(new_no)
# print None.new_no()

# int.new_no = staticmethod(new_no)
# print int.new_no()