class Solution(object):
    def combine1(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if n < k:
            return []
        if n == k:
            return [range(1,n+1)]
        nums = range(n)
        dp = [[ [[]] for _ in xrange(n+1)] for _ in xrange(k+1)]
        for i in xrange(1, k+1):
            for j in xrange(i, n+1):
                if i == j:
                    dp[i][j] = [range(1,j+1)]
                    # (i,j,dp[i][j]).p()
                else:
                    dp[i][j] = dp[i][j-1] + [l+[j] for l in dp[i-1][j-1]]
                    # (i,j,dp[i][j]).p()
        # dp.p()
        return dp[k][n]
    def combine(self, n, k):
        combs = [[]]
        def inner(l, i):
            result = [i] + l
            (l,i,result).p()
            return [i] + l
        for _ in range(k):
            combs = [inner(c,i) for c in combs for i in range(1, c[0] if c else n+1)]
            combs.p()
        return combs

        
                    
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().combine(1,1).p()
        Solution().combine(5,3).p()
