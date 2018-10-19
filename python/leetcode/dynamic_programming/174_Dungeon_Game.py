import sys
class Solution(object):
    def calculateMinimumHP(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        m = len(grid)
        n = len(grid[0])
        # this method still has an issue
        # if grid[0] == [2,-8,-79,-88,-12,-87,-5,-56,-55,-42,18,-91,1,-30,-36,42,-96,-26,-17,-69,38,18,44,-58,-33,20,-45,-11,11,15,-40,-92,-62,-51,-23,20,-86,-2,-90,-64,-100,-42,-16,-55,29,-62,-81,-60,7,-5,31,-7,40,19,-53,-81,-77,42,-87,37,-43,37,-50,-21,-86,-28,13,-18,-65,-76]:
        #     return 85
        dp = [[] for _ in  range(n)]
        pre = dp
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    dp[j] = [(min(0, grid[0][0]), grid[0][0])]
                else:
                    
                    tmp_l = []
                    # (pre[j] + (dp[j-1] if j > 0 else [])).p()
                    for cur_min, cur_v in pre[j] + (dp[j-1] if j > 0 else []):
                        new_v = cur_v + grid[i][j]
                        new_min = min(cur_min, new_v)
                        tmp_l += (new_min, new_v),
                    # tmp_l = sorted(tmp_l, key=lambda x: (-x[0], -x[1]))
                    # tmp_l.p()
                    # dp[j] = [tmp_l.pop(0)]
                    tmp_l.sort()
                    dp[j] = [tmp_l.pop()]
                    for cur_min, cur_v in reversed(tmp_l):
                        pre_min, pre_v = dp[j][-1]
                        if cur_v - pre_v >= pre_min - cur_min:
                            dp[j] += (cur_min, cur_v),
                # (i,j,grid[i][j],dp[j]).p()

            pre = dp[:]
        # dp.p()
        return 1 - dp[-1][0][0]
    def calculateMinimumHP(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [-sys.maxint] * (n+1)
        pre = dp
        for i in range(m-1,-1,-1):
            if i == m-1:
                dp[-1] = 0
            else:
                dp[-1] = -sys.maxint
            for j in range(n-1,-1,-1):
                dp[j] = max(pre[j], dp[j+1])+grid[i][j]
                dp[j] = min(0, dp[j])
                # (i,j,dp[j]).p()

            pre = dp[:]
            # dp.p()
        return 1 - dp[0]

                
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().calculateMinimumHP([[0]]).must_equal(1)
        Solution().calculateMinimumHP([[-2, -3, 3],[-5,-10, 1],[10,30,-5]]).must_equal(7)
        Solution().calculateMinimumHP([[1,-3,3],[0,-2,0],[-3,-3,-3]]).must_equal(3)
        Solution().calculateMinimumHP([[0,0,0],[-1,0,0],[2,0,-2]]).must_equal(2)
