from collections import Counter
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [k for k,v in Counter(nums).most_common() if v == 2]
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        results = []
        for i in range(n):
            while nums[i] != i+1 and nums[i]!=-1:
                if nums[nums[i]-1] == nums[i]:
                    results += nums[i],
                    nums[i] = -1
                    break
                else:
                    nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
                    
        return results
    
    # best answer
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        results = []
        for i in nums:
            index = abs(i) - 1
            # the postion has been visited, means index + 1 is duplicated.
            if nums[index] < 0:
                results += index + 1,
            nums[index] = -nums[index]
        return results
    # second try
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        results = []
        for i in range(len(nums)):
            ni = i
            # (i,nums[i]).p()
            while nums[ni] != i + 1 and nums[i] != -1:
                ni = nums[i] - 1
                nums[i], nums[ni] = nums[ni], nums[i]
                if nums[i] == nums[nums[i]-1] and nums[i] != i + 1 and nums[i] != -1:
                    results += nums[i],
                    nums[i] = -1
                    break
                # (i, ni, nums, results).p()
            # if nums[i] == nums[nums[i]-1]:
            #     results += nums[i],
            #     nums[i] = -1
        return results                    
        

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().findDuplicates([4,3,2,7,8,2,3,1]).must_equal([3,2])

