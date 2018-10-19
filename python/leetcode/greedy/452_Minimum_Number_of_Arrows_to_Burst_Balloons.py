class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        points.sort()
        if n == 0: return 0
        dp = [1] * n
        def cover(p1,p2):
            return p2[0] <= p1[1]            
        for i in xrange(1,n):
            for k in xrange(i-1,-1,-1):
                if cover(points[k], points[i]):
                    dp[i] = max(dp[i], dp[k])
                else:
                    dp[i] = max(dp[i], dp[k]+1)
                    break
        return dp[-1]
        
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n == 0: return 0
        points.sort(key=lambda x: x[1])
        shoot_pos = points[0][1]
        arrow_count = 1
        for i in xrange(1, n):
            if points[i][0] > shoot_pos:
                shoot_pos = points[i][1]
                arrow_count += 1
        return arrow_count

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]).must_equal(2)