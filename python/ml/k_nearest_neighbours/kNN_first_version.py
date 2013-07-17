# k-Nearest Neighbours algroth
# this will be the first version, 
# just for explaining the priciple.

from numpy import *
import operator

from pprint import pprint as pp

def most_common(lst):
    return max(set(lst), key=lst.count)

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

def vote_k_labels(distances, labels, k_value):
    # Returns the indices that would sort an array
    sorted_k_indicies = distances.argsort()[0:k_value]
    return [labels[i] for i in sorted_k_indicies]

def classify(input_point, data_set, labels, k_value):
    distances = calculate_distance(input_point, data_set)
    sorted_labels = vote_k_labels(distances, labels, k_value)
    return most_common(sorted_labels)

    

if __name__ == '__main__':
    import unittest
    class TestKnn(unittest.TestCase):
        def setUp(self):
            self.input_point = [2.0, 1.0]
            self.group, self.labels = create_date_set()
            self.k_value = 2
            self.expect_distances = array(
                [ 1.00498756, 1.0, 2.23606798,  2.19317122])

        def test_calculate_distance(self):
            actual = calculate_distance(self.input_point, self.group)
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
                self.group, self.labels, self.k_value), 'A')
            
    unittest.main()

