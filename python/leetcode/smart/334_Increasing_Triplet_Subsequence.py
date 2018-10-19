from itertools import combinations

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first = second = float('inf')
        for n in nums:
            if n <= first:
                first = n
            elif n <= second:
                second = n
            else:
                return True
        return False
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().increasingTriplet([120,110,50,100,60,40,70]).must_equal(True)