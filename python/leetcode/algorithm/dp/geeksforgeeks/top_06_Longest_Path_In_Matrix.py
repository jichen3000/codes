def solve(grid):
    n = len(grid)
    if n == 0: return 0
    if n == 1: return 1
    longest = 1
    dp = [ [1] * n for _ in xrange(n)]
    for i in xrange(n):
        for j in xrange(n):
            if i - 1 >= 0 and abs(grid[i][j]-grid[i-1][j]) == 1:
                dp[i][j] += dp[i-1][j]
            if j - 1 >= 0 and abs(grid[i][j]-grid[i][j-1]) == 1:
                dp[i][j] += dp[i][j-1]
            longest = max(longest, dp[i][j])
    return longest

def solve(grid):
    n = len(grid)
    if n == 0: return 0
    if n == 1: return 1
    dp = [1] * n
    for i in xrange(n):
        for j in xrange(n):
            pre, dp[j] = dp[j], 1
            if i - 1 >= 0 and abs(grid[i][j]-grid[i-1][j]) == 1:
                dp[j] += pre
            if j - 1 >= 0 and abs(grid[i][j]-grid[i][j-1]) == 1:
                dp[j] += dp[j-1]
    return max(dp)

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        grid = [[1, 2, 9],
                   [5, 3, 8],
                   [4, 6, 7]]
        solve(grid).must_equal(4)