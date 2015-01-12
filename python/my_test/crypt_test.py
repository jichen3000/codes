import crypt

if __name__ == '__main__':
    from minitest import *

    with test(""):
        crypt.crypt("123456","mm").pp()
        crypt.crypt("uC$8jO$4k","E7").must_equal("E7405819F6C85B0AFCE3A5E4FA4BFAA0")