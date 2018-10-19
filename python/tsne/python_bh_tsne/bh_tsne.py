import numpy
import sys
import time

import vantage_point_tree as vp
import space_partitioning_tree as sp
import pylab as Plot

DBL_MAX = sys.float_info.max
DBL_MIN = sys.float_info.min
FLT_MIN = 1.17549e-38


import time

def timeit(f):

    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print 'func:%r took: %2.4f sec' % \
          (f.__name__, te-ts)
        return result

    return timed

class TsneError(Exception):
    pass

def test_save_data(samples):
    import os
    import struct
    row_count, col_count = samples.shape
    # samples = numpy.array(the_data, dtype='float64').reshape(row_count, col_count)
    # samples.pp()
    file_name = "y_{0}_{1}.dat".format(row_count, col_count)
    with open(os.path.join(".", file_name), 'wb') as data_file:
        # Then write the data
        for sample in samples:
            data_file.write(struct.pack('{}d'.format(len(sample)), *sample))
    file_name.p()

def test_print_row(row_p, col_p, row_count):
    for n in range(row_count):
        sys.stdout.write("n:"+str(n)+": ")
        for i in range(row_p[n], row_p[n+1]):
            sys.stdout.write(str(col_p[i])+", ")
        print("")

def test_print_matrix(the_data, row_count, col_count):
    for n in range(row_count):
        sys.stdout.write("n:"+str(n)+": ")
        for i in range(col_count):
            sys.stdout.write(str(the_data[n*col_count + i])+", ")
        print("")

def is_perplexity_too_large(record_count, perplexity):
    return record_count - 1 < 3 * perplexity

# TSNE::zeroMean
def zero_mean(data):
    means_every_column = numpy.mean(data,0)
    m,n = data.shape
    for i in range(m):
        for j in range(n):
            data[i,j] = data[i,j] - means_every_column[j]
    # return data-numpy.mean(data,0)

# TSNE::computeSquaredEuclideanDistance
def cal_distance_matrix(x_rows):
    row_squares = numpy.sum(numpy.square(x_rows), 1);
    distance_matrix = numpy.add(numpy.add(-2 * numpy.dot(x_rows, x_rows.T),
            row_squares).T, row_squares);
    return distance_matrix

@timeit
def pca(X, no_dims = 50):
    """Runs PCA on the NxD array X in order to reduce its dimensionality to no_dims dimensions."""

    # find the component according variance
    print "Preprocessing the data using PCA..."
    (n, d) = X.shape
    # sub the mean by columns
    # X = X - numpy.tile(numpy.mean(X, 0), (n, 1))
    X = X - numpy.mean(X, 0)
    # find eig
    # import ipdb; ipdb.set_trace()
    (eig_val, eig_vec) = numpy.linalg.eig(numpy.dot(X.T, X))

    # this step is new in bh, it seems useless after testing small data
    # sorting the eigen-values in the descending order
    eig_vec1 = eig_vec[:, eig_val.argsort()[::-1]]

    dim_count = no_dims if d > no_dims else d

    Y = numpy.dot(X, eig_vec1[:,0:dim_count])
    return Y.real

