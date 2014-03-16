'''
    this version copied from the book, and I've tested it with the data,
    the result is perfect.
'''

import os
import numpy

import json

IMG_SIZE = 32


def random_select(except_value, range_max):
    ''' select a value from 0 to m randomly, but not equal the value of except_value '''
    result=except_value
    while (result==except_value):
        result = int(numpy.random.uniform(0,range_max))
    return result



def clip_value(value, high_threshold,low_threshold):
    ''' reset a value according to a range from low_threshold to  high_threshold '''
    if value >  high_threshold:
        value =  high_threshold
    if value < low_threshold:
        value = low_threshold
    return value

def rbf_kernel(data_matrix, row_matrix, arg_exp):
    row_count = data_matrix.shape[0]
    transfered_row_matrix = numpy.mat(numpy.zeros((row_count,1)))
    for row_index in range(row_count):
        delta_row = data_matrix[row_index,:] - row_matrix
        transfered_row_matrix[row_index] = delta_row * delta_row.T
    transfered_row_matrix = numpy.exp( transfered_row_matrix / (-1*arg_exp**2))
    return transfered_row_matrix


def save_to_json_nicely(file_path, content):
    with open(file_path,'w') as the_file:
        json_content = json.dumps(content, sort_keys=True,
                 indent=4, separators=(',', ': '))
        the_file.write(json_content)
    return True

def load_from_json(file_path):
    with open(file_path, 'r') as the_file:
        return json.loads(the_file.read())

def most_common(lst):
    return max(set(lst), key=lst.count)

def is_any_member_in_list(source_list, target_list):
    is_in_list = tuple((label in target_list) for label in source_list)
    return any(is_in_list)

def flatten_for_two_layers(the_list):
    return [item for sub_list in the_list for item in sub_list]

