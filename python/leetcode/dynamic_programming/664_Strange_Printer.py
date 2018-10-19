# There is a strange printer with the following two special requirements:

# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from and ending at any places, and will cover the original existing characters.
# Given a string consists of lower English letters only, your job is to count the minimum number of turns the printer needed in order to print it.

# Example 1:
# Input: "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
# Example 2:
# Input: "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of the string, which will cover the existing character 'a'.
# Hint: Length of the given string will not exceed 100.

from collections import Counter
class Solution(object):

    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        # if s == "baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa":
        #     return 19
        ss = list(s)
        # len(s).p()
        for i in range(len(s)-1, 0, -1):
            if ss[i] == ss[i-1]:
                del ss[i]
        n = len(ss)
        # n.p()
        # "".join(ss).p()
        if n == 0: return 0
        dp = [ [n] * n for _ in range(n)]
        for l in range(0,n):
            for i in range(n-l):
                j = i + l
                # dp[i][j] = dp[i][j-1]
                dp[i][j] = dp[i][j-1]+1
                if l == 0:
                    dp[i][j] = 1
                elif l > 1:
                    klist = [k for k in range(i,j) if ss[k] == ss[j]]
                    if len(klist) > 0:
                        k = klist[0]
                        dp[i][j] = dp[i][k-1] if k > i else 0
                        k = klist[-1]
                        dp[i][j] += dp[k+1][j-1] + 1
                        for ki in range(len(klist)-1):
                            dp[i][j] += dp[klist[ki]+1][klist[ki+1]-1]

                    
        dp.p()
        return dp[0][-1]

    def strangePrinter(self, s):
        """
        :type s: str
        :rtype: int
        """
        ss = list(s)
        # len(s).p()
        for i in range(len(s)-1, 0, -1):
            if ss[i] == ss[i-1]:
                del ss[i]
        s = ss
        n = len(s)
        if n == 0: return 0
        dp = [[1] * n for _ in range(n)]
        for l in range(1,n):
            for i in range(n-l):
                j = i + l
                # dp[i][j] = l + 1
                dp[i][j] = min(dp[i][k] + dp[k+1][j] - 
                        (1 if s[k] == s[j] else 0) for k in range(i, j))
        return dp[0][-1]

# class Solution {
#     public int strangePrinter(String s) {
#         int n = s.length();
#         if (n == 0) return 0;
        
#         int[][] dp = new int[101][101];
#         for (int i = 0; i < n; i++) dp[i][i] = 1;
        
#         for (int i = 1; i < n; i++) {
#             for (int j = 0; j < n - i; j++) {
#                 dp[j][j + i] = i + 1;
#                 for (int k = j + 1; k <= j + i; k++) {
#                     int temp = dp[j][k - 1] + dp[k][j + i];
#                     if (s.charAt(k - 1) == s.charAt(j + i)) temp--;
#                     dp[j][j + i] = Math.min(dp[j][j + i], temp);
#                 }
#             }
#         }
#         return dp[0][n - 1];
#     }
# }

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().strangePrinter("aba").must_equal(2)
        # Solution().strangePrinter("abaca").must_equal(3)
        # Solution().strangePrinter("ababa").must_equal(3)
        # Solution().strangePrinter("hello").must_equal(4)
        # Solution().strangePrinter("leetcode").must_equal(6)
        # Solution().strangePrinter("aaabbb").must_equal(2)
        # Solution().strangePrinter("tbgtgb").must_equal(4)
        # Solution().strangePrinter("dddccbdbababaddcbcaabdbdddcccddbbaabddb").must_equal(15)
        Solution().strangePrinter('dcbdbababadcbcabdbdcdbabdb').must_equal(15)
        # Solution().strangePrinter("baacdddaaddaaaaccbddbcabdaabdbbcdcbbbacbddcabcaaa").must_equal(19)
