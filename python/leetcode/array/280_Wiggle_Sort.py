class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1: return
        nums.sort()
        for i in range(1, n, 2):
            if i + 1 < n:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1: return
        i, j = 0, 1
        while i < n and j < n:
            if nums[j] < nums[i]:
                nums[i], nums[j] = nums[j], nums[i]
            if i < j:
                i += 2
            else:
                j += 2