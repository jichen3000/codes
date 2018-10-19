from collections import defaultdict
def solve(grid):
    n = len(grid)
    adjs = defaultdict(list)
    for i in range(n):
        for j in range(i+1, n):
            if grid[i][j] == 1:
                adjs[i] += j,
                adjs[j] += i,

    def cal_next_vertics(cur):
        return [i for i in adjs[cur] if i not in vertics]

    def dfs(vertics):
        cur = vertics[-1]
        if len(vertics) == n:
            return (0 in adjs[cur])
        next_vertics = cal_next_vertics(cur)
        if len(next_vertics) == 0:
            return False
        # sort if needed
        for i in next_vertics:
            vertics.append(i)
            if dfs(vertics):
                return True
            vertics.pop()
    vertics = [0]
    if dfs(vertics):
        return vertics + [0]
    else:
        return []

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        # /* Let us create the following graph
        #    (0)--(1)--(2)
        #     |   / \   |
        #     |  /   \  |
        #     | /     \ |
        #    (3)-------(4)    */
        grid = [
                [0, 1, 0, 1, 0],
                [1, 0, 1, 1, 1],
                [0, 1, 0, 0, 1],
                [1, 1, 0, 0, 1],
                [0, 1, 1, 1, 0],
        ]
        solve(grid).must_equal([0, 1, 2, 4, 3, 0])
        # /* Let us create the following graph
        # (0)--(1)--(2)
        #  |   / \   |
        #  |  /   \  |
        #  | /     \ |
        # (3)       (4)    */
        grid = [
                [0, 1, 0, 1, 0],
                [1, 0, 1, 1, 1],
                [0, 1, 0, 0, 1],
                [1, 1, 0, 0, 0],
                [0, 1, 1, 0, 0],
        ]
        solve(grid).must_equal([])
        
