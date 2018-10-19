# http://www.geeksforgeeks.org/backtracking-set-1-the-knights-tour-problem/
def solve(n):
    board = [[-1] * n for _ in range(n)]
    dirs = [(-1,-2),(-1,2),(1,-2),(1,2),(-2,-1),(-2,1),(2,-1),(2,1)]
    def next_moves(i,j,board):
        points = []
        for di, dj in dirs:
            ni, nj = di+i, dj+j
            if ni >= 0 and ni< n and nj >= 0 and nj<n and board[ni][nj]==-1:
                points += (ni, nj),
        return points


    def dfs(board, i, j, index):
        # moves.p()
        if index == n*n:
            # moves.pp()
            # results.append(moves)
            return board

        # these two steps are the key for this algorithm
        # calculate the degree of next move acording which one has minimul choice.
        # and will let this alrotithm become almost linear time.
        wegithed_moves = [(len(next_moves(ni,nj,board)), ni, nj) for ni, nj in next_moves(i,j, board)]
        wegithed_moves.sort()
        for _, ni,nj in wegithed_moves:
            board[ni][nj] = index
            result = dfs(board, ni, nj, index+1)
            if result:
                return result
            else:
                board[ni][nj] = -1
    return dfs(board,0,0, 0)

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        solve(8).pp()