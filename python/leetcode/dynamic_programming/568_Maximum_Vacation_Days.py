class Solution:
    ## TLE at 37th testcase, 30mins
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        if not flights or not flights[0] or \
                not days or not days[0]:
            return 0
        n, k = len(flights), len(days[0])
        def dfs(city, week):
            if week == k: return 0
            res = 0
            for j, v in enumerate(flights[city]):
                if v == 1 or j == city:
                    res = max(res, days[j][week] + dfs(j, week+1))
            return res
        return dfs(0, 0)

    ## TLE at 50th testcase, 90mins
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        if not flights or not flights[0] or \
                not days or not days[0]:
            return 0
        n, k = len(flights), len(days[0])
        dp = [[0] * n for _ in range(k)]
        for i in range(n):
            dp[k-1][i] = days[i][k-1]
        # (k-1, dp[k-1]).p()
        for wi in range(k-2,-1,-1):
            for ci in range(n):
                dp[wi][ci] = max(days[ci][wi] + dp[wi+1][cj] 
                        for cj in range(n) if flights[ci][cj]==1 or ci == cj)
        return max(dp[0][i] for i in range(n) if flights[0][i]==1 or i == 0)
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        if not flights or not flights[0] or \
                not days or not days[0]:
            return 0
        n, k = len(flights), len(days[0])
        dp = [days[i][k-1] for i in range(n)]
        for wi in range(k-2,-1,-1):
            pre = dp[::]
            for ci in range(n):
                dp[ci] = days[ci][wi] +  max(pre[cj] for cj in range(n) if flights[ci][cj]==1 or ci == cj)
            # dp = [max(days[ci][wi] + pre[cj] 
            #             for cj in range(n) if flights[ci][cj]==1 or ci == cj) 
            #             for ci in range(n)]
        return max(dp[i] for i in range(n) if flights[0][i]==1 or i == 0)
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().maxVacationDays([[0,1,1],[1,0,1],[1,1,0]],
                [[1,3,1],[6,0,3],[3,3,3]]).must_equal(12)
        Solution().maxVacationDays([[0,0,0],[0,0,0],[0,0,0]],
                [[1,1,1],[7,7,7],[7,7,7]]).must_equal(3)
        Solution().maxVacationDays([[0,1,0],[0,0,0],[0,0,0]],
                [[0,0,7],[2,0,0],[7,7,7]]).must_equal(7)
        Solution().maxVacationDays([[0,0,1,0,0],[0,0,0,1,1],[0,0,0,0,1],[0,1,1,0,0],[0,1,0,1,0]],
                [[3,1,6,2,2],[1,3,5,6,5],[3,2,5,0,0],[2,3,5,4,3],[3,3,1,5,4]]).must_equal(22)
