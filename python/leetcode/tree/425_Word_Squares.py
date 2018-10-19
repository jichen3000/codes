class Solution:
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        if not words: return []
        wn = len(words[0])
        if wn == 1: return [[w] for w in words]
        res = []  
        def dfs(cl):
            i = len(cl)
            if i == wn:
                res.append(cl)
                return
            prefix = "".join(w[i] for w in cl)
            for w in words:
                if w[:i] == prefix:
                    dfs(cl+[w])
        for w in words:
            dfs([w])
        return res        

from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.words = []

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        cur = self.root
        for c in word:
            cur = cur.children[c]
            cur.words += word,
        return self
    def get_nexts(self, word):
        cur = self.root
        for c in word:
            cur = cur.children[c]
        return cur.words

class Solution:
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        if not words: return []
        wn = len(words[0])
        if wn == 1: return [[w] for w in words]
        res = []
        trie = Trie()
        for w in words:
            trie.add(w)
        res = []  
        def dfs(cl):
            i = len(cl)
            if i == wn:
                res.append(cl)
                return
            prefix = "".join(w[i] for w in cl)
            for w in trie.get_nexts(prefix):
                dfs(cl+[w])
        for w in words:
            dfs([w])
        return res        


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().wordSquares(["a"]).must_equal(
            [["a"]])
        Solution().wordSquares(["ball","area","lead","lady"]).must_equal(
            [["ball","area","lead","lady"]])
        Solution().wordSquares(["area","lead","wall","lady","ball"]).must_equal(
            [['wall', 'area', 'lead', 'lady'], ['ball', 'area', 'lead', 'lady']])
        Solution().wordSquares(["abat","baba","atan","atal"]).must_equal(
            [['baba', 'abat', 'baba', 'atan'], ['baba', 'abat', 'baba', 'atal']])
