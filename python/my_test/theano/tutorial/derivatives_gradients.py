import numpy
import theano.tensor as T
from theano import function
import theano

if __name__ == '__main__':
    from minitest import *
    inject(numpy.allclose, 'must_close')

    # http://deeplearning.net/software/theano/tutorial/gradients.html
    with test("Computing Gradients"):
        x = T.dscalar('x')
        y = x ** 2
        # it would be 2x, one order of derivative
        gy = T.grad(y, x)
        # fill((x ** 2), 1.0) means to make a matrix of the same shape as x ** 2 and fill it with 1.0.
        theano.pp(gy).must_equal(
                '((fill((x ** TensorConstant{2}), TensorConstant{1.0}) * TensorConstant{2}) * (x ** (TensorConstant{2} - TensorConstant{1})))')
        # theano.pp(f.maker.fgraph.outputs[0]).must_equal(
        #         '(2.0 * x)')
        f = theano.function([x], gy)
        f(4).must_close(8)
        f(94.2).must_close(188.4)

    with test("gradients for logistic"):
        x = T.dmatrix('x')
        s = T.sum(1 / (1 + T.exp(-x)))
        # for T.grad, when input is matrix, it need to use T.sum
        # but the return is still a matrix, not sum.
        gs = T.grad(s, x)
        dlogistic = theano.function([x], gs)
        dlogistic([[0, 1], [-1, -2]]).must_close(
                [   [ 0.25      ,  0.19661193],
                    [ 0.19661193,  0.10499359]])

    with test("Computing only one"):
        x = T.dvector('x')
        y = x ** 2
        gy1 = T.grad(y[1], x)
        f = theano.function([x], gy1)
        f([4, 4]).must_close(
                [ 0.,  8.])        

    with test("Computing the Jacobian matrix"):
        x = T.dvector('x')
        y = x ** 2
        # first partial derivatives
        J, updates = theano.scan(lambda i, y, x : T.grad(y[i], x), 
                sequences=T.arange(y.shape[0]), 
                non_sequences=[y,x])
        f = theano.function([x], J, updates=updates)
        f([4, 4]).must_close(
                [   [ 8.,  0.],
                    [ 0.,  8.]])        
        
    # very slow
    with test("Computing the Hessian matrix"):
        x = T.dvector('x')
        y = x ** 2
        cost = y.sum()
        gy = T.grad(cost, x)
        # second partial derivatives
        H, _ = theano.scan(lambda i, gy, x : T.grad(gy[i], x), 
                sequences=T.arange(gy.shape[0]), 
                non_sequences=[gy,x])
        f = theano.function([x], H)
        f([4, 4]).must_close(
                [   [ 2.,  0.],
                    [ 0.,  2.]])        

    # product between a Jacobian and a vector
    with test("R-operator, vector on the right"):
        W = T.dmatrix('W')
        V = T.dmatrix('V')
        x = T.dvector('x')
        y = T.dot(x, W)
        JV = T.Rop(y, W, V)
        f = theano.function([W, V, x], JV)
        f([[1, 1], [1, 1]], [[2, 2], [2, 2]], [0,1]).must_close(
                [ 2.,  2.])

    # product between a Jacobian and a vector
    with test("L-operator, vector on the left"):
        W = T.dmatrix('W')
        v = T.dvector('v')
        x = T.dvector('x')
        y = T.dot(x, W)
        VJ = T.Lop(y, W, v)
        f = theano.function([v,x], VJ)
        f([2, 2], [0, 1]).must_close(
                [[ 0.,  0.], [ 2.,  2.]])

    with test("Hessian times a Vector"):
        x = T.dvector('x')
        v = T.dvector('v')
        y = T.sum(x ** 2)
        gy = T.grad(y, x)
        vH = T.grad(T.sum(gy * v), x)
        f = theano.function([x, v], vH)
        f([4, 4], [2, 2]).must_close([ 4.,  4.])

        x = T.dvector('x')
        v = T.dvector('v')
        y = T.sum(x ** 2)
        gy = T.grad(y, x)
        Hv = T.Rop(gy, x, v)
        f = theano.function([x, v], Hv)
        f([4, 4], [2, 2]).must_close([ 4.,  4.])


