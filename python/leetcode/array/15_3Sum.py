class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = set()
        from itertools import combinations
        for l in combinations(nums,3):
            if sum(l) == 0:
                res.add(l)
        return list(res)
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from bisect import bisect_left
        n = len(nums)        
        nums.sort()
        res = set()
        if n < 3: return []
        for i0 in range(n-2):
            for i1 in range(i0+1, n-1):
                remain = 0 - nums[i0] - nums[i1]
                i2 = bisect_left(nums[i1+1:], remain) + i1 + 1
                while i2 < n and nums[i2] == remain:
                    res.add((nums[i0], nums[i1], nums[i2]))
                    i2 += 1

        return list(res)
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # from bisect import bisect_right
        n = len(nums)        
        nums.sort()
        res = set()
        if n < 3: return []
        for i0 in range(n-2):
            if nums[i0] > 0: break
            if i0 > 0 and nums[i0] == nums[i0-1]:
                continue
            for i1 in range(n-1, i0 + 1, -1):
                if i1 < n - 1 and nums[i1] == nums[i1+1]:
                    continue
                i2 = i1 - 1
                remain = 0 - nums[i0] - nums[i1]
                if nums[i2] < remain:
                    break
                while i2 > i0 and nums[i2] > remain:
                    i2 -= 1
                if i2 > i0 and nums[i2] == remain:
                    res.add((nums[i0], nums[i2], nums[i1]))
        return list(res)
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # from bisect import bisect_right
        n = len(nums)        
        nums.sort()
        res = []
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, n-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    res += (nums[i], nums[l], nums[r]),
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    r -= 1; l += 1
        return res

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().threeSum([-1, 0, 1, 2, -1, -4]).must_equal([(-1, -1, 2), (-1, 0, 1)])
