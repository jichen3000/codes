# http://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html

# from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

def draw_plot():
    fig = plt.figure()
    # ax = Axes3D(fig)
    ax = fig.add_subplot(111, projection='3d')

    x = [6,3,6,9,12,24]
    y = [3,5,78,12,23,56]
    # put 0s on the y-axis, and put the y axis on the z-axis
    ax.plot(xs=x, ys=[0]*len(x), zs=y, zdir='z', label='ys=0, zdir=z')
    plt.show()

def draw_wireframe():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    x, y, z = axes3d.get_test_data(0.05)
    # def z_func(x,y):
    #     return x+y
    z = x**2+y**4
    ax.plot_wireframe(x, y, z, rstride=10, cstride=10)

    plt.show()


# def z_func(x,y):
#     return x+y
# x_list = range(10)
# plt.show()

if __name__ == '__main__':
    # draw_plot()
    draw_wireframe()