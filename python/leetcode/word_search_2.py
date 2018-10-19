from collections import defaultdict
class TrieNode:
    def __init__(self):
        self.children = defaultdict(dict)
        self.word = None
    def add(self, word):
        cur = self
        for c in word:
            # print(c, cur.children)
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = word
        

class Solution:
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        if not board or not board[0]:
            return []
        trie = TrieNode()
        m, n = len(board), len(board[0])
        for w in words:
            trie.add(w)
        res = set()
        visited = set()
        dirs = [(1,0),(0,1),(-1,0),(0,-1)]
        def get_nexts(i,j):
            res = []
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                if ni >= 0 and ni < m and nj >=0 and nj < n and (ni,nj) not in visited:
                    res += (ni, nj),
            return res
        def dfs(node, i, j):
            if node.word:
                res.add(node.word)
            nexts = get_nexts(i,j)
            for ni, nj in nexts:
                if board[ni][nj] in node.children:
                    visited.add((ni,nj))
                    dfs(node.children[board[ni][nj]], ni, nj)
                    visited.discard((ni,nj))
            
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie.children:
                    visited.add((i,j))
                    dfs(trie.children[board[i][j]], i, j)
                    visited.discard((i,j))
        return list(res)
                    
if __name__ == '__main__':
    from minitest import *

    board = [
              ['o','a','a','n'],
              ['e','t','a','e'],
              ['i','h','k','r'],
              ['i','f','l','v']
            ]

    words = ["oath","pea","eat","rain"]

    with test(Solution):
        res = Solution().findWords(board, words)
        res.sort()
        res.must_equal(['eat', 'oath'])
