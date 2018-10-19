class Solution(object):
    def findMaxLength_time(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        mem = [0] * n
        max_l = 0
        for i in xrange(n):
            cur = 1 if nums[i] == 1 else -1
            # cur.p()
            for j in xrange(i+1):
                mem[j] += cur
                # (cur, j, mem[j]).p()
                if mem[j] == 0:
                    max_l = max(max_l, i+1-j)
        
        return max_l
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        mem = {0:-1}
        sum_v = 0
        max_l = 0
        for i in xrange(n):
            cur = 1 if nums[i] == 1 else -1
            sum_v += cur
            if sum_v in mem:
                max_l = max(max_l, i - mem[sum_v])
            else:
                mem[sum_v] = i
        return max_l

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().findMaxLength([0,1,1]).must_equal(2)
        Solution().findMaxLength([0,0,0,0,1,1]).must_equal(4)
        Solution().findMaxLength([0,0,0,1,0,0,0,0,1,1]).must_equal(4)
        Solution().findMaxLength([0,0,0,1,0,1]).must_equal(4)
        Solution().findMaxLength([0,0,1,0,0,0,1,1]).must_equal(6)
