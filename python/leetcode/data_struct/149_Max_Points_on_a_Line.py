# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b
    
def create_points(l):
    return [Point(x,y) for x, y in l]

class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        from collections import defaultdict
        if not points: return 0
        n = len(points)
        counts = defaultdict(lambda : 0)
        for i in range(n):
            pi = points[i]
            counts[(pi.x, pi.y)] += 1
        point_list = list(counts.keys())
        pn = len(point_list)
        res = max(counts.values())
        for i in range(pn-1):
            xi,yi = point_list[i]
            mem = defaultdict(lambda : counts[(xi, yi)])
            # print(mem)
            for j in range(i+1, pn):
                xj,yj = point_list[j]
                if xi == xj:
                    k = float("inf")
                    b = xi
                else:
                    k = (yi-yj) / (xi - xj)
                    # k.p()
                    b = round(yi + yj - k * (xi + xj), 8)
                # (point_list[i], point_list[j], k, b).p()
                mem[(k, b)] += counts[(xj, yj)]
            res = max(res, max(mem.values()))
            # print(res, mem)
        return res
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().maxPoints(create_points(
        #         [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])).must_equal(4)
        # Solution().maxPoints(create_points(
        #         [[1,1],[1,1],[2,3]])).must_equal(3)
        Solution().maxPoints(create_points(
                [[3,1],[12,3],[3,1],[-6,-1]])).must_equal(4)


        