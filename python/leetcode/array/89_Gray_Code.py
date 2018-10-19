class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0: return [0]
        res = ["0","1"]
        for i in range(n-1):
            res = ["0" + s for s in res] + ["1" + s for s in reversed(res)]
        return [int(s,2) for s in res]
        
if __name__ == '__main__':
    from minitest import *

    with test("Solution"):
        Solution().grayCode(3).must_equal([0, 1, 3, 2, 6, 7, 5, 4])


