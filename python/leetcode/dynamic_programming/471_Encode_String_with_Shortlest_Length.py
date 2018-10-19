class Solution:
    def encode(self, s):
        """
        :type s: str
        :rtype: str
        """        
        if not s or len(s) < 5:
            return s
        n = len(s)
        dp = [[None] * n for _ in range(n)]
        for l in range(n):
            for i in range(n-l):
                j = i + l
                cur = s[i:j+1]
                if l < 4:
                    dp[i][j] = cur
                    continue
                dp[i][j] = cur
                for k in range(i, j):
                    if len(dp[i][j]) > len(dp[i][k]+dp[k+1][j]):
                        dp[i][j] = dp[i][k]+dp[k+1][j]
                # check cur can be encode
                for k in range(len(cur)):
                    sub = cur[:k+1]
                    if len(cur) % len(sub) == 0 and len(cur.replace(sub, "")) == 0:
                        # using dp[i][i+k] not sub, is the key
                        en_s = str(len(cur) // len(sub)) + "["+ dp[i][i+k] +"]"
                        if len(en_s) < len(dp[i][j]):
                            dp[i][j] = en_s
        return dp[0][-1]


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().encode("aaa").must_equal("aaa")
        Solution().encode("aaaaa").must_equal("5[a]")
        Solution().encode("a"*10).must_equal("a9[a]")
        Solution().encode("mnabcdabcd").must_equal("mn2[abcd]")
        Solution().encode("abbbabbbc").must_equal("2[abbb]c")
        Solution().encode("abbbabbbcabbbabbbc").must_equal('2[2[abbb]c]')

