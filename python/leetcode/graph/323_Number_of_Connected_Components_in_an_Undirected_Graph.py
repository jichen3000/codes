class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int

        using bfs
        time: O(V+E)
        space: O(VE)
        """
        from collections import defaultdict
        graph = defaultdict(set)
        for s, t in edges:
            graph[s].add(t)
            graph[t].add(s)
        visited = [False] * n
        count = 0
        def bfs(vertex):
            cur_set = graph[vertex]
            while cur_set:
                temp = set()
                for v in cur_set:
                    if not visited[v]:
                        visited[v] = True
                        temp |= graph[v]
                cur_set = temp
                
            
        for v in range(n):
            if not visited[v]:
                visited[v] = True
                count += 1
                bfs(v)
        return count
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        
        using union find
        time: O(V*E + E**2)
        space: O(V)
        """
        mem = {}
        def union(s, t):
            mem[s] = t
        def find(s):
            old_s = s
            while s in mem:
                s = mem[s]
            if old_s != s:
                mem[old_s] = s
            return s
        for s, t in edges:
            ps = find(s)
            pt = find(t)
            if ps != pt:
                union(ps, pt)
        parents = set()
        for v in range(n):
            pv = find(v)
            parents.add(pv)
        return len(parents)

if __name__ == '__main__':
    from minitest import *

    with test(""):
        Solution().countComponents(5, [[0,1],[1,2],[3,4]]).must_equal(2)