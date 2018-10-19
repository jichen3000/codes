class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # from collections import defaultdict
        s = s.strip()
        allowed = set("0123456789.e+-")
        others = set(".e")
        if not s: return False
        if s[0] in set("+-"):
            s = s[1:]
        if not s: return False
        if s in others: return False
        if s[0] == "e" or s[-1]=="e": return False
        mem = {}
        for i,c in enumerate(s):
            if c not in allowed:
                return False
            if c == ".":
                if c in mem or "e" in mem:
                    return False
                mem[c] = i
            if c == "e":
                if c in mem or ("." in mem and mem["."]+1==i and mem["."] == 0):
                    return False
                mem[c] = i
            if c in set("+-"):
                if "e" not in mem or c in mem or i == len(s)-1:
                    return False
                mem[c] = i

        return True
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().isNumber(".e1").must_equal(False)
        Solution().isNumber("4e+").must_equal(False)
        Solution().isNumber("46.e3").must_equal(True)
        Solution().isNumber(".2e81").must_equal(True)
        Solution().isNumber(" 005047e+6").must_equal(True)
        Solution().isNumber("32.e-80123").must_equal(True)
