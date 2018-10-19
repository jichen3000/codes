# http://www.geeksforgeeks.org/top-20-backtracking-algorithm-interview-questions/
def solve(board):
    m = len(board)
    n = len(board[0])
    shortest_len = [m * n]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(m):
        for j in range(n):
            if board[i][j] == 0:
                for di, dj in dirs:
                    ni, nj = di + i, dj + j
                    if ni >= 0 and ni < m and nj >= 0 and nj < n and board[ni][nj] != 0:
                        board[ni][nj] = 2
    def get_nexts(i, j, visited):
        results = []
        for di, dj in dirs:
            ni, nj = di + i, dj + j
            if ni >= 0 and ni < m and nj >= 0 and nj < n \
                    and board[ni][nj] == 1 and not visited[ni][nj]:
                results += (ni, nj),
        return results

                        
    def dfs(path, visited):
        x,y  = path[-1]
        if y == n-1:
            shortest_len[0] = min(len(path), shortest_len[0])
            return True
        next_cells = get_nexts(x, y, visited)
        if len(next_cells) == 0:
            return False
        for nx, ny in next_cells:
            path += (nx,ny),
            visited[nx][ny] = True 
            dfs(path, visited)
            path.pop()
            visited[nx][ny] = False 


    j = 0
    visited = [[False] * n for _ in range(m)]
    for i in range(m):
        if board[i][j] == 1:            
            path = [(i,j)]
            visited[i][j] = True
            dfs(path, visited)
            for x,y in path:
                visited[x][y] = False
    # the first one is not in count
    return shortest_len[0] - 1

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        board = [
                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                [ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 ],
                [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ],
                [ 1, 1, 1, 1, 0, 1, 1, 1, 1, 1 ],
                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                [ 1, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
                [ 1, 0, 1, 1, 1, 1, 1, 1, 0, 1 ],
                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                [ 0, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ],
        ]
        solve(board).must_equal(13)