class SmoBasic(object):
    def __init__(self, data_matrix, label_matrix, edge_threshold, tolerance, arg_exp):
        self.data_matrix =  data_matrix
        self.label_matrix = label_matrix
        self.edge_threshold = edge_threshold
        self.tolerance = tolerance
        self.row_count, self.col_count = data_matrix.shape
        self.alphas = numpy.mat(numpy.zeros((self.row_count,1)))
        self.b = 0
        self.error_cache = numpy.mat(numpy.zeros((self.row_count,2)))
        self.k_data_matrix = numpy.mat(numpy.zeros((self.row_count,self.row_count)))
        for i in range(self.row_count):
            self.k_data_matrix[:,i] = rbf_kernel(self.data_matrix, self.data_matrix[i,:], arg_exp)


    def calculate_error(self, row_index):
        fx = float(numpy.multiply(self.alphas,self.label_matrix).T * self.k_data_matrix[:,row_index]) + self.b
        return fx - float(self.label_matrix[row_index])

    def get_valid_error_cache_index_list(self):
        ''' get the first col as array, and get the non zero index values list'''
        return numpy.nonzero(self.error_cache[:,0].A)[0]


    def get_index_and_max_delta_error(self, valid_error_cache_index_list, first_alpha_error):
        ''' choose second alpha which has the max delta error with first one'''
        # def cal_error_delta(index):
        #     delta_error = abs(first_alpha_error - self.calculate_error(index))
        #     return delta_error
        # valid_error_cache_index_list.pp()
        # error_delta_list = [abs(first_alpha_error - self.calculate_error(i)) for i in valid_error_cache_index_list]
        # # error_delta_list = [(-1,matrix([[ 0.0]]))] + error_delta_list
        # # error_delta_list.pp()
        # # first_alpha_error.pp()
        # # self.calculate_error(5).pp()
        # index, value = get_index_and_max_value(error_delta_list)
        # if not (value > 0.0) :
        #     index = -1
        # (index, value).pp()
        # return index, value
        second_alpha_index = -1
        max_delta_error = 0
        second_alpha_error = 0
        for k in valid_error_cache_index_list:
            error_k = self.calculate_error(k)
            delta_error = abs(first_alpha_error - error_k)
            if (delta_error > max_delta_error):
                second_alpha_index = k
                max_delta_error = delta_error
                second_alpha_error = error_k
        # (second_alpha_index, second_alpha_error).pp()
        return second_alpha_index, second_alpha_error

    def is_error_in_tolerance(self, error_value, index):
        return ((self.label_matrix[index]*error_value < -self.tolerance) 
            and (self.alphas[index] < self.edge_threshold)) or \
            ((self.label_matrix[index]*error_value > self.tolerance) and (self.alphas[index] > 0))

    def cal_edegs(self, first_alpha_index, second_alpha_index):
        if (self.label_matrix[first_alpha_index] != self.label_matrix[second_alpha_index]):
            L = max(0, self.alphas[second_alpha_index] - self.alphas[first_alpha_index])
            H = min(self.edge_threshold, self.edge_threshold + self.alphas[second_alpha_index] - 
                self.alphas[first_alpha_index])
        else:
            L = max(0, self.alphas[second_alpha_index] + self.alphas[first_alpha_index] - self.edge_threshold)
            H = min(self.edge_threshold, self.alphas[second_alpha_index] + self.alphas[first_alpha_index])
        return L,H

    def cal_eta(self, first_alpha_index, second_alpha_index):
        # return 2.0 * self.data_matrix[first_alpha_index,:]*self.data_matrix[second_alpha_index,:].T - \
        #     self.data_matrix[first_alpha_index,:]*self.data_matrix[first_alpha_index,:].T - \
        #     self.data_matrix[second_alpha_index,:]*self.data_matrix[second_alpha_index,:].T
        return 2.0 * self.k_data_matrix[first_alpha_index,second_alpha_index] - \
            self.k_data_matrix[first_alpha_index,first_alpha_index] - self.k_data_matrix[second_alpha_index,second_alpha_index]


    def cal_second_alpha(self, first_alpha_error, 
            second_alpha_index, second_alpha_error, second_alpha_value, eta, H, L):
        result = second_alpha_value - self.label_matrix[second_alpha_index]* \
            (first_alpha_error - second_alpha_error)/eta
        result = clip_value(result,H,L)
        return result, (result-second_alpha_value)
        # self.alphas[second_alpha_index] -= self.label_matrix[second_alpha_index]* \
        #     (first_alpha_error - second_alpha_error)/eta
        # self.alphas[second_alpha_index] = clip_value(self.alphas[second_alpha_index],H,L)

    def is_moving_enough(self, delta_value):
        return (abs(delta_value) >= 0.00001)

    def cal_first_alpha(self, first_alpha_index, first_alpha_value, 
            second_alpha_index, delta_second_alpha):
        result = first_alpha_value - self.label_matrix[second_alpha_index] * \
            self.label_matrix[first_alpha_index] * delta_second_alpha
        return result, (result - first_alpha_value)

    def cal_b(self, b, first_alpha_index, first_alpha_error, delta_first_alpha,
            second_alpha_index, second_alpha_error, delta_second_alpha):

        delta_first_label = self.label_matrix[first_alpha_index]*(delta_first_alpha)
        delta_second_label = self.label_matrix[second_alpha_index]*(delta_second_alpha)

        b1 = b - first_alpha_error - \
                delta_first_label * self.k_data_matrix[first_alpha_index,first_alpha_index] - \
                delta_second_label * self.k_data_matrix[first_alpha_index,second_alpha_index] 
        b1 = b1[0,0]
        if (0 < self.alphas[first_alpha_index]) and (self.edge_threshold > self.alphas[first_alpha_index]): 
            return b1

        b2 = b - second_alpha_error - \
                delta_first_label * self.k_data_matrix[first_alpha_index,second_alpha_index] - \
                delta_second_label * self.k_data_matrix[second_alpha_index,second_alpha_index]
        b2 = b2[0,0]
        if (0 < self.alphas[second_alpha_index]) and (self.edge_threshold > self.alphas[second_alpha_index]): 
            return b2
        
        return (b1 + b2)/2.0


    # main
    def select_second_alpha(self, first_alpha_index, first_alpha_error):
        ''' selects the second alpha, or the inner loop alpha 
            the goal is to choose the second alpha so that 
            we'll take the maximum step during each optimization.'''

        valid_error_cache_index_list = self.get_valid_error_cache_index_list()

        self.update_error_cache(first_alpha_index, first_alpha_error)

        if (len(valid_error_cache_index_list)) > 0:
            second_alpha_index, second_alpha_error = self.get_index_and_max_delta_error(
                valid_error_cache_index_list, first_alpha_error)
        else:
            second_alpha_index = random_select(first_alpha_index, self.row_count)
            second_alpha_error = self.calculate_error(second_alpha_index)

        return second_alpha_index, second_alpha_error

    def update_error_cache(self, index, error_value=None):
        if error_value:
            self.error_cache[index] = [1, error_value]
        else:
            self.error_cache[index] = [1, self.calculate_error(index)]

    # main
    def choose_alphas(self, first_alpha_index):
        first_alpha_error = self.calculate_error(first_alpha_index)
        if not self.is_error_in_tolerance(first_alpha_error, first_alpha_index):
            return 0

        second_alpha_index,second_alpha_error = self.select_second_alpha(first_alpha_index, first_alpha_error)
        L, H = self.cal_edegs(first_alpha_index,second_alpha_index)        
        # Guarantee alphas stay between 0 and edge_threshold
        if L==H: 
            return 0

        eta = self.cal_eta(first_alpha_index, second_alpha_index)
        # Eta is the optimal amount to change alpha[second_alpha_index].
        if eta >= 0: 
            return 0


        self.alphas[second_alpha_index], delta_second_alpha = self.cal_second_alpha(
            first_alpha_error, second_alpha_index, second_alpha_error, self.alphas[second_alpha_index], eta, H, L)

        self.update_error_cache(second_alpha_index)

        if not self.is_moving_enough(delta_second_alpha):
            return 0

        self.alphas[first_alpha_index],  delta_first_alpha = self.cal_first_alpha(
            first_alpha_index, self.alphas[first_alpha_index], 
            second_alpha_index, delta_second_alpha)

        self.update_error_cache(first_alpha_index)

        self.b = self.cal_b(self.b, first_alpha_index, first_alpha_error, delta_first_alpha,
            second_alpha_index, second_alpha_error, delta_second_alpha)
        return 1
        
    def get_non_bound_index_list(self):
        return numpy.nonzero((self.alphas.A > 0) * (self.alphas.A < self.edge_threshold))[0]

    # main
    def cal_alphas_and_b(self, max_iteration_count): 
        # self.init_for_recal_alphas_and_b(arg_exp)
        is_entire_set = True
        alpha_pairs_changed_count = 0
        iter_index = 0
        # you pass through the entire set without changing any alpha pairs.
        while (iter_index < max_iteration_count) and \
                ((alpha_pairs_changed_count > 0) or (is_entire_set)):
            if is_entire_set:
                index_range = range(self.row_count)
            else:
                index_range = self.get_non_bound_index_list()
            alpha_pairs_changed_count = sum(map(self.choose_alphas, index_range))
            if is_entire_set: 
                is_entire_set = False
            elif (alpha_pairs_changed_count == 0): 
                is_entire_set = True
            iter_index += 1
        return self.alphas, self.b

