if __name__ == '__main__':
    from minitest import *

    with test("c"):
        x = 10
        a = lambda y: x + y
        x = 20
        b = lambda y: x+y
        # a free variable that gets bound at runtime, not definition time. 
        b(10).must_equal(30)
        a(10).must_equal(30)

        # If you want an anonymous function to capture a value 
        # at the point of definition and keep it, 
        # include the value as a default value, like this:
        x = 10
        b = lambda y, x=x: x + y
        x = 20
        b(10).must_equal(20)
        pass