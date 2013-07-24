class Person(object):
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def __str__(self):
        return "person "+self.name
    __repr__ = __str__


person_list =  map(Person, "colin john albert".split(" "))

print person_list
print map(Person.get_name, person_list)
