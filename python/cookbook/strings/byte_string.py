if __name__ == '__main__':
    from minitest import *

    with test("byte"):
        a = "Hello World"
        a[0].must_equal("H")
        b = b"Hello World"
        b[0].pp()
        pass