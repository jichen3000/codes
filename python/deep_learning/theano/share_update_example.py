import numpy
import theano.tensor as T
from theano import function
import theano

if __name__ == '__main__':
    from minitest import *
    inject(numpy.allclose, 'must_close')


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

    with test("hash"):
        state = theano.shared(0)
        inc = T.iscalar('inc')
        accumulator = function([inc], state, updates={state: state+inc})
        state.get_value().must_equal(0)
        accumulator(1).must_close(0)
        state.get_value().must_equal(1)
        accumulator(300).must_close(1)
        state.get_value().must_equal(301)


    with test("replace"):
        state = theano.shared(0)
        inc = T.iscalar('inc')
        fn_of_state = state * 2 + inc
        # The type of foo must match the shared variable we are replacing
        # with the ``givens``
        foo = T.scalar(dtype=state.dtype)
        skip_shared = function([inc, foo], fn_of_state, givens=[(state, foo)])
        skip_shared(1, 3).must_close(7)  # we're using 3 for the state, not state.value
        state.get_value().must_equal(0)  # old state still there, but we didn't use it        

