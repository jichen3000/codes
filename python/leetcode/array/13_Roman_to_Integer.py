class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
        }
        res, pre_large_v = 0, None
        for c in s[::-1]:
            v = roman_dict[c]
            if pre_large_v and v < pre_large_v:
                res -= v
            else:
                res += v
                pre_large_v = v
        return res

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().romanToInt("XIIX").must_equal(18)
        Solution().romanToInt("MCMXCIV").must_equal(1994)
