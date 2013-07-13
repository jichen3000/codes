# k-Nearest Neighbours algroth
# this will be the first version, 
# just for explaining the priciple.

from numpy import *
import operator

from pprint import pprint as pp

def create_date_set():
    group = array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels

def calculate_distance(input_point, data_set):
    data_set_size = data_set.shape[0]
    # copy input_point, and minus every point
    diff_mat = tile(input_point, (data_set_size, 1)) - data_set
    sq_diff_mat = diff_mat ** 2
    sq_distances = sq_diff_mat.sum(axis = 1)
    distances = sq_distances ** 0.5
    return distances

def vote_k_elements(distances, labels, k_value):
    sorted_dist_indicies = distances.argsort()
    class_count = {}
    for i in range(k_value):
        vote_input_label = labels[sorted_dist_indicies[i]]
        class_count[vote_input_label] = class_count.get(
            vote_input_label, 0) + 1
    return class_count

def select_first_sorted_elements(class_count):
    sorted_class_count = sorted(class_count.iteritems(),
        key=operator.itemgetter(1), reverse=True)
    return sorted_class_count[0][0]

def classify0(input_point, data_set, labels, k_value):
    distances = calculate_distance(input_point, data_set)
    class_count = vote_k_elements(distances, labels, k_value)
    return select_first_sorted_elements(class_count)

import unittest
class TestKnn(unittest.TestCase):
    def setUp(self):
        self.input_point = [2.0, 1.0]
        self.group, self.labels = create_date_set()
        self.k_value = 2

    def test_calculate_distance(self):
        expect = array([ 1.00498756,1.0, 2.23606798,  2.19317122])
        actual = calculate_distance(self.input_point, self.group)
        self.assertTrue(allclose(actual, expect))

    def test_classify0(self):
        self.assertEqual(classify0(self.input_point, 
            self.group, self.labels, self.k_value), 'A')


if __name__ == '__main__':
    unittest.main()