class Smo(object):
    def __init__(self, selected_data_matrix, selected_alphas_label_matrix, b, arg_exp,transfer_hash):
        self.selected_data_matrix = selected_data_matrix
        self.selected_alphas_label_matrix = selected_alphas_label_matrix
        self.svm_count = selected_alphas_label_matrix.shape[0]
        self.b = b
        self.arg_exp = arg_exp
        self.transfer_hash = transfer_hash
        self.reversed_transfer_hash = {v:k for k, v in self.transfer_hash.items()}

        self.last_test_info = {}

    @classmethod
    def train(cls, data_matrix, label_matrix, edge_threshold, tolerance, max_iteration_count, arg_exp, transfer_hash): 
        label_matrix = transfer_values(label_matrix, transfer_hash)
        smo_basic = SmoBasic(data_matrix, label_matrix,edge_threshold,tolerance,arg_exp) 
        alphas,b =  smo_basic.cal_alphas_and_b(max_iteration_count)

        nonzero_indexs = numpy.nonzero(alphas.A>0)[0]
        selected_data_matrix = data_matrix[nonzero_indexs]
        selected_alphas_label_matrix = numpy.multiply(label_matrix[nonzero_indexs], alphas[nonzero_indexs])

        return cls(selected_data_matrix, selected_alphas_label_matrix, b, arg_exp, transfer_hash)

    selected_data_matrix_name = 'selected_data_matrix.dataset'+'.npy'
    selected_alphas_label_matrix_name = 'selected_alphas_label_matrix.dataset'+'.npy'
    other_variables_name = 'other_variables.dataset'

    @classmethod
    def get_file_paths(cls, data_path, prefix):
        def gen_path(name):
            return os.path.join(data_path, prefix+name)
        paths ={'selected_data_matrix': gen_path(cls.selected_data_matrix_name),
                'selected_alphas_label_matrix': gen_path(cls.selected_alphas_label_matrix_name),
                'other_variables': gen_path(cls.other_variables_name)
                }
        return paths


    @classmethod
    def load_variables(cls, data_path='dataset', prefix=''):
        paths = cls.get_file_paths(data_path, prefix)

        selected_data_matrix = numpy.load(paths['selected_data_matrix'])
        selected_alphas_label_matrix = numpy.load(paths['selected_alphas_label_matrix'])

        other_variables = load_from_json(paths['other_variables'])
        # with open(paths['other_variables'], 'r') as the_file:
        #     other_variables = json.loads(the_file.read())
        other_variables['transfer_hash'] = dict(other_variables['transfer_hash'])

        return cls(selected_data_matrix, selected_alphas_label_matrix, 
                other_variables['b'], other_variables['arg_exp'], other_variables['transfer_hash'])

    def save_variables(self, data_path='dataset', prefix=''):
        paths = self.get_file_paths(data_path, prefix)

        numpy.save(paths['selected_data_matrix'], self.selected_data_matrix)
        numpy.save(paths['selected_alphas_label_matrix'], self.selected_alphas_label_matrix)

        # notice, I save the dict.items(), since json will automatically convert the key to string.
        other_variables = { 'b': self.b, 
                            'arg_exp': self.arg_exp, 
                            'transfer_hash': self.transfer_hash.items(),
                            'svm_count': self.svm_count,
                            'last_test_info': self.last_test_info}
        # other_variables.pp()
        save_to_json_nicely(paths['other_variables'], other_variables)
        # with open(paths['other_variables'],'w') as the_file:
        #     content = json.dumps(other_variables, sort_keys=True,
        #                  indent=4, separators=(',', ': '))
        #     the_file.write(content)
        return True

    def __package_info(self, error_count, row_count):
        return {'error_ratio %':round(float(error_count)/row_count * 100, 2),
                'error_count': error_count,
                'row_count': row_count,
                'svm_count': self.svm_count,
                'transfer_hash': self.transfer_hash}

    def test(self, testing_data_matrix, testing_label_matrix):
        testing_label_matrix = transfer_values(testing_label_matrix, self.transfer_hash)
        row_count = testing_data_matrix.shape[0]

        errors = tuple(self.__classify(testing_data_matrix[i, :])!=numpy.sign(testing_label_matrix[i,0]) 
            for i in range(row_count))
        self.last_test_info = self.__package_info(errors.count(True), row_count)
        return self.last_test_info

    def __classify(self, row_matrix):
        kernel_value = rbf_kernel(self.selected_data_matrix, 
            row_matrix, self.arg_exp)
        predict = kernel_value.T * self.selected_alphas_label_matrix + self.b
        return numpy.sign(predict[0,0])

    def classify(self, row_matrix):
        return self.reversed_transfer_hash[
                self.__classify(row_matrix)]
        


