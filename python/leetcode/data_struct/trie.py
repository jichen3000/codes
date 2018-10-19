# http://www.geeksforgeeks.org/trie-insert-and-search/
# 208. Implement Trie (Prefix Tree)
from collections import defaultdict
class TrieNode(object):
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_end_of_word = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()
    def insert(self, word):
        cur = self.root
        for c in word:
            cur = cur.children[c]
        # cur = cur.children[word[-1]]
        cur.is_end_of_word = True
        return self
    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]            
        return cur.is_end_of_word
    def startsWith(self, prefix):
        return self.starts_with(prefix)
    def starts_with(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]            
        return True

if __name__ == '__main__':
    from minitest import *

    with test(Trie):
        trie = Trie()
        trie.insert("colin").insert("ji").insert("li").insert("call")
        trie.search("niu").must_equal(False)
        trie.search("li").must_equal(True)
        trie.search("ca").must_equal(False)
        trie.starts_with("ca").must_equal(True)
        trie.starts_with("co").must_equal(True)
        trie.starts_with("cm").must_equal(False)
        trie.starts_with("calla").must_equal(False)

        trie = Trie()
        trie.insert("hello")
        trie.search("helloa").must_equal(False)
        trie.starts_with("helloa").must_equal(False)

        trie = Trie()
        trie.insert("aaaaaaaaaaaaaaaa")
        trie.insert("aaaaaaaaaaaaaaaabe")
        trie.search("a").must_equal(False)
        trie.starts_with("aa").must_equal(True)
