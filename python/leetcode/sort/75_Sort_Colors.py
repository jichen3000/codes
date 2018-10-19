class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i0, i1, i2 = 0, 0, 0
        for v in nums:
            if v == 0:
                nums[i2] = 2
                nums[i1] = 1
                nums[i0] = 0
                i0+=1
                i1+=1
                i2+=1
            elif v == 1:
                nums[i2] = 2
                nums[i1] = 1
                i1+=1
                i2+=1
            elif v == 2:
                nums[i2] = 2
                i2+=1
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i0, i1, i2 = 0, 0, 0
        for v in nums:
            nums[i2] = 2
            i2+=1        
            if v <= 1:
                nums[i1] = 1
                i1+=1
            if v == 0:
                nums[i0] = 0
                i0+=1


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        nums = [1,0]
        Solution().sortColors(nums)
        nums.must_equal([0,1])
        nums = [2,2,0,1,1,0]
        Solution().sortColors(nums)
        nums.must_equal([0,0,1,1,2,2])
