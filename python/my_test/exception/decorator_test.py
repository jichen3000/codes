# def my_log(f):
#     def inner(*args, **kwargs):
#         # print("function({}) start...".format(f.__name__))
#         result = f(*args, **kwargs)
#         # print("function({}) end!".format(f.__name__))
#         return result
#     return inner

# @my_log
def do(a):
    return a + 1

do(234)
# if __name__ == '__main__':
#     from minitest import *

#     with test(my_log):
#         do(123)