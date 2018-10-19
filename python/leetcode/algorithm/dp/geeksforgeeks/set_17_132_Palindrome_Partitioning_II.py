class Solution(object):
    def minCut_complex_timeout(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        n.p()
        if n <= 1: return 0
        dp = [[0]*n for _ in xrange(n)]
        for l in xrange(1, n):
            for i in xrange(n-l):
                j = i + l 
                if l == 1:
                    if s[i] != s[j]:
                        dp[i][j] = 1
                else:
                    if s[i] == s[j] and dp[i+1][j-1]==0:
                        dp[i][j] = 0
                    else:
                        result = []
                        for k in xrange(i,j):
                            if s[k] == s[j] and dp[k+1][j-1] == 0:
                                if i == k:
                                    result += 0,
                                    break
                                else:
                                    result += dp[i][k-1] + 1,
                            else:
                                if i == k:
                                    result += dp[k][j-1] + 1,
                                else:
                                    result += dp[i][k-1] + dp[k][j-1] + 2,
                        dp[i][j] = min(result)
                    # (i,j,dp[i][j],result).p()
        # dp.pp()
        return dp[0][-1]
    def minCut_timeout(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        # n.p()
        if n <= 1: return 0
        dp = [[0]*n for _ in xrange(n)]
        for l in xrange(1, n):
            for i in xrange(n-l):
                j = i + l 
                if l == 1:
                    if s[i] != s[j]:
                        dp[i][j] = 1
                else:
                    if s[i] == s[j] and dp[i+1][j-1]==0:
                        dp[i][j] = 0
                    else:
                        dp[i][j] = min(dp[i][k] + 1 + dp[k+1][j] for k in xrange(i,j))
                    # (i,j,dp[i][j],result).p()
        # dp.pp()
        return dp[0][-1]

    # ababbbabb need to min cut 2
    # then aba b bbabb become all palidrome
    # use dp, left big section and right small section
    # just like cur rope
    # base case: no char, dp[0] = -1,
    #   only one char, dp[1] = 0,
    #   means no cut needed
    # induction rule:
    #   ab: i = 2
    #     case 1: j=0, left "", right ab, right is not palidrome, pass
    #     case 2: j=1, left a, right b, right is palidrome, dp[2] = dp[1] + 1
    #   aba: i = 3
    #     case 1: j=0, left "", right aba, dp[3] = dp[0] + 1 = 0
    #     case 2: j=1, left a, right ba, pass
    #     case 3: j=2, left ab, right a, dp[3] = dp[2] + 1 = 2
    #     get min of them
    #   so dp[i], means including at the position of before i, how many min cut
    #   loop j for 0 to i-1, if right section is palidrome, get the cuts,
    #   and get the min values from them.
    # time: O(n^3)
    # space: O(n)
    def minCut(self, s):
        n = len(s)
        dp = [n-1] * (n+1)
        dp[0] = -1
        def is_p(left, right):
            while (left < right):
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        for i in range(n+1):
            for j in range(i):
                if is_p(j, i-1):
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[-1]

    # improve by how to check palidrome
    # generate the palidrome array first
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        # just like cur words, but don't have dict
        # so 
        n = len(s)
        # n.p()
        if n <= 1: return 0
        p_dp = [[False]*n for _ in range(n)]
        for l in range(0, n):
            for i in range(n-l):
                j = i + l
                if l == 0:
                    p_dp[i][j] = True
                if l == 1 and s[i] == s[j]:
                    p_dp[i][j] = True
                if l>1 and s[i] == s[j] and p_dp[i+1][j-1]:
                        p_dp[i][j] = True 
        # p_dp.p() 
        dp = [n-1] * n
        for i in range(n):
            if p_dp[0][i]:
                dp[i] = 0
            else:
                for j in range(i):
                    if p_dp[j+1][i]:
                        dp[i] = min(dp[i],dp[j] + 1)
        # dp.p()
        return dp[-1]



if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().minCut("a").must_equal(0)
        # Solution().minCut("aab").must_equal(1)
        # Solution().minCut("cdd").must_equal(1)
        # Solution().minCut("efe").must_equal(0)
        # Solution().minCut("ababb").must_equal(1)
        # Solution().minCut("ababbbab").must_equal(1)
        # Solution().minCut("ababbbabb").must_equal(2)
        # Solution().minCut("ababbbabbababa").must_equal(3)
        s = "apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
        Solution().minCut(s).must_equal(452)
        pass
