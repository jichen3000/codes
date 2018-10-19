class Solution:
    ## TLE 40mins
    def minmaxGasDist(self, stations, k):
        """
        :type stations: List[int]
        :type k: int
        :rtype: float
        """
        from heapq import heappop, heappush
        from math import ceil
        if not stations: return None
        if len(stations) < 2: return 0
        # stations.sort()
        q = []
        for i in range(1, len(stations)):
            dist = stations[i] - stations[i-1]
            heappush(q, (-dist, 0 , dist))
        if k == 0: return -heappop(q)
        if len(q) == 1: return -heappop(q) / (k+1)
        while k > 0:
            max_dist, count, origin = heappop(q)
            max_dist = -max_dist
            second_dist = -q[0][0]
            # (k,max_dist, second_dist, q).p()
            need_k = max(ceil(origin / second_dist) - 1 - count, 1) 
            # need_k.p()
            if k >= need_k:
                k -= need_k
                heappush(q, (-(origin / (count+need_k+1)) , count+need_k, origin))
            else:
                return origin / (k+count+1)
        return -q[0][0]


    def minmaxGasDist(self, stations, k):
        """
        :type stations: List[int]
        :type k: int
        :rtype: float
        """
        import math
        left, right = 1e-6, stations[-1] - stations[0]
        while left + 1e-6 < right:
            mid = (left + right) / 2
            # count is the number of gas station we need to make it possible
            count = sum(math.ceil((stations[i] - stations[i-1]) / mid) - 1 
                    for i in range(1, len(stations)))
            # it means mid is too small to realize using only K more stations
            if count > k:
                left = mid
            # it means mid is possible and we can continue to find a bigger one
            else:
                right = mid
        return right

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().minmaxGasDist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10],9).must_equal(0.5)
        Solution().minmaxGasDist([1,2,3,5,7],1).must_equal(2)
        Solution().minmaxGasDist([1,2,3,5,7],2).must_equal(1)
        Solution().minmaxGasDist([10,19,25,27,56,63,70,87,96,97],3).must_equal(9.666666666666666)
        Solution().minmaxGasDist([13,15,20,31,46,49,51,52,67,87],7).must_equal(6.666666666666667)

