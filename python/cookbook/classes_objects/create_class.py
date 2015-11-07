# http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python

class OriginalFoo(object):
    bar = True
    def set_bar2(self,bar2):
        self.bar2 = bar2



if __name__ == '__main__':
    from minitest import *

    with test(OriginalFoo):
        o_foo = OriginalFoo()
        o_foo.bar.must_equal(True)
        o_foo.set_bar2(2)
        o_foo.bar2.must_equal(2)
        o_foo.__dict__.must_equal({'bar2': 2})
        hasattr(o_foo, 'bar2').must_true()
        str(o_foo.__class__).must_equal("<class '__main__.OriginalFoo'>")
        str(o_foo.__class__.__class__).must_equal("<type 'type'>")
        hasattr(OriginalFoo, "new_attribute").must_false()
        OriginalFoo.new_attribute = "foo"
        hasattr(OriginalFoo, "new_attribute").must_true()
        
        pass

    with test(type):
        #    type(name of the class, 
        # tuple of the parent class (for inheritance, can be empty), 
        # dictionary containing attributes names and values)
        Foo = type("Foo", (), {'bar2':2})
        foo = Foo()
        str(foo.__class__).must_equal("<class '__main__.Foo'>")
        str(foo.__class__.__class__).must_equal("<type 'type'>")
        foo.bar2.must_equal(2)
        foo.__dict__.must_equal({})
        hasattr(foo, 'bar2').must_true()
