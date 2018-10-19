class Solution:
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        def dfs(s, f1, v1, v2):
            if not s:
                return v1 > v2
            if f1:
                return dfs(s[1:], False, v1+s[0], v2) or dfs(s[:-1], False, v1+s[-1], v2)
            else:
                return dfs(s[1:], True, v1, v2+s[0]) or dfs(s[:-1], True, v1, v2+s[-1])

        return dfs(piles, True, 0, 0)
         
    def stoneGame(self, s):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(s)
        dp = [ [0] * n for _ in range(n)]
        for l in range(1, n, 2):
            for i in range(0, n-l):
                j = i + l
                if l == 1:
                    dp[i][j] = max(s[i],s[j])
                else:
                    dp[i][j] = max(s[i] + dp[i+2][j],
                                  s[i] + dp[i+1][j-1],
                                  s[j] + dp[i+1][j-1],
                                  s[j] + dp[i][j-2])
        return dp[0][-1] * 2 > sum(s)         
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().stoneGame([5,3,4,5]).must_equal(True)
        Solution().stoneGame([3,7,2,3]).must_equal(True)
