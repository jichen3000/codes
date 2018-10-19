def is_p(s):
    n = len(s)
    for i in range(n/2):
        if s[i] != s[n-1-i]:
            return False
    return True
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = len(s)
        for i in range(len(s)):
            for j in range(i):
                count += is_p(s[j:i+1])
        return count
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = len(s)
        n = len(s)
        dp = [[True] * n for _ in range(n)]
        for l in range(1,n):
            for i in range(n-l):
                j = i + l
                if s[i] == s[j]:
                    dp[i][j] = (dp[i+1][j-1] if l > 1 else True)
                    count += dp[i][j]
                else:
                    dp[i][j] = False
        return count  
    def countSubstrings(self, S):
        # I didn't see the detail of this one
        def manachers(S):
            A = '@#' + '#'.join(S) + '#$'
            Z = [0] * len(A)
            center = right = 0
            for i in xrange(1, len(A) - 1):
                if i < right:
                    Z[i] = min(right - i, Z[2 * center - i])
                while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                    Z[i] += 1
                if i + Z[i] > right:
                    center, right = i, i + Z[i]
            return Z

        return sum((v+1)/2 for v in manachers(S)) 
    # see manacher_for_palindrome.py
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        def manachers(s):
            origin_n = len(s)
            n = 2 * origin_n + 1
            lps_l = [0] * n
            lps_l[1] = 1
            right_i = 1
            center_i = 1
            right_border = 2
            max_lps_center_i = 1
            max_lps_len = 1

            for right_i in range(2, n):
                left_i = 2 * center_i - right_i
                diff = right_border - right_i
                if diff > 0:
                    # cannot beyond the right_border
                    lps_l[right_i] = min(lps_l[left_i], diff)

                while right_i + lps_l[right_i] < n and right_i > lps_l[right_i] and \
                        ( (right_i + lps_l[right_i] + 1) % 2 == 0 or \
                        ((right_i + lps_l[right_i] + 1)/2 < origin_n and \
                        s[(right_i + lps_l[right_i] + 1)/2] == s[(right_i - lps_l[right_i] - 1)/2]) ):
                    lps_l[right_i] += 1
                if max_lps_len < lps_l[right_i]:
                    max_lps_len = lps_l[right_i]
                    max_lps_center_i = right_i
                if right_i + lps_l[right_i] > right_border:
                    center_i = right_i
                    right_border = right_i + lps_l[right_i]
            return lps_l
        return sum((v+1)/2 for v in manachers(s))    

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().countSubstrings("abc").must_equal(3)
        Solution().countSubstrings("aba").must_equal(4)
        Solution().countSubstrings("ababa").must_equal(9)
        Solution().countSubstrings("abba").must_equal(6)
        Solution().countSubstrings("abaaba").must_equal(11)
        Solution().countSubstrings("aaa").must_equal(6)

