from theano import function, shared, sandbox
from theano.ifelse import ifelse
import theano.tensor as tensor
import numpy
import time
import theano

FLOATX = "float32"

def timeit(f):

    def timed(*args, **kw):

        ts = time.time()
        result = f(*args, **kw)
        te = time.time()

        print 'func:%r took: %2.4f sec' % \
          (f.__name__, te-ts)
        return result

    return timed

# Took 1.074328 seconds, almost like without theano
def pca_theano(x, no_dims):
    # x_sym = shared(x, )
    x_sym = tensor.matrix()
    (n, _) = x_sym.shape
    y_sym = x_sym - tensor.tile(tensor.mean(x_sym, 0), (n, 1))
    (_, m_sym) = tensor.nlinalg.eig(tensor.dot(y_sym.T, y_sym))
    result_sym = tensor.dot(y_sym, m_sym[:,0:no_dims])
    the_fun = function([x_sym], result_sym)
    return the_fun(x)

@timeit
def pca(X, no_dims = 50):
    """Runs PCA on the NxD array X in order to reduce its dimensionality to no_dims dimensions."""

    # find the component according variance
    print "Preprocessing the data using PCA..."
    (n, d) = X.shape
    # sub the mean by columns
    X = X - numpy.tile(numpy.mean(X, 0), (n, 1))
    # find eig
    (l, M) = numpy.linalg.eig(numpy.dot(X.T, X))
    Y = numpy.dot(X, M[:,0:no_dims])
    return Y

def Hbeta(D = numpy.array([]), beta = 1.0):
    """Compute the perplexity and the P-row for a specific value of the precision of a Gaussian distribution."""

    # Compute P-row and corresponding perplexity
    P = numpy.exp(-D.copy() * beta)
    sumP = sum(P)
    H = numpy.log(sumP) + beta * numpy.sum(D * P) / sumP
    P = P / sumP
    return H, P


def x2p(X = numpy.array([]), tol = 1e-5, perplexity = 30.0):
    """Performs a binary search to get P-values in such a way that each conditional Gaussian has the same perplexity."""
    # not exactly as equation 1 in t-SNE

    # Initialize some variables
    print "Computing pairwise distances..."
    (n, d) = X.shape
    # sum_X = numpy.sum(numpy.square(X), 1)
    # D is matrix of distance numpy.add(numpy.add(-2 * numpy.dot(cc, cc.T), sum_cc).T, sum_cc)
    # d12, means, the distance between X1 and X2, d11 will be 0. 
    # D = numpy.add(numpy.add(-2 * numpy.dot(X, X.T), sum_X).T, sum_X)
    D = cal_distance_matrix(X)
    P = numpy.zeros((n, n))
    beta = numpy.ones((n, 1))
    logU = numpy.log(perplexity)

    # Loop over all datapoints
    for i in range(n):

        # Print progress
        if i % 500 == 0:
            print "Computing P-values for point ", i, " of ", n, "..."

        # Compute the Gaussian kernel and entropy for the current precision
        betamin = -numpy.inf
        betamax =  numpy.inf
        Di = D[i, numpy.concatenate((numpy.r_[0:i], numpy.r_[i+1:n]))]
        (H, thisP) = Hbeta(Di, beta[i])

        # Evaluate whether the perplexity is within tolerance
        Hdiff = H - logU
        tries = 0
        while numpy.abs(Hdiff) > tol and tries < 50:

            # If not, increase or decrease precision
            if Hdiff > 0:
                betamin = beta[i].copy()
                if betamax == numpy.inf or betamax == -numpy.inf:
                    beta[i] = beta[i] * 2
                else:
                    beta[i] = (beta[i] + betamax) / 2
            else:
                betamax = beta[i].copy()
                if betamin == numpy.inf or betamin == -numpy.inf:
                    beta[i] = beta[i] / 2
                else:
                    beta[i] = (beta[i] + betamin) / 2

            # Recompute the values
            (H, thisP) = Hbeta(Di, beta[i])
            Hdiff = H - logU
            tries = tries + 1

        # Set the final row of P
        P[i, numpy.concatenate((numpy.r_[0:i], numpy.r_[i+1:n]))] = thisP

    # Return final P-matrix
    print "Mean value of sigma: ", numpy.mean(numpy.sqrt(1 / beta))
    return P

def cal_distance_matrix(x_rows):
    row_squares = numpy.sum(numpy.square(x_rows), 1)
    distance_matrix = numpy.add(numpy.add(-2 * numpy.dot(x_rows, x_rows.T), row_squares).T, row_squares)
    return distance_matrix

@timeit
def compute_p(X, perplexity):
    # Compute P-values
    # P = x2p(X, 1e-5, perplexity)
    # P = P + numpy.transpose(P)
    # P = P / numpy.sum(P)
    # P = P * 4                                  # early exaggeration
    # P = numpy.maximum(P, 1e-12)
    # # numpy.savetxt('p.txt',P)
    P = numpy.loadtxt('data/matrix_p_cache.txt', dtype=FLOATX)
    print "loaded P from the file"
    return P

