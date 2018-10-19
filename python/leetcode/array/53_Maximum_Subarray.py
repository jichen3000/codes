class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = cur = -float("inf")
        for v in nums:
            cur += v
            cur = max(cur, v)
            res = max(res, cur)
        return res
        

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]).must_equal(6)