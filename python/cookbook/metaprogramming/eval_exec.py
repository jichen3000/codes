x = 42

if __name__ == '__main__':
    from minitest import *

    with test(eval):
        eval('2+3*4+x').must_equal(56)
        exec('for i in range(10): print i')
        pass