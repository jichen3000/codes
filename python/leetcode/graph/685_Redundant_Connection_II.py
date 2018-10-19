class Solution(object):

    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        parents = {}
        first, second = None, None
        for parent, child in edges:
            # (parent, child, parents).p()
            if child not in parents:
                parents[child] = parent
            else:
                first, second = [parents[child], child],[parent, child]
        # (first, second).p()

        def union_find(edges):
            parents = {}
            def find_first_parent(vertex):
                if vertex not in parents:
                    return vertex
                return find_first_parent(parents[vertex])
            def union(parent, child):
                parents[child] = parent

            for parent, child in edges:
                # (parent, child).p()
                parent_parent = find_first_parent(parent)
                child_parent = find_first_parent(child)
                if parent_parent == child_parent:
                    return [parent, child]
                union(parent_parent, child_parent)
                # (parent_parent, child_parent, parents).p()
            return None
        def remove_ok(edge):
            # edge.p()
            # union_find([e for e in edges if tuple(e)!=tuple(edge)]).p()
            return union_find([e for e in edges if tuple(e)!=tuple(edge)]) == None
            # pass

        if first:
            if remove_ok(first):
                if remove_ok(second):
                    return second
                else:
                    return first
            else: 
                return second
        else:
            return union_find(edges)

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        edges = [[1,2], [1,3], [2,3]]
        Solution().findRedundantDirectedConnection(edges).must_equal([2,3])
        edges = [[1,2], [2,3], [3,4], [4,1], [1,5]]
        Solution().findRedundantDirectedConnection(edges).must_equal([4,1])
        edges = [[2,1],[3,1],[4,2],[1,4]]
        Solution().findRedundantDirectedConnection(edges).must_equal([2,1])
        edges = [[1,2],[2,3],[3,4],[4,1],[1,5]]
        Solution().findRedundantDirectedConnection(edges).must_equal([4,1])
        edges = [[4,2],[1,5],[5,2],[5,3],[2,4]]
        Solution().findRedundantDirectedConnection(edges).must_equal([4,2])
        edges = [[4,1],[1,5],[4,2],[5,1],[4,3]]
        Solution().findRedundantDirectedConnection(edges).must_equal([5,1])

