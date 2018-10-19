class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n == 0: return []
        cur_set = [("(", 1, 0)]
        for i in range(1, 2 * n):
            temp_set = []
            for s, l, r in cur_set:
                if l < n:
                    temp_set += (s+"(", l+1, r),
                if l > r:
                    temp_set += (s+")", l, r+1),
            cur_set = temp_set
        return [s for s, l, r in cur_set]

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().generateParenthesis(3).must_equal([
                '((()))', 
                '(()())', 
                '(())()', 
                '()(())', 
                '()()()'])



