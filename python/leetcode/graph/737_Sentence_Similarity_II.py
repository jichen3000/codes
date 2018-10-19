class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        mem = {}
        pos_dict = {}
        if len(words1) != len(words2):
            return False
        for w1, w2 in pairs:
            if w1 not in mem and w2 not in mem:
                mem[w1] = len(mem)
                mem[w2] = mem[w1]
                pos_dict[mem[w1]] = {w1, w2}
            elif w1 in mem and w2 in mem:
                if mem[w1] != mem[w2]:
                    pre = mem[w2]
                    for w in pos_dict[mem[w2]]:
                        mem[w] = mem[w1]
                    pos_dict[mem[w1]] |= pos_dict[pre]
                    del pos_dict[pre]
                    # pos_dict.p()
            elif w1 in mem:
                mem[w2] = mem[w1]
                pos_dict[mem[w1]].add(w2)
            else:
                mem[w1] = mem[w2]
                pos_dict[mem[w2]].add(w1)
        # mem.pp()
        for i in range(len(words1)):
            w1, w2 = words1[i], words2[i]
            if w1 == w2: continue
            if w1 not in mem or w2 not in mem or mem[w1] != mem[w2]:
                return False
        return True

class Solution:
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        parents = {}
        def find(src):
            origin = src
            while src in parents:
                src = parents[src]
            # path compression
            if origin != src:
                parents[origin] = src
            return src
        def union(src, dst):
            parents[src] = dst

        if len(words1) != len(words2):
            return False
        for src, dst in pairs:
            src_parent = find(src)
            dst_parent = find(dst)
            if src_parent != dst_parent:
                union(src_parent, dst_parent)

        for w1, w2 in zip(words1, words2):
            if w1 == w2: continue
            if find(w1) != find(w2):
                return False
        return True


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().areSentencesSimilarTwo(["great","acting","skills"],
        #         ["fine","drama","talent"],
        #         [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]
        #         ).must_equal(True)
        Solution().areSentencesSimilarTwo(["this","summer","thomas","get","really","very","rich","and","have","any","actually","wonderful","and","good","truck","every","morning","he","drives","an","extraordinary","truck","around","the","nice","city","to","eat","some","extremely","extraordinary","food","as","his","meal","but","he","only","entertain","an","few","well","fruits","as","single","lunch","he","wants","to","eat","single","single","and","really","healthy","life"],
                ["this","summer","thomas","get","very","extremely","rich","and","possess","the","actually","great","and","wonderful","vehicle","every","morning","he","drives","unique","extraordinary","automobile","around","unique","fine","city","to","drink","single","extremely","nice","meal","as","his","super","but","he","only","entertain","a","few","extraordinary","food","as","some","brunch","he","wants","to","take","any","some","and","really","healthy","life"],
                [["good","nice"],["good","excellent"],["good","well"],["good","great"],["fine","nice"],["fine","excellent"],["fine","well"],["fine","great"],["wonderful","nice"],["wonderful","excellent"],["wonderful","well"],["wonderful","great"],["extraordinary","nice"],["extraordinary","excellent"],["extraordinary","well"],["extraordinary","great"],["one","a"],["one","an"],["one","unique"],["one","any"],["single","a"],["single","an"],["single","unique"],["single","any"],["the","a"],["the","an"],["the","unique"],["the","any"],["some","a"],["some","an"],["some","unique"],["some","any"],["car","vehicle"],["car","automobile"],["car","truck"],["auto","vehicle"],["auto","automobile"],["auto","truck"],["wagon","vehicle"],["wagon","automobile"],["wagon","truck"],["have","take"],["have","drink"],["eat","take"],["eat","drink"],["entertain","take"],["entertain","drink"],["meal","lunch"],["meal","dinner"],["meal","breakfast"],["meal","fruits"],["super","lunch"],["super","dinner"],["super","breakfast"],["super","fruits"],["food","lunch"],["food","dinner"],["food","breakfast"],["food","fruits"],["brunch","lunch"],["brunch","dinner"],["brunch","breakfast"],["brunch","fruits"],["own","have"],["own","possess"],["keep","have"],["keep","possess"],["very","super"],["very","actually"],["really","super"],["really","actually"],["extremely","super"],["extremely","actually"]]
                ).must_equal(True)


