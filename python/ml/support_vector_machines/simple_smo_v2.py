''' sequential minimal optimization (SMO)
John C. Platt, "Using Analytic QP and Sparseness 
to Speed Training of Support Vector Machines"
'''

from functional_style import *
from operator import itemgetter
from numpy import *
import random

def get_dataset_from_file(filename):
    with open(filename) as datafile:
        words = [line.strip().split('\t') for line in datafile]
    dataset = [ [float(cell) for cell in row[:-1]] for row in words]
    labels = map(comb(itemgetter(-1), float), words)
    return dataset, labels

def romdom_select(i,m):
    ''' select a value from 0 to m randomly, but not equal the value of i '''

    j=i
    while (j==i):
        j = int(random.uniform(0,m))
    return j

def clip_alpha(aj,hight_value,low_value):
    ''' reset a value according to a range from low_value to hight_value '''

    if aj > hight_value:
        aj = hight_value
    if aj < low_value:
        aj = low_value
    return aj

# def new():
#     while(not_changed_count < max_count):
#         for row_i in row_count:
#             cal row_i_error
#             check row_i_error is tolerance
#             if not pass check:
#                 continue
#             set row_j
#             cal row_j_error
#             check eta is little than 0
#             if not pass check:
#                 continue
#             cal alphas[row_j]
#             check alphas[row_j] is moving enough
#             if not pass check:
#                 continue
#             cal alphas[row_i]
#             cal b
#             set changed
#         if not changed:
#             set not_changed_count plus 1

def continue_call_until_no_change(called_func, max_no_changed_count, *args):
    ''' it asks the called_func should return the values which are its own arguments except the first one,
    and the first one is a bool which means if it is changed.
    '''
    no_changed_count = 0
    results =(True,) + args
    while(no_changed_count < max_no_changed_count):
        results = called_func(*results[1:])
        if results[0]:
            ''' changed '''
            no_changed_count = 0
        else:
            no_changed_count += 1
    return results


def __calculate_error(data_matrix, label_matrix, alphas, b, row_index):
    alpha_labels = multiply(alphas,label_matrix).T
    index_row_to_col = data_matrix[row_index,:].T
    fx = float(alpha_labels* (data_matrix*index_row_to_col)) + b
    return fx - float(label_matrix[row_index])

def __is_error_in_tolerance(error_value, label_matrix, alphas, edge_threshold, tolerance, row_index):
    ''' Alphas will be clipped at 0 or C, so if they are equal to these,
    they are "bound" and can't be increased or decreased,
    so it is not worth trying to optimize these alphas.'''
    return ((label_matrix[row_index]*error_value < -tolerance) and  
                (alphas[row_index] < edge_threshold)) or \
                ((label_matrix[row_index]*error_value > tolerance) and
                (alphas[row_index] > 0))

def __cal_edegs(label_matrix, alphas, edge_threshold, row_i, row_j):
    ''' Guarantee alphas stay between 0 and edge_threshold '''
    if (label_matrix[row_i] != label_matrix[row_j]):
        L = max(0, alphas[row_j] - alphas[row_i])
        H = min(edge_threshold, edge_threshold + alphas[row_j] - alphas[row_i])
    else:
        L = max(0, alphas[row_j] + alphas[row_i] - edge_threshold)
        H = min(edge_threshold, alphas[row_j] + alphas[row_i])
    return L,H

def __cal_eta(data_matrix, row_i, row_j):
    eta = 2.0 * data_matrix[row_i,:]*data_matrix[row_j,:].T - \
            data_matrix[row_i,:]*data_matrix[row_i,:].T - \
            data_matrix[row_j,:]*data_matrix[row_j,:].T
    return eta

def __is_moving_enough(new_value, old_value):
    return abs(new_value - old_value) > 0.00001 

