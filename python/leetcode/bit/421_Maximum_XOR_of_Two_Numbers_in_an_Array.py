class Solution(object):
    def findMaximumXOR(self, nums):
        res = 0
        for i in xrange(31, -1, -1):
            res <<= 1
            res_1 = res + 1
            prefix_set = {num>>i for num in nums}
            for prefix in prefix_set:
                if prefix ^ res_1 in prefix_set:
                    res = res_1
        return res
        
class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mask = res = 0
        for i in xrange(31, -1, -1):
            mask |= 1 << i
            prefix_set = {mask & num for num in nums}
            temp = res | 1 << i
            for p in prefix_set:
                if p ^ temp in prefix_set:
                    res = temp
                    break
        return res

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().findMaximumXOR([3, 10, 5, 25, 2, 8]).must_equal(28)
        Solution().findMaximumXOR([10, 2, 8]).must_equal(10)
