class Solution(object):
    ## TLE 30mins
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if k == 1: return 1
        cur = 1
        for i in range(2,k+1):
            nxt = cur * 10
            if nxt > n:
                nxt = cur + 1
                if nxt > n:
                    nxt = cur / 10 + 1
                else:
                    while nxt % 10 == 0:
                        nxt /= 10                    
            cur = nxt
        return cur
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def cal_steps(cur, nxt):
            steps = 0
            while cur < n:
                steps += min(n+1, nxt) - cur
                cur *= 10
                nxt *= 10
            return steps
        cur = 1
        k = k - 1
        while k > 0:
            steps = cal_steps(cur, cur+1)
            if steps <= k:
                k -= steps
                cur += 1
            else:
                k -= 1
                cur = cur * 10
        return cur

if __name__ == '__main__':
    from minitest import *


    with test(Solution):
        # Solution().findKthNumber(13, 2).must_equal(10)
        # Solution().findKthNumber(2, 1).must_equal(1)
        # Solution().findKthNumber(2, 2).must_equal(2)
        # Solution().findKthNumber(10, 3).must_equal(2)
        # Solution().findKthNumber(100, 10).must_equal(17)
        # Solution().findKthNumber(1999, 9).must_equal(1005)
        Solution().findKthNumber(7747794,5857460).must_equal(6271710)
