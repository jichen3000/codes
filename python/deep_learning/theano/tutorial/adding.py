import numpy
import theano.tensor as T
from theano import function
import theano

if __name__ == '__main__':
    from minitest import *
    inject(numpy.allclose, 'must_close')

    # http://deeplearning.net/software/theano/tutorial/adding.html
    with test(T.dscalar):
        x = T.dscalar('x')
        y = T.dscalar('y')
        z = x + y
        f = function([x, y], z)
        f(16.3, 12.1).must_close(28.4)
        theano.pp(z).must_equal('(x + y)')
        x.type.__str__().must_equal('TensorType(float64, scalar)')
        T.dscalar.__str__().must_equal('TensorType(float64, scalar)')
        x.type.must_equal(T.dscalar)

        # first time will be slow, need to compile to function
        z.eval({x : 16.3, y : 12.1}).must_close(28.4)

    with test(T.dmatrix):
        x, y = T.dmatrices('x','y')
        # x = T.dmatrix('x')
        # y = T.dmatrix('y')
        z = x + y
        f = function([x, y], z)
        x.type.__str__().must_equal('TensorType(float64, matrix)')
        T.dmatrix.__str__().must_equal('TensorType(float64, matrix)')
        x.type.must_equal(T.dmatrix)
        f([[1, 2], [3, 4]], [[10, 20], [30, 40]]).must_close(
                numpy.array([[ 11.,  22.], [ 33.,  44.]]))
        f(numpy.array([[1, 2], [3, 4]]), numpy.array([[10, 20], [30, 40]])).must_close(
                numpy.array([[ 11.,  22.], [ 33.,  44.]]))

    # byte: bscalar, bvector, bmatrix, brow, bcol, btensor3, btensor4
    # 16-bit integers: wscalar, wvector, wmatrix, wrow, wcol, wtensor3, wtensor4
    # 32-bit integers: iscalar, ivector, imatrix, irow, icol, itensor3, itensor4
    # 64-bit integers: lscalar, lvector, lmatrix, lrow, lcol, ltensor3, ltensor4
    # float: fscalar, fvector, fmatrix, frow, fcol, ftensor3, ftensor4
    # double: dscalar, dvector, dmatrix, drow, dcol, dtensor3, dtensor4
    # complex: cscalar, cvector, cmatrix, crow, ccol, ctensor3, ctensor4

