# http://www.geeksforgeeks.org/partition-a-set-into-two-subsets-such-that-the-difference-of-subset-sums-is-minimum/
def solve(nums):
    n = len(nums)
    if n == 0: return 0
    if n == 1: return nums[0]
    sum_v = sum(nums)
    amout = sum_v/2 + 1
    dp = [False] * (amout+1)
    for i in xrange(n):
        for j in xrange(amout, nums[i]-1, -1):
            if j == nums[i]:
                dp[j] = True
            else:
                dp[j] = dp[j-nums[i]]
    for j in xrange(amout, -1, -1):
        if dp[j]:
            return abs(sum_v - j - j)

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        solve([1,5,6,11]).must_equal(1)
