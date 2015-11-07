import mymodule

if __name__ == '__main__':
    from minitest import *

    with test(mymodule):
        mymodule.B().bar().must_equal('bar')