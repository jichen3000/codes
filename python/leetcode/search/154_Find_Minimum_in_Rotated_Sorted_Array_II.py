class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        low, high = 0, n - 1
        while low < high:
            mid = (low + high) / 2
            if nums[mid] > nums[high]:
                low = mid + 1
            elif nums[mid] < nums[high]:
                high = mid
            else:
                high = high - 1
        return nums[low]
    
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().findMin([9,9,9,1,9,9]).must_equal(1)
        Solution().findMin([2,1]).must_equal(1)
        Solution().findMin([1,2]).must_equal(1)
        Solution().findMin([1,2,3,4,5]).must_equal(1)
        Solution().findMin([2,3,4,5,1]).must_equal(1)
        Solution().findMin([4,5,1,2,3]).must_equal(1)
        Solution().findMin([4,5,1,2]).must_equal(1)
        Solution().findMin([4,5,1]).must_equal(1)

