from collections import defaultdict
class Node:
    def __init__(self):
        self.children = defaultdict(Node)
        self.tops = []
    def search(self, c):
        if c in self.children:
            return self.children[c]
        else:
            return None
    def set_tops(self, sentence, count):
        # find
        for i in range(len(self.tops)):
            if self.tops[i][1] == sentence:
                self.tops[i][0] = -count
                break
        else:
            self.tops += [-count, sentence],
        self.tops.sort()
        if len(self.tops) > 3:
            self.tops.pop()
        
class Trie:
    def __init__(self):
        self.root = Node()
        
    def insert(self, sentence, count):
        cur = self.root
        for c in sentence:
            cur = cur.children[c]
            cur.set_tops(sentence, count)
            

class AutocompleteSystem:

    def __init__(self, sentences, times):
        """
        :type sentences: List[str]
        :type times: List[int]
        """
        self.trie = Trie()
        self.mem = defaultdict(lambda : 0)
        for i in range(len(sentences)):
            self.trie.insert(sentences[i], times[i])
            self.mem[sentences[i]] = times[i]
        self.cur_s = ""
        self.cur_node = self.trie.root
        

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        res = []
        if c == "#":
            self.mem[self.cur_s] += 1
            self.trie.insert(self.cur_s, self.mem[self.cur_s])
            self.cur_s = ""
            self.cur_node = self.trie.root
        else:
            self.cur_s += c
            if self.cur_node:
                self.cur_node = self.cur_node.search(c)
                if self.cur_node:
                    res = self.cur_node.tops
        return [i[1] for i in res]
            
            
            
        


# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)