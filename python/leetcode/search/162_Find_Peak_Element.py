class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        if len(nums) == 1: return 0
        nums = [-sys.maxint] + nums + [-sys.maxint]
        for i in range(1,len(nums)-1):
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                return i-1
        
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        nums = [-sys.maxint] + nums + [-sys.maxint]
        l, r = 1, len(nums) - 1
        while l < r:
            m = (l+r)/2
            if nums[m-1] < nums[m] and nums[m] > nums[m+1]:
                return m-1
            elif nums[m-1] > nums[m]:
                r = m
            else:
                l = m + 1
        