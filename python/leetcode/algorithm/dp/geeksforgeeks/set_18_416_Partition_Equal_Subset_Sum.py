## 22mins
class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n <= 1:
            return False
        sum_v = sum(nums)
        if sum_v % 2 != 0:
            return False
        half_sum = sum_v / 2
        nums.sort()
        dp = [False] * (half_sum+1)
        for v in nums:
            if v > half_sum:
                return False
            for j in xrange(half_sum, v-1, -1):
                if j==v or dp[j-v]:
                    dp[j] = True
            if dp[-1]:
                return True
        return False

