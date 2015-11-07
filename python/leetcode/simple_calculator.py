def cal(the_str):
    for c in (" ", "(", ")"):
        the_str = the_str.replace(c,'')
    return add(the_str.split("+"))
def add(the_list):
    result = 0
    for item in the_list:
        if item.find("-") > 0:
            cur = sub(item.split("-"))
        else:
            cur = int(item)
        result += cur
    return result

def sub(the_list):
    int_list = map(int, the_list)
    return int_list.pop(0) - sum(int_list)


if __name__ == '__main__':
    from minitest import *

    with test(cal):
        cal("(1 + 1)").pp()
        cal(" 2-1 + 2 ").pp()
        cal("(1+(4+5+2)-3)+(6+8)").pp()