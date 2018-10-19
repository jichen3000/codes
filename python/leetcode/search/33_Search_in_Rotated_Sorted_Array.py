class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        from bisect import bisect_left
        if not nums: return -1
        first = nums[0]
        if target == first:
            return 0
        l, r = 0, len(nums)
        while l < r:
            m = (l+r) // 2
            if nums[m-1] > first > nums[m]:
                break
            elif nums[m] > first:
                l = m + 1
                # print(l)
            elif nums[m] < first:
                # print("r")
                r = m
            else:
                m = m + 1
                break
        if target < first:            
            i = bisect_left(nums[m:], target) + m
        else:
            i = bisect_left(nums[:m], target)
        if i < len(nums) and nums[i] == target:
            return i
        return -1   
    # https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple
    # great idea
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums: return -1
        l, r, f = 0, len(nums), nums[0]
        while l < r:
            m = (l+r) // 2
            v = nums[m] 
            if not(nums[m] < f and target < f):
                v = float("inf")
                if target < f:
                    v = -float("inf")

            if v == target:
                return m
            elif v < target:
                l = m + 1
            else:
                r = m
        return -1

                
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().search([4,5,6,7,0,1,2], 0).must_equal(4)
        Solution().search([1], 0).must_equal(-1)