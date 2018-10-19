class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        from collections import Counter
        if len(words) < 1: return []
        wn = len(words[0])
        if any(len(w) != wn for w in words): return []
        all_len = wn * len(words)
        res = []
        for i in range(wn):
            mem = Counter(words)
            start, end, count = i, i, len(mem)
            while end < len(s):
                w = s[end:end+wn]
                if w in mem:
                    mem[w] -= 1
                    if mem[w] == 0:
                        count -= 1
                end += wn
                while count == 0:
                    sw = s[start:start+wn]
                    if sw in mem:
                        mem[sw] += 1
                        if mem[sw] > 0:
                            count += 1
                    if end - start == all_len:
                        res += start,
                    start += wn
                
        return res
        