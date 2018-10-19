class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0: return "0"
        sign = "-" if (numerator>=0) ^ (denominator>=0) else ""
        numerator, denominator = abs(numerator), abs(denominator)
        l, r = divmod(numerator, denominator)
        r_map = {}
        res = [sign, str(l)]
        if r > 0:
            res += "."
        # r.p()
        r_map[r] = len(res)
        while r > 0:
            r *= 10
            l, r = divmod(r, denominator)
            # r.p()
            res += str(l),
            if r in r_map:
                res.insert(r_map[r], "(")
                res += ")",
                break
            r_map[r] = len(res)

        return "".join(res)



if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().fractionToDecimal(1,6).must_equal("0.1(6)")
        # Solution().fractionToDecimal(1,2).must_equal("0.5")
        # Solution().fractionToDecimal(555,10000).must_equal("0.0555")
        # Solution().fractionToDecimal(1,99).must_equal("0.(01)")
        # Solution().fractionToDecimal(1,90).must_equal("0.0(1)")
        Solution().fractionToDecimal(1,17).must_equal("0.(0588235294117647)")
