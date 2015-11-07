def get_first_and_rest(first, *rest):
    return first, rest


if __name__ == '__main__':
    from minitest import *

    with test(get_first_and_rest):
        get_first_and_rest(*range(3)).must_equal( 
                (0,(1,2)) )

        pass

