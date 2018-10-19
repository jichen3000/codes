class Solution(object):
    # dp top to bottom, TLE, 40mins
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sn, pn = len(s), len(p)
        if pn == 0: return sn == 0
        if p == "*" * pn: return True
        if sn == 0: return pn == 0
        mem = {}
        def dp(i, j):
            if (i,j) in mem:
                return mem[(i,j)]
            if i == sn: 
                mem[(i,j)] =  p[j:] == "*" * (pn-j) or j == pn
                return mem[(i,j)]
            if j == pn: 
                mem[(i,j)] = False
                return mem[(i,j)]
            if s[i] == p[j] or p[j] == "?":
                mem[(i,j)] = dp(i+1, j+1)
                return mem[(i,j)]
            elif p[j] == "*":
                while j < pn and p[j] == "*":
                    j += 1
                if j == pn:
                    mem[(i,j)] = True
                    return mem[(i,j)]
                for k in range(sn-1, i-1, -1):
                    if (s[k] == p[j] or p[j] == "?") and dp(k, j):
                        mem[(i,j)] = True
                        return mem[(i,j)]
                mem[(i,j)] = False
                return mem[(i,j)]
            else: 
                mem[(i,j)] = False
                return mem[(i,j)]
        return dp(0,0)

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
                
        sn, pn = len(s), len(p)
        dp = [ [False] * (pn+1) for _ in range(sn+1)]
        dp[0][0] = True
        for j in range(1,pn+1):
            if p[j-1] == "*":
                dp[0][j] = True
            else:
                break

        for i in range(1, sn+1):
            for j in range(1, pn+1):
                if s[i-1] == p[j-1] or p[j-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i-1][j-1] or dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = False
        return dp[-1][-1]
    # http://yucoding.blogspot.com/2013/02/leetcode-question-123-wildcard-matching.html
    def isMatch(self, s, p):
        sn, pn = len(s), len(p)
        i, j = 0, 0
        match = 0;
        star = -1;
        while i<sn:
            if j< pn and (s[i]==p[j] or p[j]=='?'):
                i += 1
                j += 1
            elif j<pn and p[j]=='*':
                match = i
                star = j
                j += 1
            elif star > -1:
                j = star+1
                match += 1
                i = match
            else:
                return False
        while j<pn and p[j]=='*':
            j += 1
             
        return j == pn
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().isMatch("aa","a").must_equal(False)
        # Solution().isMatch("aa","aa").must_equal(True)
        # Solution().isMatch("aaa","aa").must_equal(False)
        # Solution().isMatch("aa", "*").must_equal(True)
        # Solution().isMatch("aa", "a*").must_equal(True)
        # Solution().isMatch("ab", "?*").must_equal(True)
        # Solution().isMatch("aab", "c*a*b").must_equal(False)
        # Solution().isMatch("aabc", "a*").must_equal(True)
        # Solution().isMatch("abca", "a*a").must_equal(True)
        # Solution().isMatch("aaaa", "***a").must_equal(True)
        # Solution().isMatch("c", "*?*").must_equal(True)
        # Solution().isMatch("ho", "ho**").must_equal(True)
        # Solution().isMatch("ho", "*ho").must_equal(True)
        # Solution().isMatch("hho", "h*ho").must_equal(True)
        # Solution().isMatch("ho", "**ho").must_equal(True)
        s = "abbaabbbbababaababababbabbbaaaabbbbaaabbbabaabbbbbabbbbabbabbaaabaaaabbbbbbaaabbabbbbababbbaaabbabbabb"
        p = "***b**a*a*b***b*a*b*bbb**baa*bba**b**bb***b*a*aab*a**"
        Solution().isMatch(s, p).must_equal(True)
        s = "ababbaaaaabbbbbabaabaaabaababbbaabbabbaabbbabaaababbaaaaabbbaabbbababbaabbaaaaabaaaaaabaaabaabbbbabbaabbbabbababbabbbabbabbaabbbbbabbaaaabaabababbaabbbaaaaabaabbaaaabaaaabbbaaabaabbbbabbabbaaabaabbbaabb"
        p = "ba**a***abb*bbab***aa**ba**aabbb*bb*aabab*****abb*b*ba*b*b*****aaa*abaa***b**b*a*b*abbb***bb*ab*baa*aaa*"
        Solution().isMatch(s, p).must_equal(False)
        s = "abababbbbabbbbbaabaabaabbbababbababbbabaaababaabbbbbbbabaaabaabbababbbbaaaabbabababbaaaaaabaabbaaabbbabbbbbaaaabaaaaaabababbbaababbaaabbaabaabbbbabbaaabbbbabbaaabaabbbbaabaabbbbbbbbbbaaabbbbbbababbbbbaab"
        p = "a*bba**abbba*bb*aa***ab*bbaa*b**aaab**baa*aa*b**bb**ba**b**aa**a**bb**b*ab*******b*bba******aba*ab**a"
        Solution().isMatch(s, p).must_equal(False)

