
def f1(str):
    return "f1( %s ) " % str

def f2(str):
    return "f2( %s ) " % str

def f3(str1, str2):
    return "f3( %s, %s ) " % (str1, str2)


if __name__ == '__main__':
    from minitest import *
    from functional_style import *

    with test_case("functional_style"):

        with test("comb"):
            f12 = comb(f2, f1)
            # f12("123").pp()        
            f123 = comb(f3, f2, f1)
            # f123("123","ddd").pp()                    