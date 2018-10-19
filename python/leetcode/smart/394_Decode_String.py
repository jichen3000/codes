import re
from operator import add, mul
# def add(s1,s2):
#     return s1+s2
# def mul(s,mul):
#     return s * num

def find_sub(strs):
    # strs.p()
    count = 1
    for i in range(1,len(strs)):
        s = strs[i]
        if s == "[":
            count += 1
        elif s == "]":
            count -= 1
            if count == 0:
                # print(strs[1:i])
                return strs[1:i]
    raise Exception("cannot find")

DIGITALS = "0123456789"
def find_digits(strs):
    for i in range(len(strs)):
        s = strs[i]
        if s not in DIGITALS:
            return strs[:i]
    raise Exception("cannot find")

def gen_tokens(strs):
    tokens = []
    last_s = None
    op_count = 0
    operand_count = 0
    i = 0
    while i < len(strs):
        s = strs[i]
        if s in DIGITALS:
            if last_s:
                tokens += last_s,
                operand_count += 1
                last_s = None
                if op_count + 1 < operand_count:
                    tokens += add,
                    op_count += 1
            dig_str = find_digits(strs[i:])
            # dig_str.p()
            i += len(dig_str)
            sub_strs = find_sub(strs[i:])
            sub_tokens = gen_tokens(sub_strs)
            i += len(sub_strs) + 2
            # sub_tokens.p()
            tokens += sub_tokens + [int(dig_str), mul]
            op_count += 1
            operand_count += 2
            # (op_count, len(tokens)).p()
            if op_count + 1 < operand_count:
                tokens += add,
                op_count += 1
        else:
            if last_s == None:
                last_s = ""
            last_s += s
            i += 1
    if last_s:
        tokens += last_s,
        operand_count += 1
        last_s = None
    if op_count + 1 < operand_count:
        tokens += add,
        op_count += 1
    return tokens

def cal_reverse_polish(tokens):
    stack = []
    ops = [add,mul]
    for token in tokens:
        if token in ops:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = token(operand1, operand2)
            stack += result,
        else:
            stack += token,
    return stack[-1]


class Solution(object):
    def decodeString(self, strs):
        """
        :type strs: str
        :rtype: str
        """
        if len(strs) == 0:
            return ""
        return cal_reverse_polish(gen_tokens(strs))
                    
    def decodeString(self, s):
        def inner(m):
            m.groups().p()
            return int(m.group(1)) * m.group(2)
        while '[' in s:
            s = re.sub(r'(\d+)\[([a-z]*)\]', inner, s)
        return s     

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, n = 0, len(s)
        res = ""
        stack = []
        while i < n:
            i_s = ""
            while i < n and s[i].isnumeric():
                i_s += s[i]
                i += 1
            int_v = int(i_s) if i_s else None
            if s[i] == "[":
                stack += (res, int_v),
                res = ""
            elif s[i] == "]":
                pre, pi = stack.pop()
                res = pre + res * pi
            else:
                res += s[i]
            i += 1
        return res       

class Solution:
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s: return s
        stack = []
        int_s, res = "", ""
        for c in s:
            if c.isnumeric():
                if res and len(int_s) == 0: 
                    stack += res,
                int_s += c
            elif c == "[":
                stack += int_s,
                int_s = ""
                res = ""
            elif c == "]":
                v = stack.pop()
                res = res * int(v)
                while stack and stack[-1].isalpha():
                    res = stack.pop() + res
            else:
                res += c
        return res                    
if __name__ == '__main__':
    from minitest import *

    # with test(gen_tokens):
    #     gen_tokens("100[a]").must_equal(['a',100,mul])
    #     gen_tokens("ef").must_equal(['ef'])
    #     gen_tokens("3[a]2[bc]").must_equal(['a', 3, mul, 'bc', 2, mul, add ])
    #     gen_tokens("3[a]").must_equal(['a',3,mul])
    #     gen_tokens("3[a2[c]]").must_equal(['a','c',2,mul,add,3,mul])
    #     gen_tokens("2[abc]3[cd]ef").must_equal(['abc', 2, mul, 'cd', 3, mul, add, 'ef',add])
    #     gen_tokens("sd2[f2[e]g]i").must_equal(['sd','f','e',2, mul, add, 'g', add, 2, mul, add, 'i', add])

    with test(Solution):
        # Solution().decodeString("ef").p()
        # Solution().decodeString("3[a]2[bc]").p()
        # Solution().decodeString("3[a]").p()
        # Solution().decodeString("10[a]").must_equal("a"*10)
        Solution().decodeString("3[a2[c]]").p()
        # Solution().decodeString("2[abc]3[cd]ef").p()
        # Solution().decodeString("sd2[f2[e]g]i").p()
