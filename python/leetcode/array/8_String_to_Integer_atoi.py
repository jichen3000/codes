class Solution:
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        nums = {str(i) for i in range(10)}
        if not s: return 0
        res = 0
        sign = 1
        carry = 1
        signed = False
        for c in reversed(s):
            if c in nums:
                res += int(c) * carry
                carry *= 10
            elif c == "-":
                sign = -1
                if signed:
                    return 0
                signed = True                    
            elif c == "+":
                if signed:
                    return 0
                signed = True
            else:
                res = 0
                carry = 1
        res = res * sign
        if res > 2147483647:
            return 2147483647
        elif res < -2147483648:
            return -2147483648
        return res
        
if __name__ == '__main__':
    from minitest import *

    with test("Solution"):
        Solution().myAtoi("  +-0012a42").must_equal(0)
        Solution().myAtoi("  -0012a42").must_equal(-12)
        Solution().myAtoi("2147483649").must_equal(2147483647)
