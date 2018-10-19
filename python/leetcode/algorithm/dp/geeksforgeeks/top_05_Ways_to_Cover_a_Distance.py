def solve(nums,k):
    n = len(nums)
    def inner(k):
        # k.p()
        if k<0: return 0
        if k==0: return 1
        return sum(inner(k - nums[i]) for i in range(n))
    return inner(k)

def solve(nums, k):
    n = len(nums)
    if n == 0: return 0
    dp = [0] * (k+1)
    for i in xrange(1,k+1):
        for j in xrange(n):
            if i == nums[j]:
                dp[i] += 1
            if i > nums[j]:
                dp[i] += dp[i-nums[j]]


    return dp[-1]
    


if __name__ == '__main__':
    from minitest import *

    with test(solve):
        solve([1,2,3], 3).must_equal(4)
        solve([1,2,3], 4).must_equal(7)
        solve([1,2,3], 10).must_equal(274)
        solve([2,3,4], 10).must_equal(17)