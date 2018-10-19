from collections import defaultdict
class WordDistance:

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.pos_dict = defaultdict(list)
        for i, w in enumerate(words):
            self.pos_dict[w] += i,
        

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        res = float("inf")
        i = j =0
        while i < len(self.pos_dict[word1]) and j < len(self.pos_dict[word2]):
            p1, p2 = self.pos_dict[word1][i], self.pos_dict[word2][j]
            if p1 > p2:
                res = min(res, p1 - p2)
                j += 1
            else:
                res = min(res, p2 - p1)
                i += 1
        return res
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)

# Assume that words = ["practice", "makes", "perfect", "coding", "makes"]