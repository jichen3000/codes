class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == "0" or "00" in s: return 0
        cur, pre1, pre2 = 1, 1, 1
        for i in range(1, len(s)):
            if s[i] == "0":
                if i-1 >= 0 and int(s[i-1]) > 2:
                    return 0
                cur = pre1
            elif s[i-1]!="0" and int(s[i-1:i+1]) <= 26:
                if i + 1 < len(s) and s[i+1] == "0":
                    cur = pre1
                else:
                    cur = pre1 + pre2
            else:
                cur = pre1
            pre1, pre2 = cur, pre1
        return cur
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().numDecodings("226").must_equal(3)
        Solution().numDecodings("00").must_equal(0)