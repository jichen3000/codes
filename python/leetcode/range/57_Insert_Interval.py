# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        ns, ne = newInterval.start, newInterval.end
        replaced = False
        pre = None
        if len(intervals) == 0:
            intervals.append(newInterval)
            return intervals
        for i in range(len(intervals)-1, -1, -1):
            cur = intervals[i]
            s, e = cur.start, cur.end
            if ne == e:
                if ns >= s:
                    break
                else:
                    cur.start = ns
                    pre = cur
                    replaced = True
            elif ne > e and ns <= e:
                if ns == s:
                    if replaced:
                        del intervals[i]
                    else:
                        cur.end = ne
                        break
                elif ns > s:
                    if replaced:
                        pre.start = s
                        del intervals[i]
                        break
                    else:
                        cur.end = ne
                        pre = cur
                        replaced = True
                else:
                    if replaced:
                        del intervals[i]
                    else:
                        cur.start, cur.end = ns, ne
                        pre = cur
                        replaced = True
            elif ne < e and ne >= s:
                if ns >= s:
                    break
                else:
                    cur.start = ns
                    pre = cur
                    replaced = True
            elif ns > e:
                if not replaced:
                    intervals.insert(i+1, newInterval)
                break
            elif ne < s and i == 0:
                intervals.insert(0, newInterval)


        return intervals

