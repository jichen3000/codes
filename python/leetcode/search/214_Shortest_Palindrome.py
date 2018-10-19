def is_p(s):
    n = len(s)
    for i in range(n/2):
        if s[i] != s[n-1-i]:
            return False
    return True
        
class Solution(object):
    # TLE 13mins
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if is_p(s): return s
        for i in range(len(s)-1,0,-1):
            # (i, s[:i]).p()
            if is_p(s[:i]):
                break
        # i.p()
        return s[i:][::-1] + s
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        if n == 0: return s
        dp = [[True] * n  for _ in range(n)]
        for l in range(1, n):
            for i in range(n-l):
                j = i + l
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] if l > 1 else True
                else:
                    dp[i][j] = False
        for j in range(n-1,-1,-1):
            if dp[0][j]:
                break
        return s[j+1:][::-1] + s

    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def longest_prefix(s):
            i, j, n = 1, 0, len(s)
            lp = [0] * n
            while i < n:
                if s[i] == s[j]:
                    j += 1
                    lp[i] = j
                    i += 1
                else:
                    if j > 0:
                        j = lp[j-1]
                    else:
                        i += 1
            return lp
        tmp = s + "#" + s[::-1]
        lp = longest_prefix(tmp)
        # lp.p()
        j = lp[-1]
        # (j, s[j+1:]).p()
        return s[j:][::-1] + s

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def get_lps(s):
            n = len(s)
            if n == 0: return [0]
            i, j = 0, 1
            lps = [0] * n
            while j < n:
                if s[i] == s[j]:
                    i+=1
                    lps[j] = i
                    j+=1
                else:
                    if i > 0:
                        i = lps[i-1]
                    else:
                        lps[j] = 0
                        j += 1
            return lps
        new_s = s + "+" + s[::-1]
        lps = get_lps(new_s)
        # print lps
        longest_p = lps[-1]
        return s[longest_p:][::-1] + s
        