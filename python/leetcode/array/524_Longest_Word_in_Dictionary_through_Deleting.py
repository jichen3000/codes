class Solution:
    def findLongestWord(self, s, words):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        res = ""
        def check(word):
            pre = 0
            for c in word:
                if c not in s[pre:]:
                    return False
                pre = s[pre:].index(c) + pre + 1
            return True
        for w in words:
            # (w, check(w), res).p()
            if check(w) and (len(w) > len(res) or (len(w) == len(res) and w < res)):
                res = w
        return res

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().findLongestWord("abpcplea",
                ["ale","apple","monkey","plea"]).must_equal("apple")
        Solution().findLongestWord("abpcplea",
                ["mm"]).must_equal("")
        Solution().findLongestWord("abpcplea",
                ["a","b"]).must_equal("a")
