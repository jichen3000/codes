def solve(grid, src_cell, des_cell):
    m = len(grid)
    n = len(grid[0])
    max_path_length = [1]
    dirs = [(0,1),(0,-1), (1,0),(-1,0)]
    def get_nexts(x,y,visited):
        results = []
        for dx,dy in dirs:
            nx, ny = dx + x, dy + y
            if nx >= 0 and nx < m and ny >= 0 and ny < n \
                    and not visited[nx][ny] and grid[nx][ny] == 1:
                results += (nx,ny),
        return results
    def dfs(path, visited):
        x, y = path[-1]
        if des_cell == (x, y):
            max_path_length[0] = max(max_path_length[0], len(path))
            return
        next_cells = get_nexts(x,y, visited)
        if len(next_cells) == 0:
            return
        for nx, ny in next_cells:
            path.append((nx,ny))
            visited[nx][ny] = True
            dfs(path, visited)
            path.pop()
            visited[nx][ny] = False
    visited = [ [False] * n for _ in range(m)]
    path = [src_cell]
    dfs(path, visited)
    return max_path_length[0] - 1

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        grid = [
                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
                [ 1, 1, 0, 1, 1, 0, 1, 1, 0, 1 ],
                [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
        ]
        solve(grid, (0,0), (1,7)).p()