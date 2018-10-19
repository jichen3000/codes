# http://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/
def solve(maze):
    n = len(maze)
    dirs = [(0,1),(1,0)]
    def next_moves(i,j):
        results = []
        for di, dj in dirs:
            ni, nj = i + di, j + dj
            if ni >= 0 and ni < n and nj >= 0 and nj < n and maze[ni][nj]==1:
                results += (ni,nj),
        return results
    def dfs(moves):
        i, j= moves[-1]
        if i == n-1 and j == n-1:
            return moves
        for ni, nj in next_moves(i,j):
            result = dfs(moves+[(ni,nj)])
            if result: return result
    return dfs([(0,0)])


if __name__ == '__main__':
    from minitest import *

    with test(solve):
        maze = [
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]
        ]
        solve(maze).pp()