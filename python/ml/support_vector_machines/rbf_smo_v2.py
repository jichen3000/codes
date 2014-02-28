# sequential minimal optimization (SMO)
# John C. Platt, "Using Analytic QP and Sparseness 
# to Speed Training of Support Vector Machines"

# radial bias function,
# mapping from one feature space to another feature space.
# inner products.
# One great thing about the SVM optimization is that all 
# operations can be written in terms of inner products. 
# Inner products are two vectors multiplied together to 
# yield a scalar or single number.

# kernel trick or kernel substation.
# A popular kernel is the radial bias function, which we'll introduce next.

from functional_style import *

from functools import partial
from operator import itemgetter, gt, lt
from numpy import *
import random

def get_dataset_from_file(filename):
    with open(filename) as datafile:
        words = [line.strip().split('\t') for line in datafile]
    dataset = [ [float(cell) for cell in row[:-1]] for row in words]
    labels = map(comb(itemgetter(-1), float), words)
    return dataset, labels

def matrix_dataset_labels(data_tuple):
    return mat(data_tuple[0]), mat(data_tuple[1]).transpose()

def get_data_matrix_from_file(filename):
    return matrix_dataset_labels(get_dataset_from_file(filename))


def random_select(except_value, range_max):
    ''' select a value from 0 to m randomly, but not equal the value of except_value '''
    result=except_value
    while (result==except_value):
        result = int(random.uniform(0,range_max))
    return result



def clip_value(value,hight_value,low_value):
    ''' reset a value according to a range from low_value to hight_value '''
    if value > hight_value:
        value = hight_value
    if value < low_value:
        value = low_value
    return value

def get_index_and_max_value(lst):
    return max(enumerate(lst), key=itemgetter(1))

def rbf_kernel(data_matrix, row_count, arg_exp, row_matrix):
    transfered_row_matrix = mat(zeros((row_count,1)))
    for row_index in range(row_count):
        delta_row = data_matrix[row_index,:] - row_matrix
        transfered_row_matrix[row_index] = delta_row * delta_row.T
    transfered_row_matrix = exp( transfered_row_matrix / (-1*arg_exp**2))
    return transfered_row_matrix


class SmoBasic(object):
    def __init__(self, data_matrix, label_matrix, edge_threshold, tolerance):
        self.data_matrix = data_matrix
        self.label_matrix = label_matrix
        self.edge_threshold = edge_threshold
        self.tolerance = tolerance
        self.row_count, self.col_count = shape(data_matrix)
        # self.alphas = mat(zeros((self.row_count,1)))
        self.b = 0 
        # The first column is a flag bit stating whether the error_cache is valid, 
        # and the second column is the actual E value.
        # self.error_cache = mat(zeros((self.row_count,2)))
        # self.transfered_data_matrix = self.rbf_kernel_transfer(arg_exp)

    def init_for_recal_alphas_and_b(self,arg_exp):
        self.alphas = mat(zeros((self.row_count,1)))
        self.error_cache = mat(zeros((self.row_count,2)))
        self.transfered_data_matrix = self.rbf_kernel_transfer(arg_exp)

    def rbf_kernel_transfer(self, arg_exp):
        transfered_data_matrix = mat(zeros((self.row_count,self.row_count)))
        rbf_func = partial(rbf_kernel, self.data_matrix, self.row_count, arg_exp)
        for col_index in range(self.row_count):
            transfered_data_matrix[:,col_index] = rbf_func(self.data_matrix[col_index,:])
        return transfered_data_matrix


    def calculate_error(self, row_index):
        fx = float(multiply(self.alphas,self.label_matrix).T * self.transfered_data_matrix[:,row_index]) + self.b
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

    def update_error_cache(self, index, error_value=None):
        if error_value:
            self.error_cache[index] = [1, error_value]
        else:
            self.error_cache[index] = [1, self.calculate_error(index)]

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
        return 2.0 * self.transfered_data_matrix[first_alpha_index,second_alpha_index] - \
            self.transfered_data_matrix[first_alpha_index,first_alpha_index] - self.transfered_data_matrix[second_alpha_index,second_alpha_index]


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

        first_things = self.label_matrix[first_alpha_index]*delta_first_alpha*\
            self.data_matrix[first_alpha_index,:]
        second_things = self.label_matrix[second_alpha_index] *\
            delta_second_alpha * self.data_matrix[second_alpha_index,:]

        b1 = b - first_alpha_error - \
             first_things*self.data_matrix[first_alpha_index,:].T -\
             second_things*self.data_matrix[first_alpha_index,:].T
        b2 = b - second_alpha_error- \
             first_things*self.data_matrix[second_alpha_index,:].T - \
             second_things*self.data_matrix[second_alpha_index,:].T
        if (0 < self.alphas[first_alpha_index]) and (self.edge_threshold > self.alphas[first_alpha_index]): 
            result = b1
        elif (0 < self.alphas[second_alpha_index]) and (self.edge_threshold > self.alphas[second_alpha_index]): 
            result = b2
        else: 
            result = (b1 + b2)/2.0
        return result



    def get_non_bound_index_list(self):
        return nonzero((self.alphas.A > 0) * (self.alphas.A < self.edge_threshold))[0]


