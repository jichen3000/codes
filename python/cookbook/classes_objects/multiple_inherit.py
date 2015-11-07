class Base(object):
    def __init__(self):
        print('Base.__init__')


class A(Base):
    def __init__(self):
        Base.__init__(self) 
        print('A.__init__')

class B(Base):
    def __init__(self):
        Base.__init__(self) 
        print('B.__init__')

class C(A,B):
    def __init__(self):
        A.__init__(self) 
        B.__init__(self) 
        print('C.__init__')        

class A1(Base):
    def __init__(self):
        super(A1,self).__init__() 
        print('A1.__init__')
    def spam(self):
        print('A1.spam') 
        super(A1, self).spam()

class B1(Base):
    def __init__(self):
        super(B1,self).__init__() 
        print('B1.__init__')
    def spam(self):
        print('B1.spam') 
        # super(B1, self).spam()

class C1(A1,B1):
    def __init__(self):
        super(C1, self).__init__() 
        print('C1.__init__')        

if __name__ == '__main__':
    from minitest import *

    with test("multiple"):
        (lambda : C()).must_output([
                "Base.__init__",
                "A.__init__",
                "Base.__init__",
                "B.__init__",
                "C.__init__"])
        C.__mro__.__str__().must_equal(
                "(<class '__main__.C'>, <class '__main__.A'>, "+
                "<class '__main__.B'>, <class '__main__.Base'>, "+
                "<type 'object'>)")
        (lambda : C1()).must_output([
                "Base.__init__",
                "B1.__init__",
                "A1.__init__",
                "C1.__init__"])    
        C1.__mro__.__str__().must_equal(
                "(<class '__main__.C1'>, <class '__main__.A1'>, "+
                "<class '__main__.B1'>, <class '__main__.Base'>, "+
                "<type 'object'>)")
        (lambda : C1().spam()).must_output([
                "Base.__init__",
                "B1.__init__",
                "A1.__init__",
                "C1.__init__",
                "A1.spam",
                "B1.spam"]) 
        C1().spam().must_output([
                "Base.__init__",
                "B1.__init__",
                "A1.__init__",
                "C1.__init__",
                "A1.spam",
                "B1.spam"]) 
