
def test1():
    a=13
    exec('b = a + 1')
    return b

if __name__ == '__main__':
    from minitest import *

    with test("exec"):
        test1().must_equal(14)

