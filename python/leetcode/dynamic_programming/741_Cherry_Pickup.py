class Solution(object):
    # 36mins not working
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        dp = [(0,[]) for _ in range(n+1)]
        pre = dp
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:
                    dp[j+1] = (-1, None)
                else:
                    if pre[j+1][0] == -1 and dp[j][0] == -1:
                        return 0
                    last = pre[j+1] if pre[j+1][0] > dp[j][0] else dp[j]
                    # (i,j,last).p()
                    if grid[i][j] == 1:
                        last[1].append((i,j))
                        dp[j+1] = (last[0]+1, last[1][:])
                    else:
                        dp[j+1] = (last[0], last[1][:])                    
            pre = dp
        first_count = dp[-1][0]
        # first_count.p()
        for x,y in dp[-1][1]:
            grid[x][y] = 0
        dp = [0] * (n+1)
        pre = dp
        for i in range(m):
            for j in range(n):
                if grid[i][j] == -1:                    
                    dp[j+1] = 0
                else:
                    dp[j+1] = max(pre[j+1], dp[j]) + grid[i][j]
                # (i,j, grid[i][j], dp[j+1]).p()
            pre = dp
        # dp.p()
        return first_count + dp[-1]
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        mem = {}
        def dp(r1, c1, r2):
            c2 = r1 + c1 - r2
            if c1 == n or c2 == n or r1 == n or r2 == n:
                return float('-inf')
            if grid[c1][r1] == -1 or grid[c2][r2] == -1:
                return float('-inf')
            if r1 == c1 == n -1:
                return grid[c1][r1]
            if (r1,c1,r2) in mem:
                return mem[(r1,c1,r2)]
            add_v = grid[c1][r1] + (grid[c2][r2] if c1 != c2 else 0)
            ans = add_v + max(
                dp(r1+1, c1, r2), #c2+1
                dp(r1, c1+1, r2), #c2+1
                dp(r1+1, c1, r2+1), #c2
                dp(r1, c1+1, r2+1)  #c2
            )
            mem[(r1,c1,r2)] = ans
            return ans
        return max(0, dp(0,0,0))



        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().cherryPickup([[0,1,-1],[1,0,-1],[1,1,1]]).must_equal(5)
        # Solution().cherryPickup([[0,1,-1],[1,0,-1],[1,-1,1]]).must_equal(0)
        # Solution().cherryPickup([
        #         [1,1,1,1,0,0,0],
        #         [0,0,0,1,0,0,0],
        #         [0,0,0,1,0,0,1],
        #         [1,0,0,1,0,0,0],
        #         [0,0,0,1,0,0,0],
        #         [0,0,0,1,0,0,0],
        #         [0,0,0,1,1,1,1]]).must_equal(15)
