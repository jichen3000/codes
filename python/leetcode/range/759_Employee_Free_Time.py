# 759. Employee Free Time

# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def employeeFreeTime(self, avails):
        """
        :type avails: List[List[Interval]]
        :rtype: List[Interval]
        """
        from bisect import bisect
        def merge_pre(pre_i, r):
            if final[pre_i][0] <= r[0] and r[0] <= final[pre_i][1]:
                if r[1] <= final[pre_i][1]:
                    return None
                else:
                    final[pre_i][1] = r[1]
                    return [pre_i, final[pre_i]]
            else:
                final.insert(pre_i+1, r)
                return [pre_i+1, r]
        def merge_next(next_i):
            r = final[next_i-1]
            if r[1] < final[next_i][0]:
                return None
            elif r[1] <= final[next_i][1]:
                r[1] = final[next_i][1]
                del final[next_i]
                return None
            else:
                del final[next_i]
                return [next_i-1, r]
        if len(avails) == 0:
            return []
        final = []
        for r_list in avails:
            pre_fi = 0
            for r in r_list:
                # r = [r.start, r.end]
                ri = bisect(final[pre_fi:], r)
                # (pre_fi, ri, r).p()
                merge_result = None
                if ri == 0:
                    final.insert(ri + pre_fi, r)
                    merge_result = [ri + pre_fi, r]
                else:
                    merge_result = merge_pre(ri + pre_fi-1, r)
                    # merge_result.p()
                while merge_result and merge_result[0] + 1 < len(final):
                    pre_fi = merge_result[0]
                    merge_result = merge_next(merge_result[0] + 1)
                # final.p()
        # final.p()
        fn = len(final)
        if fn:
            return [[final[i-1][1], final[i][0]] for i in range(1,fn)]
        else:
            return []


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def employeeFreeTime(self, schedule):
        """
        :type schedule: List[List[Interval]]
        :rtype: List[Interval]
        """
        from heapq import heappop, heappush
        q = []
        busy_list = []
        for i in range(len(schedule)):
            if schedule[i]:
                v = schedule[i].pop(0)
                heappush(q, (v.start, v.end, i))
        while q:
            s, e, i = heappop(q)
            if not busy_list:
                busy_list += [s, e],
            else:
                cs, ce = busy_list[-1]
                if cs <= s <= ce:
                    busy_list[-1][-1] = max(ce, e)
                else:
                    busy_list += [s, e],
            if schedule[i]:
                v = schedule[i].pop(0)
                heappush(q, (v.start, v.end, i))
        res = []     
        for i in range(1, len(busy_list)):
            res += (busy_list[i-1][1], busy_list[i][0]),
        return res


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().employeeFreeTime([[[1,2],[5,6]],[[1,3]],[[4,10]]]).must_equal([[3, 4]])
        # Solution().employeeFreeTime([[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]).must_equal([[5, 6], [7, 9]])
        # Solution().employeeFreeTime([[[7,24]],[[6,24], [26,27]]]).must_equal([[24, 26]])
        # Solution().employeeFreeTime([[[39, 59], [61, 75], [78, 81], [94, 99]],[[57, 87]]]).must_equal([[87,94]])
        # Solution().employeeFreeTime([[[68, 71], [78, 81], [91, 99]],[[57,87]]]
        #         ).must_equal([[87,91]])
        # Solution().employeeFreeTime([[[7,24],[29,33],[45,57],[66,69],[94,99]],[[6,24],[43,49],[56,59],[61,75],[80,81]],[[5,16],[18,26],[33,36],[39,57],[65,74]],[[9,16],[27,35],[40,55],[68,71],[78,81]],[[0,25],[29,31],[40,47],[57,87],[91,94]]]
        #         ).must_equal([[26,27],[36,39],[87,91]])
        Solution().employeeFreeTime([[[45, 56], [58, 75], [77, 100]],[[47, 65]]]
                ).must_equal([[75,77]])
        Solution().employeeFreeTime([[[0,16],[29,34],[52,56],[66,75],[91,96]],[[4,36],[45,56],[58,68],[78,83],[84,100]],[[14,16],[40,41],[48,51],[66,73],[91,100]],[[5,14],[15,29],[45,49],[65,68],[77,84]],[[7,20],[25,31],[47,65],[66,74],[93,98]]]
                ).must_equal([[36,40],[41,45],[75,77]])
    