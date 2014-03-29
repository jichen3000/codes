import cv2
# import numpy as np

def using_plt():
    from matplotlib import pyplot as plt

    img = cv2.imread('original.jpg',0)
    one_dim_array = img.ravel()
    plt.hist(one_dim_array, 256, [0,256])
    plt.show()

if __name__ == '__main__':
    from minitest import *

    with test("using_plt"):
        using_plt()
        pass