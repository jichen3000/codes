class Solution(object):
    def findReplaceString(self, s, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        pre_i = ii = 0
        res = ""
        ist_list = list(zip(indexes, sources, targets))
        ist_list.sort()
        while ist_list:
            ii, si, ti = ist_list.pop(0)
            if s[ii:ii+len(si)] == si:
                res += s[pre_i:ii] + ti
                pre_i = ii + len(si)
        res += s[pre_i:]
        return res
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().maskPII("LeetCode@LeetCode.com").must_equal("l*****e@leetcode.com")
        # Solution().maskPII("AB@qq.com").must_equal("a*****b@qq.com")
        # Solution().maskPII("1(234)567-890").must_equal("***-***-7890")
        # Solution().maskPII("86-(10)12345678").must_equal("+**-***-***-5678")
        Solution().findReplaceString("vmokgggqzp",
                [3,5,1],
                ["kg","ggq","mo"],
                ["s","so","bfr"]).must_equal("vbfrssozp")
