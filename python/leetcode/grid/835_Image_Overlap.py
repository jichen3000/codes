class Solution(object):
    def largestOverlap(self, a, b):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: int
        """
        if not a or not a[0]: return 0
        m, n = len(a), len(a[0])
        a_points, b_points = set(), set()
        for i in range(m):
            for j in range(n):
                if a[i][j] == 1:
                    a_points.add((i,j))
                if b[i][j] == 1:
                    b_points.add((i,j))
        res = 0
        for di in range(-m+1, m):
            for dj in range(-n+1, n):
                count = 0
                for i, j in a_points:
                    np = (i+di, j+dj)
                    if np in b_points:
                        count += 1
                res = max(res, count)
        return res
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().largestOverlap(
                [[1,1,0],[0,1,0],[0,1,0]],
                [[0,0,0],[0,1,1],[0,0,1]]).must_equal(3)
        # this should be wrong
        Solution().largestOverlap([
                [0,1],
                [1,1]],[
                [1,1],
                [1,0]]).must_equal(3)