def run(X, no_dims, perplexity, theta, randseed, max_iter):
    row_count, col_count = X.shape

    if(theta<1e-5):
        raise TsneError("theta too small")

    zero_mean(X)
    X = X/numpy.max(X)

    K = int(3*perplexity)
    row_p, col_p, val_p = compute_gaussian_perplexity(X, perplexity, K)

    row_p, col_p, val_p = symmetrize_matrix(row_p, col_p, val_p, row_count, K)

    # test_print_row(row_p, val_p, N)
    sum_p = numpy.sum(val_p)
    for i in range(row_p[-1]):
        val_p[i] = val_p[i] / sum_p * 12.0

    numpy.random.seed(randseed)
    # Y = [numpy.random.normal() for i in range(row_count*no_dims)]
    Y = numpy.random.normal(loc=0.0, scale=1.0, size=(row_count,no_dims))
    for i in range(row_count):
        for j in range(no_dims):
            while abs(Y[i,j]) < 0.1:
                Y[i,j] *= 10
    for i in range(row_count):
        for j in range(no_dims):
            Y[i,j] = round(Y[i,j],8)

    # for test
    # test_save_data(Y)

    dY = numpy.zeros((row_count, no_dims));
    iY = numpy.zeros((row_count, no_dims));
    uY = numpy.zeros((row_count, no_dims));
    gains = numpy.ones((row_count, no_dims));
    momentum = .5
    final_momentum = .8
    eta = 200.0
    min_gain = 0.01
    # max_iter=1000
    stop_lying_iter=250
    mom_switch_iter=250

    # max_iter = 27
    # max_iter = 50
    start_time = time.time()
    total_time = 0.0
    # Y.pp()
    for iter_index in range(max_iter):
        compute_gradient(row_p, col_p, val_p, Y, dY, theta)
        # iter_index.p()
        # Y.pp()
        # dY.pp()

        for i in range(row_count):
            for j in range(no_dims):
                # Update gains
                if numpy.sign(dY[i,j]) != numpy.sign(uY[i,j]):
                    gains[i,j] +=  0.2
                else:
                    gains[i,j] *=  0.8
                if gains[i,j] < min_gain:
                    gains[i,j] = min_gain
                # Perform gradient update
                uY[i,j] = momentum * uY[i,j] - eta * gains[i,j] * dY[i,j]
                Y[i,j] = Y[i,j] + uY[i,j]

        zero_mean(Y)
        # Y.pp()

        # Stop lying about the P-values after a while, and switch momentum
        if iter_index == stop_lying_iter:
            for i in range(row_p[-1]):
                val_p[i] /= 12.0

        if iter_index == mom_switch_iter:
            momentum = final_momentum

        # Print out progress
        if(iter_index > 0 and (iter_index % 50 == 0 or iter_index == max_iter - 1)):
        # if True:
            end_time = time.time()
            error_value = evaluate_error(row_p, col_p, val_p, Y, theta)
            total_time += (end_time - start_time)
            print("Iteration {0}: error is {1} (50 iterations in {2} seconds)".format(
                    iter_index, error_value, (end_time - start_time)))
            start_time = time.time()
    end_time = time.time()
    total_time += (end_time - start_time)
    print("Fitting performed in {0} seconds.".format(total_time))


    return Y

def evaluate_error(row_p, col_p, val_p, Y, theta):
    row_count, no_dims = Y.shape
    tree = sp.SpNode().fill(Y)
    buff = numpy.zeros(no_dims)
    sum_q = [0.0]
    for i in range(row_count):
        tree.compute_non_edge_forces(Y, i, theta, buff, sum_q)
    sum_q = sum_q[0]

    the_error = .0

    for n in range(row_count):
        for i in range(row_p[n], row_p[n+1]):
            tmp = ((Y[n] - Y[col_p[i]]) ** 2).sum()
            tmp = (1.0/(1.0+tmp)) / sum_q
            the_error += val_p[i] * numpy.log((val_p[i] + FLT_MIN) / (tmp + FLT_MIN))

    return the_error

def compute_gradient(row_p, col_p, val_p, Y, dY, theta):
    # print("Y")
    # test_print_matrix(Y, row_count, no_dims)
    # Y.pp()
    row_count, no_dims = Y.shape
    pos_f = compute_edge_forces(Y, row_p, col_p, val_p)
    # pos_f.p()
    tree = sp.SpNode().fill(Y)
    # neg_f = [0.0 for i in range(row_count * no_dims)]
    neg_f = numpy.zeros((row_count, no_dims))
    sum_q = [0.0]
    # theta.p()
    for i in range(row_count):
        tree.compute_non_edge_forces(Y, i, theta, neg_f[i], sum_q)
    sum_q = sum_q[0]
    # print type(neg_f[1,1])
    # neg_f.pp()
    # print("neg_f")
    # test_print_matrix(neg_f, row_count, no_dims)
    # n:0: 0.199256381911, 0.705126925562,
    # n:18: 1.61158022083, -0.349329631857,
    # n:19: 0.738217583558, 0.932917610011,
    for i in range(row_count):
        for j in range(no_dims):
            dY[i, j] = pos_f[i,j] - (neg_f[i,j] / sum_q)


def compute_edge_forces(Y, row_p, col_p, val_p):
    '''
        Computes edge forces
        sum of distance(normalized) of all k nearest points
    '''

    # print "iscomplex"
    # for i in range(len(val_p)):
    #     if numpy.iscomplex(val_p[i]):
    #         i.p()
    #         val_p[i].p()
    # val_p.size().p()
    # sys.exit()
    # ind1 = 0
    # pos_f = [0.0 for i in range(no_dims * row_count)]
    row_count, no_dims = Y.shape
    pos_f = numpy.zeros((row_count, no_dims))
    for n in range(row_count):
        for i in range(row_p[n], row_p[n+1]):
            D = 1.0
            buffs = [Y[n, d] - Y[col_p[i], d] for d in range(no_dims)]
            # buffs.p()
            # buffs.size().p()
            D += sum([d*d for d in buffs])
            # if n == 0 and i == 0:
            #     D.p()
            #     i.p()
            #     val_p[i].p()
            #     print type(val_p[i])
            #     print numpy.iscomplex(val_p[i])
                # numpy.iscomplex128(val_p[i]).p()
            # D.p()
            # val_p[i].p()
            D = val_p[i] / D
            for d in range(no_dims):
                # pos_f[ind1*no_dims + d] += D * buffs[d]
                pos_f[n, d] += D * buffs[d]
                #     pos_f[n, d].p()
            # pos_f.shape.p()
        # ind1 += 1
    return pos_f

