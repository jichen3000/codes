class Solution:
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from bisect import bisect_left
        if not nums: return 0
        n = len(nums)
        nums.sort()
        res = 0
        for i in range(n-2):
            for j in range(i+1, n-1):
                big = nums[i] + nums[j]
                k = bisect_left(nums[j+1:], big)
                # print(i,j,k)
                res += k
        return res
                
                
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)
        nums.sort()
        res = 0
        for i in range(n-2):
            k = i + 2
            for j in range(i+1, n-1):
                big = nums[i] + nums[j]
                k = max(j+1, k)
                while k < n and nums[k] < big:
                    k += 1
                res += k - j - 1
        return res

    # this one only O(n**2) and space O(1)
    # sort nums
    # idea: first fix the big one, from last one, call it i
    # so the sub problem become find the how many pairs which sum larger than nums[i] in nums[:i]
    # for sub problem:
    #   set left and right
    #   case 1: nums[left] + nums[right] > nums[i],
    #      means all the j from left before right are larger than nums[i],
    #      so count of pairs = right - left (key point)
    #      and right - 1, since all j from left to right has been counted
    #  case 2: nums[left] + nums[right] <= nums[i],
    #      just left + 1
    def triangleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)
        nums.sort()
        res = 0
        for i in range(n-1, 1, -1):
            l, r = 0, i - 1
            while (l < r):
                if nums[l] + nums[r] > nums[i]:
                    res += r - l
                    r -= 1
                else:
                    l += 1
        return res                    