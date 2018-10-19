class Solution:
    def compress(self, s):
        """
        :type chars: List[str]
        :rtype: int
        """
        if not s: return 0
        i = p = 0
        count, n = 1, len(s)
        for j in range(1, n+1):
            if j < n and s[i] == s[j]:
                count += 1
            else:
                s[p] = s[i]
                if count == 1:
                    p += 1
                else:
                    cs = str(count)
                    for k in range(len(cs)):
                        s[p+1+k] = cs[k]
                    count = 1
                    p += 1 + len(cs)
                i = j
        return p
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        s = ["a","a","b","b","c","c","c"]
        Solution().compress(s).must_equal(6)
        s.must_equal(['a', '2', 'b', '2', 'c', '3', 'c'])

        s = ["a"]
        Solution().compress(s).must_equal(1)
        s.must_equal(['a'])

        s = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
        Solution().compress(s).must_equal(4)
        s.must_equal(["a","b","1","2","b","b","b","b","b","b","b","b","b"])