class Smo(SmoBasic):
    """sequential minimal optimization"""
    def __init__(self, data_matrix, label_matrix, edge_threshold, tolerance):
        ''' edge_threshold controls the balance between making sure 
            all of the examples have a margin of at least 1.0 and 
            making the margin as wide as possible. 
            If edge_threshold is large, the classifier will try to make 
            all of the examples properly classified by the separating hyperplane. '''
        super(Smo, self).__init__(data_matrix, label_matrix, edge_threshold, tolerance)

    # higher
    def select_second_alpha(self, first_alpha_index, first_alpha_error):
        ''' selects the second alpha, or the inner loop alpha 
            the goal is to choose the second alpha so that 
            we'll take the maximum step during each optimization.'''

        valid_error_cache_index_list = self.get_valid_error_cache_index_list()
        # first_alpha_index.pp()
        # self.error_cache.pp()
        # valid_error_cache_index_list.pp()
        if (len(valid_error_cache_index_list)) > 0:
            second_alpha_index, second_alpha_error = self.get_index_and_max_delta_error(
                valid_error_cache_index_list, first_alpha_error)
        else:
            second_alpha_index = random_select(first_alpha_index, self.row_count)
            second_alpha_error = self.calculate_error(second_alpha_index)

        self.update_error_cache(first_alpha_index, first_alpha_error)
        return second_alpha_index, second_alpha_error

    # higher
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
        
    # high
    def cal_alphas_and_b(self, max_count, arg_exp): 
        self.init_for_recal_alphas_and_b(arg_exp)
        is_entire_set = True
        alpha_pairs_changed_count = 0
        iter_index = 0
        # you pass through the entire set without changing any alpha pairs.
        while (iter_index < max_count) and \
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
        return self.b,self.alphas

    def train(self, max_count, arg_exp):
        self.cal_alphas_and_b(max_count, arg_exp)

        alpha_nonzero_index = nonzero(self.alphas.A>0)[0]
        self.svm_count = len(alpha_nonzero_index)
        alpha_alphas = self.alphas[alpha_nonzero_index]
        alpha_training_dataset_matrix = self.data_matrix[alpha_nonzero_index]
        alpha_training_labels_matrix = self.label_matrix[alpha_nonzero_index]

        rbf_func = partial(rbf_kernel, alpha_training_dataset_matrix, self.svm_count, arg_exp)
        alphas_multiply = multiply(alpha_training_labels_matrix, alpha_alphas)
        def cal_predict_value(row_matrix):
            return rbf_func(row_matrix).T * alphas_multiply + self.b
        self.cal_predict_value_func = cal_predict_value
        return self.cal_predict_value_func

    def gen_training_statics(self):
        self.training_statics = {}
        self.training_statics['svm_count'] = self.svm_count

        self.training_statics['error_count'], self.training_statics['row_count'], \
            self.training_statics['error_ratio'] = self.gen_predict_statics(
            self.data_matrix, self.label_matrix)

        return self.training_statics

    def gen_testing_statics(self, testing_data_matrix, testing_label_matrix):
        self.testing_statics = {}
        self.testing_statics['error_count'], self.testing_statics['row_count'], \
            self.testing_statics['error_ratio'] = self.gen_predict_statics(
            testing_data_matrix, testing_label_matrix)
        return self.testing_statics

    def gen_predict_statics(self, data_matrix, label_matrix):
        error_count = 0
        row_count = shape(data_matrix)[0]
        for i in range(row_count):
            if sign(self.cal_predict_value_func(data_matrix[i,:])) != sign(label_matrix[i]):
                error_count += 1
        return error_count, row_count, float(error_count)/row_count

    def classify(self, row_matrix):
        return sign(self.cal_predict_value_func(row_matrix))[0,0]







if __name__ == '__main__':
    from minitest import *

    def allclose_atol(atol):
        def in_all(a,b):
            return allclose(a,b, atol=atol)
        return in_all

    with test("gen statics"):
        arg_exp=1.3
        edge_threshold, tolerance = 200, 0.0001
        max_count = 10000
        training_data_matrix, training_label_matrix = get_data_matrix_from_file('test_set_RBF.dataset')

        smo = Smo(training_data_matrix, training_label_matrix, edge_threshold, tolerance)
        smo.train(max_count, arg_exp)

        testing_data_matrix, testing_label_matrix = get_data_matrix_from_file('test_set_RBF2.dataset')

        smo.gen_training_statics().pp()
        smo.gen_testing_statics(testing_data_matrix, testing_label_matrix).pp()

    with test("classify"):
        smo.classify(testing_data_matrix[0,:]).must_equal(-1.0)
