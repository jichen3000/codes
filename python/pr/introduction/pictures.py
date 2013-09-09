from numpy import *
import matplotlib.pyplot as plt

def draw_sin():
    t = arange(-2., 2., 0.01)
    lines = plt.plot(t, sin(t*pi), '-')
    lines = plt.plot(t, sin(t*pi*2), '-')
    lines[0].set_antialiased(False) 
    plt.setp(lines, color='r', linewidth=2.0)
    plt.show()

if __name__ == '__main__':
    from minitest import *

    with test(""):
        draw_sin()
        pass