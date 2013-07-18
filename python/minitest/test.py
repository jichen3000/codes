from minitest import *

def div_zero(m1, m2):
    1/0

if __name__ == '__main__':
    import operator
    with test_case("new test case"):
        tself = get_test_self()
        tself.jc = "jc"
        with test("test some"):
            # print tself.mm
            'jc'.must_equal(tself.jc)
            'jc'.must_equal('jc1')
            True.must_true()
            False.must_true()
            # div_zero().must_equal(0)


        with test("test some"):
            (1).must_equal(1)
            (1).must_equal_with_func(1, operator.eq)
            (1).must_equal_with_func(2, operator.eq)
            # (1).must_equal_with_func(2, div_zero)

        with test("test some"):
            (1).must_equal(1)
            (1).must_equal(1)

