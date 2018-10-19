class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def generate_pattern_list(p):
            ps = []
            cur_s = ""
            for i in range(len(p)):
                if p[i] == ".":
                    if cur_s: ps += cur_s,
                    cur_s = ""
                    ps += ".",
                elif p[i] == "*":
                    # (cur_s,ps).p()
                    if cur_s: 
                        if cur_s[:-1]: ps += cur_s[:-1],
                        ps += cur_s[-1]+"*",
                    else:
                        ps[-1] += "*"
                    cur_s = ""
                else:
                    cur_s += p[i]
            if cur_s:
                ps += cur_s,
            return ps

        if p == ".*":
            return True
        p += "#"
        s += "#"
        n = len(s)

        ps = generate_pattern_list(p)
        # ps.p()
        m = len(ps)
        i, j = 0, 0
        def match_star_q(start, end, star_q):
            # (start, end, star_q).p()
            i, j = start, 0
            while i < end and j < len(star_q):
                while i < end and s[i] == star_q[j][0]:
                    i += 1
                j += 1
            return i == end

        def dfs(i, j):
            star_q = []
            while i < n:
                # (i,s[i],j,ps[j],star_q).p()
                if ps[j] == ".*":
                    # the previouse p in star_q will skip
                    # remove the after ps which has "*"
                    # j.p()
                    while j < m and ps[j][-1] == "*":
                        j += 1
                    match_l = []
                    if ps[j] == ".":
                        while i < n-1:
                            i += 1
                            match_l += i,
                    else:
                        while i < n:
                            if s[i:i+len(ps[j])] == ps[j]:
                                match_l += i+len(ps[j]),
                            i += 1
                    # (i,s,j,match_l).p()
                    return any(dfs(ni, j+1) for ni in reversed(match_l))

                elif ps[j][-1] == "*":
                    star_q += ps[j],
                    j += 1
                elif ps[j] == ".":
                    if len(star_q) == 0:
                        i += 1
                        j += 1
                    else:
                        ni = i
                        match_l = []
                        # (i, ni, star_q).p()
                        # match_star_q(i, ni, star_q).p()
                        while ni < n and match_star_q(i, ni, star_q):
                            match_l += ni,
                            ni += 1
                        return any(dfs(ni, j) for ni in reversed(match_l))


                else:
                    # (i,j,ps, star_q).p()
                    if s[i:i+len(ps[j])] == ps[j]:
                        if len(ps[j]) == 1 and (ps[j] + "*") in star_q:
                            match_l = []
                            while i < n and s[i:i+len(ps[j])] == ps[j]:
                                i += 1
                                match_l += i,
                            return any(dfs(ni, j+1) for ni in reversed(match_l))
                        else:
                            star_q = []
                            i += len(ps[j])
                            j += 1
                    else:
                        if len(star_q) == 0:
                            return False
                        ni = i + 1
                        while ni < n and s[ni:ni+len(ps[j])] != ps[j]:
                            ni += 1
                        if ni == n: return False
                        # match_star_q(i, ni, star_q).p()
                        if match_star_q(i, ni, star_q) == False:
                            return False
                        star_q = []
                        i = ni
                # (i,j,ps).p()
                if j >= m:
                    if i == n:
                        return True
                    return False
            
            return all(c[-1] == "*" for c in ps[j:]) 
        return dfs(0,0)

    # TLE
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # (s,p).p()
        n, m = len(s), len(p)
        if m == 0:
            return n == 0
        if m == 1:
            return n == 1 and (p[0] == "." or s[0] == p[0])
        if p[1] != "*":
            if n == 0: return False
            if p[0] != "." and p[0] != s[0]: 
                return False
            else:
                return self.isMatch(s[1:], p[1:])
        else:
            if p[0] == ".":
                return any(self.isMatch(s[i:], p[2:]) for i in reversed(range(n+1)))
            else:
                match_l = [0]
                for i in range(n):
                    if s[i] == p[0]:
                        match_l += i+1,
                    else:
                        break
                # match_l.p()
                # if len(match_l)==0: match_l = [0]
                return any(self.isMatch(s[i:], p[2:]) for i in reversed(match_l))

    # http://www.cnblogs.com/grandyang/p/4461713.html method 1
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # (s,p).p()
        n, m = len(s), len(p)
        if m == 0:
            return n == 0
        if m == 1:
            return n == 1 and (s[0] == p[0] or p[0]==".")
        if p[1] != "*":
            if n == 0: return False
            return (s[0] == p[0] or p[0]==".") and self.isMatch(s[1:], p[1:])
        while s and (s[0] == p[0] or p[0]=="."):
            if self.isMatch(s, p[2:]): return True
            s = s[1:]
        return self.isMatch(s, p[2:])
        
    # http://www.cnblogs.com/grandyang/p/4461713.html method 2
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # (s,p).p()
        n, m = len(s), len(p)
        if m == 0:
            return n == 0
        if m > 1 and p[1] == "*":
            return self.isMatch(s, p[2:]) or ( n>0 and (s[0] == p[0] or p[0]==".") and self.isMatch(s[1:], p))
        else:
            return  (n>0 and (s[0] == p[0] or p[0]==".") and self.isMatch(s[1:], p[1:]))
        
    # http://www.cnblogs.com/grandyang/p/4461713.html method dp
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        # (s,p).p()
        n, m = len(s), len(p)
        dp = [[False] * (m+1) for _ in range(n+1)]
        dp[0][0] = True
        for i in range(n+1):
            for j in range(1,m+1):
                if p[j-1] == "*" and j > 1:
                    # dp[i][j] = dp[i][j-2] or (i > 0 and (s[i-1]==p[j-2] or p[j-2] == ".")
                    #         and dp[i-1][j])
                    if i > 0 and (s[i-1]==p[j-2] or p[j-2] == "."):
                        dp[i][j] = dp[i-1][j] or dp[i][j-2]
                    else:
                        dp[i][j] = dp[i][j-2]
                else:
                    # dp[i][j] = (dp[i-1][j-1] and i > 0 and (s[i-1]==p[j-1] or p[j-1] == "."))
                    # (i,j, (s[i-1]==p[j-1] or p[j-1] == ".")).p()
                    if i > 0 and (s[i-1]==p[j-1] or p[j-1] == "."):
                        dp[i][j] = dp[i-1][j-1]
                    else:
                        dp[i][j] = False
        # dp.p()
        return dp[-1][-1]

