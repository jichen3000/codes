from collections import Counter
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        counts = Counter(nums)
        # counts.p()
        n = max(counts.keys()) + 1
        dp = [0] * n
        dp[1] = counts.get(1, 0)
        max_point = dp[1]
        for i in range(2, n):
            if i in counts:
                dp[i] = max(dp[i-2] + counts[i] * i, max_point)
            else:
                dp[i] = max_point
            # (i,counts.get(i, 0),dp[i]).p()
            max_point = max(max_point, dp[i])
        return max_point
            
if __name__ == '__main__':
    from minitest import *

    with test("bs"):
        # Solution().deleteAndEarn([]).must_equal(0)
        # Solution().deleteAndEarn([3,4,2]).must_equal(6)
        # Solution().deleteAndEarn([2, 2, 3, 3, 3, 4]).must_equal(9)
        # Solution().deleteAndEarn([1,1,1,2,4,5,5,5,6]).must_equal(18)
        # Solution().deleteAndEarn([8,10,4,9,1,3,5,9,4,10]).must_equal(37)
        Solution().deleteAndEarn([1,6,3,3,8,4,8,10,1,3]).must_equal(43)
