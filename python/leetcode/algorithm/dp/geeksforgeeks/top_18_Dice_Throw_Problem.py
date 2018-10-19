def solve(n,m,x):
    dp = [[0] * (n+1) for i in xrange(x+1)]
    for i in xrange(1,x+1):
        for j in xrange(1,n+1):
            if j == 1:
                if i <= m:
                    dp[i][j] = 1
                else:
                    dp[i][j] = 0
            elif j > i: 
                dp[i][j] = 0
            elif j == i: 
                dp[i][j] = 1
            else:
                dp[i][j] = sum(dp[i-k][j-1] for k in range(1, min(m+1, i)))
    # dp.pp()
    return dp[-1][-1]

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        solve(2,6,7).must_equal(6)
        solve(2,2,3).must_equal(2)
        solve(6,3,8).must_equal(21)
        solve(4,2,5).must_equal(4)
        solve(4,3,5).must_equal(4)
