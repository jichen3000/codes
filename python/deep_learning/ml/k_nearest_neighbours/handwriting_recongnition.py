from numpy import *
import knn
from pprint import pprint as pp
import os

IMG_SIZE = 32

def img_to_vector(filename):
    with open(filename) as data_file:
        result = [int(line[index]) for line in data_file 
            for index in range(IMG_SIZE)]
    return result

def get_label_from_filename(filename):
    return filename.split('_')[0]

def get_label_and_data(pathname,filename):
    return get_label_from_filename(filename), img_to_vector(os.path.join(
            pathname, filename))

def get_handwriting_dataset(pathname):
    label_and_data_list = [get_label_and_data(pathname, filename) 
        for filename in os.listdir(pathname)]
    labels, dataset = zip(*label_and_data_list)
    return array(dataset), labels

def run_evaluate(output=True):
    k_value = 3
    classify_fun = knn.gen_classify_fun(
        get_handwriting_dataset('training_digits'), k_value)
    test_pathname = 'test_digits'
    test_dataset, test_labels = get_handwriting_dataset(
        test_pathname)

    error_list, result = knn.evaluate(
        classify_fun, test_dataset, test_labels, k_value)
    if output:
        print "error info:", error_list
        pp([(os.listdir(test_pathname)[index], "actual:"+actual, "expected:"+expected) 
            for index, actual, expected, content in result])
    return error_list, result


if __name__ == '__main__':
    import unittest
    class TestHandwriting(unittest.TestCase):
        def test_img_to_vector(self):
            vector = img_to_vector('test_digits/0_13.dataset')
            self.assertEqual(vector[0:31],[0, 0, 0, 0, 0, 
                0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0])

        def test_get_handwriting_dataset(self):
            pass
            # dataset, labels= get_handwriting_dataset('test_digits')
            # print(type(labels))
            # print labels[1], len(labels)
            # print(type(dataset))
            # print dataset.shape
            # for data in dataset:
            #     print data[0:31]

        def test_run_evaluate(self):
            result = run_evaluate()
            # print result

    unittest.main()
