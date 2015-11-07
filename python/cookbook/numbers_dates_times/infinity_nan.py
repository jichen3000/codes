if __name__ == '__main__':
    from minitest import *
    import math
    with test("infinity nan"):
        a = float('inf') 
        b = float('-inf') 
        c = float('nan')
        a.p()
        b.p()
        c.p()
        math.isinf(a).must_true()
        math.isnan(c).must_true()
        pass