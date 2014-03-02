import os
from numpy import *

from rbf_smo_v2 import *

IMG_SIZE = 32

def img_to_vector(filename):
    with open(filename) as data_file:
        result = [int(line[index]) for line in data_file 
            for index in range(IMG_SIZE)]
    return result

def get_label_from_filename(filename):
    # filename.p()
    return filename.split('_')[0]

def get_label_and_data(pathname,filename):
    return get_label_from_filename(filename), img_to_vector(os.path.join(
            pathname, filename))

def get_handwriting_dataset(pathname, filename_list):
    label_and_data_list = [get_label_and_data(pathname, filename) 
        for filename in filename_list]
    labels, dataset = zip(*label_and_data_list)
    return array(dataset), to_binary_labels(labels)

def filter_filenames_with_num(pathname,start_with_number):
    num_str = str(start_with_number)
    # num_str.p()
    # filter(os.listdir)
    return [filename for filename in os.listdir(pathname) if filename.startswith(num_str)] 

def to_binary_labels(labels):
    return [-1 if label=='9' else 1 for label in labels]

if __name__ == '__main__':
    from minitest import *

    pic_path = '../k_nearest_neighbours'
    training_pic_path = os.path.join(pic_path,'training_digits')
    test_pic_path = os.path.join(pic_path,'test_digits')

    with test("filter_filenames_with_num"):
        filename_list = os.listdir(training_pic_path)
        len(filename_list).must_equal(1934)
        # filename_list.p()
        all_filenames = [filter_filenames_with_num(training_pic_path, i) for i in range(10)]
        # file0_names = filter_filenames_with_num(training_pic_path, 0)
        len(all_filenames[0]).must_equal(189)
        len(all_filenames[5]).must_equal(187)
        len(all_filenames[9]).must_equal(204)

    with test("img_to_vector"):
        img_vector00 = img_to_vector(os.path.join(training_pic_path,'0_0.dataset'))
        len(img_vector00).must_equal(1024)

    with test("gen statics"):
        arg_exp=10
        edge_threshold, tolerance = 200, 0.0001
        max_count = 100
        # training_data_matrix, training_label_matrix = matrix_dataset_labels(
        #     get_handwriting_dataset('../k_nearest_neighbours/training_digits'))
        # training_data_matrix, training_label_matrix = get_data_matrix_from_file('test_set_RBF.dataset')

        # smo = Smo(training_data_matrix, training_label_matrix, edge_threshold, tolerance)
        # smo.train(max_count, arg_exp)
        # smo.gen_training_statics().pp()

        # testing_data_matrix, testing_label_matrix = get_data_matrix_from_file('test_set_RBF2.dataset')

        # smo.gen_testing_statics(testing_data_matrix, testing_label_matrix).pp()

