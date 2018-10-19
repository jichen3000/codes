# http://www.geeksforgeeks.org/dynamic-programming-set-8-matrix-chain-multiplication/
from operator import mul
def solve(nums):
    # nums.p()
    n = len(nums)
    if n < 3: raise Exception("not support")
    if n == 3:
        return reduce(mul, nums)
    return min(reduce(mul,nums[i-1:i+2]) + solve(nums[:i]+nums[i+1:]) 
            for i in xrange(1,n-1))

def solve(nums):
    # nums.p()
    n = len(nums)
    dp = [[0] * n for _ in xrange(n)]
    for l in xrange(2,n):
        for i in xrange(n-l):
            j = i + l
            if l == 2:
                dp[i][i+l] = reduce(mul, nums[i:i+l+1])
            else:
                dp[i][j] = min(dp[i][k] + reduce(mul, [nums[i],nums[k],nums[j]]) + dp[k][j] 
                    for k in xrange(i+1,j))
    # dp.pp()
    return dp[0][-1]

def solve(nums):
    # nums.p()
    n = len(nums)
    dp = [[0] * n for _ in xrange(n)]
    for l in xrange(2,n):
        for i in xrange(n-l):
            j = i + l
            dp[i][j] = min(dp[i][k] + reduce(mul, [nums[i],nums[k],nums[j]]) + dp[k][j] 
                    for k in xrange(i+1,j))
    return dp[0][-1]

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        # solve([40, 20, 30, 10, 30]).must_equal(26000)
        solve([10, 20, 30, 40, 30]).must_equal(30000)