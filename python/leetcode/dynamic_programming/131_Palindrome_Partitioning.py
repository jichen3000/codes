# matrix
def is_p(s):
    n = len(s)
    if n == 1:
        return True
    m = n / 2
    for i in xrange(m):
        if s[i] != s[n-1-i]:
            return False
    return True

class Solution(object):
    # it work
    def partition_r(self, s):
        """
        recursive 
        :type s: str
        :rtype: List[List[str]]
        """
        def p(s):
            n = len(s)
            if n == 0:
                return [[]]
            if n == 1:
                return [[s]]
            cur_l = []
            for i in xrange(0, n):
                if is_p(s[i:n]):
                    pre_list = p(s[0:i])
                    cur_l += [l+[s[i:n]] for l  in pre_list]
            return cur_l
        return p(s)

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        n = len(s)
        if n == 0:
            return [[]]
        if n == 1:
            return [[s]]
        dp = [[] for i in xrange(n)]
        # dp[0] = [[s[0]]]
        # dp[0].p()
        for i in xrange(0,n):
            for j in xrange(0,i):
                if is_p(s[i-j:i+1]):
                    dp[i] += [l+[s[i-j:i+1]] for l in dp[i-1-j]]

            if is_p(s[0:i+1]):
                dp[i] += [s[0:i+1]],
            # dp[i].p()
        return dp[n-1]



    # not work                
    def partition_1(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        pre_list = []
        results = []
        n = len(s)                    
        for i in xrange(1,n):
            pre_s = s[0:i]
            # pre_s.p()
            if len(pre_list) > 0:
                pre_list = [l+[s[i-1]] for l  in pre_list]
                # pre_list.p()
            if is_p(pre_s):
                pre_list += [pre_s],
                # pre_list.p()
            left_s = s[i:n]
            # left_s.p()
            if is_p(left_s):
                results += [l+[left_s] for l  in pre_list]
                # results.p()
        if is_p(s):
            results += [[s]]
        return results

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().partition("aa").must_equal([["a","a"],["aa"]])
        Solution().partition("abbab").must_equal(
                [["a","b","b","a","b"],["a","b","bab"],["a","bb","a","b"],["abba","b"]])
        Solution().partition("aaba").must_equal(
                [['a', 'aba'], ['a', 'a', 'b', 'a'], ['aa', 'b', 'a']])

                
                