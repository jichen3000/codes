import numpy
import theano.tensor as T
from theano import function
import theano

if __name__ == '__main__':
    from minitest import *
    inject(numpy.allclose, 'must_close')

    with test("T.dot matrixs"):
        X = T.matrix("X")
        W = T.matrix("W")
        # result will be matrix * matrix,
        # c11 = a11*b11 + a12*b21
        dot_XW = T.dot(X,W)
        dot_f = theano.function([X,W],dot_XW)
        dot_f([[1,2],[3,4]],[[1,2],[3,4]]).must_close(
                [   [  7.,  10.],
                    [ 15.,  22.]])
        # cannot do this
        # dot_f([[1,2],[3,4]],[[1,2],[3,4],[5,6]]).must_close(
        #         [   [  7.,  10.],
        #             [ 15.,  22.]])

    with test("T.dot matrix with vector"):
        v = T.vector("v")
        dot_vX = T.dot(v, X)
        dot_f = theano.function([v, X],dot_vX)
        dot_f([1,2],[[1,2],[3,4]]).must_close(
                [  7.,  10.])

        # in this case, v will be become a column
        dot_Xv = T.dot(X,v)
        dot_f = theano.function([X, v],dot_Xv)
        dot_f([[1,2],[3,4]], [1,2]).must_close(
                [  5.,  11.])

    with test("T.dot matrix with scalar"):
        s = T.scalar("s")
        dot_Xs = T.dot(X,s)
        dot_f = theano.function([X, s],dot_Xs)
        dot_f([[1,2],[3,4]], 2).must_close(
                [[2,4],[6,8]])

