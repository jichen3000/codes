import sys

class MyError(Exception):
    pass

# if __name__ == '__main__':
#     from minitest import *

#     with test(MyError):
#         # raise MyError("something wrong")
#         # pass
#         try:
#             # raise MyError("something wrong")
#             pass
#         except Exception as e:
#             raise e
#         else:
#             print("ok")

try:
    raise MyError("something wrong")
    pass
except Exception as e:
    # raise e
    print("a"+str(e))
else:
    print("ok")