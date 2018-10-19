## see set_3_300_Longest_Increasing_Subsequence.py
# http://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
import bisect
class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        chains = [[nums[0]]]
        max_len = 1
        for i in nums:
            added = False
            for chain_i in xrange(len(chains)):
                chain = chains[chain_i]
                if i > chain[-1]:
                    # if i - 1 > chain[-1]:
                    #     chains.append(chain[:])
                    chain.append(i)
                    added = True
                    max_len = max(len(chain), max_len)
                elif i < chain[-1]:
                    if len(chain) == 1:
                        chain[-1] = i
                        added = True
                    elif chain[-2] < i:
                        chain[-1] = i
                        added = True
            if not added:
                chains.append([i])
        return max_len
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        dp = [1] * n
        for i in xrange(1,len(nums)):
            for j in xrange(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
    
    # actually this is not dp, its binary search
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            low, high = 0, size
            while low != high:
                middle = (low + high) / 2
                if tails[middle] < x:
                    low = middle + 1
                else:
                    high = middle
            tails[low] = x
            size = max(low + 1, size)
        return size
    def lengthOfLIS(self, nums):
        tails = [0] * len(nums)
        size = 0
        for x in nums:
            i = bisect.bisect_left(tails[:size], x)
            tails[i] = x
            if i == size:
                size += 1                
        return size

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().lengthOfLIS([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]).must_equal(6)