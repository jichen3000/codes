class Solution(object):
    def wordBreak(self, s, word_dict):
        """
        :type s: str
        :type word_dict: List[str]
        :rtype: bool
        """
        n = len(s)
        if n == 0: return s in word_dict
        def dfs(start):
            if n == start: return True
            for i in range(start, n):
                if s[start:i+1] in word_dict:
                    if dfs(i+1):
                        return True
            return False
        return dfs(0)
    def wordBreak(self, s, word_dict):
        """
        :type s: str
        :type word_dict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [ [False] * n for _ in range(n)]    
        for l in xrange(n):
            for i in xrange(n-l):
                if s[i:i+l+1] in word_dict:
                    dp[i][i+l] = True
                else:
                    for k in range(i+1, i+l+1):
                        if dp[i][k-1] and dp[k][i+l]:
                            dp[i][i+l] = True
                            break
        return dp[0][-1]


class Solution(object):
    def wordBreak(self, s, word_dict):
        m = len(s)  
        n = len(word_dict)
        dp = [False] * m
        for i in range(m):
            for j in range(n):
                len_w = len(word_dict[j])
                # (i,j,s[i-len(w)+1:i+1],w,i-len(w)+1).p()
                if s[i-len_w+1:i+1] == word_dict[j]:
                    if i-len_w+1 == 0:
                        dp[i] = True
                        # dp[i][j].p()
                    elif i-len_w+1 > 0:
                        dp[i] = dp[i-len_w]
                # dp[i]
        # dp.pp()
        return dp[-1]    
    def wordBreak(self, s, word_dict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        result = [False] * len(s)
        for i in range(len(s)):
            for word in word_dict:
                # last part is the word, and first part should be true or this is the first word in s
                if s[i-len(word)+1:i+1] == word and (result[i-len(word)] or i-len(word)==-1):
                    result[i] = True
        return result[-1]

class Solution(object):
    def wordBreak(self, s, words):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True
        for i,c in enumerate(s):
            for w in words:
                wn = len(w)
                if wn <= i+1 and s[i+1-wn:i+1] == w:
                    # dp[i+1] = dp[i+1-wn]
                    # if dp[i+1]: break
                    dp[i+1] |= dp[i+1-wn]
        return dp[-1]            
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        s = "myword"
        word_dict = ["my","word"]
        Solution().wordBreak(s,word_dict).must_equal(True)
        word_dict = ["word","my"]
        Solution().wordBreak(s,word_dict).must_equal(True)
        word_dict = ["myword"]
        Solution().wordBreak(s,word_dict).must_equal(True)
        Solution().wordBreak("aaaaa",["aa","aaa"]).must_equal(True)
        Solution().wordBreak("aaaaaaa",["aaaa","aaa"]).must_equal(True)
