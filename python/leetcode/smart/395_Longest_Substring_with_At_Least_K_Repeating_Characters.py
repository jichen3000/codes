class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)
                
                
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().longestSubstring("mabaabb",3).must_equal(6)