class Solution:
    def intToRoman(self, num):
        """
        :type s: str
        :rtype: int
        """
        roman_dict = {
            1   :"I",
            5   :"V",
            10  :"X",
            50  :"L",
            100 :"C",
            500 :"D",
            1000:"M",
        }
        def get_roman(n, exp):
            t = 10 ** exp
            if 1 <= n <= 3:
                return roman_dict[t] * n
            elif 4 <= n <= 5:
                return roman_dict[t] * (5-n) + roman_dict[5*t]
            elif 6 <= n <= 8:
                return roman_dict[5*t] + roman_dict[t] * (n-5)
            elif 9 == n:
                return  roman_dict[t] + roman_dict[10*t]
            else:
                return ""
        res, exp = "", 0
        while num > 0:
            num, m = divmod(num, 10)
            res = get_roman(m, exp) + res
            exp += 1
        return res

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().intToRoman(18).must_equal("XVIII")
        Solution().intToRoman(1994).must_equal("MCMXCIV")
