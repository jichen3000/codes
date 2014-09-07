''' show how to use the 'map' function. '''

if __name__ == '__main__':
    from minitest import *

    with test("show zip"):
        arr1 = range(3)
        arr2 = ['a','b','c']
        def show_some(arg1, arg2):
            # (arg1, arg2).pl()
            return (arg1, arg2)
        result = map(show_some, arr1, arr2)
        result.pl()
        (zip(*result))[1].pl()