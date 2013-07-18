===========
Mini Test
===========

Using like the below:

if __name__ == '__main__':
    import operator
    with test_case("new test case"):


        with test("test some"):
            'jc'.must_equal('jc1')
            True.must_true()
            False.must_true()
            # div_zero().must_equal(0)


        with test("test some"):
            (1).must_equal(1)
            (1).must_equal_with_func(1, operator.eq)
            (1).must_equal_with_func(2, operator.eq)

        with test("test some"):
            (1).must_equal(1)
            (1).must_equal(1)


