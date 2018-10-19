class Solution:
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        if not grid or not grid[0]:
            return res
        m, n = len(grid), len(grid[0])
        for i in range(m):
            count, q = 0, []
            for j in range(n):
                if grid[i][j] == "0":
                    q += j,
                elif grid[i][j] == "E":
                    count += 1
                else:
                    for nj in q:
                        grid[i][nj] = count
                    count, q = 0, []
            for nj in q:
                grid[i][nj] = count
        for j in range(n):
            count, q = 0, []
            for i in range(m):
                if isinstance(grid[i][j], int):
                    q += i,
                elif grid[i][j] == "E":
                    count += 1
                else:
                    for ni in q:
                        grid[ni][j] +=  count
                        res = max(res, grid[ni][j])
                    count, q = 0, []
            for ni in q:
                grid[ni][j] += count
                res = max(res, grid[ni][j])
        # print(grid)
        return res
            
        