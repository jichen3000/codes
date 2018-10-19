class Solution:
    ## TLE
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        if not graph: return False
        def dfs(i, set1, set2):
            # (i, set1, set2).p()
            if i == len(graph): return True
            n1, n2 = {i}, set(graph[i])
            if (len(n1.intersection(set1)) >0 and len(n1.intersection(set2)) > 0) or \
                    (len(n2.intersection(set1)) >0 and len(n2.intersection(set2)) > 0):
                return False
            return dfs(i+1, set1 | n1, set2 | n2) or dfs(i+1, set1 | n2, set2 | n1)
        return dfs(1, {0}, set(graph[0]))
    # time: O(v+e)
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        if not graph: return False
        n = len(graph)
        colors = [None] * n
        for k in range(n):
            if colors[k] == None:
                q = [(k,0)]
            while q:
                i, color = q.pop(0)
                if colors[i] == None:
                    colors[i] = color
                else:
                    if colors[i] != color:
                        return False
                    continue
                for j in graph[i]:
                    q += (j, 1-color),
        return True

        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().isBipartite([[3],[2,4],[1],[0,4],[1,3]]).must_equal(True)
        Solution().isBipartite([[],[2,4,6],[1,4,8,9],[7,8],[1,2,8,9],[6,9],[1,5,7,8,9],[3,6,9],[2,3,4,6,9],[2,4,5,6,7,8]]).must_equal(False)
