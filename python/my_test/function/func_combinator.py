def conb(*funcs):
    def conb_f(*args, **kvargs):
        first_func = funcs[-1]
        result = first_func(*args, **kvargs)
        others_reverse_funcs = reversed(funcs[:-1])
        for func in others_reverse_funcs:
            result = func(result)
        return result
    return conb_f

def conb_tow(func1, func2):
    def conb(*args, **kvargs):
        return func1(func2(*args, **kvargs))
    return conb


def f1(str):
    return "f1( %s ) " % str

def f2(str):
    return "f2( %s ) " % str

def f3(str1, str2):
    return "f3( %s, %s ) " % (str1, str2)


if __name__ == '__main__':
    from minitest import *

    with test_case("combinator"):

        with test("conb_tow"):
            f12 = conb_tow(f1, f2)
            f12("123").pp()
        with test("conb"):
            f12 = conb(f1, f2)
            f12("123").pp()        
            f123 = conb(f1, f2, f3)
            f123("123","ddd").pp()                    