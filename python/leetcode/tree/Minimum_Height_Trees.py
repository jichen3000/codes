class Solution(object):
    
    def findMinHeightTrees_timelimited(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        heights = []
        for i in xrange(n):
            acc = [(0,i)]
            handled = []
            height = 1
            while len(acc) > 0:
                cur_level, cur_node = acc.pop()
                print("cur_level, cur_node,handled",cur_level, cur_node,handled)
                for edge_i in xrange(len(edges)):
                    if edge_i not in handled:
                        first, second = edges[edge_i]
                        print("first, second",first, second)
                        if first == cur_node:
                            acc.append((cur_level+1, second))
                            handled.append(edge_i)
                            height = max(height, cur_level+1)
                        elif second == cur_node:
                            acc.append((cur_level+1, first))
                            handled.append(edge_i)
                            height = max(height, cur_level+1)
            heights.append(height)
            print("heights",heights)
        max_height = max(heights)
        result = []
        for i,v in enumerate(heights):
            if v == (max_height+1)/2:
                result.append(i)
        return result
            
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]

        cur the leaves one layer by one layer
        """
        if n == 1:
            return [0]
        adj_list = [[] for _ in xrange(n)]
        for i,j in edges:
            adj_list[i].append(j)
            adj_list[j].append(i)
        leaves = [i for i in xrange(n) if len(adj_list[i])==1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for leave in leaves:
                cur_adj = adj_list[leave].pop()
                adj_list[cur_adj].remove(leave)
                if len(adj_list[cur_adj]) == 1: new_leaves.append(cur_adj)
            leaves = new_leaves
        return leaves




            
            
            
if __name__ == '__main__':
    from minitest import *
    # import numpy
    # inject(numpy.allclose, 'must_close')


    with test(Solution):
        Solution().findMinHeightTrees(
            3,[[0,1],[1,2]]).must_equal(
            [1])        
        Solution().findMinHeightTrees(
            4,[[1,0],[1,2],[1,3]]).must_equal(
            [1])        
        # Solution().findMinHeightTrees_timelimited(
        #     6,[[3,0],[3,1],[3,2],[3,4],[5,4]]).must_equal(
        #     [3,4])
        n = 126
        # edges = [[0,1],[1,2],[1,3],[0,4],[3,5],[3,6],[3,7],[0,8],[0,9],[0,10],[1,11],[0,12],[6,13],[7,14],[3,15],[2,16],[0,17],[8,18],[10,19],[0,20],[16,21],[18,22],[3,23],[19,24],[7,25],[2,26],[13,27],[3,28],[25,29],[20,30],[5,31],[7,32],[32,33],[29,34],[3,35],[22,36],[21,37],[37,38],[3,39],[31,40],[34,41],[21,42],[40,43],[3,44],[7,45],[25,46],[4,47],[41,48],[17,49],[27,50],[28,51],[17,52],[36,53],[3,54],[37,55],[37,56],[4,57],[10,58],[12,59],[33,60],[33,61],[23,62],[3,63],[13,64],[29,65],[2,66],[31,67],[25,68],[16,69],[4,70],[67,71],[36,72],[54,73],[18,74],[31,75],[75,76],[59,77],[33,78],[2,79],[45,80],[53,81],[8,82],[63,83],[40,84],[44,85],[36,86],[33,87],[83,88],[83,89],[49,90],[16,91],[75,92],[32,93],[19,94],[22,95],[58,96],[72,97],[14,98],[17,99],[12,100],[77,101],[54,102],[21,103],[103,104],[79,105],[53,106],[77,107],[75,108],[22,109],[80,110],[92,111],[76,112],[64,113],[16,114],[10,115],[89,116],[93,117],[13,118],[113,119],[9,120],[30,121],[17,122],[86,123],[39,124],[104,125]]
        # Solution().findMinHeightTrees(n, edges)