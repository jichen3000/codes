class Solution:
    def longestMountain(self, a):
        """
        :type A: List[int]
        :rtype: int
        """
        if not a or len(a) < 3:
            return 0
        a = [float("inf")] + a + [float("inf")]
        res = 0
        pre_min = None
        for i in range(1, len(a)-1):
            (i, a[i]).p()
            if a[i-1] == a[i]:
                if a[i] < a[i+1]:
                    pre_min = i  
                else:
                    pre_min = None                  
            if a[i-1] > a[i] <= a[i+1]:
                if pre_min:
                    res = max(res, i - pre_min + 1)
                pre_min = i
        return res


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().longestMountain([2,1,4,7,3,2,5]).must_equal(5)
        Solution().longestMountain([2,1,4,7,3,2]).must_equal(5)
        Solution().longestMountain([2,2,2]).must_equal(0)
        Solution().longestMountain([0,1,2,3,4]).must_equal(0)
        Solution().longestMountain([1,1,0,0,1,0]).must_equal(3)
        Solution().longestMountain([0,1,1]).must_equal(0)
        Solution().longestMountain([2,3,3,2,0,2]).must_equal(0)
        Solution().longestMountain([0,0,1,0,0,1,1,1,1,1]).must_equal(3)


        

