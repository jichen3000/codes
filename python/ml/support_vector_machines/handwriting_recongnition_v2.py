import os
from numpy import *

from rbf_smo_v2 import *

IMG_SIZE = 32

def binary_number_to_lists(file_path):
    with open(file_path) as data_file:
        result = [int(line[index]) for line in data_file 
            for index in range(IMG_SIZE)]
    return result

def binary_number_to_intn_lists(file_path, split_number=16):
    with open(file_path) as data_file:
        result = [int(line[index*split_number:(index+1)*split_number],2) 
            for line in data_file for index in range(IMG_SIZE/split_number)]
    return result

def get_dataset_from_filenames(path_name, file_names, 
    binary_func=binary_number_to_lists):
    return [binary_func(os.path.join(path_name,file_name))
        for file_name in file_names]

def get_label_from_filename(filename):
    return int(filename.split('_')[0])

def get_labels_from_filenames(file_names):
    return map(get_label_from_filename, file_names)

def flat(lst):
    return [item for sublist in lst for item in sublist]

def filter_filenames_with_num(pathname,start_with_number):
    '''
        return list of list of the file names under the path.
        Like:
            [ ['0_0.dataset', ... '0_99.dataset'],
                ...
              ['9_0.dataset', ... '9_99.dataset'] ]
    '''
    num_str = str(start_with_number)
    return [filename for filename in os.listdir(pathname) if filename.startswith(num_str)] 

def filter_filenames_with_numbers(pathname,numbers):
    all_filenames = [filter_filenames_with_num(pathname,num) for num in numbers]
    return flat(all_filenames)

def transfer_values(arr, rule_hash, is_reverse=False):
    '''
        rule_hash = {0:1, 255:0}
    '''
    if not is_reverse:
        for source, target in rule_hash.items():
            arr[arr==source] = target
    else:
        for target, source in rule_hash.items():
            arr[arr==source] = target
    return arr

if __name__ == '__main__':
    from minitest import *

    pic_path = '../k_nearest_neighbours'
    training_pic_path = os.path.join(pic_path,'training_digits')
    test_pic_path = os.path.join(pic_path,'test_digits')
    file00_path = os.path.join(training_pic_path,'0_0.dataset')

    with test("binary_number_to_lists"):
        dataset = binary_number_to_lists(file00_path)
        # dataset.p()
        dataset.size().must_equal(1024)
        dataset.count(1).must_equal(303)

        # cur_pic_path = '../../projects/font_number_binary/number_images'
        # file01_path = os.path.join(cur_pic_path, '0_italic_bold_antiqua.txt')
        # dataset = binary_number_to_lists(file01_path)
        # dataset.size().pp()
        # dataset.count(1).pp()


    with test("binary_number_to_intn_lists"):
        dataset = binary_number_to_intn_lists(file00_path)
        # dataset.p()
        dataset.size().must_equal(64)
        dataset[1].must_equal(32768)

    with test("filter_filenames_with_num"):
        filename_list = os.listdir(training_pic_path)
        len(filename_list).must_equal(1934)
        # filename_list.p()
        all_filenames = [filter_filenames_with_num(training_pic_path, i) for i in range(10)]
        all_filenames[0][0].must_equal('0_0.dataset')
        all_filenames[-1][-1].must_equal('9_99.dataset')
        # file0_names = filter_filenames_with_num(training_pic_path, 0)
        len(all_filenames[0]).must_equal(189)
        len(all_filenames[5]).must_equal(187)
        len(all_filenames[9]).must_equal(204)

    with test("filter_filenames_with_numbers"):
        filenames_059 = filter_filenames_with_numbers(training_pic_path,[0,5,9])
        filenames_059.size().must_equal(580)
        filenames_059[0].must_equal('0_0.dataset')
        filenames_059[-1].must_equal('9_99.dataset')

    with test("get_dataset_from_filenames"):
        dataset_matrix05 = mat(get_dataset_from_filenames(training_pic_path, 
                all_filenames[0]+all_filenames[5]))
        dataset_matrix05.shape.must_equal((376, 1024))

        # cur_pic_path = '../../projects/font_number_binary/number_images'
        # cur_all_filenames = [filter_filenames_with_num(cur_pic_path, i) for i in range(10)]
        # dataset_matrix05 = mat(get_dataset_from_filenames(cur_pic_path, 
        #         cur_all_filenames[0]+cur_all_filenames[5]))
        # dataset_matrix05.shape.must_equal((216, 1024))


    with test("get_labels_from_filenames"):
        labels05 = get_labels_from_filenames(all_filenames[0]+all_filenames[5])
        labels05.size().must_equal(376)
        labels05.count(0).must_equal(189)
        labels05.count(5).must_equal(187)
        # labels05.p()


    with test("gen statics"):
        cur_pic_path = '../../projects/font_number_binary/number_images'
        training_pic_path = cur_pic_path
        arg_exp=20
        edge_threshold, tolerance = 200, 0.0001
        max_count = 1000
        numbers = [9,1,5,4, 2,3,6,7,8,0]
        # numbers = [9,1]
        filenames = filter_filenames_with_numbers(training_pic_path,numbers)
        # filenames.pp()
        training_data_matrix = mat(get_dataset_from_filenames(training_pic_path, 
                filenames))
        training_label_matrix = mat(get_labels_from_filenames( 
                filenames)).transpose()
        # transfer_hash = {number1:1}
        transfer_hash = {numbers[0]:-1, 
            numbers[1]:1,
            numbers[2]:1,
            numbers[3]:1, 
            numbers[4]:1,
            numbers[5]:1, 
            numbers[6]:1,
            numbers[7]:1, 
            numbers[8]:1, 
            numbers[9]:1}
        training_label_matrix = transfer_values(training_label_matrix, transfer_hash)
        training_label_matrix.shape.pp()
        training_data_matrix.shape.pp()
        # training_data_matrix.pp()
        # training_data_matrix.pp()
        # training_label_matrix.p()

        # training_data_matrix, training_label_matrix = matrix_dataset_labels(
        #     get_handwriting_dataset('../k_nearest_neighbours/training_digits'))
        # training_data_matrix, training_label_matrix = get_data_matrix_from_file('test_set_RBF.dataset')

        smo = Smo(training_data_matrix, training_label_matrix, edge_threshold, tolerance)
        smo.train(max_count, arg_exp)
        smo.gen_training_statics().pp()

        # testing_data_matrix, testing_label_matrix = get_data_matrix_from_file('test_set_RBF2.dataset')

        # smo.gen_testing_statics(testing_data_matrix, testing_label_matrix).pp()

