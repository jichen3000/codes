def solve(prices):
    n = len(prices)
    if n == 0: return 0
    dp = [ [0] * (n+1) for _ in xrange(n+1)]
    # type
    for i in xrange(1, n+1):
        # length
        for j in xrange(1, n+1):
            if i > j:
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-i]+prices[i-1])
    # dp.pp()
    return dp[-1][-1]

def solve(prices):
    n = len(prices)
    if n == 0: return 0
    dp = [0] * (n+1)
    # type
    for i in xrange(1, n+1):
        # length
        for j in xrange(i, n+1):
            dp[j] = max(dp[j], dp[j-i]+prices[i-1])
    # dp.pp()
    return dp[-1]

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        prices = [1,5,8,9,10,17,17,20]
        solve(prices).must_equal(22)
        prices = [3,5,8,9,10,17,17,20]
        solve(prices).must_equal(24)