@timeit
def compute_gaussian_perplexity(X, perplexity, K):
    vp_tree = vp.VpTree(X)
    n,D = X.shape
    row_p = [i*K for i in range(n+1)]
    col_p = [-1 for i in range(n*K)]
    val_p = [0 for i in range(n*K)]
    for i in range(n):
        distances, indexes = vp_tree.search(X[i], K+1)
        # indexes.p()
        # distances.p()

        found = False
        beta = 1.0
        min_beta = -DBL_MAX
        max_beta =  DBL_MAX
        tolerance = 1e-5

        sum_p = 0.0
        iter_index = 0
        cur_p_list = None
        while(not found and iter_index < 200):
            cur_p_list = [numpy.exp(-beta * distances[m + 1])
                    for m in range(K)]
            # avoid sum_p be the zero
            sum_p = DBL_MIN + numpy.sum(cur_p_list)
            H = 0.0
            for m in range(K):
                H += beta * (distances[m + 1] * cur_p_list[m])
            H = (H / sum_p) + numpy.log(sum_p)

            Hdiff = H - numpy.log(perplexity)
            if Hdiff < tolerance and -Hdiff < tolerance:
                found = True
            else:
                if Hdiff > 0:
                    min_beta = beta
                    if max_beta == DBL_MAX or max_beta == -DBL_MAX:
                        beta *= 2.0
                    else:
                        beta = (beta + max_beta) / 2.0
                else:
                    max_beta = beta
                    if min_beta == DBL_MAX or min_beta == -DBL_MAX:
                        beta /= 2.0
                    else:
                        beta = (beta + min_beta) / 2.0
            iter_index += 1

        for m in range(K):
            cur_p_list[m] /= sum_p
            col_p[ row_p[i] + m] = indexes[m+1]
            val_p[ row_p[i] + m] = cur_p_list[m]


    return (row_p, col_p, val_p)