@timeit
def compute_y(P, no_dims, max_iter):
    (n, d) = P.shape
    # n = 2500    
    # max_iter = 100
    initial_momentum = 0.5
    final_momentum = 0.8
    eta = 500
    min_gain = 0.01

    initial_momentum_f = tensor.cast(initial_momentum, FLOATX)
    final_momentum_f = tensor.cast(final_momentum, FLOATX)
    min_gain_f = tensor.cast(min_gain, FLOATX)

    # sample of normal distribution, mean = 0, stardand_variance = 1
    numpy.random.seed(2)
    Y = numpy.random.randn(n, no_dims)
    # print Y[0,:]
    # print Y[1,:]
    # dY = numpy.zeros((n, no_dims))
    iY = numpy.zeros((n, no_dims))
    gains = numpy.ones((n, no_dims))

    steps_sym = tensor.ivector()
    # p_sym = tensor.matrix()
    # y_sym = tensor.matrix()
    # # dy_sym = tensor.matrix()
    # iy_sym = tensor.matrix()
    # gains_sym = tensor.matrix()


    y_arg = theano.shared(Y)
    iy_arg = theano.shared(iY)
    gains_arg = theano.shared(gains)
    p_arg = theano.shared(P)

    # y_arg = tensor.cast(y_arg, FLOATX)
    # p_arg = tensor.cast(p_arg, FLOATX)




    def scan_y(cur_step):
        # Compute pairwise affinities
        sum_y = tensor.sum(tensor.square(y_arg), 1)
        num = 1 / (1 + tensor.add(tensor.add(-2 * tensor.dot(y_arg, y_arg.T), sum_y).T, sum_y))
        num = tensor.set_subtensor(num[range(n),range(n)], 0)

        Q = num / tensor.sum(num)
        Q = tensor.maximum(Q, 1e-12)

        PQ = p_arg - Q

        def inner(pq_i, num_i, y_arg_i):
            return tensor.sum(tensor.tile(pq_i * num_i, (no_dims, 1)).T * (y_arg_i - y_arg), 0)
        dy_arg, _ = theano.scan(inner,
                outputs_info = None,
                sequences = [PQ, num, y_arg])
        # dy_arg = y_arg
        # dy_arg = tensor.cast(dy_arg,FLOATX)

        momentum = ifelse(tensor.lt(cur_step, 20), 
                initial_momentum_f, 
                final_momentum_f)

        indexsa = tensor.neq((dy_arg>0), (iy_arg>0)).nonzero()
        indexsb = tensor.eq((dy_arg>0), (iy_arg>0)).nonzero()
        resulta = tensor.set_subtensor(gains_arg[indexsa], gains_arg[indexsa]+0.2)
        resultb = tensor.set_subtensor(resulta[indexsb], resulta[indexsb]*0.8)

        indexs_min = (resultb<min_gain_f).nonzero()
        new_gains_arg = tensor.set_subtensor(resultb[indexs_min], min_gain_f)

        # last step in simple version of SNE
        new_iy_arg = momentum * iy_arg - eta * (new_gains_arg * dy_arg)
        new_y_arg = y_arg + new_iy_arg
        new_y_arg = new_y_arg - tensor.tile(tensor.mean(new_y_arg, 0), (n, 1))

        # # Compute current value of cost function
        # if (cur_step + 1) % 10 == 0:
        #     C = tensor.sum(p_arg * tensor.log(p_arg / Q))
        #     print "Iteration ", (cur_step + 1), ": error is ", C

        # Stop lying about P-values

        new_p_arg = ifelse(tensor.eq(cur_step, 100), 
                p_arg / 4, 
                p_arg)
        return [(y_arg,new_y_arg),(iy_arg,new_iy_arg), (gains_arg,new_gains_arg), (p_arg,new_p_arg)]

        # return [y_arg, iy_arg, gains_arg, p_arg]



    results, updates = theano.scan(
            scan_y,
            sequences=steps_sym)
    compute_y_fun = theano.function(inputs=[steps_sym], 
            outputs=results, updates=updates) 

    real_results = compute_y_fun(range(max_iter)) 

    # return real_results[0][-1]
    return y_arg.get_value()


def tsne(X = numpy.array([]), max_iter=1000, no_dims = 2, initial_dims = 50, perplexity = 30.0):
    """Runs t-SNE on the dataset in the NxD array X to reduce its dimensionality to no_dims dimensions.
    The syntaxis of the function is Y = tsne.tsne(X, no_dims, perplexity), where X is an NxD NumPy array."""

    # X = pca(X, initial_dims).real
    X = None
    P = compute_p(X, perplexity)
    Y = compute_y(P, no_dims, max_iter)
    return Y


# THEANO_FLAGS=mode=FAST_RUN,device=gpu python tmp_tsne.py    
if __name__ == "__main__":
    from minitest import *
    import sys

    if len(sys.argv) > 1:
        max_iter = int(sys.argv[1])
    else:
        max_iter = 2


    print "Run Y = tsne.tsne(X, no_dims, perplexity) to perform t-SNE on your dataset."
    print "Running example on 2,500 MNIST digits..."
    # X.shape is 2500,784
    # one image is 28 * 28 =784
    X = numpy.loadtxt("./data/mnist2500_X.txt")
    # start_time = time.time()
    max_iter.p()
    Y = tsne(X, max_iter, 2, 50, 20.0)
    # Y = pca(X, 50)
    # Y = pca_theano(X, 50)
    # end_time = time.time()
    Y.shape.p()
    # numpy.savetxt('data/Y_theano.txt',Y)
    # Y[0,].p()
    # Y[1,].p()
    # print("Took %f seconds" % (end_time - start_time))
