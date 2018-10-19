class Solution:
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
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
    
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        mem = {}
        def union(s, t):
            mem[s] = t
        
        def find(s):
            while s in mem:
                s = mem[s]
            return s
        for s, t in edges:
            parent_s = find(s)
            parent_t = find(t)
            if parent_s == parent_t:
                return False
            union(parent_s, parent_t)
        return self.countComponents(n, edges) == 1
        
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        using union find(if using rank, every find or union would be logn)
        but I didn't use rank, so just n
        time: O(n*n + E * n)
        space: O(n) 
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
            parent_s = find(s)
            parent_t = find(t)
            if parent_s == parent_t:
                return False
            union(parent_s, parent_t)
        components = set()
        for v in range(n):
            components.add(find(v))
            
        return len(components) == 1
                