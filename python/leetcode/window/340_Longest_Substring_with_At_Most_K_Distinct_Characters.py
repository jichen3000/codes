class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        from collections import defaultdict
        if k == 0: return 0
        res = i = j = 0
        count = k
        mem = defaultdict(lambda : 0)
        while j < len(s):
            mem[s[j]] += 1
            if mem[s[j]] == 1:
                count -= 1
            j += 1
            
            if count == 0:
                res = max(res, j-i)
                
            while count < 0 and i < j:
                mem[s[i]] -= 1
                if mem[s[i]] == 0:
                    count += 1
                i += 1
        if res == 0: return len(s)
        return res

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        mem = {}
        i, j, res, count = 0, 0, 0, k
        while j < len(s):
            if s[j] not in mem:
                mem[s[j]] = 1
                count -= 1
            else:
                mem[s[j]] += 1
            # print(i, j, count)
            
            j += 1
            if count >= 0:
                res = max(res, j-i)
            while count < 0:
                mem[s[i]] -= 1
                if mem[s[i]] == 0:
                    del mem[s[i]]
                    count += 1
                i += 1
        return res
            

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().lengthOfLongestSubstringKDistinct("eceba",2).must_equal(3)
        Solution().lengthOfLongestSubstringKDistinct("a",3).must_equal(1)
        Solution().lengthOfLongestSubstringKDistinct("a",0).must_equal(0)