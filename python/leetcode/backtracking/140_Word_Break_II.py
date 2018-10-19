

class Solution(object):

    # TLE 90mins
    def wordBreak(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[str]
        """
        sn, wn = len(s), len(words)
        if wn == 0: return []
        dp = [[ [] for _ in range(wn)] for _ in range(sn)]
        for i in range(sn):
            for j in range(wn):
                cur_n = len(words[j])
                dp[i][j] = dp[i][j-1][:]
                if i+1 >= cur_n and words[j] == s[i+1-cur_n:i+1]:                    
                    if dp[i-cur_n][-1]:
                        dp[i][j] += [l+[words[j]] for l in dp[i-cur_n][-1]]
                    elif i+1-cur_n==0:
                        dp[i][j] += [words[j]],
                # (i,j,dp[i][j]).p()
                    
        # dp.p()
        return [" ".join(l) for l in dp[-1][-1]]

    def wordBreak(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[str]
        """
        sn, wn = len(s), len(words)
        if wn == 0: return []
        dp = [ [] for _ in range(sn)]
        for i in range(sn):
            for j in range(wn):
                cur_n = len(words[j])
                # (i,s[i+1-cur_n:i+1], j,words[j]).p()
                if i+1 >= cur_n and words[j] == s[i+1-cur_n:i+1]:                    
                    if dp[i-cur_n]:
                        dp[i] += [l+ (" " if l else "")+words[j] for l in dp[i-cur_n]]
                        # dp[i] += [l+[words[j]] for l in dp[i-cur_n]]
                    elif i+1-cur_n==0:
                        # dp[i] += [[words[j]]]
                        dp[i] += [words[j]]
            # (i,dp[i]).p()
        # dp.p()
        return dp[-1]

        
    def wordBreak(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[str]
        """
        sn, wn = len(s), len(words)
        if wn == 0: return []
        mem = {}
        def dfs(s):
            # s.p()
            if s in mem:
                return mem[s]
            results = []
            if len(s) == 0:
                results += "",
                return results
            for word in words:
                if s.startswith(word):
                    lefts = dfs(s[len(word):])
                    results += [word +(" " if l else "")+ l for l in lefts]
            mem[s] = results
            return results
        anw = dfs(s)
        # mem.p()
        return anw
    ## review
    def wordBreak(self, s, word_dict):
        """
        :type s: str
        :type word_dict: List[str]
        :rtype: List[str]
        """
        mem = {}
        def dfs(s):
            if s in mem:
                return mem[s]
            # if len(s) == 0: return []
            res = []
            for w in word_dict:
                if s.startswith(w):
                    if len(s[len(w):]) == 0:
                        res += w,
                    else:
                        res += [w + " " + l for l in dfs(s[len(w):])]                        
            mem[s] = res
            return res
        return dfs(s)                           
    def wordBreak(self, s, words):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        n = len(s)
        mem = {}
        def dfs(i):
            res = []
            if i in mem:
                return mem[i]
            if i == n:
                mem[i] = [""]
                return [""]
            for j in range(i+1, n+1):
                for w in words:
                    if w == s[i:j]:
                        res += [ w+(" "+l if l else "") for l in dfs(j)]
                        # (i,j,w, res).p()
            mem[i] = res
            return res
        
        return dfs(0)
                
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().wordBreak("catdog", ["cat", "cats", "dog"]).must_equal(
        #         ["cat dog"])
        # Solution().wordBreak("catdogs", ["cat", "cats", "and", "sand", "dog"]).must_equal(
        #         [])
        # Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]).must_equal(
        #         ['cats and dog', 'cat sand dog'])
        # Solution().wordBreak("a",[]).must_equal(
        #         [])
        # Solution().wordBreak("aaaaaaa",["aaaa","aa"]).must_equal(
        #         [])
        # Solution().wordBreak("aaaaaaa",["aaaa","aaa"]).must_equal(
        #         ['aaa aaaa', 'aaaa aaa'])
        # Solution().wordBreak("aaaaa",["a","aa","aaa","aaaa","aaaaa"])
        # Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaa",["a","aa","aaa","aaaa","aaaaa","aaaaaaa"])
        s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        words = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
        Solution().wordBreak(s, words).must_equal(
                [])
#         "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
# ["aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa","ba"]


