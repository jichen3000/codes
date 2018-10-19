from numpy import *
from operator import gt, le, itemgetter

def get_column_as_list(matrix, column_index):
    return matrix[:, column_index].T.tolist()[0]

def get_column_as_set(matrix, column_index):
    return set(get_column_as_list(matrix, column_index))


def count_nodes(tree,nodes_count=0):
    ''' the count of leafs always equals the count of nodes plusing 1'''
    if isTree(tree):
        nodes_count += (count_nodes(tree['left_gt'],nodes_count) + \
            count_nodes(tree['right_le'],nodes_count) + 1) 
    return nodes_count


def load_dataset(fileName):
    dataMat = []
    fr = open(fileName)
    for line in fr.readlines():
        curLine = line.strip().split('\t')
        fltLine = map(float,curLine)
        dataMat.append(fltLine)
    return dataMat

def binSplitDataset(data_matrix, feature, value):
    def choose_rows(choose_fun):
        # nonzero will return the coodinate of the points which is non zero.
        row_indices = nonzero(choose_fun(data_matrix[:,feature],value))[0]
        return data_matrix[row_indices, :][0]
    return choose_rows(gt), choose_rows(le)

# why the leaf will like this, it is nonsense.
def create_leaf(data_matrix):
    return mean(data_matrix[:,-1])

def calculate_error(data_matrix, mean_value=None):
    if not mean_value:
        return var(data_matrix[:,-1]) * shape(data_matrix)[0]
    else:
        return sum(power(data_matrix[:,-1] - mean_value,2)) 

def createTree(dataset, create_leaf_func=create_leaf, 
        calculate_error_func=calculate_error, options=(1,4)): 
    feature, value = chooseBestSplit(dataset, create_leaf_func, 
        calculate_error_func, options)
    if feature == None: 
        return value
    tree = {}
    tree['feature'] = feature
    tree['value'] = value
    gt_rows, le_rows = binSplitDataset(dataset, feature, value) 
    tree['left_gt'] = createTree(gt_rows, create_leaf_func, calculate_error_func, options) 
    tree['right_le'] = createTree(le_rows, create_leaf_func, calculate_error_func, options) 
    return tree



def chooseBestSplit(data_matrix, create_leaf_func=create_leaf, 
        calculate_error_func=calculate_error, options=(1,4)):
    tolerance_error = options[0]; 
    minimum_row_count = options[1]
    if len(get_column_as_set(data_matrix, -1)) == 1: 
        return None, create_leaf_func(data_matrix)
    m,n = shape(data_matrix)
    error = calculate_error_func(data_matrix)
    best_error = inf
    best_fearture = 0
    best_value = 0
    for feature_index in range(n-1):
        for split_value in get_column_as_set(data_matrix, feature_index):
            left_gt_mat, right_le_mat = binSplitDataset(
                data_matrix, feature_index, split_value)
            if (shape(left_gt_mat)[0] < minimum_row_count) or \
                    (shape(right_le_mat)[0] < minimum_row_count): 
                continue
            new_error = calculate_error_func(left_gt_mat) + \
                calculate_error_func(right_le_mat)
            if new_error < best_error:
                best_fearture = feature_index
                best_value = split_value
                best_error = new_error
    if (error - best_error) < tolerance_error:
        return None, create_leaf_func(data_matrix)
    left_gt_mat, right_le_mat = binSplitDataset(
        data_matrix, best_fearture, best_value)
    if (shape(left_gt_mat)[0] < minimum_row_count) or \
            (shape(right_le_mat)[0] < minimum_row_count):
        return None, create_leaf_func(data_matrix)
    return best_fearture,best_value

def draw_points(dataset, x_column=0, y_column=1, show=True):
    import matplotlib.pyplot as plt
    # dataset.p()
    xs = map(itemgetter(x_column), dataset)
    ys = map(itemgetter(y_column), dataset)
    plt.plot(xs, ys,'ro')
    if show:
        plt.show()
    return plt

