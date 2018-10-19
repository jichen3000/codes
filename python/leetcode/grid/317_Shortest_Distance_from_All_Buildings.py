class Solution:
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        count, res = 0, float("inf")
        if not grid or not grid[0]:
            return -1
        m, n = len(grid), len(grid[0])
        point = None
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
                    point = (i,j)
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        def get_nexts(i, j, visited):
            res = set()
            for di, dj in dirs:
                ni, nj = di+i, dj+j
                if ni >= 0 and ni < m and nj >= 0 and nj < n and \
                        (ni,nj) not in visited and grid[ni][nj]!=2:
                    res.add((ni, nj))
            return res
        def bfs(i, j):
            visited = set()
            res, dist, cc = 0, 0, 0
            cur_set = {(i,j)}
            while cur_set:
                temp_set = set()
                for ci, cj in cur_set:
                    visited.add((ci, cj))
                    if grid[ci][cj] == 1:
                        res += dist
                        cc += 1
                    else:
                        temp_set |= get_nexts(ci, cj, visited)
                cur_set = temp_set
                dist += 1
            return res, cc
        if count == 1:
            if get_nexts(*point, set()):
                return 1
            else:
                return -1
        else:
            grid[point[0]][point[1]] = 0
            cres, cc = bfs(*point)
            if cc != count-1:
                return -1
            grid[point[0]][point[1]] = 1

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    cres, cc = bfs(i, j)
                    if cc == count:
                        res = min(res, cres)
        if res == float("inf"):
            return -1
        return res


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().shortestDistance([[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]).must_equal(7)
        Solution().shortestDistance([[1,2,0]]).must_equal(-1)
        Solution().shortestDistance([[1,0,0]]).must_equal(1)
        Solution().shortestDistance([[1,1],[0,1]]).must_equal(-1)
        Solution().shortestDistance([
                [1,1,1,1,1,0],
                [0,0,0,0,0,1],
                [0,1,1,0,0,1],
                [1,0,0,1,0,1],
                [1,0,1,0,0,1],
                [1,0,0,0,0,1],
                [0,1,1,1,1,0]]).must_equal(88)
