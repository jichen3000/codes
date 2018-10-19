## 24mins
def solve(nums):
    n = len(nums)
    if n == 0: return 0
    dp = [0] * n
    for i in range(0,n):
        cur_list = [dp[k]+nums[i] for k in range(i) if nums[i]>nums[k]]
        dp[i] = max(cur_list) if cur_list else nums[i]
    return max(dp)

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        nums = [1, 101, 2, 3, 100, 4, 5]
        solve(nums).must_equal(106)
        nums = [101, 100, 5]
        solve(nums).must_equal(101)

