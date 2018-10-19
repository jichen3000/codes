
class Solution(object):
    # TLE, sometimes, the top down dp is more efficient
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        sn = len(s)
        tn = len(t)
        if tn == 0: return sn
        positions = {}
        for ti in range(tn):
            if t[ti] not in positions:
                positions[t[ti]] = []
            else:
                continue
            for si in range(sn):
                if s[si] == t[ti]:
                    positions[t[ti]] += si,
            if len(positions[t[ti]]) == 0:
                return 0
        # positions.pp()
        dp = [[0]* sn for _ in range(tn)]
        for i in range(tn):
            for j in range(i, sn):
                if i == j:
                    dp[i][j] = 1 if s[:i+1] == t[:j+1] else 0
                else:
                    equals = [k for k in positions[t[i]] if k <=j and k >= 0]
                    # (i,j,t[i],equals).p()
                    if i == 0:
                        dp[i][j] = len(equals)
                    else:
                        dp[i][j] = sum(dp[i-1][k-1] if k > 0 else 0 for k in equals)
        # dp.pp()
        return dp[-1][-1]
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        sn = len(s)
        tn = len(t)
        positions = {}
        for ti in range(tn):
            if t[ti] not in positions:
                positions[t[ti]] = []
            else:
                continue
            for si in range(sn):
                if s[si] == t[ti]:
                    positions[t[ti]] += si,
            if len(positions[t[ti]]) == 0:
                return 0
        # positions.pp()
        mem = {}
        def dfs(si,ti):
            if (si,ti) in mem:
                return mem[(si,ti)]
            left_s = sn - si
            left_t = tn - ti
            # (si,ti, left_s, left_t ).p()
            if ti == tn: 
                mem[(si,ti)] = 1
                return 1
            if left_s < left_t: 
                mem[(si,ti)] = 0
                return 0
            if left_s == left_t:
                if s[si:] == t[ti:]:
                    mem[(si,ti)] = 1
                    return 1
                else:
                    mem[(si,ti)] = 0
                    return 0
            next_moves = [i for i in positions[t[ti]] if i >=si]
            # next_moves.p()
            mem[(si,ti)] = sum(dfs(nsi+1, ti+1) for nsi in next_moves)
            return mem[(si,ti)]
        return dfs(0,0)

               
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().numDistinct("c","").must_equal(1)
        # Solution().numDistinct("BCC","CB").must_equal(0)
        # Solution().numDistinct("ABCDE","ACE").must_equal(1)
        # Solution().numDistinct("ABCDE","AEC").must_equal(0)
        # Solution().numDistinct("rabbbit","rabbit").must_equal(3)
        # Solution().numDistinct("ccc","c").must_equal(3)
        s = "aabdbaabeeadcbbdedacbbeecbabebaeeecaeabaedadcbdbcdaabebdadbbaeabdadeaabbabbecebbebcaddaacccebeaeedababedeacdeaaaeeaecbe"
        t = "bddabdcae"
        Solution().numDistinct(s,t).must_equal(10582116)
