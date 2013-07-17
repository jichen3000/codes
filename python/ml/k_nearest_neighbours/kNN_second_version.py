# k-Nearest Neighbours algroth
# this will be the first version, 
# just for explaining the priciple.

# data_set like:
# 40920   8.326976    0.953952    3
# 14488   7.153469    1.673904    2
# 26052   1.441871    0.805124    1

from numpy import *
import knn
from pprint import pprint as pp

def get_data_set_from_file(filename):
    with open(filename) as data_file:
        all_mat = matrix([ [item for item in line.strip().split('\t')] 
            for line in data_file])
    # data_set = all_mat.take(range(3), axis=1).astype(float)
    data_set = all_mat[:, 0:3].astype(float)
    labels = all_mat[:, -1].astype(int)
    labels = labels.flatten().tolist()[0]
    return data_set, labels


def create_date_set():
    data_set = matrix([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A', 'A', 'B', 'B']
    return data_set, labels

def evaluate(output=True):
    ratio = 0.1
    k_value = 3
    data_set, labels = get_data_set_from_file("dating.dataset")
    data_set, m, l = knn.auto_normalize(data_set)
    row_count = data_set.shape[0]
    row_test_count = int(ratio * row_count)
    test_data_set = data_set[0:row_test_count,:]
    classify_fun = knn.gen_classify_fun(
        [data_set[row_test_count:row_count,:],
        labels[row_test_count:row_count]], k_value)
    def is_right(row, label):
        result = classify_fun(row)
        if (result != label):
            if output:
                print "the classifier came back with: %d, the real answer is: %d" \
                    % (result, label)
            return False
        return True
    result = [is_right(row.tolist()[0], label) 
        for label, row in zip(labels, test_data_set)]
    error_count = result.count(False)
    error_rate = error_count/float(row_test_count)
    if output:
        print "the total error rate is: %f (%d / %d)" \
            % (error_rate, error_count, row_test_count)
    return error_rate

def classify_person(percent_game, fly_miles, ice_cream):
    k_value = 3
    labels_str = ['not at all','in small doses', 'in large doses']
    input_point = array([percent_game, fly_miles, ice_cream])
    data_set, labels = get_data_set_from_file("dating.dataset")
    data_set, value_ranges, min_values = knn.auto_normalize(data_set)
    normalized_point = knn.normalize(input_point, value_ranges, min_values)
    result = knn.classify(normalized_point, data_set, labels, k_value)
    return labels_str[result-1]
    # result_label = knn.classify(input_point-min)
    # ffMiles =

    
def draw(data_set, x, y, labels):
    import matplotlib
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(data_set[:,x], data_set[:,y], 
        15.0*array(labels), 15.0*array(labels))
    plt.show()
            

if __name__ == '__main__':
    import unittest
    class TestKnn(unittest.TestCase):

        def test_get_data_set_from_file(self):
            data_set, labels = get_data_set_from_file("dating.dataset")
            self.assertEqual(len(data_set),1000)
            self.assertEqual(len(labels),1000)


        def test_evaluate(self):
            self.assertEqual(evaluate(output=False), 0.05)
            # pass

        def test_classify_person(self):
            # 72993   10.141740   1.032955    1
            # 14488   7.153469    1.673904    2
            # 35948   6.830792    1.213192    3
            labels_str = ['not at all','in small doses', 'in large doses']
            percent_game, fly_miles, ice_cream = 70000, 20.1, 1.1
            self.assertEqual(classify_person(
                percent_game, fly_miles, ice_cream), labels_str[0])

    unittest.main()

