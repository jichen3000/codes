class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        mem = [-1] * (n+1)
        for num in nums:
            if num-1 >=0 and num-1<n:
                mem[num-1] = 1
        for i, v in enumerate(mem):
            if v == -1:
                return i+1
        
            
           
if __name__ == '__main__':
    from minitest import *


    with test(Solution):
        Solution().firstMissingPositive([1,2,0]).must_equal(3)
        Solution().firstMissingPositive([3,4,-1,1]).must_equal(2)
        Solution().firstMissingPositive([1000,-1]).must_equal(1)
