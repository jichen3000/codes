class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0: return
        largest_i = 0
        for i in range(n-2,-1,-1):
            if nums[i] < nums[i+1]:
                largest_i = i + 1
                break
        sn = n + largest_i
        # nums.p()
        if largest_i > 0:
            i = largest_i-1
            for i in range(n-1,largest_i-1,-1):
                if nums[i] > nums[largest_i-1]:
                    break
            # (largest_i, nums[largest_i-1], largest_i-1,i).p()
            nums[i], nums[largest_i-1] = nums[largest_i-1], nums[i]
            # nums.p()
        for i in range(largest_i, sn/2):
            j = sn - 1 - i
            nums[i], nums[sn - 1 - i] = nums[sn - 1 - i], nums[i]
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        def find_last_peak_index():
            res = 0
            for i in range(n-1, 0, -1):
                if nums[i] > nums[i-1]:
                    return i
            return res
        def reverse_list(start_i, end_i):
            sum_i = start_i+end_i
            for i in range(start_i, (sum_i+1)/2):
                j = start_i + end_i - i
                nums[i], nums[sum_i-i] = nums[sum_i-i], nums[i]
            
        peak_i = find_last_peak_index()
        if peak_i == n - 1:
            nums[n-1], nums[n-2] = nums[n-2], nums[n-1]
        elif peak_i == 0:
            reverse_list(0, n-1)
        else:
            change_i = peak_i
            for i in range(n-1,peak_i-1, -1):
                if nums[i] > nums[peak_i-1]:
                    change_i = i
                    break
            nums[peak_i-1], nums[change_i] = nums[change_i], nums[peak_i-1]
            reverse_list(peak_i, n-1)
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0: return nums
        peak_i = 0
        for i in range(n-1, 0, -1):
            if nums[i] > nums[i-1]:
                peak_i = i
                break
        # peak_i.p()
        if peak_i > 0:
            change_v = nums[peak_i-1]
            change_i = peak_i
            for i in range(n-1, peak_i, -1):
                if nums[i] > change_v:
                    change_i = i
                    break
            # (change_v, change_i, nums[change_i]).p()
            nums[peak_i-1], nums[change_i] = nums[change_i], nums[peak_i-1]
        for i in range(peak_i, (peak_i+n)/2):
            nums[i], nums[n-1-i+peak_i] = nums[n-1-i+peak_i], nums[i]
            
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        nums = [1,2,3,4]
        Solution().nextPermutation(nums)
        nums.must_equal([1,2,4,3])
        nums = [1,2,4,3]
        Solution().nextPermutation(nums)
        nums.must_equal([1,3,2,4])
        nums = [1,3,4,2]
        Solution().nextPermutation(nums)
        nums.must_equal([1,4,2,3])
        nums = [4,3,2,1]
        Solution().nextPermutation(nums)
        nums.must_equal([1,2,3,4])

        nums = [2,3,1]
        Solution().nextPermutation(nums)
        nums.must_equal([3,1,2])
        nums = [3,1,2]
        Solution().nextPermutation(nums)
        nums.must_equal([3,2,1])
