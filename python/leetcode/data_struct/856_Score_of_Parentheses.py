class Solution:
    def scoreOfParentheses(self, s):
        """
        :type S: str
        :rtype: int
        """
        res, stack = 0, []
        for c in s:
            if c == "(":
                stack += 0,
            else:
                pre = stack.pop()
                if pre == 0:
                    v = 1
                else:
                    v = pre * 2
                if stack:
                    stack[-1] += v
                else:
                    res += v
        return res

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().scoreOfParentheses("()").must_equal(1)
        Solution().scoreOfParentheses("(())").must_equal(2)
        Solution().scoreOfParentheses("()(())").must_equal(3)
        Solution().scoreOfParentheses("(()(()))").must_equal(6)


