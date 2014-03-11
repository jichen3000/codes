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

class SmoBasic(object):
    def __init__(self, data_matrix, label_matrix, edge_threshold, tolerance):
        self.data_matrix = data_matrix
        self.label_matrix = label_matrix
        self.edge_threshold = edge_threshold
        self.tolerance = tolerance
        self.row_count, self.col_count = shape(data_matrix)
        self.alphas = mat(zeros((self.row_count,1)))
        self.b = 0 
        # The first column is a flag bit stating whether the error_cache is valid, 
        # and the second column is the actual E value.
        self.error_cache = mat(zeros((self.row_count,2)))

    def calculate_error(self, row_index):
        alpha_labels = multiply(self.alphas,self.label_matrix).T
        index_row_to_col = self.data_matrix[row_index,:].T
        fx = float(alpha_labels* (self.data_matrix*index_row_to_col)) + self.b
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
        return 2.0 * self.data_matrix[first_alpha_index,:]*self.data_matrix[second_alpha_index,:].T - \
            self.data_matrix[first_alpha_index,:]*self.data_matrix[first_alpha_index,:].T - \
            self.data_matrix[second_alpha_index,:]*self.data_matrix[second_alpha_index,:].T

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
    def cal_alphas_and_b(self, max_count, kTup=('lin', 0)): 
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

    def cal_weights(self):
        self.weights = zeros((self.col_count,1))
        for i in range(self.row_count):
            self.weights += multiply(self.alphas[i]*self.label_matrix[i],self.data_matrix[i,:].T)
        return self.weights

    def sequential_mmminimal_optimization(self, max_count, kTup=('lin', 0)):
        self.cal_alphas_and_b(max_count, kTup)
        return self.cal_weights()


    def judge_class(self, point_matrix):
        ''' If this value is greater than 0, then its class is a 1, 
            and the class is -1 if it's less than 0.'''
        if (point_matrix * mat(self.weights) + self.b) > 0: 
            return 1
        else:
            return -1



def get_support_vectors(dataset, labels, alphas):
    # [item.pp() for item in zip(alphas, dataset, labels)]
    # return []
    return filter(lambda item: item[0]>0, 
        zip(alphas, dataset, labels))

if __name__ == '__main__':
    from minitest import *

    def allclose_atol(atol):
        def in_all(a,b):
            return allclose(a,b, atol=atol)
        return in_all

    dataset, labels = get_dataset_from_file(
        "test_set.dataset")
    data_matrix = mat(dataset)
    label_matrix = mat(labels)

    with test("cal_alphas_and_b"):
        smo = Smo(data_matrix,label_matrix.transpose(),0.6, 0.001) 
        b, alphas = smo.cal_alphas_and_b(200)
        # this method will have great difference
        b.must_equal(matrix([[-3.1]]), allclose_atol(0.5))
        # alphas[alphas>0].pp()
        pass

    with test("get_support_vectors"):
        alphas_list = matrix([[ 0.10356041,  0.25615675,  
            0.01420587,  0.34551129]]).tolist()[0]
        get_support_vectors(dataset, labels, 
            alphas_list).must_equal(
            [(0.10356041, [3.542485, 1.977398], -1.0),
             (0.25615675, [3.018896, 2.556416], -1.0),
             (0.01420587, [7.55151, -1.58003], 1.0),
             (0.34551129, [2.114999, -0.004466], -1.0)])

    with test("cal_weights"):
        weights = smo.cal_weights()
        weights.must_equal(
            array([[ 0.65307162],
                   [-0.17196128]]), allclose_atol(0.2))

    with test("judge_class"):
        smo.judge_class(data_matrix[0]).must_equal(-1)
        labels[0].must_equal(-1.0)
        smo.judge_class(data_matrix[51]).must_equal(1)
        labels[51].must_equal(1.0)
