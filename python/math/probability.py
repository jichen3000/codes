from __future__ import division
import operator as op
import math
import numpy as np
def ncr(n, r):
    r = min(r, n-r)
    if r == 0: return 1
    numer = reduce(op.mul, xrange(n, n-r, -1))
    denom = reduce(op.mul, xrange(1, r+1))
    return numer//denom



if __name__ == '__main__':
    from minitest import *

    with test(ncr):
        ncr(3,2).p()
        ncr(52,5).p()
        # (float(ncr(13,5))*4/ncr(52,5) ).p()

        # (float(52*3*48*44*40)/math.factorial(3)/2/ncr(52,5)).p()

        (float(ncr(13,1) * ncr(4,2) * ncr(12,3) * 4 * 4 * 4)/ncr(52,5)).p()
        (float(ncr(13,2) * ncr(4,2) * ncr(4,2) * ncr(11,1) * 4)/ncr(52,5)).p()
        (float(ncr(13,1) * ncr(4,3) * ncr(12,2) * 4 * 4)/ncr(52,5)).p()
        (float(ncr(13,1) * ncr(12,1) * 4)/ncr(52,5)).p()
        np.sum([i**4 for i in range(7)]).p()


