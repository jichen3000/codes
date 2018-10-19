from collections import defaultdict
from heapq import heappop, heappush
class Solution(object):
    def networkDelayTime(self, times, n, start):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        mem = defaultdict(list)
        for s, t, w in times:
            mem[s] += (t, w),
        # mem.p()
        min_heap = []
        heappush(min_heap, (0, start))
        no_visited = set(i+1 for i in range(n))
        max_w = 0
        while min_heap:
            w, s = heappop(min_heap)
            if s not in no_visited:
                continue
            # (w,s).p()
            max_w = w
            no_visited.discard(s)
            for nt, nw in mem[s]:
                if nt in no_visited:
                    heappush(min_heap, (nw+w, nt))
        # no_visited.p()
        if len(no_visited) == 0:
            return max_w
        return -1
        
        
if __name__ == '__main__':
    from minitest import *


    with test(Solution):
        # Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2).must_equal(2)
        # Solution().networkDelayTime([[1,2,1],[2,1,3]], 2, 2).must_equal(3)
        # Solution().networkDelayTime([[1,2,1],[2,3,7],[1,3,4],[2,1,2]], 4, 1).must_equal(-1)
        Solution().networkDelayTime([[1,2,1],[2,3,2],[1,3,2]], 3, 1).must_equal(2)
