from functional_style import comb

from operator import itemgetter
from numpy import *


def get_dataset_from_file(filename):
    with open(filename) as datafile:
        words = [line.strip().split('\t') for line in datafile]
    dataset = [ [float(cell) for cell in row[:-1]] for row in words]
    labels = map(comb(itemgetter(-1), float), words)
    return dataset, labels

def dataset_to_mat(dataset_and_labels, labels=None):
    if labels:
        return mat(dataset_and_labels), mat(labels).T
    return mat(dataset_and_labels[0]), mat(dataset_and_labels[1]).T

get_matrix_from_file = comb(get_dataset_from_file, dataset_to_mat)


def standard_regress(x_matrix,y_matrix):
    # x_matrix = mat(x_list)
    # y_matrix = mat(y_list).T
    x_t_x = x_matrix.T*x_matrix
    if linalg.det(x_t_x) == 0.0:
        raise "This matrix is singular, cannot do inverse"
    # I is inverse, equal exp -1 to a matrix
    return x_t_x.I * (x_matrix.T*y_matrix)

def draw_points(x_list, y_list, weight_matrix):
    import matplotlib.pyplot as plt
    x_matrix = mat(x_list)
    y_matrix = mat(y_list)
    # y_prediction_matrix = x_matrix * weight_matrix

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x_matrix[:,1].flatten().A[0], y_list)

    x_copy_matrix = x_matrix.copy()
    x_copy_matrix.sort(0)
    y_prediction_matrix = x_copy_matrix * weight_matrix
    ax.plot(x_copy_matrix[:, 1], y_prediction_matrix)

    plt.show()

def computer_correlation(x_list, y_list, weight_matrix):
    x_matrix = mat(x_list)
    y_matrix = mat(y_list)
    # x_matrix.shape.p()
    # y_matrix.shape.p()
    # weight_matrix.shape.p()
    y_prediction_matrix = x_matrix * weight_matrix
    # y_prediction_matrix.shape.p()
    return corrcoef(y_prediction_matrix.T, y_matrix)

# add the weights, the closer, the bigger is weight.
# locally weighted linear regression
def lwlr(test_point,x_list,y_list,k=1.0):
    x_matrix = mat(x_list)
    y_matrix = mat(y_list).T
    m = shape(x_matrix)[0]
    weights = mat(eye((m)))
    for j in range(m):
        diff_matrix = test_point - x_matrix[j,:]
        weights[j,j] = exp(diff_matrix*diff_matrix.T/(-2.0*k**2))
    x_weighted_t_x = x_matrix.T * (weights * x_matrix)
    if linalg.det(x_weighted_t_x) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = x_weighted_t_x.I * (x_matrix.T * (weights * y_matrix))
    return test_point * ws

def lwlr_list(test_list,x_list,y_list,k=1.0):
    m = shape(test_list)[0]
    y_prediction_matrix = zeros(m)
    for i in range(m):
        y_prediction_matrix[i] = lwlr(test_list[i],x_list,y_list,k)
    return y_prediction_matrix

def draw_locally_weighted_line(x_list, y_list, y_prediction_matrix):
    import matplotlib.pyplot as plt
    x_matrix = mat(x_list)
    y_matrix = mat(y_list)

    sorted_indexs = x_matrix[:,1].argsort(0)
    x_sorted_matrix=x_matrix[sorted_indexs][:,0,:]

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(x_matrix[:,1].flatten().A[0], y_matrix.T.flatten().A[0] , s=2,
        c='red')

    ax.plot(x_sorted_matrix[:,1],y_prediction_matrix[sorted_indexs])

    plt.show()

def regress_error(y_list,y_prediction_matrix_t):
    return ((y_list-y_prediction_matrix_t)**2).sum()



if __name__ == '__main__':
    from minitest import *

    with test_case("regression"):

        with test("some"):
            dataset, labels = get_dataset_from_file('ex0.dataset')
            labels.size().must_equal(200)
            labels[:3].must_equal([3.176513, 3.816464, 4.550095])
            weight_matrix = standard_regress(*dataset_to_mat(dataset, labels))
            pass

        with test("draw_points"):
            # draw_points(dataset, labels, weight_matrix)
            pass

        with test("computer_correlation"):
            computer_correlation(dataset, labels, weight_matrix)\
                .tolist().must_equal([[ 1.        ,  0.98647356],
                                      [ 0.98647356,  1.        ]], 
                                      key=allclose)
            pass

        with test("lwlr"):
            dataset[0].must_equal([1.0, 0.067732])
            labels[0].must_equal(3.176513)
            lwlr(dataset[0], dataset, labels, k=1.0).A.tolist()\
                .must_equal([[ 3.12204471]], key=allclose)
            lwlr(dataset[0], dataset, labels, k=0.001).A.tolist()\
                .must_equal([[ 3.20175729]], key=allclose)
            lwlr(dataset[0], dataset, labels, k=0.0001).A.tolist()\
                .must_equal([[ 3.17660182]], key=allclose)

        with test("lwlr_list"):
            # y_prediction_matrix = lwlr_list(dataset, dataset, labels, k=0.003)
            # y_prediction_matrix.shape.must_equal((200,))
            # y_prediction_matrix.tolist()[:3].must_equal(
            #     [3.2020066489839647, 3.759401863225539, 4.536701337005885], key=allclose)
            pass

        with test("draw_locally_weighted_line"):
            # draw_locally_weighted_line(dataset, labels, y_prediction_matrix)
            pass

