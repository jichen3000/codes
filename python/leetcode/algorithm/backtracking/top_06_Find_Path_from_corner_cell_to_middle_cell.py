# http://www.geeksforgeeks.org/find-paths-from-corner-cell-to-middle-cell-in-maze/
def solve(grid):
    n = len(grid)
    mid_point = (n/2, n/2)
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def cal_next_points(point):
        results = []
        i, j = point
        v = grid[i][j]
        for di, dj in dirs:
            ni, nj = di*v + i, dj*v + j
            if ni>=0 and ni < n and nj >= 0 and nj < n and (ni, nj) not in points:
                results += (ni, nj),
        return results
    def cmp_by_least(point):
        return len(cal_next_points(point))

    def dfs(points):
        next_points = cal_next_points(points[-1])
        if len(next_points) == 0:
            return False
        if mid_point in next_points:
            points += mid_point,
            return True
        next_points.sort(key=cmp_by_least)
        for point in next_points:
            points += point,
            if dfs(points):
                return True
            points.pop()
    points = [(0,0)]
    dfs(points)
    return points

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        grid = [
                [ 3, 5, 4, 4, 7, 3, 4, 6, 3 ],
                [ 6, 7, 5, 6, 6, 2, 6, 6, 2 ],
                [ 3, 3, 4, 3, 2, 5, 4, 7, 2 ],
                [ 6, 5, 5, 1, 2, 3, 6, 5, 6 ],
                [ 3, 3, 4, 3, 0, 1, 4, 3, 4 ],
                [ 3, 5, 4, 3, 2, 2, 3, 3, 5 ],
                [ 3, 5, 4, 3, 2, 6, 4, 4, 3 ],
                [ 3, 5, 1, 3, 7, 5, 3, 6, 4 ],
                [ 6, 2, 4, 3, 4, 5, 4, 5, 1 ],
        ]
        solve(grid).pp()