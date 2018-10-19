import numpy

from guppy import hpy

if __name__ == '__main__':
    from minitest import *

    with test(""):
        h = hpy()
        print h.heap()
        numpy.random.seed(2)
        a = numpy.random.rand(10000000)
        for i in range(1000):
            b = numpy.partition(a, 10000)
        # b.nbytes.p()
        h = hpy()
        print h.heap()
