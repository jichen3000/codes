# min wall moves
from Queue import PriorityQueue
class Solution(object):
    def trapRainWater(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        m = len(board)
        if m == 0: return 0
        n = len(board[0])
        queue = PriorityQueue()
        visited = [[False] * n for _ in range(m)]
        for i in range(m):
            visited[i][0] = True
            queue.put((board[i][0], i, 0))
            visited[i][n-1] = True
            queue.put((board[i][n-1], i, n-1))
        for j in range(n):
            visited[0][j] = True
            queue.put((board[0][j], 0, j))
            visited[m-1][j] = True
            queue.put((board[m-1][j], m-1, j))
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        res = 0
        while not queue.empty():
            h, i, j = queue.get()
            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if ni >= 0 and ni < m and nj >= 0 and nj < n and not visited[ni][nj]:
                    visited[ni][nj] = True
                    res += max(0, h - board[ni][nj])
                    queue.put((max(h, board[ni][nj]), ni, nj))
        return res
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        board = [
                [1,4,3,1,3,2],
                [3,2,1,3,2,4],
                [2,3,3,2,3,1]
                ]
        Solution().trapRainWater(board).must_equal(4)