import numpy
import theano.tensor as T
from theano import function
import theano

if __name__ == '__main__':
    from minitest import *
    inject(numpy.allclose, 'must_close')

    with test("multiple matrixs"):
        X = T.matrix("X")
        W = T.matrix("W")
        # result will be matrix * matrix,
        # c11 = a11*b11 + a12*b21
        dot_XW = X * W
        dot_f = theano.function([X,W],dot_XW)
        dot_f([[1,2],[3,4]],[[1,2],[3,4]]).must_close(
                [   [  1.,  4.],
                    [  9.,  16.]])
        # cannot do this
        # dot_f([[1,2],[3,4]],[[1,2],[3,4],[5,6]]).must_close(
        #         [   [  7.,  10.],
        #             [ 15.,  22.]])

