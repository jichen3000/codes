class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter
        mem = Counter()
        count = 0
        start, end = 0, 0
        res = 0
        while end < len(s):
            c = s[end]
            mem[c] += 1
            if mem[c] == 1:
                count += 1
            end += 1
            while count > 2:
                sc = s[start]
                mem[sc] -= 1
                if mem[sc] == 0:
                    count -= 1
                start += 1
            res = max(res, end-start)
        return res
        