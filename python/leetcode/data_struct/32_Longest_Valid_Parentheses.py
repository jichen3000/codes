class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        cur_left_count = 0
        # item consist with left_count and length
        stack = []
        max_len = 0
        for c in s:
            # (c,cur_left_count).p()
            if c == "(":
                cur_left_count += 1
                stack += 0,
            else:
                if cur_left_count > 0:
                    stack[-1] += 2
                    cur_left_count -= 1
                    if len(stack) > 1:
                        v = stack.pop()
                        stack[-1] += v
                    max_len = max(max_len, stack[-1])
                else:
                    stack += 0,
            # (c,cur_left_count,stack).p()
        return max_len

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().longestValidParentheses("").must_equal(0)
        Solution().longestValidParentheses("()").must_equal(2)
        Solution().longestValidParentheses("()(()").must_equal(2)
        Solution().longestValidParentheses("()(()(()()").must_equal(4)
        Solution().longestValidParentheses("()(()(()())").must_equal(8)
        Solution().longestValidParentheses(")()())()()(").must_equal(4)
