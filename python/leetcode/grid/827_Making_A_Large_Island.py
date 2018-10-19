class Solution:
    def largestIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m, n = len(grid), len(grid[0])
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        def get_nexts(i, j):
            res = set()
            for di, dj in dirs:
                ni, nj = di + i, dj + j
                if ni >= 0 and ni < m and nj >= 0 and nj < n and grid[ni][nj] == 1:
                    res.add((ni,nj))
            return res
        def get_ids(i, j):
            res = []
            for di, dj in dirs:
                ni, nj = di + i, dj + j
                if ni >= 0 and ni < m and nj >= 0 and nj < n and grid[ni][nj] < 0:
                    res += grid[ni][nj],
            return res
        def get_area(i, j, i_id):
            cur_set, area = {(i,j)}, 0
            while cur_set:
                temp_set = set()
                for ni, nj in cur_set:
                    grid[ni][nj] = i_id
                    area += 1
                    temp_set |= get_nexts(ni,nj)
                cur_set = temp_set
            return area
        
        i_id = -1
        res = 0
        area_d = {}
        zero_q = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    zero_q += (i,j),
                elif grid[i][j] == 1:
                    area = get_area(i, j, i_id)
                    res = max(res, area)
                    area_d[i_id] = area
                    i_id -= 1
        # zero_q.p()
        for i, j in zero_q:
            next_ids = get_ids(i,j)
            next_ids.sort()
            area, pre_id = 1, 0
            for id in next_ids:
                if pre_id != id:
                    area += area_d[id]
                    pre_id = id
            res = max(res, area)
        return res
        
        
if __name__ == '__main__':
    from minitest import *

    with test("Solution"):
        Solution().largestIsland([[1,1],[1,0]]).must_equal(4)
        Solution().largestIsland([[0,1],[1,0]]).must_equal(3)
        Solution().largestIsland([[1,1],[1,1]]).must_equal(4)
