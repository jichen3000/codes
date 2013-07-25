# http://matplotlib.org/users/pyplot_tutorial.html

import matplotlib.pyplot as plt
import numpy as np


def f1():
    plt.plot([1,2,3,4])
    plt.ylabel('some numbers')
    plt.show()

def f2():
    plt.plot([1,2,3,4], [1,4,9,16], 'ro')
    # axis [xmin, xmax, ymin, ymax]
    plt.axis([0, 6, 0, 20])
    plt.show()

def f3():
    # evenly sampled time at 200ms intervals
    t = np.arange(0., 5., 0.1)

    # red dashes, blue squares and green triangles
    plt.plot(t, t, 'r--', t, t**2, 'bs', t, t**3, 'g^')
    plt.show()

def f4():
    t = np.arange(0., 5., 0.1)
    lines = plt.plot(t, 0.5*t+2, '-')
    lines[0].set_antialiased(False) 
    plt.setp(lines, color='r', linewidth=2.0)
    plt.show()

def f5():
    def f(t):
        return np.exp(-t) * np.cos(2*np.pi*t)

    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)

    # plt.figure(1)
    plt.subplot(211)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')

    plt.subplot(212)
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--')

    plt.show()

def f6():
    plt.figure(1)                # the first figure
    plt.subplot(211)             # the first subplot in the first figure
    plt.plot([1,2,3])
    plt.subplot(212)             # the second subplot in the first figure
    plt.plot([4,5,6])


    plt.figure(2)                # a second figure
    plt.plot([4,5,6])            # creates a subplot(111) by default

    plt.figure(1)                # figure 1 current; subplot(212) still current
    plt.subplot(211)             # make subplot(211) in figure1 current
    plt.title('Easy as 1,2,3')   # subplot 211 title

    plt.show()

def f7():
    "with text"
    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)

    # the histogram of the data
    n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)


    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    plt.title('Histogram of IQ')
    plt.text(60, .025, r'$\mu=100,\ \sigma=15$')
    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)

    plt.show()

def f8():
    "annotate"
    ax = plt.subplot(111)

    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2*np.pi*t)
    line, = plt.plot(t, s, lw=2)

    plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
                arrowprops=dict(facecolor='black', shrink=0.05),
                )

    plt.ylim(-2,2)
    plt.show()


def get_last_one_fun(prefix="f"):
    import re
    from functools import partial
    import operator
    re_func = partial(re.match, 'f\d')
    matchs = map(re_func, globals().keys())
    matchs = filter(partial(operator.ne, None),matchs)
    last_func = None
    if len(matchs) > 0:
        func_names = map(type(matchs[0]).group, matchs)
        func_names = sorted(func_names)
        last_func = globals()[func_names[-1]]
    return last_func

if __name__ == '__main__':
    get_last_one_fun()()
