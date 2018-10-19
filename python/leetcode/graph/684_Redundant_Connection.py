from collections import defaultdict

class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        union = {}
        for edge in edges:
            parent, cur = edge
            if parent not in union:
                union[parent] = parent
            if cur not in union:
                union[cur] = cur
            if union[parent] == union[cur]:
                return edge
            else:
                parent_value = union[parent]
                for k in union.keys():
                    if union[k] == parent_value:
                        union[k] = union[cur]
    # # for python3, very good
    # def findRedundantConnection(self, edges):
    #     tree = ''.join(map(chr, range(2001)))
    #     for u, v in edges:
    #         if tree[u] == tree[v]:
    #             return [u, v]
    #         tree = tree.replace(tree[u], tree[v])   

   
    # http://www.geeksforgeeks.org/union-find/
    def findRedundantConnection(self, edges):
         
        # Allocate memory for creating V subsets and
        # Initialize all subsets as single element sets
        # parent = [-1]*(2001)
        parents = defaultdict(lambda: -1)
        def union(src, dst):
            parents[src] = dst
        def find_first_parent(vertex):
            if parents[vertex] == -1:
                return vertex
            if parents[vertex]!= -1:
                parents[vertex] = find_first_parent(parents[vertex])
                return parents[vertex]
        # Iterate through all edges of graph, find subset of both
        # vertices of every edge, if both subsets are same, then
        # there is cycle in graph.
        for src, dst in edges:
            src_parent = find_first_parent(src)
            dst_parent = find_first_parent(dst) 
            # (dst,src,dst_parent,src_parent).p()
            if dst_parent == src_parent:
                return [src, dst]
            # can exchange the src_parent, dst_parent
            union(src_parent, dst_parent)
            # parents.p()

    # changed from the above one,
    def findRedundantConnection(self, edges):
         
        # Allocate memory for creating V subsets and
        # Initialize all subsets as single element sets
        # parent = [-1]*(2001)
        parents = {}
        def union_find(vertex):
            if vertex not in parents:
                return vertex
            else:
                # create the short cut
                parents[vertex] = union_find(parents[vertex])
                return parents[vertex]
        # Iterate through all edges of graph, find subset of both
        # vertices of every edge, if both subsets are same, then
        # there is cycle in graph.
        for src, dst in edges:
            src_parent = union_find(src)
            dst_parent = union_find(dst) 
            # (dst,src,dst_parent,src_parent).p()
            if dst_parent == src_parent:
                return [src, dst]
            # can exchange the src_parent, dst_parent
            parents[src_parent] = dst_parent            
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().findRedundantConnection([[1,2],[1,3]]).must_equal(None)
        Solution().findRedundantConnection([[1,2],[1,3],[2,3]]).must_equal([2,3])
        Solution().findRedundantConnection([[0,1],[1,2],[2,0]]).must_equal([2,0])
        pass