@timeit
def symmetrize_matrix(row_p, col_p, val_p, N, K):
    # for n = 0, whether in the list of nearest of 0, 0 is in the list of nearest
    row_counts = [K for i in range(N)]
    for n in range(N):
        for i in range(row_p[n], row_p[n+1]):
            present = False
            for m in range(row_p[col_p[i]], row_p[col_p[i]+1]):
                # n.p()
                # i.p()
                # m.p()
                # col_p[m].p()
                if col_p[m] == n:
                    present = True
                    break
            # row_counts[n] += 1
            # row_counts[n].p()
            if not present:
                row_counts[col_p[i]] += 1
                # row_counts[col_p[i]].p()
                # col_p[i].p()
    no_elem = sum(row_counts)
    # row_counts.pp()
    # no_elem.p()

    sym_row_p = [0]
    for n in range(N):
        sym_row_p.append(sym_row_p[n] + row_counts[n])
    # sym_row_p.p()

    sym_col_p = [0 for i in range(no_elem)]
    sym_val_p = [0.0 for i in range(no_elem)]
    offset = [0 for i in range(N)]

    for n in range(N):
        for i in range(row_p[n], row_p[n+1]):
            # considering element(n, col_P[i])
            # Check whether element (col_P[i], n) is present
            present = False
            # n.p()
            # i.p()
            # print("m={0}~{1}".format(row_p[col_p[i]],row_p[col_p[i]+1]-1))
            for m in range(row_p[col_p[i]], row_p[col_p[i]+1]):
                # col_p[m].p()
                # col_p[i].p()
                # (col_p[m] == n).p()
                if(col_p[m] == n):
                    present = True
                    # make sure we do not add elements twice
                    # (n <= col_p[i]).p()
                    # present.p()
                    # m.p()
                    if n <= col_p[i]:
                        # (sym_row_p[n]        + offset[n]).p()
                        # sym_row_p[n].p()
                        # offset[n].p()
                        # (sym_row_p[col_p[i]] + offset[col_p[i]]).p()
                        # offset[col_p[i]].p()
                        # print "sym_col_p[{0},{1}]={2}".format(n, offset[n],col_p[i])
                        # print "sym_col_p[{0},{1}]={2}".format(col_p[i], offset[col_p[i]],n)
                        # val_p[i].p()
                        # val_p[m].p()
                        # import os;os._exit(1)
                        sym_col_p[sym_row_p[n]        + offset[n]]        = col_p[i]
                        sym_col_p[sym_row_p[col_p[i]] + offset[col_p[i]]] = n
                        sym_val_p[sym_row_p[n]        + offset[n]]        = val_p[i] + val_p[m]
                        sym_val_p[sym_row_p[col_p[i]] + offset[col_p[i]]] = val_p[i] + val_p[m]
                    # else:
                    #     print("skip, since n({0})>col_p[i]({1})".format(n,col_p[i]))
                    break
            # If (col_P[i], n) is not present, there is no addition involved
            if not present:
                # present.p()
                # n.p()
                # i.p()
                # (sym_row_p[n]        + offset[n]).p()
                # sym_row_p[n].p()
                # offset[n].p()
                # (sym_row_p[col_p[i]] + offset[col_p[i]]).p()
                # col_p[i].p()
                # sym_row_p[col_p[i]].p()
                # offset[col_p[i]].p()
                # print "sym_col_p[{0},{1}]={2}".format(n, offset[n],col_p[i])
                # print "sym_col_p[{0},{1}]={2}".format(col_p[i], offset[col_p[i]],n)
                sym_col_p[sym_row_p[n]        + offset[n]]        = col_p[i]
                sym_col_p[sym_row_p[col_p[i]] + offset[col_p[i]]] = n
                sym_val_p[sym_row_p[n]        + offset[n]]        = val_p[i]
                sym_val_p[sym_row_p[col_p[i]] + offset[col_p[i]]] = val_p[i]
            # Update offsets
            if(not present or  (present and n <= col_p[i])):
                # (not present or  (present and n <= col_p[i])).p()
                offset[n]+=1
                # print("offset[{0}]={1}".format(n,offset[n]))
                if(col_p[i] != n):
                    offset[col_p[i]]+=1
                    # (col_p[i] != n).p()
                    # print("offset[{0}]={1}".format(col_p[i],offset[col_p[i]]))
                    # col_p[i].p()
                    # offset[col_p[i]].p()
    # Divide the result by two
    for i in range(no_elem):
        sym_val_p[i] /= 2.0

    return (sym_row_p, sym_col_p, sym_val_p)


@timeit
def test_with_small_data():
        no_dims = 2
        N = 20
        D = 5
        perplexity = 2 # K = 6
        # a = [15, 19, 12,  9,  3, 11,  0, 14, 16, 13, 18,  7, 10,  4,  2,  1,  5,
        #         6, 17,  8]
        a = range(20)
        # X = numpy.array([range(i, i+D) for i in a])
        X = numpy.array([[float(i*i)] * D for i in a])
        # X.pp()
        theta = 0.05
        randseed = 2
        max_iter=1000
        # max_iter=1
        Y = run(X, no_dims, perplexity, theta, randseed, max_iter)
        import os
        dir_path = os.path.dirname(os.path.realpath(__file__))
        file_path = os.path.join(dir_path,"small_y.csv")
        numpy.savetxt(file_path, Y, delimiter=",")
        # Y = numpy.loadtxt(open(file_path,"rb"),delimiter=",",skiprows=0)
        # Y.pp()
    	# Plot.scatter(Y[:,0], Y[:,1], 20);
        # Plot.show();

@timeit
def test_with_mnist_2500():
        import os
        dir_path = os.path.dirname(os.path.realpath(__file__))
        data_path = os.path.join(dir_path,"..","data")
        x_file_path = os.path.join(data_path,"mnist2500_X.txt")

        no_dims = 2
        perplexity = 30.0
        theta = 0.5
        verbose = True
        X = numpy.loadtxt(x_file_path)

        X = pca(X, 50)
        # X = X[0:100,:]
        X.shape.p()
        randseed = 2
        max_iter=1000
        max_iter=50
        Y = run(X, no_dims, perplexity, theta, randseed, max_iter)
        y_file_path = os.path.join(data_path,"mnist_bhtns_y_numpy.csv")
        numpy.savetxt(y_file_path, Y, delimiter=",")
        # Y = numpy.loadtxt(open(file_path,"rb"),delimiter=",",skiprows=0)
        # Y.pp()
    	# Plot.scatter(Y[:,0], Y[:,1], 20);
        # Plot.show();


if __name__ == '__main__':
    from minitest import *

    test_with_mnist_2500()
