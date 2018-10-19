# python/leetcode/algorithm/backtracking/top_04_Remove_Invalid_Parentheses.py
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def validate(s):
            # if len(s) == 0: return False
            count = 0
            for c in s:
                if c == "(":
                    count += 1
                elif c == ")":
                    count -= 1
                    if count < 0:
                        return  False
            return count == 0
        acc = {s}
        while acc:
            good_list = filter(validate, acc)
            if good_list:
                return good_list
            # next_acc = set()
            # for cur_s in acc:
            #     for i in xrange(len(cur_s)):
            #         next_acc.add(cur_s[:i]+cur_s[i+1:])
            # acc = next_acc
            acc = {cur_s[:i]+cur_s[i+1:] for cur_s in acc for i in xrange(len(cur_s))}
        return []

class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def validate(s):
            # if len(s) == 0: return False
            count = 0
            for c in s:
                if c == "(":
                    count += 1
                elif c == ")":
                    count -= 1
                    if count < 0:
                        return  False
            return count == 0
        acc = {s}
        while acc:
            good_list = filter(validate, acc)
            if good_list:
                return good_list
            next_acc = set()
            for cur_s in acc:
                for i in xrange(len(cur_s)):
                    if cur_s[i] in "()":
                        next_acc.add(cur_s[:i]+cur_s[i+1:])
            acc = next_acc
            # acc = {cur_s[:i]+cur_s[i+1:] for cur_s in acc for i in xrange(len(cur_s))}
        return []

## in test, it is fastest, but not easy one to understand
class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = {("",0)}
        max_len = 0
        for c in s:
            temps = set()
            if c == "(":
                for item in res:
                    temps.add(item)
                    temps.add((item[0] + "(", item[1] + 1))
            elif c == ")":
                for item in res:
                    temps.add(item)
                    if item[1] > 0:
                        temps.add((item[0] + ")", item[1] - 1))
                        if item[1] == 1:
                            max_len = max(max_len, len(item[0])+1)
            else:
                for item in res:
                    temps.add((item[0] + c, item[1]))
                    if item[1] == 0:
                        max_len = max(max_len, len(item[0])+1)
            res = temps
        return [item[0] for item in res if len(item[0]) == max_len and item[1]==0]

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().removeInvalidParentheses("()())()").must_equal(
                ['(())()', '()()()'])        
        Solution().removeInvalidParentheses("(a)())()").must_equal(
                ["(a)()()", "(a())()"])
        Solution().removeInvalidParentheses(")(").must_equal(
                [""])
