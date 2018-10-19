class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n == 0:
            return []
        all_mask = 1 << n
        results = []
        for mask in xrange(all_mask):
            cur = []
            for i in xrange(n):
                if mask >> i & 1:
                    cur += nums[i],
            results += cur,
        return results
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        n = len(nums)
        mask = 1 << n
        results = []
        for m in xrange(mask):
            j = 0
            cur = []
            while m > 0:
                if m & 1:
                    cur += nums[j],
                m >>= 1
                j += 1
            results += cur,
        return results  
    

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().subsets([]).must_equal([[]])
        Solution().subsets([1,2,3]).must_equal(
                [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]])

