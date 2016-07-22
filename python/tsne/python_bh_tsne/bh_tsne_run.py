import numpy
import time

def pca(X, no_dims = 50):
    """Runs PCA on the NxD array X in order to reduce its dimensionality to no_dims dimensions."""

    # find the component according variance
    print "Preprocessing the data using PCA..."
    (n, d) = X.shape
    # sub the mean by columns
    # X = X - numpy.tile(numpy.mean(X, 0), (n, 1))
    X = X - numpy.mean(X, 0)
    # find eig
    (eig_val, eig_vec) = numpy.linalg.eig(numpy.dot(X.T, X))

    # this step is new in bh, it seems useless after testing small data
    # sorting the eigen-values in the descending order
    eig_vec1 = eig_vec[:, eig_val.argsort()[::-1]]

    dim_count = no_dims if d > no_dims else d

    Y = numpy.dot(X, eig_vec1[:,0:dim_count])
    return Y

def main():
    data = np.loadtxt("./data/mnist2500_X.txt")
    print("data.shape:",data.shape)
    no_dims = 2
    perplexity = 50
    theta = 0.5
    randseed = 2
    initial_dims 50

    data = np.asarray(data, dtype='float64')
    pca_data = pca(data, initial_dims)

    Y = bh_tsne(pca_data.tolist(), no_dims=no_dims, perplexity=perplexity, theta=theta,
            randseed=randseed)
    numpy.savetxt('data/Y_bh1.txt',Y)
