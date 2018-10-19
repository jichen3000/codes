class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0: return []
        if k == 1: return nums
        if n <= k: return [max(nums)]
        results = []
        for i in range(0,n-k+1):
            results += max(nums[i:i+k]),
        return results
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0: return []
        if k == 1: return nums
        if n <= k: return [max(nums)]
        # pre = max(nums[:k])
        results = []
        queue = []
        for i in range(n):
            while queue and queue[0] < i-k+1:
                queue.pop(0)
            while queue and nums[queue[-1]] < nums[i]:
                queue.pop()
            queue.append(i)
            if i >= k -1:
                results += nums[queue[0]],
                
        return results        
    # not better than the above one
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0: return []
        if n <= k: return [max(nums)]
        res = []        
        q = []
        for i in range(n):
            if q and q[0][1] == i - k:
                q.pop(0)
            while q and q[-1][0] < nums[i]:
                q.pop()
            q += (nums[i],i),
            if i + 1 >= k:
                res += q[0][0],
        return res

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums) < k: return []
        q, res = [], []
        for i, num in enumerate(nums):
            if q and q[0] <= i - k:
                q.pop(0)
            while q and nums[q[-1]] <= num:
                q.pop()
            q += i,
            if i + 1 >= k:
                res += nums[q[0]],
        return res
                    
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # boxes = [1, 3, 2, 2, 2, 3, 4, 3, 1]
        # Solution().removeBoxes(boxes).must_equal(23)
        Solution().maxSlidingWindow([7,2,4], 2).must_equal([7,4])
        # Solution().maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3).must_equal([3,3,5,5,6,7])
