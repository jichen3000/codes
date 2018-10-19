class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        result = 1
        if x == 1: return x
        if x == -1:
            if n % 2 == 0:
                return 0-x
            else:
                return x
        if n < 0:
            x = 1 / x
            n = 0 - n
        for i in xrange(n):
            result *= x
            if result == 0:
                return result
        return result
    
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0:
            return 1
        if n < 0:
            x = 1 / x
            n = -n
        if n % 2 == 1:
            return x * self.myPow(x, n-1)
        return self.myPow(x * x, n/2)
    

    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n < 0:
            x = 1 / x
            n = -n        
        res = 1
        while n:
            if n % 2 == 1:
                res *= x
            x *= x
            # (n, res, x).p()
            n >>= 1
        return res 

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().myPow(2.0, 3).must_equal(8.0)
        Solution().myPow(2.0, 4).must_equal(16.0)
        Solution().myPow(2.0, 10).must_equal(1024.0)
