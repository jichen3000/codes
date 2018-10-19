def solve(nums, k):
    n = len(nums)
    def inner(n, k):
        if k == 0: return True
        if n == 0: return False
        if nums[n-1] > k:
            return inner(n-1, k)
        return inner(n-1,k) or inner(n-1, k-nums[n-1])
    return inner(n, k)
def solve(nums, k):
    n = len(nums)
    if k == 0: return True
    if n == 0: return False
    dp = [False] * (k+1) 
    for i in xrange(n):
        for j in xrange(k, nums[i]-1, -1):
            if j == nums[i]:
                dp[j] = True
            else:
                dp[j] = dp[j-nums[i]]
        if dp[-1]:
            return True
    return False

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        solve([3,4,5,10],9).must_equal(True)
        solve([3,4,5,10],11).must_equal(False)


