class Person(object):
    """docstring for Person"""
    def __init__(self, name):
        super(Person, self).__init__()
        self.name = name

    def __repr__(self):
        # return "%s(%r)" % (self.__class__, self.__dict__)
        return "Person({0})".format(self.name)

if __name__ == '__main__':
        from minitest import *

        with test(Person):
            colin = Person('colin')
            colin.p()
            print repr(colin)

            new_colin = colin
            new_colin.p()
            colin = None
            new_colin.p()
            colin.p()
