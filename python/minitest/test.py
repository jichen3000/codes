# http://guide.python-distribute.org/creation.html
# https://github.com/jichen3000/codes/tree/master/python/minitest

if __name__ == '__main__':
    from minitest import *

    import operator
    with test_case("new test case"):


        with test("test must_equal"):
            'jc'.must_equal('jc')

        with test("test must_true"):
            True.must_true()
            False.must_true()


        with test("test must_equal_with_func"):
            (1).must_equal_with_func(1, operator.eq)
            (1).must_equal_with_func(2, operator.eq)

        def div_zero():
            1/0
            
        with test("test must_raise"):
            (lambda : div_zero()).must_raise(ZeroDivisionError)
