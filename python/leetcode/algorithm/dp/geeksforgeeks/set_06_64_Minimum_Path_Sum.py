class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0: return 0
        dirs = [(0,-1),(-1,0)]                
        n = len(grid[0])
        def get_adjs(i,j):
            return [dp[i+x][j+y] for x,y in dirs if i+x>=0 and j+y>=0 ]
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[i][j] = grid[0][0]
                else:
                    dp[i][j] = min(get_adjs(i,j)) + grid[i][j]
        return dp[-1][-1]
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        if m == 0: return 0
        n = len(grid[0])
        dp = [0] * n
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = grid[0][0]
                else:
                    if i == 0:
                        dp[j] = dp[j-1] + grid[i][j]
                    elif j==0:
                        dp[j] += grid[i][j]
                    else:
                        dp[j] = min(dp[j-1],dp[j]) + grid[i][j]
        return dp[-1]
                        
        