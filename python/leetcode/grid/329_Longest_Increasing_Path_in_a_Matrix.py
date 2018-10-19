from Queue import PriorityQueue
class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        queue = PriorityQueue()
        res = 0
        mem = [[0] * n for _ in range(m)]
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        def next_smalles(i,j):
            results = [0]
            for di, dj in dirs:
                ni, nj = di + i, dj + j
                if ni >= 0 and ni < m and nj >= 0 and nj < n and matrix[i][j] > matrix[ni][nj]:
                    results += mem[ni][nj],
            return results
        for i in range(m):
            for j in range(n):
                queue.put((matrix[i][j],i,j))
        while not queue.empty():
            v, i, j = queue.get()
            mem[i][j] = max(next_smalles(i,j)) + 1
            res = max(res, mem[i][j])
        return res
    

                
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        res = [0]
        dp = [[0] * n for _ in range(m)]
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        def dfs(i,j):
            if dp[i][j] == 0:
                counts = [0]
                for di, dj in dirs:
                    ni, nj = di + i, dj + j
                    if ni >= 0 and ni < m and nj >= 0 and nj < n and matrix[i][j] > matrix[ni][nj]:
                        counts += dfs(ni,nj),
                dp[i][j] = max(counts)+1
                res[0] = max(res[0], dp[i][j])
            return dp[i][j]
        for i in range(m):
            for j in range(n):
                dfs(i,j)
        return res[0]

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        matrix = [
            (7,8,9),
            (9,7,6),
            (7,2,3),
        ]
        Solution().longestIncreasingPath(matrix).must_equal(6)