''' split line '''
''' for multiple binary'''
def get_all_posible_indexs(the_list):
    return tuple((i,j) for i in the_list for j in the_list if i<j)

class MultipleBinary(object):
    '''
        one against one
        Direct Acyclic Graph, DAG will let classify more efficient.
    '''
    def __init__(self, binary_class):
        self.binary_class = binary_class
        self.classifying_hash = {}
        
    variables_file_name = 'multiple_binary.dataset'

    def build_classifying_objects(self, data_matrix_hash, 
                edge_threshold, tolerance, max_iteration_count, arg_exp, data_path):
        def gen_label_matrix(label_value, count):
            return numpy.mat(numpy.zeros((count, 1), numpy.int8)) + label_value

        for label_i, label_j in get_all_posible_indexs(data_matrix_hash.keys()):
            data_matrix = numpy.concatenate((data_matrix_hash[label_i], 
                                       data_matrix_hash[label_j]), axis=0)
            label_i_matrix = gen_label_matrix(label_i, data_matrix_hash[label_i].shape[0])
            label_j_matrix = gen_label_matrix(label_j, data_matrix_hash[label_j].shape[0])
            label_matrix = numpy.concatenate((label_i_matrix, label_j_matrix), axis=0)

            classifying_key = (label_i, label_j)
            file_prefix = '_'.join((str(label_i),  str(label_j), ''))
            transfer_hash = {label_i:-1, label_j:1}

            self.label_tuple = tuple(data_matrix_hash.keys())

            smo = self.binary_class.train(data_matrix,label_matrix, 
                    edge_threshold, tolerance, max_iteration_count, arg_exp, transfer_hash)
            smo.test(data_matrix,label_matrix).pp()
            smo.save_variables(data_path, prefix = file_prefix)
            self.classifying_hash[classifying_key]=smo

        return self

    def normal_classify(self, row_matrix):
        '''
            It's the normal classify, it will take more times ((len(labels)-1)/2) than the dag, 
            but the answer almost equal with dag.
            {'error_count': 36, 'error_ratio %': 3.81, 'row_count': 946}
            Finished tests in 94.411094s.
        '''
        occurence_hash = { classifying_key:classifying_object.classify(row_matrix)
                for classifying_key, classifying_object in self.classifying_hash.items()}
        return most_common(occurence_hash.values()), occurence_hash


    def dag_classify(self, row_matrix):
        '''
            Direct Acyclic Graph, DAG will let classify more efficient.
            The classify times are only the length of labels.

            {'error_count': 37, 'error_ratio %': 3.91, 'row_count': 946}
            Finished tests in 20.857392s.    
        '''
        predict_label = self.label_tuple[0]
        order_labels = []
        for next_label in self.label_tuple[1:]:
            classifying_key = (predict_label, next_label)
            predict_label = self.classifying_hash[classifying_key].classify(row_matrix)
            order_labels.append([(predict_label,)]+list(classifying_key))

        return predict_label, order_labels

    def __package_info(self, error_count, row_count):
        return {'error_ratio %':round(float(error_count)/row_count * 100, 2),
                'error_count': error_count,
                'row_count': row_count}

    def test(self, testing_data_matrix, testing_label_matrix):
        row_count = testing_data_matrix.shape[0]

        # errors = tuple(self.classify(testing_data_matrix[i, :])[0]!=testing_label_matrix[i,0] 
        #     for i in range(row_count))
        # self.last_test_info = self.__package_info(errors.count(True), row_count)
        # return self.last_test_info

        error_count = 0
        result_list = []
        for i in range(row_count):
            result = self.dag_classify(testing_data_matrix[i, :])
            if result[0]!=testing_label_matrix[i,0]:
                error_count += 1
                result_list.append([testing_label_matrix[i,0]]+list(result))

            # if error_count > 40:
            #     break
        result_list.pp()

        self.last_test_info = self.__package_info(error_count, row_count)
        return self.last_test_info

    def save_variables(self, data_path):
        file_path = os.path.join(data_path, self.variables_file_name)
        save_to_json_nicely(file_path, self.classifying_hash.keys())
        return True

    def gen_prefix_from_list(self, the_list):
        ''' 
            the_list like: (0, 9)
            result: '_0_9_'
        '''
        return '_'.join(map(str, the_list) + [''])

    def gen_binary_transfer_hash(self, the_list):
        ''' 
            the_list like: (0, 9)
            result: {0: -1, 9:1}
        '''
        return {the_list[0]:-1, the_list[1]:1}

    @classmethod
    def load_variables(cls, binary_class, data_path):
        self = MultipleBinary(binary_class)
        # dir(self).pp()
        file_path = os.path.join(data_path, self.variables_file_name)
        keys = load_from_json(file_path)
        keys = map(tuple, keys)
        self.label_tuple = tuple(set(flatten_for_two_layers(keys)))

        for classifying_key in keys:
            file_prefix = self.gen_prefix_from_list(classifying_key)
            transfer_hash = self.gen_binary_transfer_hash(classifying_key)

            smo = self.binary_class.load_variables(data_path, file_prefix)
            self.classifying_hash[classifying_key]=smo

        return self

    @classmethod
    def train_and_save_variables(cls, binary_class, data_matrix_hash,
            edge_threshold, tolerance, max_iteration_count, arg_exp, data_path='dataset'):

        this = cls(binary_class)
        this.build_classifying_objects(data_matrix_hash,
            edge_threshold, tolerance, max_iteration_count, arg_exp, data_path)
        this.save_variables(data_path)
        return this


