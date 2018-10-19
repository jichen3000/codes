class Solution:
    def wordPatternMatch(self, pattern, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        pn, sn = len(pattern), len(s)
        if pn > sn: return False
        mem = {}
        value_set = set()
        def dfs(i,j):
            # (i,j).p()
            if j == sn and i == pn:
                return True
            if j == sn or i == pn: return False
            key = pattern[i]
            if key in mem:
                # (i,j,key,mem[key],s[j:j+len(mem[key])]).p()
                if j+len(mem[key]) <= sn and mem[key] == s[j:j+len(mem[key])]:
                    return dfs(i+1, j+len(mem[key]))
                else:
                    return False
            for l in range(1, sn-j+1):
                if s[j:j+l] in value_set:
                    continue
                mem[key] = s[j:j+l]
                value_set.add(s[j:j+l])
                # (i,j,l,key,mem[key]).p()
                result = dfs(i+1, j+l)
                if result: return True
                value_set.discard(s[j:j+l])
            if key in mem: del mem[key]
            return False
        
        return dfs(0,0)

class Solution:
    def wordPatternMatch(self, p, s):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        mem = {}
        key_set = set()
        pn, sn = len(p), len(s)
        def dfs(i, j):
            if i == pn and j == sn:
                return True
            if i == pn or j == sn:
                return False
            if p[i] in mem:
                cur_n = len(mem[p[i]])
                if mem[p[i]] == s[j:j+cur_n]:
                    return dfs(i+1, j+cur_n)
                else:
                    return False
            mem[p[i]] = ""
            for jj in range(j+1, sn+1):
                if s[j:jj] in key_set:
                    continue
                mem[p[i]] = s[j:jj]
                key_set.add(s[j:jj])
                if dfs(i+1, jj):
                    return True
                key_set.discard(s[j:jj])
            del mem[p[i]]
            return False
        return dfs(0, 0)
            
        
        
if __name__ == '__main__':
    from minitest import *

    with test("Solution"):
        # Solution().wordPatternMatch("aa","ab").must_equal(False)
        Solution().wordPatternMatch("ab","aa").must_equal(False)
        # Solution().wordPatternMatch("abba","dogcatcatdog").must_equal(True)
        # Solution().wordPatternMatch("edcs","electronicengineeringcomputerscience").must_equal(True)
        # Solution().wordPatternMatch("ats","ataa").must_equal(True)
        