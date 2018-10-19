import numpy
import theano.tensor as T
from theano import function
import theano

if __name__ == '__main__':
    from minitest import *
    inject(numpy.allclose, 'must_close')

    # http://deeplearning.net/software/theano/tutorial/examples.html
    with test("Logistic Function"):
        x = T.dmatrix('x')
        s = 1 / (1+T.exp(-x))
        logistic = function([x], s)
        logistic([[0, 1], [-1, -2]]).must_close(
                [   [ 0.5       ,  0.73105858],
                    [ 0.26894142,  0.11920292]])

        s2 = (1 + T.tanh(x / 2)) / 2
        logistic2 = function([x], s2)
        logistic2([[0, 1], [-1, -2]]).must_close(
                [   [ 0.5       ,  0.73105858],
                    [ 0.26894142,  0.11920292]])


    with test("Computing More than one Thing at the Same Time"):
        a, b = T.dmatrices('a', 'b')
        diff = a - b
        abs_diff = abs(diff)
        diff_squared = diff**2
        f = theano.function([a, b], [diff, abs_diff, diff_squared])
        out_a, out_b, out_c = f([[1, 1], [1, 1]], [[0, 1], [2, 3]])
        out_a.must_close([[ 1.,  0.],[-1., -2.]])
        out_b.must_close([[ 1.,  0.],[1., 2.]])
        out_c.must_close([[ 1.,  0.],[1., 4.]])

    with test("Setting a Default Value for an Argument"):
        x, y= T.dscalars('x','y')
        z = x + y
        f = function([x, theano.In(y, value=1)],z)
        f(33).must_close(34.0)
        f(33,2).must_close(35.0)

        x, y, w = T.dscalars('x', 'y', 'w')
        z = (x + y) * w
        f = function([x, theano.In(y, value=1), 
                theano.In(w, value=2, name='w_by_name')], z)
        f(33).must_close(68.0)
        f(33, 2).must_close(70.0)
        f(33, 0, 1).must_close(33.0)
        f(33, w_by_name=1).must_close(34.0)
        f(33, w_by_name=1, y=0).must_close(33.0)

    with test("Using Shared Variables"):
        state = theano.shared(0)
        inc = T.iscalar('inc')
        accumulator = function([inc], state, updates=[(state, state+inc)])
        state.get_value().must_equal(0)
        accumulator(1).must_close(0)
        state.get_value().must_equal(1)
        accumulator(300).must_close(1)
        state.get_value().must_equal(301)

        state.set_value(-1)
        state.get_value().must_equal(-1)
        accumulator(3).must_close(-1)
        state.get_value().must_equal(2)

        decrementor = function([inc], state, updates=[(state, state-inc)])
        decrementor(2).must_close(2)
        state.get_value().must_equal(0)

        fn_of_state = state * 2 + inc
        # The type of foo must match the shared variable we are replacing
        # with the ``givens``
        foo = T.scalar(dtype=state.dtype)
        skip_shared = function([inc, foo], fn_of_state, givens=[(state, foo)])
        skip_shared(1, 3).must_close(7)  # we're using 3 for the state, not state.value
        state.get_value().must_equal(0)  # old state still there, but we didn't use it        

    with test("Copying functions"):
        state = theano.shared(0)
        inc = T.iscalar('inc')
        accumulator = theano.function([inc], state, updates=[(state, state+inc)])
        accumulator(10).must_close(0)
        state.get_value().must_equal(10)

        new_state = theano.shared(0)
        new_accumulator = accumulator.copy(swap={state:new_state})
        new_accumulator(100).must_close(0)
        new_state.get_value().must_equal(100)
        state.get_value().must_equal(10)

        # cannot use like this one, skip
        # null_accumulator = accumulator.copy(delete_updates=True)
        # null_accumulator(9000).must_close(10)
        # state.get_value().must_equal(10)

    with test("Using Random Numbers"):
        # this is only for cpu, for gpu use other
        # http://deeplearning.net/software/theano/tutorial/examples.html#other-implementations
        srng = T.shared_randomstreams.RandomStreams(seed=234)
        # a random of 2x2 matrices from a uniform distribution
        rv_u = srng.uniform((2,2))
        rv_n = srng.normal((2,2))
        f = function([], rv_u)
        g = function([], rv_n, no_default_updates=True)    #Not updating rv_n.rng
        nearly_zeros = function([], rv_u + rv_u - 2 * rv_u) 
        f_val0 = f()
        f_val0.must_close(
                [   [ 0.12672381,  0.97091597],
                    [ 0.13989098,  0.88754825]])       
        f_val1 = f()
        f_val1.must_close(
                [   [ 0.31971415,  0.47584377],
                    [ 0.24129163,  0.42046081]]) 
                          
        g_val0 = g()
        g_val0.must_close(
                [   [ 0.37328447, -0.65746672],
                    [-0.36302373, -0.97484625]])       
        g_val1 = g()
        g_val1.must_close(
                [   [ 0.37328447, -0.65746672],
                    [-0.36302373, -0.97484625]])

        # a random variable is drawn at most once during any single function execution
        nearly_zeros().must_close(
                [   [ 0.0, 0.0],
                    [ 0.0, 0.0]])

    with test("Seeding Streams"):
        # seed individually
        rng_val = rv_u.rng.get_value(borrow=True)   # Get the rng for rv_u
        rng_val.seed(89234)                         # seeds the generator
        rv_u.rng.set_value(rng_val, borrow=True)    # Assign back seeded rng

        # seed all
        srng.seed(902340)  # seeds rv_u and rv_n with different seeds each

    with test("Sharing Streams Between Functions"):
        state_after_v0 = rv_u.rng.get_value().get_state()
        nearly_zeros()       # this affects rv_u's generator
        v1 = f()
        rng = rv_u.rng.get_value(borrow=True)
        rng.set_state(state_after_v0)
        rv_u.rng.set_value(rng, borrow=True)
        v2 = f()             # v2 != v1
        (numpy.allclose(v1,v2)).must_equal(False)
        v3 = f()             # v3 == v1        
        v3.must_close(v1)

    with test("GPU"):
        # MRG31k3p work on the CPU and GPU
        # from theano.sandbox.rng_mrg import MRG_RandomStreams as RandomStreams
        # CURAND only work on the GPU
        pass