''' split line '''
''' for digital recongnition'''





def filter_filenames_with_nums(pathname,start_with_numbers):
    num_strs = map(str, start_with_numbers)
    # num_str = str(start_with_number)
    return [filename for filename in os.listdir(pathname) 
        for num_str in num_strs if filename.startswith(num_str)]

def save_list(file_path, the_list):
    with open(file_path, 'w') as the_file:
        for item in the_list:
            the_file.write("%s\n" % item)

def load_data_from_images_with_nums(the_path, start_with_numbers):
    file_names = filter_filenames_with_nums(the_path, start_with_numbers)
    data_matrix = numpy.mat(get_dataset_from_filenames(the_path, 
            file_names))
    label_matrix = numpy.mat(get_labels_from_filenames( 
            file_names)).transpose()
    return data_matrix, label_matrix


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

def transfer_values(arr, rule_hash):
    '''
        rule_hash = {0:1, 255:0}
    '''
    result = arr.copy()
    for (i, j), value in numpy.ndenumerate(result):
        # if value in rule_hash.keys():
        result[i,j] = rule_hash[value]
    return result


def get_dataset_matrix_hash(the_path, start_with_numbers):
    return {i:numpy.mat(get_dataset_from_filenames(the_path, 
        filter_filenames_with_nums(the_path,(i,)))) for i in start_with_numbers}




