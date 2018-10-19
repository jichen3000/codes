class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        mem = {}
        for n in nums:
            if n not in mem:
                left = mem[n-1] if n-1 in mem else 0
                right = mem[n+1] if n+1 in mem else 0

                mem[n] = left + right + 1

                # mem[n] = mem[n]
                res = max(res, mem[n])

                mem[n-left] = mem[n]
                mem[n+right] = mem[n]
        return res

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().longestConsecutive([1,2,0,1]).must_equal(3)