import numpy

def is_perplexity_too_large(record_count, perplexity):
    return record_count - 1 < 3 * perplexity

def zero_mean(data):
    return data-numpy.mean(data,0)

def run(X, no_dims, perplexity, theta, randseed):
    n,D = X.shape
    max_iter=1000
    stop_lying_iter=250
    mom_switch_iter=250

    # put seed

    if(is_perplexity_too_large):
        raise Exception("perplexity too large")
    if(theta<1e-5):
        raise Exception("theta too small")

    numpy.random.seed(2)
    Y = numpy.random.randn(n, no_dims);
    # print Y[0,:]
    # print Y[1,:]
    dY = numpy.zeros((n, no_dims));
    iY = numpy.zeros((n, no_dims));
    gains = numpy.ones((n, no_dims));

    initial_momentum = 0.5;
    final_momentum = 0.8;
    eta = 500;
    # min_gain = 0.01;

    X = zero_mean(X)
    X = X/numpy.max(X)

    return Y
