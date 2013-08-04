# sequential minimal optimization (SMO)
# John C. Platt, "Using Analytic QP and Sparseness 
# to Speed Training of Support Vector Machines"


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

# select a value from 0 to m, but not equal the value of i
def selectJrand(i,m):
    j=i
    while (j==i):
        j = int(random.uniform(0,m))
    return j

# reset a value according to a range from low_value to hight_value
def clipAlpha(aj,hight_value,low_value):
    if aj > hight_value:
        aj = hight_value
    if aj < low_value:
        aj = low_value
    return aj

def smoSimple(dataset, labels, constant, tolerance, max_count):
    def cal_error(row_index):
        # f(X) is a matrix wich (1, 1)
        # dataset_matrix[i,:] equals dataset_matrix[i]
        fx = float(multiply(alphas,label_matrix).T*\
               (dataset_matrix*dataset_matrix[row_index,:].T)) + b
        return  fx - float(label_matrix[row_index])
    dataset_matrix = mat(dataset)
    label_matrix = mat(labels).T
    b = 0; m,n = shape(dataset_matrix)
    alphas = mat(zeros((m,1)))
    no_change_count = 0
    # test
    # dataset_matrix.p()
    # label_matrix.p()
    # constant.p()
    # tolerance.p()
    # alphas.p()
    while (no_change_count < max_count):
        alpha_pairs_changed = 0
        for i in range(m):
            error_i = cal_error(i)
            # enter optimization if alphas can be changed.
            if ((label_matrix[i]*error_i < -tolerance) and  
                    (alphas[i] < constant)) or \
                    ((label_matrix[i]*error_i > tolerance) and
                    (alphas[i] > 0)):
                # random select second alpha
                j = selectJrand(i,m)
                error_j = cal_error(j)
                alphaIold = alphas[i].copy();
                alphaJold = alphas[j].copy();
                # Guarantee alphas stay between 0 and constant
                if (label_matrix[i] != label_matrix[j]):
                    L = max(0, alphas[j] - alphas[i])
                    H = min(constant, constant + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - constant)
                    H = min(constant, alphas[j] + alphas[i])
                if L==H: 
                    # print "L==H"
                    continue
                # Eta is the optimal amount to change alpha[j].
                eta = 2.0 * dataset_matrix[i,:]*dataset_matrix[j,:].T - \
                        dataset_matrix[i,:]*dataset_matrix[i,:].T - \
                        dataset_matrix[j,:]*dataset_matrix[j,:].T
                if eta >= 0: 
                    # print "eta>=0"
                    continue
                alphas[j] -= label_matrix[j]*(error_i - error_j)/eta
                alphas[j] = clipAlpha(alphas[j],H,L)
                if (abs(alphas[j] - alphaJold) < 0.00001): 
                    # print "j not moving enough"
                    continue
                alphas[i] += label_matrix[j]*label_matrix[i]*\
                        (alphaJold - alphas[j])
                b1 = b - error_i- label_matrix[i]*(alphas[i]-alphaIold)*\
                        dataset_matrix[i,:]*dataset_matrix[i,:].T - \
                        label_matrix[j]*(alphas[j]-alphaJold)*\
                        dataset_matrix[i,:]*dataset_matrix[j,:].T
                b2 = b - error_j- label_matrix[i]*(alphas[i]-alphaIold)*\
                        dataset_matrix[i,:]*dataset_matrix[j,:].T - \
                        label_matrix[j]*(alphas[j]-alphaJold)*\
                        dataset_matrix[j,:]*dataset_matrix[j,:].T
                if (0 < alphas[i]) and (constant > alphas[i]): b = b1
                elif (0 < alphas[j]) and (constant > alphas[j]): b = b2
                else: b = (b1 + b2)/2.0
                alpha_pairs_changed += 1
                # print "no_change_count: %d i:%d, pairs changed %d" % \
                #                   (no_change_count,i,alpha_pairs_changed)
        if (alpha_pairs_changed == 0): no_change_count += 1
        else: no_change_count = 0
        # print "iteration number: %d" % no_change_count
    return b,alphas

# def get_support_vectors(dataset, labels, alphas):
#     return filter(lambda alpha data label: alpha>0, zip(alphas, dataset, labels))


if __name__ == '__main__':
    from minitest import *

    with test_case("simple smo"):
        tself = get_test_self()
        tself.dataset, tself.labels = get_dataset_from_file(
            "test_set.dataset")
        # tself.dataset.pp()
        tself.small_dataset = tself.dataset[:]
        tself.small_labels = tself.labels[:]
        with test("smo"):
            # smoSimple(tself.dataset, tself.labels, 0.6, 0.001, 1)
            b, alphas = smoSimple(tself.small_dataset, tself.small_labels, 
                0.6, 0.001, 40)
            b.p()
            alphas[alphas>0].p()
            pass