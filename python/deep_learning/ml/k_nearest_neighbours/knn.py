# k-Nearest Neighbours algroth

from numpy import *

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

def gen_classify_fun(data_set_and_labels, k_value):
    def fixed_classify(input_point):
        return classify(input_point, data_set_and_labels[0], 
            data_set_and_labels[1], k_value)
    return fixed_classify



def normalize(point, value_ranges, min_values):
    return (point - min_values) / value_ranges

def evaluate(classify_fun, test_dataset, test_labels, k_value):
    test_count = len(test_labels)

    result = [(index, actual_label, expected_lable, row) 
        for index, row, actual_label, expected_lable 
        in zip(range(test_count), test_dataset, 
            map(classify_fun,test_dataset), test_labels) 
        if (actual_label != expected_lable)]
    error_count = len(result)
    error_rate = error_count * 1.0 / test_count
    return (error_rate, error_count, test_count),result

            

if __name__ == '__main__':
    import unittest
    class TestKnn(unittest.TestCase):
        def create_date_set(self):
            data_set = array([[1.0,100],[1.0,100],[0,0],[0,10]])
            labels = ('A', 'A', 'B', 'B')
            return data_set, labels

        def setUp(self):
            self.input_point = (0.9, 80)
            self.data_set, self.labels = self.create_date_set()
            self.k_value = 2
            self.expect_distances = array(
                [20.00025,     20.00025,     80.00506234,  70.00578548])

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

        def test_auto_normalize(self):
            data_set, l, m  = auto_normalize(self.data_set)
            self.assertTrue((data_set<=1).all())

        def test_gen_classify_fun(self):
            fixed_classify = gen_classify_fun(self.create_date_set(), 
                self.k_value)
            self.assertEqual(fixed_classify(self.input_point), "A")


    unittest.main()

