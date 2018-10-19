# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        from heapq import heappop, heappush
        # intervals = [(x.start, x.end) for x in intervals]
        intervals.sort(key=lambda x: (x[0], x[1]))
        # intervals.p()
        q, res = [], 0
        for item in intervals:
            # (item, q).p()
            while q:
                if q[0] <= item[0]:
                    heappop(q)
                else:
                    break
            heappush(q, item[1])
            res = max(res, len(q))
        return res

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().minMeetingRooms([[2,11],[6,16],[11,16]]).must_equal(2)
        Solution().minMeetingRooms([[4,18],[1,35],[12,45],[25,46],[22,27]]).must_equal(4)
        Solution().minMeetingRooms([[8,14],[12,13],[6,13],[1,9]]).must_equal(3)


