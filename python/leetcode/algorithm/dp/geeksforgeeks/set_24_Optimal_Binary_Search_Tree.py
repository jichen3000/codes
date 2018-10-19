def solve(freqs):
    n = len(freqs)
    if n == 0: return 0
    def recursive(i,j):
        if j < i: return 0
        if j == i: return freqs[i]
        return min(recursive(i,r-1)+recursive(r+1,j)+sum(freqs[i:j+1])
                for r in xrange(i,j+1))
    return recursive(0,n-1)

def sovle(freqs):
    n = len(freqs)
    if n == 0: return 0
    dp = [ [0] * n for _ in xrange(n)]
    for l in range(0,n):
        for i in range(0,n-l):
            j = i + l
            if j == i:
                dp[i][j] = freqs[i]
            else:
                sum_v = sum(freqs[i:j+1])
                dp[i][j] = min(sum_v+
                        (dp[i][r-1] if r-1>=i else 0)+
                        (dp[r+1][j] if r+1<=j else 0) 
                        for r in xrange(i,j+1))
    return dp[0][-1]

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        freqs = [34,8,50]
        solve(freqs).must_equal(142)