## review, more clear for me, but the dp is the fastest
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def dfs(s, p):
            # (s,p).p()
            if p == "": return s == ""
            sn, pn = len(s), len(p)
            i, j = sn-1, pn-1
            while j >= 0:
                # (i,j).p()
                if p[j] == "*":
                    if p[j-1] == ".":
                        sames = xrange(i+1, -1, -1)
                    else:
                        sames = [i+1]
                        while i >= 0 and s[i] == p[j-1]:
                            sames += i,
                            i -= 1
                    return any(dfs(s[:k], p[:j-1]) for k in sames)
                elif i >=0 and (p[j] == "." or s[i] == p[j]):
                    i -= 1
                    j -= 1
                else:
                    return False
            return i == -1 and j == -1
        return dfs(s, p)        
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sn, pn = len(s), len(p)
        dp = [[False] * (pn+1) for _ in range(sn+1)]
        dp[0][0] = True
        for i in range(sn+1):
            for j in range(1, pn+1):
                if p[j-1] == "*":
                    if p[j-2] == ".":
                        sames = range(i, -1, -1)
                    else:
                        sames = [i]
                        k = i - 1
                        while k >= 0 and s[k] == p[j-2]:
                            sames += k,
                            k -= 1
                    dp[i][j] = any(dp[k][j-2] for k in sames)
                elif i > 0 and (p[j-1] == "." or p[j-1] == s[i-1]):
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        sn, pn = len(s), len(p)
        dp = [[False] * (pn+1) for _ in range(sn+1)]
        dp[0][0] = True
        for i in range(sn+1):
            for j in range(1, pn+1):
                if p[j-1] == "*":
                    if i > 0 and (p[j-2] == "." or p[j-2] == s[i-1]):
                        dp[i][j] = dp[i][j-2] or dp[i-1][j]
                    else:
                        dp[i][j] = dp[i][j-2]
                elif i > 0 and (p[j-1] == "." or p[j-1] == s[i-1]):
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]
                
if __name__ == '__main__':
    from minitest import *

    with test(Solution):

        Solution().isMatch("aa","aa").must_equal(True)
        Solution().isMatch("aaa","aa").must_equal(False)
        Solution().isMatch("aa", "a*").must_equal(True)
        Solution().isMatch("aab", "c*a*b").must_equal(True)
        Solution().isMatch("aa", ".*").must_equal(True)
        Solution().isMatch("ab", ".*").must_equal(True)
        Solution().isMatch("ab", "a.*b").must_equal(True)
        Solution().isMatch("a", ".*..a*").must_equal(False)
        Solution().isMatch("a", ".*..").must_equal(False)
        Solution().isMatch("ab", ".*..").must_equal(True)
        Solution().isMatch("abbbaabccbaabacab", "ab*b*b*bc*ac*.*bb*").must_equal(True)
        Solution().isMatch("abbcbb", "ab*a*..b*").must_equal(True)
        Solution().isMatch("abcbccbcbaabbcbb", "c*a.*ab*.*ab*a*..b*").must_equal(True)
        Solution().isMatch("a", "c*.").must_equal(True)
        Solution().isMatch("ab", ".*c").must_equal(False)




