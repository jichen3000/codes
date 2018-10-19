from operator import mul

def solve(n,k):
    if n <= 2: return 1
    if k == 0: return 1
    return reduce(mul, [n-i for i in xrange(k)]) / \
            reduce(mul, [i+1 for i in xrange(k)])

def solve(n,k):
    if n <= 2: return 1
    if k == 0: return 1
    dp = [[1] * n for _ in range(n+1)]
    for i in range(n+1):
        for j in range(1,i):
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
            # (j,dp).p()
    return dp[-1][k]

def solve(n,k):
    if n <= 2: return 1
    if k == 0: return 1
    dp = [1] * n
    for i in range(2,n+1):
        for j in range(1,i):
            dp[j] += dp[j-1]
    return dp[k]


if __name__ == '__main__':
    from minitest import *

    with test(solve):
        solve(5,1).must_equal(5)
        # solve(5,2).must_equal(10)