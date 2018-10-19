def create_board(n):
    return [["."] * n for _ in range(n)]
def set_queen(x, y, board, n):
    board[x][y] = "Q"
    for i in range(n):
        if i != x:
            board[i][y] = "N"
    for j in range(n):
        if j != y:
            board[x][j] = "N"
    for k in range(1, min(x,y)+1):
        board[x-k][y-k] = "N"
    for k in range(1, min(n-1-x,n-1-y)+1):
        board[x+k][y+k] = "N"
    for k in range(1, min(n-1-x,y)+1):
        board[x+k][y-k] = "N"
    for k in range(1, min(x,n-1-y)+1):
        board[x-k][y+k] = "N"

class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        board = create_board(n)
        def copy_board(board):
            new_board = create_board(n)
            for i in range(n):
                for j in range(n):
                    new_board[i][j] = board[i][j]
            return new_board

        def clear_board(board):
            for i in range(n):
                for j in range(n):
                    if board[i][j] == "N":
                        board[i][j] = "."
                board[i] = "".join(board[i])



        def f(i, board, results):
            # i.p()
            for j in range(n):
                # (i,j).p()
                # board.pp()
                if board[i][j] == ".":
                    new_board = copy_board(board)
                    set_queen(i,j,new_board,n)
                    if i + 1 == n:
                        clear_board(new_board)
                        results += new_board,
                    else:
                        f(i+1, new_board, results)
        results = []
        f(0, board, results)
        return results
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        def dfs(queens, xy_difs, xy_sums):
            x1 = len(queens)
            if x1 == n:
                results.append(queens)
                return None
            for y1 in range(n):
                # y1 not in queens for not in same column
                # (x1 - y1) not in xy_difs not in 45 degree diagonal
                # (x1 + y1) not in xy_sums not in 135 degree diagonal
                if y1 not in queens and (x1 - y1) not in xy_difs and (x1 + y1) not in xy_sums:
                    dfs(queens+[y1], xy_difs+[x1 - y1], xy_sums+[x1 + y1])
        results = []
        dfs([],[],[])
        return [["."*i+"Q"+"."*(n-1-i) for i in queens] for queens in results]

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # board = create_board(6)
        # set_queen(1,0, board, 6)
        # board.pp()
        Solution().solveNQueens(4).pp()