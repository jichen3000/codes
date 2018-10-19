# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        res = []
        intervals.sort(key=lambda x: x.start)
        for i in range(len(intervals)):
            if res and intervals[i].start <= res[-1].end:
                res[-1].end = max(intervals[i].end, res[-1].end)
            else:
                res += intervals[i],
        return res
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        first you need to understand the above, then you can understand this one
        see the discussion
        """
        res = []
        starts = sorted([i.start for i in intervals])
        ends = sorted([i.end for i in intervals])
        j, n = 0, len(intervals)
        for i in range(n):
            if i == n - 1 or starts[i+1] > ends[i]:
                res += Interval(starts[j], ends[i]),
                j = i + 1
        return res        