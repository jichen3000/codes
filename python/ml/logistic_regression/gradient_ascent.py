from operator import *
from functools import partial
import numpy
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# support value and values
def combinate(*funcs):
    def comb_func(*args, **kvargs):
        first_func = funcs[0]
        result = first_func(*args, **kvargs)
        others_reverse_funcs = funcs[1:]
        for func in others_reverse_funcs:
            result = func(result)
        return result
    return comb_func

comb = combinate

def sigmoid(x):
    return 1.0/(1+numpy.exp(-x))

def gradient_ascent(dataset, labels):
    dataset_matrix = numpy.mat(dataset)
    label_matrix = numpy.mat(labels).transpose()
    # alpha is the step size
    alpha = 0.001
    row_count, col_count =  numpy.shape(dataset_matrix)
    weights = numpy.ones((col_count,1))
    cycle_count = 500
    for i in range(cycle_count):
    # for i in range(1):
        calculated_lable_matrix = sigmoid(dataset_matrix*weights)
        # Qualitatively you can see we're calculating the error 
        # between the actual class and the predicted class 
        # and then moving in the direction of that error.
        error = (label_matrix - calculated_lable_matrix)
        # print error
        # why
        weights = weights + alpha * dataset_matrix.transpose() * error
    return weights

def gradient_ascent_generator(dataset, labels, cycle_count = 500):
    dataset_matrix = numpy.mat(dataset)
    label_matrix = numpy.mat(labels).transpose()
    # alpha is the step size
    alpha = 0.001
    row_count, col_count =  numpy.shape(dataset_matrix)
    weights = numpy.ones((col_count,1))   
    # i = 0
    # while i < cycle_count:
    for i in range(cycle_count):
    # for i in range(1):
        calculated_lable_matrix = sigmoid(dataset_matrix*weights)
        # Qualitatively you can see we're calculating the error 
        # between the actual class and the predicted class 
        # and then moving in the direction of that error.
        error = (label_matrix - calculated_lable_matrix)
        # print error
        # why
        weights = weights + alpha * dataset_matrix.transpose() * error
        yield weights
        # i += 1


def draw_dataset_points(subplot, dataset,labels):
    def get_point_group(point_label):
        return filter(lambda item: int(item[1]) == point_label, zip(dataset, labels))
    def get_x_y(point_group):
        return map(comb(itemgetter(0), itemgetter(1) ), point_group),\
            map(comb(itemgetter(0), itemgetter(2) ), point_group)
    x1, y1 = get_x_y(get_point_group(1))
    x0, y0 = get_x_y(get_point_group(0))

    subplot.scatter(x1, y1, s=30, c='red', marker='s') 
    subplot.scatter(x0, y0, s=30, c='green')

def draw_weight_line(subplot, weights):
    weights = weights.getA()
    x = numpy.arange(-3.0, 3.0, 0.1)
    y = (-weights[0]-weights[1]*x)/weights[2]
    return subplot.plot(x, y)

def draw_points_and_weight_line():
    fig = plt.figure()
    subplot = fig.add_subplot(111)
    dataset, labels =load_dataset()
    weights = gradient_ascent(dataset, labels)

    draw_weight_line(subplot, weights)
    plt.xlabel('X1'); plt.ylabel('X0');
    draw_dataset_points(subplot, dataset, labels)
    plt.show()



def draw_every_weight_line():
    fig = plt.figure()
    subplot = fig.add_subplot(111)
    plt.xlabel('X1'); plt.ylabel('X0');

    dataset, labels =load_dataset()
    draw_dataset_points(subplot, dataset, labels)

    weights_generator = gradient_ascent_generator(dataset, labels, 1000)
    weights_list = [item for item in weights_generator]
    weights_list = weights_list[10:]

    def update_weight_line(data):
        index_str = str(data[0])
        plt.title("Weight Lines ("+index_str+")")        
        weights = data[1]
        return draw_weight_line(subplot, weights)
    weights_line = update_weight_line((0, weights_list[0]))


    ani = animation.FuncAnimation(fig, update_weight_line, zip(range(len(weights_list)), weights_list), interval=10, repeat=False)

    plt.show()

if __name__ == '__main__':
    from minitest import *


    def load_dataset(filename='test_set.dataset'):
        with open(filename) as data_file:
            strs = map(comb(str.strip, str.split), data_file.readlines())
        labels = map(comb(itemgetter(2), int), strs)
        dataset = [[1.0, float(item[0]), float(item[1])] for item in strs]
        return dataset, labels

    with test_case("gradient_ascent"):
        tself = get_test_self()
        tself.dataset, tself.labels =load_dataset()

        with test("sigmoid"):
            sigmoid(0).must_equal(0.5)

        with test("gradient_ascent"):
            tself.weights = gradient_ascent(tself.dataset, tself.labels)
            tself.weights.must_equal_with_func(
                numpy.matrix([
                    [ 4.12414349],
                    [ 0.48007329],
                    [-0.6168482 ]]), numpy.allclose)

        with test("gradient_ascent_generator"):
            gtr = gradient_ascent_generator(tself.dataset, tself.labels)
            gtr.next().must_equal(
                numpy.matrix([
                    [ 0.96358575],
                    [ 0.98285296],
                    [ 0.48828325]]), 
                key=numpy.allclose)

        with test("draw_points_and_weight_line"): 
            # draw_points_and_weight_line()
            pass

        with test("draw_every_weight_line"):
            draw_every_weight_line()
            pass


