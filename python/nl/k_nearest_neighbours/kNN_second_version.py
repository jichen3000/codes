# k-Nearest Neighbours algroth
# this will be the first version, 
# just for explaining the priciple.

# data_set like:
# 40920   8.326976    0.953952    3
# 14488   7.153469    1.673904    2
# 26052   1.441871    0.805124    1

from numpy import *
import operator

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

def auto_normalize(data_set):
    min_values = data_set.min(0)
    value_ranges = data_set.max(0) - min_values
    row_count = data_set.shape[0]
    normal_data_set = data_set - tile(
        min_values, (row_count, 1))
    normal_data_set = normal_data_set / tile(
        value_ranges,(row_count, 1))
    return normal_data_set, value_ranges, min_values
    

def most_common(lst):
    return max(set(lst), key=lst.count)

def create_date_set():
    data_set = matrix([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A', 'A', 'B', 'B']
    return data_set, labels

def calculate_distance(input_point, data_set):
    data_set_size = data_set.shape[0]
    # copy input_point, and minus every point
    diff_mat = tile(input_point, (data_set_size, 1)) - data_set
    sq_diff_mat = array(diff_mat) ** 2
    sq_distances = sq_diff_mat.sum(axis = 1)
    distances = sq_distances ** 0.5
    return distances

def vote_k_labels(distances, labels, k_value):
    # Returns the indices that would sort an array
    sorted_k_indicies = distances.argsort()[0:k_value]
    return [labels[i] for i in sorted_k_indicies]

def classify(input_point, data_set, labels, k_value):
    distances = calculate_distance(input_point, data_set)
    sorted_labels = vote_k_labels(distances, labels, k_value)
    return most_common(sorted_labels)

def evaluate(output=True):
    ratio = 0.1
    k_value = 3
    data_set, labels = get_data_set_from_file("dating.dataset")
    data_set, m, l = auto_normalize(data_set)
    row_count = data_set.shape[0]
    row_test_count = int(ratio * row_count)
    test_data_set = data_set[0:row_test_count,:]
    caculating_data_set = data_set[row_test_count:row_count,:]
    caculating_labels = labels[row_test_count:row_count]
    def is_right(row, label):
        result = classify(row, 
            caculating_data_set, caculating_labels, k_value)
        if (result != label):
            if output:
                print "the classifier came back with: %d, the real answer is: %d" \
                    % (result, label)
            return False
        return True
    result = [is_right(row.tolist()[0], labels[index]) 
        for index, row in enumerate(test_data_set)]
    error_count = result.count(False)
    error_rate = error_count/float(row_test_count)
    if output:
        print "the total error rate is: %f (%d / %d)" \
            % (error_rate, error_count, row_test_count)
    return error_rate

def normalize(point, value_ranges, min_values):
    return (point - min_values) / value_ranges



def classify_person(percent_game, fly_miles, ice_cream):
    k_value = 3
    labels_str = ['not at all','in small doses', 'in large doses']
    input_point = array([percent_game, fly_miles, ice_cream])
    data_set, labels = get_data_set_from_file("dating.dataset")
    data_set, value_ranges, min_values = auto_normalize(data_set)
    normalized_point = normalize(input_point, value_ranges, min_values)
    result = classify(normalized_point, data_set, labels, k_value)
    return labels_str[result-1]
    # result_label = classify(input_point-min)
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
        def setUp(self):
            self.input_point = (2.0, 1.0)
            self.data_set, self.labels = create_date_set()
            self.k_value = 2
            self.expect_distances = array(
                [ 1.00498756, 1.0, 2.23606798,  2.19317122])

        def test_calculate_distance(self):
            actual = calculate_distance(self.input_point, self.data_set)
            self.assertTrue(allclose(actual, self.expect_distances))

        def test_vote_k_labels(self):
            self.assertEqual(
                vote_k_labels(self.expect_distances, 
                    self.labels, self.k_value), 
                ['A','A'])

        def test_most_common(self):
            self.assertEqual(most_common([1,2,2,3,3,4,3,4,3,4]), 3)


        def test_classify(self):
            self.assertEqual(classify(self.input_point, 
                self.data_set, self.labels, self.k_value), 'A')

        def test_get_data_set_from_file(self):
            data_set, labels = get_data_set_from_file("dating.dataset")
            self.assertEqual(len(data_set),1000)
            self.assertEqual(len(labels),1000)

        def test_auto_normalize(self):
            data_set, labels = get_data_set_from_file("dating.dataset")
            data_set, l, m  = auto_normalize(data_set)
            self.assertTrue((data_set<=1).all())
            # draw(data_set, 0, 1, labels)

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

