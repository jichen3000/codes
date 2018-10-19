import fileinput
# import time

# def timing(f):
#     def wrap(*args):
#         time1 = time.time()
#         ret = f(*args)
#         time2 = time.time()
#         print('%s function took %0.3f ms' % (f.func_name, (time2-time1)*1000.0))
#         return ret
#     return wrap

# @timing
def main(files=None):
    index_dict = {}
    input_count = 0
    for line in fileinput.input(files=files):
        if fileinput.lineno() == 1:
            n, input_count = map(int, line.split(" "))
            # input_count = float(input_count)
            # print("input_count:{}".format(input_count))
        else:
            start, end, value = map(int,line.split(" "))
            if start in index_dict:
                index_dict[start] += value
            else:
                index_dict[start] = value
            end = end + 1
            if end in index_dict:
                index_dict[end] -= value
            else:
                index_dict[end] = 0 - value

    # index_dict.p()
    cur_value = 0
    max_value = 0
    for key in sorted(index_dict.keys()):
        cur_value += index_dict[key]
        if cur_value > max_value:
            max_value = cur_value
    print(max_value)
    return max_value

if __name__ == '__main__':
        from minitest import *
    
        with test(main):
            # main("test3.txt").must_equal(8628)
            # main("test4.txt").must_equal(7542539201)
            main("test.txt").must_equal(7542539201)
