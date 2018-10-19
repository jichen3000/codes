from collections import Counter
from operator import xor
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        return [k for k,v in Counter(nums).items() if v == 1]
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xor_v = reduce(xor, nums)
        # first 1, very clever here
        first_1 = xor_v & (-xor_v)
        results = [0,0]
        for num in nums:
            # very clever here
            if (num & first_1) == 0:
                results[0] ^= num
            else:
                results[1] ^= num
        return results

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().singleNumber([0,0,1,2]).must_equal([2,1])