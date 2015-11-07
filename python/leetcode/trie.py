class TrieNode(object):
    def __init__(self, value):
        self.children = []
        self.keys = []
        self.value = value
        self.is_word_end = False


    def insert(self, word):
        # if len(word) == 0:
        #     return self
        first_c = word[0]
        index = None
        if first_c in self.keys:
            index = self.keys.index(first_c)
        else:
            self.keys.append(first_c)
            self.children.append(TrieNode(first_c))
            index = -1
        if len(word) == 1:
            self.is_word_end = True
        else:
            self.children[index].insert(word[1:])
        return self

    def starts_with(self, word):
        if len(word) == 0:
            return True
        first_c = word[0]
        if first_c in self.keys:
            index = self.keys.index(first_c)
            return self.children[index].starts_with(word[1:])
        else:
            return False

    def search(self, word):
        if len(word) == 0:
            return False
        first_c = word[0]
        if first_c in self.keys:
            index = self.keys.index(first_c)
            if len(word) == 1:
                return self.is_word_end
            else:
                return self.children[index].search(word[1:])
        else:
            return False

    def to_breadth_first_list(self):
        stack = [self]
        result = []
        while len(stack) > 0:
            cur = stack.pop(0)
            result.append(cur)
            stack += cur.children
        return result

    def to_depth_first_list(self):
        stack = [self]
        result = []
        while len(stack) > 0:
            cur = stack.pop()
            result.append(cur)
            stack += cur.children[::-1]
        return result

    def __repr__(self):
        return "'{0}'".format(self.value)

    def __str__(self):
        return self.value

    def __eq__(self, other):
        return str(self) == str(other)

class Trie(object):
    def __init__(self):
        self.root = TrieNode("")

    @classmethod
    def create(klass, words):
        trie = klass()
        map(trie.insert, words)
        return trie
    # @param {string} word
    # @return {void}
    # Inserts a word into the trie.
    def insert(self, word):
        self.root.insert(word)
        return self


    # @param {string} word
    # @return {boolean}
    # Returns if the word is in the trie.
    def search(self, word):
        return self.root.search(word)
        

    # @param {string} prefix
    # @return {boolean}
    # Returns if there is any word in the trie
    # that starts with the given prefix.
    def starts_with(self, prefix):
        return self.root.starts_with(prefix)

    def to_breadth_first_list(self):
        return self.root.to_breadth_first_list()
    def to_depth_first_list(self):
        return self.root.to_depth_first_list()


if __name__ == '__main__':
    from minitest import *

    with test(Trie):
        trie = Trie()
        trie.insert("colin").insert("ji").insert("li").insert("call")
        trie.search("niu").must_false()
        trie.search("li").must_true()
        trie.search("ca").must_false()
        trie.starts_with("ca").must_true()

        trie.to_breadth_first_list().must_equal(
                ['', 'c', 'j', 'l', 'o', 'a', 'i', 'i', 
                 'l', 'l', 'i', 'l', 'n'])
        trie.to_depth_first_list().must_equal(
                ['', 'c', 'o', 'l', 'i', 'n', 'a', 'l', 
                 'l', 'j', 'i', 'l', 'i'])

        new_trie = Trie.create(["colin","ji","li","call"])
        new_trie.to_depth_first_list().must_equal(
                trie.to_depth_first_list())
        pass