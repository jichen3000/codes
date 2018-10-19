class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0: return
        for i,v in enumerate(nums[n-k:]+nums[:n-k]):
            nums[i] = v
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0: return
        count, i, temp, nums[0] = 0, 0, nums[0], None
        while count < n:
            count += 1
            if temp == None:
                i += 1
                temp, nums[i] = nums[i], temp
            ni = (i+k) % n
            nums[ni], temp, i = temp, nums[ni], ni
        return nums

    # the best one, exactly O(n) and Space(1)
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n == 0: return
        k = k % n
        if k == 0: return
        i, cur = 0, nums[0]
        nums[0] = None
        for _ in range(n):
            if cur == None:
                i = (i+1) % n
                cur, nums[i] = nums[i], None
            j = (i+k) % n
            nums[j], cur, i = cur, nums[j], j

    # esay to remember and understand
    def rotate(self, nums, k):
        n = len(nums)
        if n == 0: return
        k = k % n
        if k == 0: return
        def reverse(nums, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)  
                    
if __name__ == '__main__':
    from minitest import *

    with test("Solution"):
        # Solution().rotate([1,2,3,4,5,6,7],3).must_equal([5,6,7,1,2,3,4])
        Solution().rotate([1,2,3,4,5,6],2).must_equal([5,6,1,2,3,4])
        # Solution().rotate([1,2],1).must_equal([2,1])


