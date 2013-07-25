# http://matplotlib.org/users/pyplot_tutorial.html

import matplotlib.pyplot as plt
def f1():
    plt.plot([1,2,3,4])
    plt.ylabel('some numbers')
    plt.show()

def f2():
    plt.plot([1,2,3,4], [1,4,9,16], 'ro')
    plt.axis([0, 6, 0, 20])
    plt.show()

if __name__ == '__main__':
    # f1()
    f2()