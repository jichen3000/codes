class AClass(object):
    def tell(self):
        print("AClass")
class BClass(object):
    def tell(self):
        print("BClass")

class ChildClass(AClass, BClass):
    pass

if __name__ == '__main__':
    child = ChildClass() 
    child.tell()
    print(dir(child))
    print(child.__class__())