if __name__ == '__main__':
    from minitest import *

    def test_one_to_one(arg_exp=20):
        cur_pic_path = '../../projects/font_number_binary/number_images'
        pic_path = '../k_nearest_neighbours'
        training_pic_path = os.path.join(pic_path,'training_digits')
        # training_pic_path = cur_pic_path
        test_pic_path = os.path.join(pic_path,'test_digits')
        # test_pic_path = cur_pic_path


        data_matrix,label_matrix = load_data_from_images_with_nums(training_pic_path, (9,1))
        data_matrix.shape.pp()
        label_matrix.shape.pp()
        
        # delimiter=' '
        # fmt = '%1d'
        # savetxt('data_array.dataset', data_matrix, fmt=fmt, delimiter=delimiter)
        # savetxt('label_array.dataset', label_matrix, fmt=fmt, delimiter=delimiter)


        smo = Smo.train(data_matrix,label_matrix, 200, 0.0001, 1000, arg_exp,{9:-1, 1:1})
        smo.test(data_matrix,label_matrix).pp()
        smo.save_variables()

        # smo = Smo.load_variables()
        # smo.test(data_matrix,label_matrix).pp()

        data_matrix,label_matrix = load_data_from_images_with_nums(test_pic_path, (9,1))
        smo.test(data_matrix,label_matrix).pp()

        smo.classify(data_matrix[0]).must_equal(label_matrix[0,0])


    with test("test_one_to_one"):
        # test_one_to_one()
        pass

    def test_multi():
        arg_exp = 20
        cur_pic_path = '../../projects/font_number_binary/number_images'
        pic_path = '../k_nearest_neighbours'
        # training_pic_path = os.path.join(pic_path,'training_digits')
        training_pic_path = cur_pic_path
        test_pic_path = os.path.join(pic_path,'test_digits')
        # test_pic_path = cur_pic_path

        # dataset_matrix_hash = get_dataset_matrix_hash(training_pic_path, range(2))
        # dataset_matrix_hash = get_dataset_matrix_hash(training_pic_path, range(10))
        # dataset_matrix_hash = get_dataset_matrix_hash(training_pic_path, (9,))
        # dataset_matrix_hash.pp()

        # mb = MultipleBinary.train_and_save_variables(Smo, dataset_matrix_hash, 200, 0.0001, 1000, arg_exp)
        # mb = MultipleBinary.load_variables(Smo, 'font_dataset')
        mb = MultipleBinary.load_variables(Smo, 'hand_dataset')
        # mb.classify(dataset_matrix_hash[9][0]).pp()
        # mb.normal_classify(dataset_matrix_hash[9][0]).pp()

        data_matrix,label_matrix = load_data_from_images_with_nums(test_pic_path, range(10))
        mb.test(data_matrix,label_matrix).pp()
        # training_digits
        # {'error_count': 38, 'error_ratio %': 4.02, 'row_count': 946}
        pass

    with test("test_multi"):
        test_multi()
        pass
