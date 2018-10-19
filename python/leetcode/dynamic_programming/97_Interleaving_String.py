class Solution(object):
    # TLE 
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3: return False
        # i1,i2,i3 = 0, 0, 0
        def inner(i1, i2, i3):
            while i1 < n1 and i2 < n2:
                if s3[i3] == s1[i1] and s3[i3] == s2[i2]:
                    return inner(i1+1, i2, i3+1) or inner(i1, i2+1, i3+1)
                elif s3[i3] != s1[i1] and s3[i3] != s2[i2]:
                    return False
                elif s3[i3] == s1[i1]:
                    i3 += 1
                    i1 += 1
                elif s3[i3] == s2[i2]:
                    i3 += 1
                    i2 += 1
            if i1 == n1:
                return s2[i2:] == s3[i3:]
            if i2 == n2:
                return s1[i1:] == s3[i3:]
        return inner(0, 0, 0)
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3: return False
        dp = [[False] * (n2+1) for _ in range(n1+1)]
        for i in range(n1+1):
            dp[i][0] = (s3[:i] == s1[:i])
        for i in range(n2+1):
            dp[0][i] = (s3[:i] == s2[:i])

        for i1 in range(n1):
            for i2 in range(n2):
                i3 = i1 + i2 + 1
                if s3[i3] == s1[i1] and s3[i3] == s2[i2]:
                    dp[i1+1][i2+1] = dp[i1][i2+1] or dp[i1+1][i2]
                elif s3[i3] != s1[i1] and s3[i3] != s2[i2]:
                    dp[i1+1][i2+1] = False
                elif s3[i3] == s1[i1]:
                    dp[i1+1][i2+1] = dp[i1][i2+1]
                elif s3[i3] == s2[i2]:
                    dp[i1+1][i2+1] = dp[i1+1][i2]
        # dp.p()
        return dp[-1][-1]

if __name__ == '__main__':
    from minitest import *


    with test(Solution):
        Solution().isInterleave('ba','bc','babc').must_equal(True)
        Solution().isInterleave('ba','bc','bbac').must_equal(True)
        Solution().isInterleave('ba','ba','babc').must_equal(False)
        Solution().isInterleave('ba','baa','babc').must_equal(False)
        Solution().isInterleave('acc','bccb','abccccb').must_equal(True)
        Solution().isInterleave('acc','bccb','abccbcc').must_equal(True)
        Solution().isInterleave('aabcc','dbbca','aadbbcbcac').must_equal(True)
        Solution().isInterleave('aabcc','dbbca','aadbbbaccc').must_equal(False)
        Solution().isInterleave('aa','ab','aaba').must_equal(True)
        Solution().isInterleave('aa','ba','abaa').must_equal(True)
        Solution().isInterleave("aabc","abad","aabaabdc").must_equal(True)
        Solution().isInterleave("aabc","abad","aabcabad").must_equal(True)
