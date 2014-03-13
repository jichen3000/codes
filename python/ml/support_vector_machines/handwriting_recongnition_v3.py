'''
    this version copied from the book, and I've tested it with the data,
    the result is perfect.
'''

import os
from numpy import *
# from rbf_smo_v3 import *

IMG_SIZE = 32


def random_select(except_value, range_max):
    ''' select a value from 0 to m randomly, but not equal the value of except_value '''
    result=except_value
    while (result==except_value):
        result = int(random.uniform(0,range_max))
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
    transfered_row_matrix = mat(zeros((row_count,1)))
    for row_index in range(row_count):
        delta_row = data_matrix[row_index,:] - row_matrix
        transfered_row_matrix[row_index] = delta_row * delta_row.T
    transfered_row_matrix = exp( transfered_row_matrix / (-1*arg_exp**2))
    return transfered_row_matrix


class SmoBasic(object):
    def __init__(self, data_matrix, label_matrix, edge_threshold, tolerance, arg_exp):
        self.data_matrix =  data_matrix
        self.label_matrix = label_matrix
        self.edge_threshold = edge_threshold
        self.tolerance = tolerance
        self.row_count, self.col_count = shape(data_matrix)
        self.alphas = mat(zeros((self.row_count,1)))
        self.b = 0
        self.error_cache = mat(zeros((self.row_count,2)))
        self.k_data_matrix = mat(zeros((self.row_count,self.row_count)))
        for i in range(self.row_count):
            self.k_data_matrix[:,i] = rbf_kernel(self.data_matrix, self.data_matrix[i,:], arg_exp)


    def calculate_error(self, row_index):
        fx = float(multiply(self.alphas,self.label_matrix).T * self.k_data_matrix[:,row_index]) + self.b
        return fx - float(self.label_matrix[row_index])

    def get_valid_error_cache_index_list(self):
        ''' get the first col as array, and get the non zero index values list'''
        return nonzero(self.error_cache[:,0].A)[0]


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

        # delta_first_label = self.label_matrix[first_alpha_index]*(delta_first_alpha)
        # delta_second_label = self.label_matrix[second_alpha_index]*(delta_second_alpha)

        # b1 = b - first_alpha_error - \
        #         delta_first_label * self.k_data_matrix[first_alpha_index,first_alpha_index] - \
        #         delta_second_label * self.k_data_matrix[first_alpha_index,second_alpha_index] 
        # if (0 < self.alphas[first_alpha_index]) and (self.edge_threshold > self.alphas[first_alpha_index]): 
        #     return b1

        # b2 = b - second_alpha_error - \
        #         delta_first_label * self.k_data_matrix[first_alpha_index,second_alpha_index] - \
        #         delta_second_label * self.k_data_matrix[second_alpha_index,second_alpha_index]
        # if (0 < self.alphas[second_alpha_index]) and (self.edge_threshold > self.alphas[second_alpha_index]): 
        #     return b2
        
        # return (b1 + b2)/2.0

        i, j = first_alpha_index, second_alpha_index
        b1 = self.b - first_alpha_error- self.label_matrix[i]*(delta_first_alpha)*self.k_data_matrix[i,i] -\
                self.label_matrix[j]*(delta_second_alpha)*self.k_data_matrix[i,j] 
        b2 = self.b - second_alpha_error- self.label_matrix[i]*(delta_first_alpha)*self.k_data_matrix[i,j]-\
                self.label_matrix[j]*(delta_second_alpha)*self.k_data_matrix[j,j]
        if (0 < self.alphas[i]) and (self.edge_threshold > self.alphas[i]): self.b = b1
        elif (0 < self.alphas[j]) and (self.edge_threshold > self.alphas[j]): self.b = b2
        else: self.b = (b1 + b2)/2.0
        return self.b

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
        return nonzero((self.alphas.A > 0) * (self.alphas.A < self.edge_threshold))[0]

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
    def __init__(self, data_matrix, label_matrix, alphas, b, arg_exp):
        nonzero_indexs = nonzero(alphas.A>0)[0]
        # self.selected_alphas = alphas[nonzero_indexs]
        self.selected_data_matrix = data_matrix[nonzero_indexs]
        # self.selected_label_matrix = label_matrix[nonzero_indexs]
        self.selected_alphas_label_matrix = multiply(label_matrix[nonzero_indexs], alphas[nonzero_indexs])
        self.svm_count = len(nonzero_indexs)
        # self.selected_data_matrix = selected_data_matrix
        # self.selected_label_matrix = selected_label_matrix
        # self.selected_alphas = selected_alphas
        self.b = b
        self.arg_exp = arg_exp
        pass

    @classmethod
    def train(cls, data_matrix, label_matrix, edge_threshold, tolerance, max_iteration_count, arg_exp=20): 
        smo_basic = SmoBasic(data_matrix, label_matrix,edge_threshold,tolerance,arg_exp) 
        alphas,b =  smo_basic.cal_alphas_and_b(max_iteration_count)
        return cls(data_matrix, label_matrix, alphas, b, arg_exp)

    def save_selected_values():
        pass

    def __package_info(self, error_count, row_count):
        return {'error_ratio %':round(float(error_count)/row_count * 100, 2),
                'error_count': error_count,
                'row_count': row_count,
                'svm_count': self.svm_count}

    def test(self, testing_data_matrix, testing_label_matrix):
        row_count = testing_data_matrix.shape[0]

        errors = tuple(self.classify(testing_data_matrix[i, :])!=sign(testing_label_matrix[i,0]) 
            for i in range(row_count))
        return self.__package_info(errors.count(True), row_count)

    def classify(self, row_matrix):
        kernel_value = rbf_kernel(self.selected_data_matrix, 
            row_matrix, self.arg_exp)
        predict = kernel_value.T * self.selected_alphas_label_matrix + self.b
        return sign(predict)


