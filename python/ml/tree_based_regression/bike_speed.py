from numpy import *
from operator import itemgetter

from cart_tree_building import *
from piecewise_linear import *

def eval_normal_leaf(model, inDat):
    return float(model)

def eval_linear_leaf(model, inDat):
    x_matrix = append(ones((1, 1)), inDat, axis=1)
    return float(x_matrix*model)

def treeForeCast(tree, inData, eval_leaf_func=eval_normal_leaf): 
    if not isTree(tree): 
        return eval_leaf_func(tree, inData) 
    if inData[tree['feature']] > tree['value']:
        if isTree(tree['left_gt']):
            return treeForeCast(tree['left_gt'], inData , eval_leaf_func)
        else:
            return eval_leaf_func(tree['left_gt'], inData)
    else:
        if isTree(tree['right_le']):
            return treeForeCast(tree['right_le'], inData , eval_leaf_func)
        else:
            return eval_leaf_func(tree['right_le'], inData)

def createForeCast(tree, testData, eval_leaf_func=eval_normal_leaf):
    yHat = [treeForeCast(tree, mat(row), eval_leaf_func) 
        for row in testData]
    return mat(yHat).T

if __name__ == '__main__':
    from minitest import *

    with test_case('bike_speed'):
        train_dataset = load_dataset('bikeSpeedVsIq_train.dataset')
        test_dataset = load_dataset('bikeSpeedVsIq_test.dataset')
        train_matrix = mat(train_dataset)
        test_matrix = mat(test_dataset)
        # draw_points(train_dataset)
        # draw_points(test_dataset)


        with test('normal_yHat'):
            normal_tree = createTree(train_matrix,
                options=(1,20))
            normal_yHat = createForeCast(normal_tree, test_matrix[:,0])
            normal_yHat.shape.must_equal((200,1))
            normal_yHat[:5,:].must_equal(
                array([[ 122.90893027],
                       [ 157.04840788],
                       [ 122.90893027],
                       [ 141.06067981],
                       [  50.94683665]]), 
                allclose)
            # the closer to 1.0 the better,
            corrcoef(normal_yHat, 
                test_matrix[:,1], rowvar=0)[0,1].must_equal(
                0.964085, allclose)
            pass

        with test('linear_yHat'):
            linear_tree = createTree(train_matrix,
                create_model_leaf, calculate_model_error,
                options=(1,20))
            linear_yHat = createForeCast(linear_tree, 
                test_matrix[:,0],eval_linear_leaf)
            linear_yHat.shape.must_equal((200,1))
            linear_yHat[:5,:].must_equal(
                matrix([[ 119.61969695],
                        [ 155.97526025],
                        [ 119.61969695],
                        [ 139.1075255 ],
                        [  45.2990143 ]]), 
                allclose)
            # the closer to 1.0 the better,
            corrcoef(linear_yHat, 
                test_matrix[:,1], rowvar=0)[0,1].must_equal(
                0.9760412191380623, allclose)
            pass

        with test('standard_regression_yHat'):
            ws,X,Y=linearSolve(train_matrix)
            standard_regression_yHat=test_matrix*ws[1,0]+ws[0,0]
            corrcoef(standard_regression_yHat, 
                test_matrix[:,1],rowvar=0)[0,1].must_equal(
                0.943468423567, allclose)
            pass
