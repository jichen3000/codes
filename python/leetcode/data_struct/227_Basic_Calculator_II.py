class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        ops = {"+","-","*","/"}
        stack = []
        sign = "+"
        i, n = 0, len(s)
        while i < n:
            cur_s = ""
            while i < n and s[i] not in ops:
                cur_s += s[i]
                i += 1
            v = int(cur_s)
            if sign == "+":
                stack += v,
            elif sign == "-":
                stack += -v,
            elif sign == "*":
                stack += stack.pop() * v,
            elif sign == "/":
                pv = stack.pop()
                if pv < 0:
                    cv = -((-pv) // v)
                else:
                    cv = pv // v
                stack += cv,
            if i < n: sign = s[i]
            i += 1
        # stack.p()
        return sum(stack)

if __name__ == '__main__':
    from minitest import *

    with test("Solution"):
        Solution().calculate("3 + 3/2").must_equal(4)
        Solution().calculate("14-3/2").must_equal(13)
