class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n < 1: return 0
        
        # start_i, max_l
        res = [0, 1]
        def extend(l, r):
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            if res[1] < r - 1 - l:
                res[1] = r - 1 - l
                res[0] = l+1
        for i in range(n-1):
            extend(i, i)
            extend(i, i+1)
        # print(res)
        start_i, max_l = res
        return s[start_i : start_i+max_l]




if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().longestPalindrome("babad").must_equal("bab")