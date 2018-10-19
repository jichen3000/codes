class Solution:
    def ambiguousCoordinates(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        from itertools import product
        def get_possibles(s):
            sn = len(s)
            if sn == 1:
                return [s]
            res = []
            cur = int(s)
            if len(str(cur)) == sn:
                res += s,
            for i in range(sn-1):
                f = s[:i+1]+"."+s[i+1:]
                if f[:2] == "00":
                    break
                if f[-1] == "0":
                    break
                if f[0] == "0" and f[1] != ".":
                    break
                res += f,
            return res
        s = s[1:len(s)-1]
        res = []
        n = len(s)
        if n <= 1: return res
        for i in range(n-1):
            lefts = get_possibles(s[:i+1])
            rights = get_possibles(s[i+1:])
            # (lefts,rights).p()
            res += product(lefts, rights)
        return ["({0}, {1})".format(*t) for t in res]

if __name__ == '__main__':
    from minitest import *

    with test("Solution"):
        Solution().ambiguousCoordinates("(123)").must_equal(['(1, 23)', '(1, 2.3)', '(12, 3)', '(1.2, 3)'])
        Solution().ambiguousCoordinates("(00011)").must_equal(['(0, 0.011)', '(0.001, 1)'])
        Solution().ambiguousCoordinates("(0123)").must_equal(['(0, 123)', '(0, 1.23)', '(0, 12.3)', '(0.1, 23)', '(0.1, 2.3)', '(0.12, 3)'])
        Solution().ambiguousCoordinates("(100)").must_equal(['(10, 0)'])
        Solution().ambiguousCoordinates("(0000001)").must_equal(["(0, 0.00001)"])
        
