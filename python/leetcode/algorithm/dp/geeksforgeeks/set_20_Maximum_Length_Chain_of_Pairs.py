def solve(pairs):
    n = len(pairs)
    if n <= 1: return n
    pairs.sort()
    dp = [1] * n
    for i in xrange(1,n):
        dp[i] = max([dp[j]+1 for j in xrange(i) 
                if pairs[j][1] <pairs[i][0]]+[1])
    return max(dp)

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        pairs = [(5, 24), (39, 60), (15, 28), (27, 40), (50, 90)]
        solve(pairs).must_equal(3)
