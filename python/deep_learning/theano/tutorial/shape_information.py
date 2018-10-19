import numpy
import theano.tensor as T
from theano import function
import theano

if __name__ == '__main__':
    from minitest import *
    inject(numpy.allclose, 'must_close')

    # http://deeplearning.net/software/theano/tutorial/shape_info.html
    with test("simple"):
        x = theano.tensor.matrix('x')
        f = theano.function([x], (x ** 2).shape)
        theano.printing.debugprint(f)