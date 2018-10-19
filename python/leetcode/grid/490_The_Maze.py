class Solution:
    def hasPath(self, maze, start, end):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type end: List[int]
        :rtype: bool
        """
        if not maze or not maze[0]:
            return False
        m, n = len(maze), len(maze[0])
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]
        visited = set()
        def dfs(x0, y0):
            # (x0, y0, end == (x0, y0)).p()
            if end[0] == x0 and end[1] == y0: return True
            visited.add((x0,y0))
            for dx, dy in dirs:
                x, y = x0, y0
                while x + dx >= 0 and x + dx < m and \
                        y + dy >= 0 and y + dy < n and maze[x+dx][y+dy] == 0:
                    x += dx
                    y += dy
                if (x, y) not in visited:
                    if dfs(x, y): return True
            return False
        return dfs(*start)



if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
            [0,4],
            [4,4]).must_equal(True)
        Solution().hasPath([[0,0,1,0,0],[0,0,0,0,0],[0,0,0,1,0],[1,1,0,1,1],[0,0,0,0,0]],
            [0,4],
            [3,2]).must_equal(False)
