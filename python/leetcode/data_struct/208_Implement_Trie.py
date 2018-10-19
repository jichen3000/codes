class Node(object):
    def __init__(self):
        self.children = {}
        self.is_word = False
        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = Node()
            cur = cur.children[c]
        cur.is_word = True
        return self
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return cur.is_word
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        return True
    def starts_with(self, prefix):
        return self.startsWith(prefix)
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
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

