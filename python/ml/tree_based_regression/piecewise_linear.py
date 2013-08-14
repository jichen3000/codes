from numpy import *
from operator import itemgetter

from cart_tree_building import *

def gen_x_y_matrix(data_matrix):
    m, n = data_matrix.shape
    x_matrix = append(ones((m, 1)), data_matrix[:, 0:n-1], axis=1)
    return x_matrix, data_matrix[:, -1]

def standard_regress(x_matrix,y_matrix):
    # x_matrix = mat(x_list)
    # y_matrix = mat(y_list).T
    x_t_x = x_matrix.T*x_matrix
    if linalg.det(x_t_x) == 0.0:
        raise "This matrix is singular, cannot do inverse"
    # I is inverse, equal exp -1 to a matrix
    return x_t_x.I * (x_matrix.T*y_matrix)

def linearSolve(data_matrix):
    x_matrix, y_matrix = gen_x_y_matrix(
        data_matrix)
    return standard_regress(x_matrix, y_matrix), x_matrix, y_matrix

def create_model_leaf(data_matrix):
    ws,X,Y = linearSolve(data_matrix)
    return ws

def calculate_model_error(data_matrix):
    ws,X,Y = linearSolve(data_matrix)
    yHat = X * ws
    return sum(power(Y - yHat, 2))


def draw_linear_tree(dataset, tree, show=True):
    import matplotlib.pyplot as plt
    draw_points(exp2_dataset, show=False)

    def draw_tree_line(tree):
        data_matrix = mat(dataset)
        if isTree(tree):
            x_le_matrix = mat([data_matrix[:, tree['feature']].min(),
                tree['value']]).T
            y_le_matrix = append(ones((2, 1)), x_le_matrix, axis=1) * \
                tree['right_le']
            x_gt_matrix = mat([tree['value'], 
                data_matrix[:, tree['feature']].max()]).T
            y_gt_matrix = append(ones((2, 1)), x_gt_matrix, axis=1) * \
                tree['left_gt']
            plt.plot(x_le_matrix, y_le_matrix, 'b')
            plt.plot(x_gt_matrix, y_gt_matrix, 'b')
    draw_tree_line(tree)
    if show:
        plt.show()
    return plt

def linear_tree_equal(this, other):
    def comp(attr):
        if type(this[attr]) is matrix:
            return allclose(this[attr], other[attr])
        else:
            return this[attr] == other[attr]
    return all(map(comp, this))


if __name__ == '__main__':
    from minitest import *

    with test_case('piecewise_linear'):

        with test('linearSolve'):
            exp2_dataset = load_dataset('exp2.dataset')
            exp2_tree = createTree(mat(exp2_dataset),
                create_model_leaf, calculate_model_error,
                options=(1,10))
            exp2_tree.must_equal({'feature': 0,
                 'left_gt': matrix([[  1.69855694e-03],
                        [  1.19647739e+01]]),
                 'right_le': matrix([[ 3.46877936],
                        [ 1.18521743]]),
                 'value': 0.285477}, linear_tree_equal)
            # draw_linear_tree(exp2_dataset, exp2_tree)
            pass