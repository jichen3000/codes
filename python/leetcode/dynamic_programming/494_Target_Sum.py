class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        n = len(nums)
        if n == 0: return 0
        sum_v = sum(nums)
        if S > sum_v: return 0
        dp = [ [0] * (2*sum_v+1) for _ in range(n) ]
        for i in xrange(n):
            for jj in xrange(-sum_v, sum_v+1):
                j = jj+sum_v
                if i == 0:
                    if nums[i] == jj:
                        dp[i][j] += 1
                    if nums[i] == -jj:
                        dp[i][j] += 1
                else:
                    if j-nums[i] >= 0:
                        dp[i][j] += dp[i-1][j-nums[i]]
                    if j+nums[i] <= 2*sum_v:
                        dp[i][j] += dp[i-1][j+nums[i]]
        # dp.pp()
        return dp[-1][S+sum_v]

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().findTargetSumWays([1,1,1,1,1], 3).must_equal(5)
        # Solution().findTargetSumWays([1], 2).must_equal(0)
        Solution().findTargetSumWays([0,0,0,0,0,0,0,0,1], 1).must_equal(256)