''' split line '''





def filter_filenames_with_nums(pathname,start_with_numbers):
    '''
        return list of list of the file names under the path.
        Like:
            [ ['0_0.dataset', ... '0_99.dataset'],
                ...
              ['9_0.dataset', ... '9_99.dataset'] ]
    '''
    num_strs = map(str, start_with_numbers)
    # num_str = str(start_with_number)
    return [filename for filename in os.listdir(pathname) 
        for num_str in num_strs if filename.startswith(num_str)]

def save_list(file_path, the_list):
    with open(file_path, 'w') as the_file:
        for item in the_list:
            the_file.write("%s\n" % item)

def load_data_from_images(the_path):
    file_names = filter_filenames_with_nums(the_path, (9,1))
    data_matrix = mat(get_dataset_from_filenames(the_path, 
            file_names))
    label_matrix = mat(get_labels_from_filenames( 
            file_names)).transpose()
    label_matrix = transfer_values(label_matrix, {9:-1, 1:1})
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



def testDigits(arg_exp=20):
    cur_pic_path = '../../projects/font_number_binary/number_images'
    pic_path = '../k_nearest_neighbours'
    training_pic_path = os.path.join(pic_path,'training_digits')
    # training_pic_path = cur_pic_path
    test_pic_path = os.path.join(pic_path,'test_digits')
    # test_pic_path = cur_pic_path

    # dataArr,labelArr = load_data_from_images(training_pic_path)
    datMat,label_matrix = load_data_from_images(training_pic_path)
    # dataArr.shape.pp()
    datMat.shape.pp()
    label_matrix.shape.pp()
    
    delimiter=' '
    fmt = '%1d'
    # savetxt('data_array.dataset', datMat, fmt=fmt, delimiter=delimiter)
    # savetxt('label_array.dataset', label_matrix, fmt=fmt, delimiter=delimiter)


    smo = Smo.train(datMat,label_matrix, 200, 0.0001, 1000, arg_exp)

    smo.test(datMat,label_matrix).pp()

    datMat,label_matrix = load_data_from_images(test_pic_path)
    smo.test(datMat,label_matrix).pp()


if __name__ == '__main__':
    from minitest import *
    testDigits()    

    # with test("compare"):
    #     pic_path = '../k_nearest_neighbours'
    #     training_pic_path = os.path.join(pic_path,'training_digits')
    #     dataArr,labelArr = load_data_from_images(training_pic_path)
    #     dataArr2,labelArr2 = load_data_from_images2(training_pic_path)
    #     # dataArr.shape.pp()
    #     # array(dataArr2).shape.pp()
    #     dataArr.shape.must_equal(dataArr2.shape)
    #     # labelArr.shape.must_equal(labelArr2.shape)
    #     dataArr.must_equal(dataArr2, allclose)
    #     labelArr.must_equal(labelArr2)

    #     pass