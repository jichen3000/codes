class Solution:
    def letterCasePermutation(self, s):
        """
        :type S: str
        :rtype: List[str]
        """
        if not s: return [s]
        n = len(s)
        def dfs(i):
            print(i)
            if i == n:
                return [""]
            for j in range(i, n):
                if s[j].isalpha():
                    return [s[i:j] + m + ss 
                            for ss in dfs(j+1)
                           for m in (s[j].lower(), s[j].upper())]
            return [s[i:]]
        return dfs(0)
    def letterCasePermutation(self, s):
        """
        :type S: str
        :rtype: List[str]
        """
        # if not s: return [s]
        n = len(s)
        res, j = [""], n
        for i in range(n-1,-1,-1):
            if s[i].isalpha():
                res = [sc + s[i+1:j] + ss for ss in res for sc in (s[i].lower(), s[i].upper())]
                j = i
        if j > 0:
            res = [s[:j] + ss for ss in res]
        return res

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().letterCasePermutation("a1b2").must_equal(['a1b2', 'A1b2', 'a1B2', 'A1B2'])
        Solution().letterCasePermutation("3z4").must_equal(['3z4', '3Z4'])
        Solution().letterCasePermutation("12345").must_equal(['12345'])
        Solution().letterCasePermutation("").must_equal([''])

