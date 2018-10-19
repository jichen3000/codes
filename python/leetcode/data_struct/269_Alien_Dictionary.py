class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # from collections import defaultdict
        relations = {}
        next_counts = {}
        for w in words:
            for c in w:
                relations[c] = set()
                next_counts[c] = 0
        pre_i = 0
        for i in range(1, len(words)):
            w1, w2 = words[pre_i], words[i]
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    # print(w1[j],w2[j])
                    if w2[j] not in relations[w1[j]]:
                        relations[w1[j]].add(w2[j])
                        next_counts[w2[j]] += 1
                    break
            pre_i = i
        cur_set = {c for c in relations.keys() if next_counts[c] == 0}
        res = ""
        # print(relations)
        # print(next_counts)
        while cur_set:
            # print(cur_set)
            temp_set = set()
            for c in cur_set:
                res += c
                for nc in relations[c]:
                    next_counts[nc] -= 1
                    if next_counts[nc] == 0:
                        temp_set.add(nc)
            cur_set = temp_set
        # print(res)
        if len(res) != len(relations):
            return ""
        return res
        
if __name__ == '__main__':
    from minitest import *

    with test("Solution"):
        Solution().alienOrder(["wrt","wrf","er","ett","rftt","te"]).must_equal(
                "wertf")
        Solution().alienOrder(["za","zb","ca","cb"]).must_equal(
                'azbc')
