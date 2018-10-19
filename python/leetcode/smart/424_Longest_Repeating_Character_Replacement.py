import collections
class Solution(object):
    def characterReplacement(self, s, k):
        lo = hi = 0
        if len(s) == 0:
            return 0
        counts = collections.Counter()
        for hi in range(0, len(s)):
            counts[s[hi]] += 1
            max_char_n = counts.most_common(1)[0][1]
            if hi - lo + 1 - max_char_n  > k:
                counts[s[lo]] -= 1
                lo += 1
        return hi - lo + 1


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().characterReplacement("ABC",1).must_equal(2)
        Solution().characterReplacement("AABABBA",1).must_equal(4)
        Solution().characterReplacement("AAABBABB",2
                ).must_equal(6)