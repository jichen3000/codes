class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        dirs = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
        def get_live_count(i,j):
            res = 0
            for di, dj in dirs:
                ni, nj = di + i, dj + j
                if ni>=0 and ni < m and nj >= 0 and nj < n and board[ni][nj] == 1:
                    res += 1
            return res
        m = len(board)
        if m == 0: return
        n = len(board[0])
        queue = []
        for i in range(m):
            for j in range(n):
                count = get_live_count(i,j)
                # print board[i][j], count
                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        queue += (i,j,0),
                else:
                    if count == 3:
                        queue += (i,j,1),
        # print queue
        for i, j, v in queue:
            board[i][j] = v
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        dirs = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
        def get_live_count(i,j):
            res = 0
            for di, dj in dirs:
                ni, nj = di + i, dj + j
                if ni>=0 and ni < m and nj >= 0 and nj < n and board[ni][nj] in [1,2]:
                    res += 1
            return res
        m = len(board)
        if m == 0: return
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                count = get_live_count(i,j)
                # print board[i][j], count
                if board[i][j] == 1:
                    if count < 2 or count > 3:
                        board[i][j] = 2
                else:
                    if count == 3:
                        board[i][j] = 3
        # print queue
        for i in range(m):
            for j in range(n):
                board[i][j] = board[i][j] % 2