def solve(s1, s2):
    n1, n2 = len(s1), len(s2)
    if n1 == 0: return n2
    if n2 == 0: return n1
    dp = [ [""] * (n2+1) for _ in xrange(n1+1) ]
    for i in xrange(n1+1):
        for j in xrange(n2+1):
            if i == 0 or j == 0:
                if i == 0:
                    dp[i][j] = s2[:j]
                else:
                    dp[i][j] = s1[:i]
            else:
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + s1[i-1]
                else:
                    if len(dp[i][j-1]) > len(dp[i-1][j]):
                        dp[i][j] = dp[i-1][j] + s1[i-1]
                    else:
                        dp[i][j] = dp[i][j-1] + s2[j-1]
    # dp.pp()
    return dp[-1][-1]

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        solve("geek","eke").must_equal("geeke")
        solve("AGGTAB","GXTXAYB").must_equal("AGGXTXAYB")