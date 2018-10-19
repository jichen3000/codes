import numpy
import theano.tensor as T
from theano import function
import theano


from theano.ifelse import ifelse

import time

if __name__ == '__main__':
    from minitest import *
    inject(numpy.allclose, 'must_close')

    # http://deeplearning.net/software/theano/tutorial/conditions.html
    with test("if"):
        a,b = T.scalars('a', 'b')
        x,y = T.matrices('x', 'y')

        z_lazy = ifelse(T.lt(a, b), T.mean(x), T.mean(y))
        f_lazyifelse = theano.function([a, b, x, y], z_lazy,
                                       mode=theano.Mode(linker='vm'))

        val1 = 0.
        val2 = 1.
        big_mat1 = numpy.ones((2, 2))
        big_mat2 = numpy.ones((2, 2))

        f_lazyifelse(val1, val2, big_mat1, big_mat2).must_close(
            [1.0])

    with test("if with value"):
        a = T.scalar()
        x = ifelse(T.lt(a, 20),  T.cast(100, 'int32'), T.cast(200, 'int32'))
        # the below line will report error, since 100 is int8, 200 is int16
        # x = ifelse(T.lt(a, 20),  100, 200)
        f = theano.function([a], x)
        f(10).must_close(100)
        f(30).must_close(200)


    with test("switch"):
        a,b = T.scalars('a', 'b')
        x,y = T.matrices('x', 'y')

        z_switch = T.switch(T.lt(a, b), T.mean(x), T.mean(y))
        f_switch = theano.function([a, b, x, y], z_switch,
                                   mode=theano.Mode(linker='vm'))

        val1 = 0.
        val2 = 1.
        big_mat1 = numpy.ones((2, 2))
        big_mat2 = numpy.ones((2, 2))


        f_switch(val1, val2, big_mat1, big_mat2).must_close(
            [1.0])

    # switch evaluates both ouput variables
    # ifelse only one
    # with test("performance"):
    #     a,b = T.scalars('a', 'b')
    #     x,y = T.matrices('x', 'y')

    #     z_switch = T.switch(T.lt(a, b), T.mean(x), T.mean(y))
    #     z_lazy = ifelse(T.lt(a, b), T.mean(x), T.mean(y))

    #     f_switch = theano.function([a, b, x, y], z_switch,
    #                                mode=theano.Mode(linker='vm'))
    #     f_lazyifelse = theano.function([a, b, x, y], z_lazy,
    #                                    mode=theano.Mode(linker='vm'))

    #     val1 = 0.
    #     val2 = 1.
    #     big_mat1 = numpy.ones((10000, 1000))
    #     big_mat2 = numpy.ones((10000, 1000))

    #     n_times = 100

    #     tic = time.clock()
    #     for i in range(n_times):
    #         f_switch(val1, val2, big_mat1, big_mat2)
    #     print('time spent evaluating both (switch) values %f sec' % (time.clock() - tic))

    #     tic = time.clock()
    #     for i in range(n_times):
    #         f_lazyifelse(val1, val2, big_mat1, big_mat2)
    #     print('time spent evaluating one (if) value %f sec' % (time.clock() - tic))        