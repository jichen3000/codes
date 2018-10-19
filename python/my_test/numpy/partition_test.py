import numpy

if __name__ == '__main__':
    from minitest import *

    inject(numpy.allclose, 'must_close')

    with test("partition"):
        numpy.random.seed(2)
        a = numpy.random.rand(5)
        # numpy.partition(a, 10000)
        b = a.partition(2)
        b.must_equal(None)
        a.must_close([ 0.02592623,  0.4203678 ,  0.43532239,  0.54966248,  0.4359949 ])

    with test("partition matrix"):
        numpy.random.seed(2)
        a = numpy.random.rand(20).reshape(10,2)
        a.p()
        a.partition(4,0)
        a.p()
