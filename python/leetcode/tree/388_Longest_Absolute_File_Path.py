class Solution:
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        res = 0
        q = []
        for c in input.split("\n"):
            l = c.count("\t")
            c = c[l:]
            while q and q[-1][0] >= l:
                q.pop()
            cur = q[-1][1] if q else 0
            cur += len(c) + (1 if q else 0)
            # print(l, c, cur)
            if "." in c:
                res = max(res, cur)
            q += (l, cur),
        return res
                


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext").must_equal(20)
        Solution().lengthLongestPath("a").must_equal(0)
