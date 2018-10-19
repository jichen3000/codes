class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter, defaultdict
        n = len(p)
        cc = Counter(p)
        mem, q, res = defaultdict(lambda : 0), [], []
        for i, c in enumerate(s):
            if c not in cc:
                mem, q = defaultdict(lambda : 0), []
            else:
                if mem[c] < cc[c]:
                    mem[c] += 1
                else:
                    while q[0] != c:
                        temp = q.pop(0)
                        mem[temp] -= 1
                    q.pop(0)
                q += c,
                if len(q) == n:
                    res += i + 1 - n,
        return res

    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        n = len(p)
        cc = Counter(p)
        mem, start, end, res = Counter(""), 0, 0, []
        for i, c in enumerate(s):
            if c not in cc:
                mem, start, end = Counter(""), i+1, i+1
            else:
                if mem[c] < cc[c]:
                    mem[c] += 1
                else:
                    while s[start] != c:
                        mem[s[start]] -= 1
                        start += 1
                    start += 1
                end += 1
                if end-start == n:
                    res += start,
        return res
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        # s += " "
        pn, sn = len(p), len(s)
        pc = Counter(p)
        mem, start, res = Counter(), 0, []
        for i, c in enumerate(s):
            if c not in pc:
                mem = Counter()
                start = i + 1
            else:
                if mem[c] >= pc[c]:
                    while s[start] != c:
                        mem[s[start]] -= 1
                        start += 1
                    start += 1
                else:
                    mem[c] += 1
                if i + 1 - start == pn:
                    res += start,
        return res
                
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        s += " "
        pn, sn = len(p), len(s)
        pc = Counter(p)
        mem, start, end, res = Counter(), 0, 0, []
        while end < sn:
            # print(mem[s[end]],pc[s[end]])
            while end < sn and s[end] in pc and mem[s[end]] < pc[s[end]]:
                mem[s[end]] += 1
                end += 1
            # (start,end).p()
            # print(end)
            if end - start == pn:
                res += start,
            if end == sn: break
            if s[end] not in pc: ## 2
                mem = Counter()
                start = end + 1
                while start < sn and s[start] not in pc:
                    mem[s[start]] -= 1
                    start += 1
                end = start
            else: ## 3
                while start < sn and s[start] != s[end]:
                    mem[s[start]] -= 1
                    start += 1
                start += 1
                end += 1
            # print(start, end, res)
        # (start, end).p()
        if end - start == pn and res[-1] != start:
            res += start,
        return res

    # figure out by myself
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        mem = Counter(p)
        i, j, count, res, pn = 0, 0, len(mem), [], len(p)
        while j < len(s):
            if j - i == pn:
                if s[i] in mem:
                    if mem[s[i]] == 0:
                        count += 1
                    mem[s[i]] += 1
                i += 1
            if s[j] in mem:
                mem[s[j]] -= 1
                if mem[s[j]] == 0:
                    count -= 1
                    # print(i,j,count, len(mem))
                    if count == 0:
                        res += i,
            j += 1
        return res
        
        
    # template, counter could be less than 0
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        # s += " "
        pn, sn = len(p), len(s)
        mem, start, end, res = Counter(p), 0, 0, []
        count = len(mem)
        while end < sn:
            c = s[end]
            if c in mem:
                mem[c] -= 1
                if mem[c] == 0: 
                    count -= 1
            end += 1
            while count == 0:
                sc = s[start]
                if sc in mem:
                    mem[sc] += 1
                    if mem[sc] > 0:
                        count += 1
                if end-start == pn:
                    res += start,
                start += 1
        return res

if __name__ == '__main__':
    from minitest import *

    with test("Solution"):
        Solution().findAnagrams("cbaebabacd","abc").must_equal([0,6])
        Solution().findAnagrams("aabaa","aa").must_equal([0,3])
        Solution().findAnagrams("abacbabc","abc").must_equal([1,2,3,5])



