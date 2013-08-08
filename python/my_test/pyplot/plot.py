import matplotlib.pyplot as plt

def draw():
    fig = plt.figure()
    ax = fig.add_subplot(111)
    x = [6,3,6,9,12,24]
    y = [3,5,78,12,23,56]
    # it will has 6 lines, first line will be through [0, x1], [1, y1], [2, x1]
    ax.plot([x,y,x], label='simple')
    plt.show()

if __name__ == '__main__':
    from minitest import *
    with test_case("plot"):
        with test("some"):
            draw()