from Queue import PriorityQueue
import heapq
class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        days = 0
        selected = PriorityQueue()
        max_cost = 0
        for cost, end in sorted(courses, key = lambda x:x[1]):
            if days + cost <= end:
                days += cost
                selected.put(-cost)
            else:
                pre_max_cost = 0-selected.get()
                if pre_max_cost > cost:
                    selected.put(-cost)
                    days -= pre_max_cost - cost
                else:
                    selected.put(-pre_max_cost)
        return selected.qsize()
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        days = 0
        selected = []
        for cost, end in sorted(courses, key = lambda x:x[1]):
            if days + cost <= end:
                days += cost
                heapq.heappush(selected, -cost)
            else:
                pre_max_cost = 0-heapq.heappop(selected)
                if pre_max_cost > cost:
                    heapq.heappush(selected, -cost)
                    days -= pre_max_cost - cost
                else:
                    heapq.heappush(selected, -pre_max_cost)
        return len(selected)
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        courses = [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
        Solution().scheduleCourse(courses).must_equal(3)
        courses = [[5,5],[4,6],[2,6]]
        Solution().scheduleCourse(courses).must_equal(2)
