class Solution:
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        mem = {}
        def dfs(n, i):
            if n in mem:
                # n.p()
                return mem[n]
            res = [[n]]
            for j in range(i, n//2+1):
                l, r = divmod(n, j)
                if r == 0:
                    res += [[j] + ll for ll in dfs(l, j) if ll[0] >= j]
                if j > l:
                    break
            # (n,i,res).p()
            mem[n] = res
            return res
        res = dfs(n, 2)
        res.pop(0)
        # mem.p()
        return res




if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().getFactors(12).must_equal([[2, 6], [2, 2, 3], [3, 4]])
        Solution().getFactors(4).must_equal([[2, 2]])
        Solution().getFactors(8).must_equal([[2, 4], [2, 2, 2]])
        Solution().getFactors(32).must_equal([[2, 16], [2, 2, 8], [2, 2, 2, 4], [2, 2, 2, 2, 2], [2, 4, 4], [4, 8]])