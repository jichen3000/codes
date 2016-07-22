# ('num.shape :', (2500, 2500))
# ('PQ.shape :', (2500, 2500))
# ('Y.shape :', (2500, 2))

from minitest import *
import numpy
n = 3
no_dims = 2
PQ = numpy.arange(n**2).reshape(n,n)
num = PQ + 1
dY = numpy.zeros((n, no_dims))
Y = numpy.arange(n*no_dims).reshape(n,no_dims)
for i in range(n):
    # equation 5
    # dY[i,:] = numpy.sum(numpy.tile(PQ[i,:] * num[i,:], (no_dims, 1)).T * (Y[i,:] - Y), 0)
    dY[i,:] = numpy.sum(numpy.tile(PQ[:,i] * num[:,i], (no_dims, 1)).T * (Y[i,:] - Y), 0);

dY.pp()

A = numpy.multiply(PQ, num)
import ipdb; ipdb.set_trace()
numpy.sum(A, 0).p()


dY1 = numpy.multiply(numpy.tile(numpy.sum(A, 0), (no_dims, 1)).T, Y) - numpy.dot(A.T,Y)
# dY1.pp()