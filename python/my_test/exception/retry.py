import sys
from time import sleep


for i in range(3):
    try:
        raise Exception("something wrong")
    except Exception as e:
        # raise e
        print("i:{}, msg: {}".format(i, e))
        sleep(1)
        continue
    break