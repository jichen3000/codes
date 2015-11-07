def take_c(the_str, index):
    return [the_str[index], the_str[0:index]+the_str[index+1:len(the_str)]]

def take_c1(the_str, index):
    str_arr = [c for c in the_str]
    r = str_arr.pop(index)
    return [r, "".join(str_arr)]

def insert_c(the_str, the_char, index):
    return the_str[0:index]+the_char+the_str[index:len(the_str)]

def gen_all(the_str):
    if len(the_str) <= 1:
        return [the_str]
    if len(the_str) == 2:
        return [the_str, the_str[::-1]]
    result = []
    for index in range(len(the_str)):
        the_char, rest_str = take_c(the_str, index)
        result += [the_char+c for c in gen_all(rest_str)]
    return result



if __name__ == "__main__":
    from minitest import *

    with test(""):
        gen_all("abcd").pp()
        gen_all("abcd").size().pp()
        pass

    with test(take_c):
        take_c("ab", 0).must_equal(["a","b"])
        take_c("ab", 1).must_equal(["b","a"])
        take_c("abc", 1).must_equal(["b","ac"])

    with test(insert_c):
        insert_c("ab","c", 0).must_equal("cab")
        insert_c("ab","c", 2).must_equal("abc")
