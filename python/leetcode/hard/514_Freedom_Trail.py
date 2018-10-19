# import sys
# 30mins
class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        n = len(ring)
        m = len(key)
        maxint = m * n
        dp = [ [0] * n for _ in range(m+1)]
        for i in range(m-1, -1, -1):
            for j in range(n):
                dp[i][j] = maxint
                for k in range(n):
                    if ring[k] == key[i]:
                        diff = abs(k-j)
                        step = min(diff, n-diff)
                        dp[i][j] = min(dp[i][j], step + dp[i+1][k])
        return dp[0][0] + m
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        n = len(ring)
        m = len(key)
        dp = [ [0] * n for _ in range(m+1)]
        def cal_step(j,k):
            diff = abs(j-k)
            return min(diff, n-diff)
        for i in range(m-1, -1, -1):
            for j in range(n):
                dp[i][j] = min(cal_step(j,k) + dp[i+1][k] 
                        for k in range(n) if ring[k] == key[i])
        return dp[0][0] + m
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        n = len(ring)
        m = len(key)
        ring_dict = {}
        for j in range(n):
            if ring[j] in ring_dict:
                ring_dict[ring[j]] += j,
            else:
                ring_dict[ring[j]] = [j]
        dp = [ [0] * n for _ in range(m+1)]
        def cal_step(j,k):
            diff = abs(j-k)
            return min(diff, n-diff)
        step_dict = {}
        for i in range(n):
            for j in range(n):
                step_dict[(i,j)] = cal_step(i,j)

        for i in range(m-1, 0, -1):
            for j in range(n):
                dp[i][j] = min(step_dict[(j,k)] + dp[i+1][k] 
                        for k in ring_dict[key[i]])
        i = 0
        j = 0
        dp[i][j] = min(cal_step(j,k) + dp[i+1][k] 
                for k in ring_dict[key[i]])
        return dp[0][0] + m


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().findRotateSteps("abcde","ade").must_equal(6)
        # Solution().findRotateSteps("pqwcx", "cpqwx").must_equal(13)
        # Solution().findRotateSteps("caotmcaataijjxi",
        #         "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx").must_equal(137)
        Solution().findRotateSteps("cpmgdtkdetcaocnvkzbvntldl",
                "dcbaggdvnctdekvzcncpnmtlvamdzmpnltvbtckkdoltkkovklcncnctogattdgvzncvotclklcldvddtledadkcnpttzbebepdm").must_equal(493)

