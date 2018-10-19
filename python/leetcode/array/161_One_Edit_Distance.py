class Solution:
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            s, t = t, s
        def dfs(i, j, count):
            if i == len(s) and j == len(t):
                return count == 1
            if i == len(s):
                return count == 0 and j+1 == len(t)
            if s[i] != t[j]:
                if count > 0:
                    return False
                else:
                    if len(s) == len(t):
                        return dfs(i+1, j+1, 1)
                    else:
                        return dfs(i, j+1, 1)
            return dfs(i+1, j+1, count)
        return dfs(0,0,0)
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) > len(t):
            s, t = t, s
        i = j = count = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                if count > 0:
                    return False
                if len(s) == len(t):
                    i += 1
                    j += 1
                else:
                    j += 1
                count = 1
        if i == len(s) and j == len(t):
            return count == 1
        else:
            return count == 0 and j+1 == len(t)
            
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().isOneEditDistance("ab","acb").must_equal(True)