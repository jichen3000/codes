import numpy
import theano.tensor as T
from theano import function
import theano

if __name__ == '__main__':
    from minitest import *
    inject(numpy.allclose, 'must_close')

    # http://deeplearning.net/software/theano/tutorial/loop.html#tutloop
    # Number of iterations to be part of the symbolic graph.
    # Minimizes GPU transfers (if GPU is involved).
    # Computes gradients through sequential steps.
    # Slightly faster than using a for loop in Python with a compiled Theano function.
    # Can lower the overall memory usage by detecting the actual amount of memory needed.    
    with test("Computing tanh(x(t).dot(W) + b) elementwise"):
        # defining the tensor variables
        X = T.matrix("X")
        W = T.matrix("W")
        b_sym = T.vector("b_sym")

        results, updates = theano.scan(
            lambda v: T.tanh(T.dot(v, W) + b_sym), sequences=X)
        # results, updates = theano.scan(
        #     lambda v: T.dot(v, W + b_sym), sequences=X)
        compute_elementwise = theano.function(
            inputs=[X, W, b_sym], outputs=results)

        # test values
        x = numpy.eye(2, dtype=theano.config.floatX)
        w = numpy.ones((2, 2), dtype=theano.config.floatX)
        b = numpy.ones((2), dtype=theano.config.floatX)
        b[1] = 2

        compute_elementwise(x, w, b).must_close(
            [[ 0.96402758, 0.99505475],
             [ 0.96402758,  0.99505475]]        
        )

        # comparison with numpy
        numpy.tanh(x.dot(w) + b).must_close(
            [[ 0.96402758,  0.99505475],
             [ 0.96402758,  0.99505475]]
        )


    with test("Computing the sequence x(t) = tanh(x(t - 1).dot(W) + y(t).dot(U) + p(T - t).dot(V))"):
        # define tensor variables
        X = T.vector("X")
        W = T.matrix("W")
        U = T.matrix("U")
        Y = T.matrix("Y")
        V = T.matrix("V")
        P = T.matrix("P")

        results, updates = theano.scan(lambda y, p, x_tm1: T.tanh(T.dot(x_tm1, W) + T.dot(y, U) + T.dot(p, V)),
                  sequences=[Y, P[::-1]], outputs_info=[X])
        compute_seq = theano.function(inputs=[X, W, Y, U, P, V], outputs=results)

        # test values
        x = numpy.zeros((2), dtype=theano.config.floatX)
        x[1] = 1
        w = numpy.ones((2, 2), dtype=theano.config.floatX)
        y = numpy.ones((5, 2), dtype=theano.config.floatX)
        y[0, :] = -3
        u = numpy.ones((2, 2), dtype=theano.config.floatX)
        p = numpy.ones((5, 2), dtype=theano.config.floatX)
        p[0, :] = 3
        v = numpy.ones((2, 2), dtype=theano.config.floatX)

        compute_seq(x, w, y, u, p, v).must_close(
            [  [-0.99505475, -0.99505475],
               [ 0.96471973,  0.96471973],
               [ 0.99998585,  0.99998585],
               [ 0.99998771,  0.99998771],
               [ 1.        ,  1.        ]])

        # comparison with numpy
        x_res = numpy.zeros((5, 2), dtype=theano.config.floatX)
        x_res[0] = numpy.tanh(x.dot(w) + y[0].dot(u) + p[4].dot(v))
        for i in range(1, 5):
            x_res[i] = numpy.tanh(x_res[i - 1].dot(w) + y[i].dot(u) + p[4-i].dot(v))
        x_res.must_close([ [-0.99505475, -0.99505475],
                           [ 0.96471973,  0.96471973],
                           [ 0.99998585,  0.99998585],
                           [ 0.99998771,  0.99998771],
                           [ 1.        ,  1.        ]])

    with test("Computing norms of lines of X"):
        # define tensor variable
        X = T.matrix("X")
        results, updates = theano.scan(lambda x_i: T.sqrt((x_i ** 2).sum()), sequences=[X])
        compute_norm_lines = theano.function(inputs=[X], outputs=results)

        # test value
        x = numpy.diag(numpy.arange(1, 6, dtype=theano.config.floatX), 1)
        compute_norm_lines(x).must_close(
                [ 1., 2., 3., 4., 5., 0.])

        # comparison with numpy
        numpy.sqrt((x ** 2).sum(1)).must_close(
                [ 1., 2., 3., 4., 5., 0.])




    with test("Computing norms of columns of X"):
        # define tensor variable
        X = T.matrix("X")
        results, updates = theano.scan(lambda x_i: T.sqrt((x_i ** 2).sum()), sequences=[X.T])
        compute_norm_cols = theano.function(inputs=[X], outputs=results)

        # test value
        x = numpy.diag(numpy.arange(1, 6, dtype=theano.config.floatX), 1)
        compute_norm_cols(x).must_close(
                [ 0.,  1.,  2.,  3.,  4.,  5.])

        # comparison with numpy
        numpy.sqrt((x ** 2).sum(0)).must_close(
                [ 0.,  1.,  2.,  3.,  4.,  5.])

    with test("Computing trace of X"):
        floatX = "float32"

        # define tensor variable
        X = T.matrix("X")
        results, updates = theano.scan(lambda i, j, t_f: T.cast(X[i, j] + t_f, floatX),
                          sequences=[T.arange(X.shape[0]), T.arange(X.shape[1])],
                          outputs_info=numpy.asarray(0., dtype=floatX))
        result = results[-1]
        compute_trace = theano.function(inputs=[X], outputs=result)

        # test value
        x = numpy.eye(5, dtype=theano.config.floatX)
        x[0] = numpy.arange(5, dtype=theano.config.floatX)
        compute_trace(x).must_close([4.0])

        # comparison with numpy
        numpy.diagonal(x).sum().must_close([4.0])

    with test("Computing the sequence x(t) = x(t - 2).dot(U) + x(t - 1).dot(V) + tanh(x(t - 1).dot(W) + b)"):
        # define tensor variables
        X = T.matrix("X")
        W = T.matrix("W")
        b_sym = T.vector("b_sym")
        U = T.matrix("U")
        V = T.matrix("V")
        n_sym = T.iscalar("n_sym")

        results, updates = theano.scan(
                lambda x_tm2, x_tm1: T.dot(x_tm2, U) + T.dot(x_tm1, V) + T.tanh(T.dot(x_tm1, W) + b_sym),
                n_steps=n_sym, 
                outputs_info=[dict(initial=X, taps=[-2, -1])])
        compute_seq2 = theano.function(inputs=[X, U, V, W, b_sym, n_sym], outputs=results)

        # test values
        x = numpy.zeros((2, 2), dtype=theano.config.floatX) # the initial value must be able to return x[-2]
        x[1, 1] = 1
        w = 0.5 * numpy.ones((2, 2), dtype=theano.config.floatX)
        u = 0.5 * (numpy.ones((2, 2), dtype=theano.config.floatX) - numpy.eye(2, dtype=theano.config.floatX))
        v = 0.5 * numpy.ones((2, 2), dtype=theano.config.floatX)
        n = 10
        b = numpy.ones((2), dtype=theano.config.floatX)

        compute_seq2(x, u, v, w, b, n).must_close(
                [  [  1.40514825,   1.40514825],
                   [  2.88898899,   2.38898899],
                   [  4.34018291,   4.34018291],
                   [  6.53463142,   6.78463142],
                   [  9.82972243,   9.82972243],
                   [ 14.22203814,  14.09703814],
                   [ 20.07439936,  20.07439936],
                   [ 28.12291843,  28.18541843],
                   [ 39.1913681 ,  39.1913681 ],
                   [ 54.28407732,  54.25282732]])

        # comparison with numpy
        x_res = numpy.zeros((10, 2))
        x_res[0] = x[0].dot(u) + x[1].dot(v) + numpy.tanh(x[1].dot(w) + b)
        x_res[1] = x[1].dot(u) + x_res[0].dot(v) + numpy.tanh(x_res[0].dot(w) + b)
        x_res[2] = x_res[0].dot(u) + x_res[1].dot(v) + numpy.tanh(x_res[1].dot(w) + b)
        for i in range(2, 10):
            x_res[i] = (x_res[i - 2].dot(u) + x_res[i - 1].dot(v) +
                        numpy.tanh(x_res[i - 1].dot(w) + b))
        x_res.must_close(
                [  [  1.40514825,   1.40514825],
                   [  2.88898899,   2.38898899],
                   [  4.34018291,   4.34018291],
                   [  6.53463142,   6.78463142],
                   [  9.82972243,   9.82972243],
                   [ 14.22203814,  14.09703814],
                   [ 20.07439936,  20.07439936],
                   [ 28.12291843,  28.18541843],
                   [ 39.1913681 ,  39.1913681 ],
                   [ 54.28407732,  54.25282732]])

    with test("Computing the Jacobian of y = tanh(v.dot(A)) wrt x"):
        # define tensor variables
        v = T.vector()
        A = T.matrix()
        y = T.tanh(T.dot(v, A))
        results, updates = theano.scan(
                lambda i: T.grad(y[i], v), 
                sequences=[T.arange(y.shape[0])])
        compute_jac_t = theano.function([A, v], results, 
                allow_input_downcast=True) # shape (d_out, d_in)

        # test values
        x = numpy.eye(5, dtype=theano.config.floatX)[0]
        w = numpy.eye(5, 3, dtype=theano.config.floatX)
        w[2] = numpy.ones((3), dtype=theano.config.floatX)
        compute_jac_t(w, x).must_close(
                [[ 0.41997434,  0,  0.41997434,  0,  0],
                   [ 0,  1,  1,  0,  0],
                   [ 0,  0,  1,  0,  0]])

        # compare with numpy
        ((1 - numpy.tanh(x.dot(w)) ** 2) * w).T.must_close(
                [[ 0.41997434,  0,  0.41997434,  0,  0],
                   [ 0,  1,  1,  0,  0],
                   [ 0,  0,  1,  0,  0]])

    with test("Accumulate number of loop during a scan"):
        # define shared variables
        k = theano.shared(0)
        n_sym = T.iscalar("n_sym")

        results, updates = theano.scan(lambda:{k:(k + 1)}, n_steps=n_sym)
        accumulator = theano.function([n_sym], [], updates=updates, allow_input_downcast=True)

        k.get_value().must_close(0)
        accumulator(5)
        k.get_value().must_close(5)


    with test("Computing tanh(v.dot(W) + b) * d where d is binomial"):
        X = T.matrix("X")
        W = T.matrix("W")
        b_sym = T.vector("b_sym")

        # define shared random stream
        trng = T.shared_randomstreams.RandomStreams(1234)
        d=trng.binomial(size=W[1].shape)

        results, updates = theano.scan(
                lambda v: T.tanh(T.dot(v, W) + b_sym) * d, 
                sequences=X)
        compute_with_bnoise = theano.function(
                inputs=[X, W, b_sym], outputs=results,
                # updates=updates, 
                allow_input_downcast=True)
        x = numpy.eye(10, 2, dtype=theano.config.floatX)
        w = numpy.ones((2, 2), dtype=theano.config.floatX)
        b = numpy.ones((2), dtype=theano.config.floatX)

        compute_with_bnoise(x, w, b).must_close(
                [  [ 0.96402758,  0.        ],
                   [ 0.        ,  0.96402758],
                   [ 0.        ,  0.        ],
                   [ 0.76159416,  0.76159416],
                   [ 0.76159416,  0.        ],
                   [ 0.        ,  0.76159416],
                   [ 0.        ,  0.76159416],
                   [ 0.        ,  0.76159416],
                   [ 0.        ,  0.        ],
                   [ 0.76159416,  0.76159416]])

    with test("Computing pow(A, k)"):
        # theano.config.warn.subtensor_merge_bug = False

        k = T.iscalar("k")
        A = T.vector("A")

        def inner_fct(prior_result, B):
            return prior_result * B

        # Symbolic description of the result
        # n_steps, aka k would not be as an argument
        result, updates = theano.scan(
                fn=inner_fct,
                outputs_info=T.ones_like(A),
                non_sequences=A, n_steps=k)

        # Scan has provided us with A ** 1 through A ** k.  Keep only the last
        # value. Scan notices this and does not waste memory saving them.
        final_result = result[-1]
        # final_result = result

        power = theano.function(
                inputs=[A, k], 
                outputs=final_result,
                updates=updates)

        power(range(10), 2).must_close(
                [  0,  1,  4,  9, 16, 25, 36, 49, 64, 81.])

    with test("Calculating a Polynomial"):
        coefficients = theano.tensor.vector("coefficients")
        x = T.scalar("x")
        max_coefficients_supported = 100

        # Generate the components of the polynomial
        full_range=theano.tensor.arange(max_coefficients_supported)
        components, updates = theano.scan(
                fn=lambda coeff, power, free_var:
                    coeff * (free_var ** power),
                    outputs_info=None,
                    sequences=[coefficients, full_range],
                    non_sequences=x)

        polynomial = components.sum()
        calculate_polynomial = theano.function(
                inputs=[coefficients, x],
                outputs=polynomial)

        test_coeff = numpy.asarray([1, 0, 2], dtype=numpy.float32)
        calculate_polynomial(test_coeff, 3).must_close(19)



