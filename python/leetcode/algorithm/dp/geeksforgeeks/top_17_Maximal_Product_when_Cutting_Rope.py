def solve(n):
    if n == 2: return 1
    if n == 3: return 2
    dp = [0] * (n+1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    for i in xrange(4,n+1):
        dp[i] = max(dp[i-k]*k for k in xrange(2,i-1))

    return dp[-1]

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        solve(10).must_equal(36)
        solve(11).must_equal(54)