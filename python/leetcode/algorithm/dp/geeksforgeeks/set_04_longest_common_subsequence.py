# top down
def solve(s1, s2):
    (s1,s2).p()
    if len(s1) == 1:
        if s1 in s2:
            return 1
        else:
            return 0
    if len(s2) == 1:
        if s2 in s1:
            return 1
        else:
            return 0
    results = [0]
    for i in xrange(len(s1)-1,0,-1):
        r_index = s2.rfind(s1[i])
        if r_index > 0:
            results += solve(s1[:i], s2[:r_index]) + 1,
        else:
            results += solve(s1[:i], s2),
    result = max(results)
    (s1,s2,result).p()
    return result

# using matrix dp
def solve(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    dp = [[0 for _ in range(n2)] for _ in range(n1)]
    last = 0
    for i in xrange(n1):
        for j in xrange(n2):
            if s2[j] == s1[i]:
                dp[i][j] = 1 + dp[i-1][j-1] if i>0 and j>0 else 0
            else:
                dp[i][j] = dp[i][j-1] if j >0 else last
            # (i,j,s1[i],s2[j],dp[i][j]).p()
        last = dp[i][-1]
        # last.p()
    dp.pp()
    return dp[-1][-1]

# only using array dp
# def solve(s1, s2):
#     n1 = len(s1)
#     n2 = len(s2)
#     dp = [0 for _ in range(n2)]
#     last = 0
#     for i in xrange(n1):
#         pre2 = pre1 = 0
#         for j in xrange(n2):
#             pre2, pre1 = pre1, dp[j]
#             if s2[j] == s1[i]:
#                 dp[j] = 1 + pre2
#             else:
#                 dp[j] = dp[j-1] if j >0 else last
#             # (i,j,s1[i],s2[j],dp[i][j]).p()
#         last = dp[-1]
#         (i,last,dp).p()
#         # last.p()
#     # dp.pp()
#     return dp[-1]

# def solve(s1, s2):
#     n1 = len(s1)
#     n2 = len(s2)
#     dp = 0
#     last = 0
#     for i in xrange(n1):
#         pre2 = pre1 = 0
#         dp = 0
#         cur_pre = last
#         for j in xrange(n2):
#             pre2, pre1 = pre1, dp
#             if s2[j] == s1[i]:
#                 dp = 1 + pre2
#             else:
#                 dp = cur_pre
#             cur_pre = dp
#             (i,s1[i],j,s2[j],dp,pre2,pre1).p()
#         last = dp
#         # (i,last,dp).p()
#         # last.p()
#     # dp.pp()
#     return dp

# according to http://www.geeksforgeeks.org/longest-common-subsequence/
def solve(s1, s2):
    # find the length of the strings
    m = len(s1)
    n = len(s2)
 
    # declaring the array for storing the dp values
    dp = [[0]*(n+1) for i in xrange(m+1)]
 
    """Following steps build dp[m+1][n+1] in bottom up fashion
    Note: dp[i][j] contains length of LCS of s1[0..i-1]
    and s2[0..j-1]"""
    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0 :
                # dp[i][j] = 0
                pass
            elif s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j] , dp[i][j-1])
 
    # dp[m][n] contains the length of LCS of s1[0..n-1] & s2[0..m-1]
    dp.pp()
    return dp[m][n]

def solve(s1, s2):
    # find the length of the strings
    m = len(s1)
    n = len(s2)
 
    # declaring the array for storing the dp values
    dp = [0]*(n+1)
 
    """Following steps build dp[m+1][n+1] in bottom up fashion
    Note: dp[i][j] contains length of LCS of s1[0..i-1]
    and s2[0..j-1]"""
    for i in range(m+1):
        pre1 = pre2 = 0
        for j in range(n+1):
            pre2, pre1 = pre1, dp[j]
            if i == 0 or j == 0 :
                # dp[i][j] = 0
                pass
            elif s1[i-1] == s2[j-1]:
                dp[j] = pre2+1
            else:
                dp[j] = max(pre1 , dp[j-1])
 
    # dp[m][n] contains the length of LCS of s1[0..n-1] & s2[0..m-1]
    dp.pp()
    return dp[n]
if __name__ == '__main__':
    from minitest import *

    with test(solve):
        solve("eabbdah","aabbdhrzz").must_equal(5)
