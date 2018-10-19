class Solution:
    def lenLongestFibSubseq(self, a):
        """
        :type A: List[int]
        :rtype: int
        """
        from collections import defaultdict
        pos_d = {v:i for i, v in enumerate(a)}
        mem = defaultdict(lambda : 2)
        res = 0
        for j in range(len(a)-2, 0, -1):
            for i in range(j-1, -1, -1):
                sv = a[i] + a[j]
                if sv in pos_d:
                    mem[(i,j)] = 1 + mem[(j, pos_d[sv])]
                    res = max(res, mem[(i,j)])
        return res

        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().lenLongestFibSubseq([1,2,3,4,5,6,7,8]).must_equal(5)
        Solution().lenLongestFibSubseq([1,3,7,11,12,14,18]).must_equal(3)
        Solution().lenLongestFibSubseq([1,2,5]).must_equal(0)
        Solution().lenLongestFibSubseq([1,2]).must_equal(0)
