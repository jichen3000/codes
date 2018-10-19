class Solution(object):
    def fb(self, s, v, k):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().pourWater([1,2,3,4,3,2,1,2,3,4,3,2,1],
                2,5).must_equal([1,2,3,4,3,3,2,2,3,4,3,2,1])
        Solution().pourWater([1,2,3,4,3,2,1,2,3,4,3,2,1]
                10,2).must_equal([4,4,4,4,3,3,3,3,3,4,3,2,1])
