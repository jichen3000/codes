class Solution:
    def consecutiveNumbersSum(self, n):
        """
        :type N: int
        :rtype: int
        """
        i, res = 1, 1
        while 2*i+1 <= n:
            l = 2
            while (2*i-1+l)*l < 2 * n:
                l += 1
            if (2*i-1+l)*l == 2 * n:
                res += 1
            i += 1
        return res
            
    def consecutiveNumbersSum(self, n):
        """
        :type N: int
        :rtype: int
        """
        l, res = 2, 1
        while (1+l)*l <= 2 * n:
            i = n / l + (1-l) / 2
            # (l,i, i == int(i)).p()
            if i == int(i):
                res += 1
            l += 1
        return res

        
if __name__ == '__main__':
    from minitest import *

    with test("Solution"):
        # Solution().consecutiveNumbersSum(5).must_equal(2)
        Solution().consecutiveNumbersSum(9).must_equal(3)
        Solution().consecutiveNumbersSum(400).must_equal(3)
