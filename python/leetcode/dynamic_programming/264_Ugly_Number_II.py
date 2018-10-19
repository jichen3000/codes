# catalog
class Solution(object):
    def nthUglyNumber(self, n):
        ugly = [1]
        i2, i3, i5 = 0, 0, 0
        for i in xrange(1,n):
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min((u2, u3, u5))
            if umin == u2:
                i2 += 1
            if umin == u3:
                i3 += 1
            if umin == u5:
                i5 += 1
            ugly.append(umin)
        return ugly[-1]
                
            
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().nthUglyNumber(200).must_equal(16200)