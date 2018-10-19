# http://www.geeksforgeeks.org/dynamic-programming-set-16-floyd-warshall-algorithm/
## 40mins
def solve(grid):
    n = len(grid)
    if n == 0: return None
    if n == 1: return 1
    # dp = [ [0] * n for _ in n]
    dp = [grid[i][:] for i in range(n)]
    for i in xrange(n):
        for j in xrange(n):
            if i != j:
                dp[i][j] = min(dp[i][k]+dp[k][j] for k in xrange(n))
    return dp[0][-1]

if __name__ == '__main__':
    from minitest import *
    INF = float("inf")
    with test(solve):
        graph = [[0,5,INF,10],
             [INF,0,3,INF],
             [INF, INF, 0,   1],
             [INF, INF, INF, 0]
        ]
        solve(graph).p()


