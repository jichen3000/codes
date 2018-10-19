## grid

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0:
            return 0
        n = len(grid[0])
        dp = [[0] * n for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[i][j]
                else:
                    left_v = float("inf")
                    if j - 1 >=0:
                        left_v = dp[i][j-1]
                    top_v = float("inf")
                    if i - 1 >=0:
                        top_v = dp[i-1][j]
                    dp[i][j] = min(left_v, top_v) + grid[i][j]
                    # print(i,j,left_v, top_v)

        # print(dp)
        return dp[m-1][n-1]
                        
        