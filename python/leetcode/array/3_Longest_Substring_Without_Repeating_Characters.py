class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1: return 0
        longest_set = s[0]
        start_i, max_l = 0, 1
        s += s[-1]
        for i, c in enumerate(s[1:]):
            if c in longest_set:
                if len(longest_set) > max_l:
                    max_l = len(longest_set)
                    start_i = i - max_l
                longest_set = longest_set[longest_set.index(c)+1:] + c
            else:
                longest_set += c
        return max_l
    # O(n)
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1: return 0
        poses = {}
        start_i, max_l = 0, 1
        for i, c in enumerate(s+s[-1]):
            if c in poses:
                new_start_i = poses[c] + 1
                max_l = max(len(poses), max_l)
                for j in range(start_i, poses[c]):
                    del poses[s[j]]
                start_i = new_start_i
            poses[c] = i
        return max_l
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 1: return 0
        poses = {}
        start_i, max_l = 0, 1
        for i, c in enumerate(s):
            if c in poses:
                start_i = max(start_i, poses[c]+1)
            max_l = max(max_l, i+1-start_i)
            poses[c] = i
        return max_l
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().lengthOfLongestSubstring("abcabcc").must_equal(3)