def isTree(obj):
    # return (type(obj).__name__=='dict')
    return (type(obj) is dict)

def getMean(tree):
    if isTree(tree['right_le']): 
        tree['right_le'] = getMean(tree['right_le'])
    if isTree(tree['left_gt']): 
        tree['left_gt'] = getMean(tree['left_gt'])
    return (tree['left_gt']+tree['right_le'])/2.0


def prune(tree, test_matrix):
    if shape(test_matrix)[0] == 0: 
        return getMean(tree)
    if (isTree(tree['right_le']) or isTree(tree['left_gt'])):
        left_gt_mat, right_le_mat = binSplitDataset(
            test_matrix, tree['feature'], tree['value'])
    if isTree(tree['left_gt']): 
        tree['left_gt'] = prune(tree['left_gt'], left_gt_mat)
    if isTree(tree['right_le']): 
        tree['right_le'] = prune(tree['right_le'], right_le_mat) 
    if not isTree(tree['left_gt']) and not isTree(tree['right_le']):
        left_gt_mat, right_le_mat = binSplitDataset(
            test_matrix, tree['feature'], tree['value'])
        errorNoMerge = calculate_error(left_gt_mat, tree['left_gt']) + \
            calculate_error(right_le_mat, tree['right_le'])
        treeMean = getMean(tree)
        errorMerge = calculate_error(test_matrix, treeMean)
        if errorMerge < errorNoMerge:
            # print "merging"
            return treeMean
        else: 
            return tree
    else: 
        return tree

if __name__ == '__main__':
    from minitest import *

    with test_case("cart"):
        with test("binSplitDataset"):
            left_gt_mat,right_le_mat=binSplitDataset(mat(eye(4)),1,0.5)
            # left_gt_mat.must_equal()
            left_gt_mat.must_equal(matrix([[ 0.,  1.,  0.,  0.]]), 
                allclose)
            right_le_mat.must_equal(matrix([[ 1.,  0.,  0.,  0.],
                [ 0.,  0.,  1.,  0.],
                [ 0.,  0.,  0.,  1.]]), allclose)
            pass

        with test("createTree simple dataset"):
            ex00_dataset = load_dataset('ex00.dataset')
            createTree(mat(ex00_dataset)).must_equal(
                {'feature': 0,
                 'left_gt': 1.018096767241379,
                 'right_le': -0.044650285714285733,
                 'value': 0.48813})

        with test("createTree pricewise dataset"):
            ex0_dataset = load_dataset('ex0.dataset')
            ex0_tree = createTree(mat(ex0_dataset))
            ex0_tree.must_equal(
                {'feature': 1,
                 'left_gt': {'feature': 1,
                          'left_gt': {'feature': 1,
                                   'left_gt': 3.9871632000000004,
                                   'right_le': 2.9836209534883724,
                                   'value': 0.797583},
                          'right_le': 1.9800350714285717,
                          'value': 0.582002},
                 'right_le': {'feature': 1,
                           'left_gt': 1.0289583666666664,
                           'right_le': -0.023838155555555553,
                           'value': 0.197834},
                 'value': 0.39435})
            count_nodes(ex0_tree).must_equal(4)


        with test("createTree bigger dataset"):
            ex2_dataset = load_dataset('ex2.dataset')
            createTree(mat(ex2_dataset), options=(10000, 4)).must_equal(
                {'feature': 0,
                 'left_gt': 101.35815937735855,
                 'right_le': -2.6377193297872341,
                 'value': 0.499171})

        with test("prune"):
            ex2_tree = createTree(mat(ex2_dataset), options=(0, 1))
            # ex2_tree.p()
            count_nodes(ex2_tree).must_equal(199)

            ex2_test_dataset = load_dataset('ex2test.dataset')
            pruned_ex2_tree = prune(ex2_tree, mat(ex2_test_dataset))
            count_nodes(pruned_ex2_tree).must_equal(140)
            pass


        with test("draw_points"):
            # draw_points(ex00_dataset)
            # draw_points(ex0_dataset, 1,2)
            pass