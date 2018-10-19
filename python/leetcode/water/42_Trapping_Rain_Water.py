class Solution(object):
    def trap(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        if n <= 1: return 0
        pre = heights[0]
        stack = []
        areas = []
        for i in range(1,n):
            h = heights[i]
            # (pre,h).p()
            if h < pre:
                stack += (i-1, pre),
                # (h < pre, stack).p()
            elif h > pre and len(stack) > 0:
                while len(stack) > 0 and stack[-1][1] <= h:
                    last_i, last_h = stack.pop()
                if len(stack) > 0:
                    last_i, last_h = stack[-1]
                area = (last_i, i, min(last_h, h))
                while len(areas) > 0 and last_i <= areas[-1][0] and i > areas[-1][1]:
                    areas.pop()
                areas += area,
                # (h > pre and len(stack) > 0, area).p()
            # areas.p()
            pre = h
        # areas.p()
        total = 0
        for si, ei, h in areas:
            total += sum(h-heights[i] for i in range(si+1, ei))
        return total
    def trap(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        left, right = 0, n-1
        area, max_left, max_right = 0, 0, 0
        while left < right:
            if heights[left] <= heights[right]:
                if heights[left] >= max_left:
                    max_left = heights[left]
                else:
                    area += max_left - heights[left]
                left += 1
            else:
                if heights[right] >= max_right:
                    max_right = heights[right]
                else:
                    area += max_right - heights[right]
                right -= 1
        return area

class Solution(object):
    def trap(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        if n == 0: return 0
        res = 0
        i, j = 0, n-1
        max_i, max_j = heights[i], heights[j]
        while i < j:
            if heights[i] <= heights[j]:
                i += 1
                if i == j: return res
                if heights[i] < max_i:
                    res += max_i - heights[i]
                else:
                    max_i = heights[i]
            else:
                j -= 1
                if i == j: return res
                if heights[j] < max_j:
                    res += max_j - heights[j]
                else:
                    max_j = heights[j]
        return res
class Solution(object):
    def trap(self, nums):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1: return 0
        res = 0
        l, r = 0, n-1
        while l < r and nums[l] == 0:
            l += 1
        while l < r and nums[r] == 0:
            r -= 1
        while l < r:
            h = nums[l]
            while l < r and nums[l] <= nums[r]:
                res += max(h - nums[l], 0)
                h = max(h, nums[l])
                l += 1
            h = nums[r]
            while l < r and nums[l] >= nums[r]:
                res += max(h - nums[r], 0)
                h = max(h, nums[r])
                r -= 1
        return res
                
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().trap([2,0,2]).must_equal(2)           
        # Solution().trap([2,1,0,2]).must_equal(3)           
        Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]).must_equal(6)           