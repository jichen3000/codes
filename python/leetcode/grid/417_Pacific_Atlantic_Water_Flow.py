class Solution(object):
    def pacificAtlantic_work(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        def get_flow_adjs(i,j):
            adjs = []
            for x,y in directions:
                ni,nj = i+x,j+y
                if ni >= 0 and ni < m and nj >= 0 and nj < n and matrix[ni][nj] <= matrix[i][j]:
                    adjs += (ni,nj),
            # if i-1>=0 and matrix[i-1][j] <= v:
            #     adjs += (i-1,j),
            # if i+1< m and matrix[i+1][j] <= v:
            #     adjs += (i+1,j),
            # if j-1>=0 and matrix[i][j-1] <= v:
            #     adjs += (i,j-1),
            # if j+1< n and matrix[i][j+1] <= v:
            #     adjs += (i,j+1),
            return adjs

        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        acc = []
        cache = {}
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 or j == 0:
                    cache[(i,j)] = (True,None)
                elif i == m - 1 or j == n - 1:
                    cache[(i,j)] = (None,True)
                else:
                    cache[(i,j)] = (None,None)
                if m == 1 or n == 1:
                    cache[(i,j)] = (True,True)
                else:
                    if (i,j) == (0,n-1) or (i,j) == (m-1,0):
                        cache[(i,j)] = (True,True)
                    else:
                        acc += (i,j),
        while True:
            new_acc = []
            old_size = len(acc)
            changed = False
            while len(acc) > 0:
                i,j = acc.pop()
                cur_p, cur_a = cache[(i,j)]
                adjs = get_flow_adjs(i,j)
                # (i,j,cur_a,cur_p,adjs).p()
                if len(adjs) == 0:
                    if cur_a == None: cur_a = False
                    if cur_p == None: cur_p = False
                else:
                    for ai,aj in adjs:
                        adj_p,adj_a = cache[(ai,aj)]
                        if adj_a: cur_a = True
                        if adj_p: cur_p = True
                if cur_a == None or cur_p == None:
                    new_acc += (i,j),
                if (cur_p,cur_a) != cache[(i,j)]:
                    cache[(i,j)] = (cur_p,cur_a)
                    changed = True
            # if old_size == len(new_acc):
            if not changed:
                break
            acc = new_acc
            # new_acc.p()
        results = []
        for i in xrange(m):
            for j in xrange(n):
                if cache[(i,j)] == (True,True):
                    results += [i,j],
        return results
    
    #bfs
    def pacificAtlantic_bfs(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def bfs(the_queue, the_linked):
            while len(the_queue) > 0:
                i,j = the_queue.pop(0)
                # (i,j).p()
                for x,y in directions:
                    ni, nj = i+x, j+y
                    # (i,j,ni,nj).p()
                    if ni >= 0 and ni < m and nj >= 0 and nj < n and \
                            the_linked[ni][nj]==False and matrix[ni][nj] >= matrix[i][j]:
                        the_queue += (ni,nj),
                        the_linked[ni][nj] = True
                        # (i,j,ni,nj,True).p()

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        results = []
        p_linked = [[False for j in xrange(n)] for i in xrange(m)]
        a_linked = [[False for j in xrange(n)] for i in xrange(m)]
        p_queue = []
        a_queue = []
        # Vertical border
        for i in xrange(m):
            p_queue += (i,0),
            a_queue += (i, n-1),
            p_linked[i][0] = True
            a_linked[i][n-1] = True
        # Horizontal border
        for j in xrange(n):
            p_queue += (0,j),
            a_queue += (m-1,j),
            p_linked[0][j] = True
            a_linked[m-1][j] = True
        bfs(p_queue, p_linked)
        bfs(a_queue, a_linked)
        for i in xrange(m):
            for j in xrange(n):
                if p_linked[i][j] and a_linked[i][j]:
                    results += [i,j],
        return results

    #dfs
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        def dfs(the_linked, height, i, j):
            (i,j).p()
            if i >= 0 and i < m and j >= 0 and j < n and \
                    the_linked[i][j]==False and matrix[i][j] >= height:
                the_linked[i][j] = True
                for x,y in directions:
                    ni, nj = i+x, j+y
                    dfs(the_linked, matrix[i][j], ni, nj)

        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        results = []
        p_linked = [[False for j in xrange(n)] for i in xrange(m)]
        a_linked = [[False for j in xrange(n)] for i in xrange(m)]

        for i in xrange(m):
            dfs(p_linked, -1, i, 0)
            dfs(a_linked, -1, i, n-1)
        for j in xrange(n):
            dfs(p_linked, -1, 0, j)
            dfs(a_linked, -1, m-1, j)
        for i in xrange(m):
            for j in xrange(n):
                if p_linked[i][j] and a_linked[i][j]:
                    results += [i,j],
        return results



if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        a = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        Solution().pacificAtlantic(a).must_equal(
                [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]])  
        a = [[13],[4],[19],[10],[1],[11],[5],[17],[3],[10],[1],[0],[1],[4],[1],[3],[6],[13],[2],[16],[7],[6],[3],[1],[9],[9],[13],[10],[9],[10],[6],[2],[11],[17],[13],[0],[19],[7],[13],[3],[9],[2]]  
        Solution().pacificAtlantic(a).must_equal(
                [[0,0],[1,0],[2,0],[3,0],[4,0],[5,0],[6,0],[7,0],[8,0],[9,0],[10,0],[11,0],[12,0],[13,0],[14,0],[15,0],[16,0],[17,0],[18,0],[19,0],[20,0],[21,0],[22,0],[23,0],[24,0],[25,0],[26,0],[27,0],[28,0],[29,0],[30,0],[31,0],[32,0],[33,0],[34,0],[35,0],[36,0],[37,0],[38,0],[39,0],[40,0],[41,0]])
