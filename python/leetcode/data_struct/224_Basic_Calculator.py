from operator import add, sub
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.replace(" ","")
        def cal(ss):
            ss = ss.replace("--","+")
            ss = ss.replace("+-","-")
            cur_n = ""
            nums, ops = [], []
            for c in ss:
                if c == "+":
                    if cur_n: nums += int(cur_n),
                    cur_n = ""
                    ops += "+"
                elif c == "-":
                    if cur_n: nums += int(cur_n),
                    cur_n = ""
                    ops += "-",
                else:
                    cur_n += c
            if cur_n: nums += int(cur_n),
            cur_v = nums[0]
            # means first ops is "-"
            if len(nums) == len(ops):
                cur_v = -nums[0]
                ops.pop(0)
            for i in range(1, len(nums)):
                if ops[i-1] == "+":
                    cur_v += nums[i]
                else:
                    cur_v -= nums[i]
            # (ss,cur_v).p()
            return cur_v
            # return eval(ss)
        def dfs(i):
            cur = ""
            while i < len(s):
                if s[i] == "(":
                    i, result = dfs(i+1)
                    cur += str(result)
                elif s[i] == ")":
                    return [i+1,cal(cur)]
                else:
                    cur += s[i]
                    i += 1
            return cal(cur)
        return dfs(0)
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        acc = [] 
        cur_n = ""      
        for c in s+" ":
            if c in (" ", "+", "-", "(",")"):
                if cur_n:
                    cur = int(cur_n)
                    if len(acc) == 0 or acc[-1] == "(":
                        acc += cur,
                    else:
                        op, pre = acc.pop(), acc.pop()
                        acc += op(pre,cur),
                    cur_n = ""

            if c == " ":
                pass
            elif c == "+":
                acc += add,
            elif c == "-":
                acc += sub,
            elif c == "(":
                acc += c
            elif c == ")":
                not_pre_parethesis = True
                while len(acc) > 1:
                    if acc[-2] == "(":
                        if not_pre_parethesis:
                            pre, pre_parethesis = acc.pop(), acc.pop()
                            acc += pre,
                            not_pre_parethesis = False
                        else:
                            break
                    else:
                        cur, op, pre = acc.pop(), acc.pop(), acc.pop()
                        acc += op(pre,cur),
            else:
                cur_n += c
        return acc[0]

## review
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        from operator import add, sub
        op_map = {"+":add,"-":sub}
        def dfs(i):
            res = 0
            cur_op = None
            while i < n:
                c = s[i]
                if c in op_map:
                    cur_op = op_map[c]
                    i += 1
                elif c == "(":
                    cur_v, i = dfs(i+1)
                    if cur_op:
                        res = cur_op(res, cur_v)
                    else:
                        res = cur_v
                elif c == ")":
                    return (res, i+1)
                elif c == " ":
                    i += 1
                else:
                    while i+1 < n and s[i+1] not in " ()+-":
                        c += s[i+1]
                        i += 1
                    cur_v = int(c)
                    if cur_op:
                        res = cur_op(res, cur_v)
                    else:
                        res = cur_v
                    i += 1
                
            return (res, i)
        return dfs(0)[0]

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        from operator import add, sub
        op_map = {"+":add,"-":sub}

        stack = []
        res, cur_op  = 0, None
        i = 0
        while i < n:
            c = s[i]
            if c in op_map:
                cur_op = op_map[c]
            elif c == "(":
                stack += (res, cur_op),
                res, cur_op  = 0, None
            elif c == ")":
                pre_res, pre_op = stack.pop()
                if pre_op:
                    res = pre_op(pre_res, res)
            elif c == " ":
                pass
            else:
                while i+1 < n and s[i+1] not in " ()+-":
                    c += s[i+1]
                    i += 1
                cur_v = int(c)
                if cur_op:
                    res = cur_op(res, cur_v)
                else:
                    res = cur_v
            i += 1
            
        return res
                
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().calculate("23").must_equal(23)
        Solution().calculate("23-(23-1)").must_equal(1)
        Solution().calculate("2-(5-6)").must_equal(3)
        Solution().calculate("2  ").must_equal(2)
        Solution().calculate("(5-(1+(5)))").must_equal(-1)
        Solution().calculate("1-(2+3-(4+(5-(1-(2+4-(5+6))))))").must_equal(-1)
        Solution().calculate("(5-(1+(5)+1))").must_equal(-2)
       

