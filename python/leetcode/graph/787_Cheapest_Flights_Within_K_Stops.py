class Solution(object):
    ## TLE
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        from collections import defaultdict
        # flights.sort()
        # flights.p()
        dst_dict = defaultdict(list)
        n = len(flights)
        for s, d, p in flights:
            dst_dict[s] += (d, p),
        visited = set()
        # res = [float('inf')]
        # mem = {}
        def dfs(src, stop_n, cur_p):
            # (src, stop_n, cur_p).p()
            # if (src,stop_n) in mem: return mem[(src,stop_n)]
            if stop_n > k: return float('inf')
            res_list = []
            for d, p in dst_dict[src]:
                if d in visited:
                    continue
                visited.add(d)
                np = cur_p + p
                if d == dst:
                    res_list += np,
                else:
                    res_list += dfs(d, stop_n+1, np),
                visited.discard(d)
            res = min(res_list) if res_list else float('inf')
            # if (src,stop_n) in mem:
            #     res = min(mem[(src,stop_n)], res)            
            # mem[(src,stop_n)] = res
            return res
        visited.add(src)  
        res = dfs(src, 0, 0)
        if res == float('inf'): return -1
        return res

class Solution(object):
    # https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
    def findCheapestPrice(self, n, flights, src, dst, k):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        from collections import defaultdict
        from heapq import heappop, heappush
        dst_dict = defaultdict(set)
        visited = set()
        for s, d, p in flights:
            dst_dict[s].add((d,p))
        q = []
        heappush(q,(0, src, k+1))
        visited.add(src)
        while q:
            sum_p, s, count = heappop(q)
            visited.add(s)
            if s == dst: return sum_p
            if count > 0:
                for d, p in dst_dict[s]:
                    if d not in visited:
                        heappush(q, (sum_p+p, d, count-1))
        return -1






if __name__ == '__main__':
    from minitest import *

    with test("Solution"):
        Solution().findCheapestPrice(3,
                [[0,1,100],[1,2,100],[0,2,500]],
                0,2,1).must_equal(200)
        Solution().findCheapestPrice(3,
                [[0,1,100],[1,2,100],[0,2,500]],
                0,2,0).must_equal(500)
        Solution().findCheapestPrice(5,
                [[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]],
                2,1,1).must_equal(-1)
        Solution().findCheapestPrice(10,
                [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]],
                6,0,7).must_equal(14)