def __cal_b(error_i, error_j, b, alphas, data_matrix, label_matrix, edge_threshold,
        row_i, row_j, alpha_i_old, alpha_j_old):
    b1 = b - error_i- label_matrix[row_i]*(alphas[row_i]-alpha_i_old)*\
            data_matrix[row_i,:]*data_matrix[row_i,:].T - \
            label_matrix[row_j]*(alphas[row_j]-alpha_j_old)*\
            data_matrix[row_i,:]*data_matrix[row_j,:].T
    b2 = b - error_j- label_matrix[row_i]*(alphas[row_i]-alpha_i_old)*\
            data_matrix[row_i,:]*data_matrix[row_j,:].T - \
            label_matrix[row_j]*(alphas[row_j]-alpha_j_old)*\
            data_matrix[row_j,:]*data_matrix[row_j,:].T
    if (0 < alphas[row_i]) and (edge_threshold > alphas[row_i]): b = b1
    elif (0 < alphas[row_j]) and (edge_threshold > alphas[row_j]): b = b2
    else: b = (b1 + b2)/2.0
    return b

def smo_once(b, alphas, data_matrix, label_matrix, edge_threshold, tolerance, row_count):

    ''' main '''    
    alpha_pairs_changed = 0
    for i in range(row_count):
        error_i = __calculate_error(data_matrix, label_matrix, alphas, b, i)
        # enter optimization if alphas can be changed.
        if not __is_error_in_tolerance(error_i, label_matrix, alphas, edge_threshold, tolerance, i):
            continue
        # random select second alpha
        j = romdom_select(i,row_count)
        error_j = __calculate_error(data_matrix, label_matrix, alphas, b, j)
        alpha_i_old = alphas[i].copy();
        alpha_j_old = alphas[j].copy();
        L, H = __cal_edegs(label_matrix, alphas, edge_threshold, i,j)
        # Guarantee alphas stay between 0 and edge_threshold
        if L==H: 
            continue
        # Eta is the optimal amount to change alpha[j].
        eta = __cal_eta(data_matrix, i, j)
        if eta >= 0: 
            # print "eta>=0"
            continue
        alphas[j] -= label_matrix[j]*(error_i - error_j)/eta
        alphas[j] = clip_alpha(alphas[j],H,L)
        if not __is_moving_enough(alphas[j], alpha_j_old): 
            # print "j not moving enough"
            continue
        alphas[i] += label_matrix[j]*label_matrix[i]*\
                (alpha_j_old - alphas[j])
        b = __cal_b(error_i, error_j, b, alphas, data_matrix, label_matrix, edge_threshold,
            i, j, alpha_i_old, alpha_j_old)
        alpha_pairs_changed += 1
    return alpha_pairs_changed, b, alphas, data_matrix, label_matrix, edge_threshold, tolerance, row_count 


def smo_simple(dataset, labels, edge_threshold, tolerance, max_count):
    data_matrix = mat(dataset)
    label_matrix = mat(labels).T
    b = 0; row_count,n = shape(data_matrix)
    alphas = mat(zeros((row_count,1)))
    results = continue_call_until_no_change(smo_once, max_count,
        b, alphas, data_matrix, label_matrix, edge_threshold, tolerance, row_count)
    return results[1:3]

def get_svm_points(dataset, labels, alphas):
    return [(one_set, label) for one_set, label, alpha in zip(dataset, labels, alphas) if alpha > 0.0]
        

if __name__ == '__main__':
    from minitest import *

    def allclose_atol(atol):
        def in_all(a,b):
            return allclose(a,b, atol=atol)
        return in_all

    dataset, labels = get_dataset_from_file(
        "test_set.dataset")
    small_count = 10
    small_dataset = dataset[:small_count]
    small_labels = labels[:small_count]
    # small_dataset.pp()
    # small_labels.pp()

    with test("calculate_error"):
        small_data_matrix = mat(small_dataset)
        small_label_matrix = mat(small_labels).T
        m,n = shape(small_data_matrix)
        b=0
        small_alphas = mat(zeros((m,1)))
        row_index = 1
        __calculate_error(small_data_matrix, small_label_matrix, 
            small_alphas, b, row_index).must_equal(1.0)


    with test("smo"):
        # b, alphas = smo_simple(small_dataset, small_labels, 
        #     0.6, 0.001, 40)
        b, alphas = smo_simple(dataset, labels, 
            0.6, 0.001, 40)
        b.must_equal(matrix([[-3.816]]), allclose_atol(0.1))
        # alphas[alphas>0].pp()

        # every time, it could be different
        get_svm_points(dataset, labels, alphas).pp()
        pass

