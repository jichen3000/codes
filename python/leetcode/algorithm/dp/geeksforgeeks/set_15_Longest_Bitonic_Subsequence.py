# 30mins
def solve(nums):
    n = len(nums)
    if n <= 2: return n
    # increase
    dp1 = [1] * n
    for i in xrange(1,n):
        cur_list = [dp1[k]+1 for k in xrange(i) if nums[i] > nums[k]]
        if cur_list: dp1[i] = max(cur_list)
    dp2 = [1] * n
    for i in xrange(n-2,-1,-1):
        cur_list = [dp2[k]+1 for k in xrange(n-1, i, -1) if nums[i] > nums[k]]
        if cur_list: dp2[i] = max(cur_list)
    return max(dp1[i]+dp2[i+1] for i in xrange(n-1))

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        nums = [1, 11, 2, 10, 4, 5, 2, 1]
        solve(nums).must_equal(6)
        nums = [12, 11, 40, 5, 3, 1]
        solve(nums).must_equal(5)
        nums = [12, 11, 5, 3, 1]
        solve(nums).must_equal(5)
        nums = [1,2]
        solve(nums).must_equal(2)
        nums = [1]
        solve(nums).must_equal(1)
