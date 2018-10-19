from collections import Counter
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        counter = Counter(t)
        mem = {key:[] for key in counter.keys()}
        n = len(s)
        min_i = n
        min_s = ""
        for i in range(n):
            c = s[i]
            if c in counter:
                mem[c] += i,
                if len(mem[c]) > counter[c]:
                    fi = mem[c].pop(0)
                    # (i,c,fi,mem).p()
                    if fi == min_i:
                        min_i = n
                        for l in mem.values():
                            if l:
                                min_i = min(min_i, l[0])
                    # min_i.p()
                # (counter, mem, all(len(mem[k])>=count for k, count in counter.items())).p()
                if min_i == n: min_i = i
                if all(len(mem[k])>=count for k, count in counter.items()):
                    cur_s = s[min_i:i+1]
                    if len(cur_s) < len(min_s) or min_s == "":
                        min_s = cur_s
        return min_s
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        n = len(s)
        start, left = n, 0
        l, t_count = n+1, len(t)
        counter = Counter(t)
        for i, c in enumerate(s):
            counter[c] -= 1
            if counter[c] >= 0: 
                t_count -= 1
            while t_count == 0:
                cur_l = i + 1 - left
                cur_c = s[left]
                if cur_l < l:
                    l = cur_l
                    start = left
                left += 1
                counter[cur_c] += 1
                if counter[cur_c] > 0:
                    t_count += 1
        # (start,l).p()
        return s[start:start+l]
                

## review
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        n = len(s)
        i, j = 0, None
        res = ""
        min_n = n+1
        tc = Counter(t)
        cur_c = Counter()
        # Counter(s).p()
        # tc.p()
        # (tc-Counter(s) ).p()
        while i < n:
            while i < n and s[i] not in tc:
                i += 1
            if i == n: break
            if not j: j = i
            while j < n and len(tc - cur_c) > 0:
                if s[j] in tc:
                    cur_c[s[j]] += 1
                j += 1
            if len(tc - cur_c) == 0 and j - i < min_n:
                min_n = j - i
                res = s[i:j]
            # (i,j, cur_c, res,s[i]).p()
            cur_c[s[i]] -= 1
            i += 1
        return res
                
        
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        n, tn = len(s), len(t)
        i, j = 0, None
        res = ""
        min_n = n+1
        tc = Counter(t)
        count = 0
        while i < n:
            while i < n and s[i] not in tc:
                i += 1
            if i == n: break
            if j==None: j = i
            while j < n and count < tn:
                if s[j] in tc:
                    tc[s[j]] -= 1
                    if tc[s[j]] >= 0:
                        count += 1
                j += 1
            if count == tn and j - i < min_n:
                min_n = j - i
                res = s[i:j]
            # (i,j, cur_c, res,s[i]).p()
            tc[s[i]] += 1
            if tc[s[i]] > 0:
                count -= 1
            i += 1
        return res

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        from collections import Counter
        mem = Counter(t)
        i, j, count, res = 0, 0, len(mem), None
        while j < len(s):
            if s[j] in mem:
                mem[s[j]] -= 1
                if mem[s[j]] == 0:
                    count -= 1
            j += 1
            while count == 0:
                if s[i] in mem:
                    if mem[s[i]] == 0:
                        count += 1
                    mem[s[i]] += 1
                if res == None or len(res) > j - i:
                    res = s[i:j]
                i += 1
        if res == None:
            return ""
        return res
        
if __name__ == '__main__':
    from minitest import *


    with test(Solution):
        Solution().minWindow("a","a").must_equal("a")
        Solution().minWindow("a","b").must_equal("")
        Solution().minWindow("ADOBECODEBANC","ABC").must_equal("BANC")
