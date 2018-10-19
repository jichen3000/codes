class Solution:
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        mem = {0:-1}
        sum_v = res = 0
        for i,v in enumerate(nums):
            sum_v += v
            if sum_v not in mem:
                mem[sum_v] = i
            if sum_v - k in mem:
                res = max(res, i - mem[sum_v - k])
        return res
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().maxSubArrayLen([1, -1, 5, -2, 3], 3).must_equal(4)
        Solution().maxSubArrayLen([-2, -1, 2, 1], 1).must_equal(2)


