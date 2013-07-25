import operator
from functools import partial
import numpy

def combinate(*funcs):
    def comb_func(*args, **kvargs):
        first_func = funcs[-1]
        result = first_func(*args, **kvargs)
        others_reverse_funcs = reversed(funcs[:-1])
        for func in others_reverse_funcs:
            result = func(result)
        return result
    return comb_func

co = combinate

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
    # print weights
    return weights

import matplotlib.pyplot as plt

# def draw_dataset_points(dataset, labels):


def plotBestFit(weights,dataMat,labelMat):
    weights = weights.getA()
    dataArr = numpy.array(dataMat)
    n = numpy.shape(dataArr)[0]
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i])== 1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s') 
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = numpy.arange(-3.0, 3.0, 0.1)
    # print weights
    # print weights[1]*x
    y = (-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x, y)
    plt.xlabel('X1'); plt.ylabel('X2');
    plt.show()

if __name__ == '__main__':
    from minitest import *


    def load_dataset(filename='test_set.dataset'):
        with open(filename) as data_file:
            strs = map(co(str.split, str.strip), data_file.readlines())
        labels = map(co(int, operator.itemgetter(2)), strs)
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

        with test("plotBestFit"): 
            plotBestFit(tself.weights, tself.dataset, tself.labels)
            pass
