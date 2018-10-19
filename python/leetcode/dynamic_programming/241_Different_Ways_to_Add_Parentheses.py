from operator import add, sub, mul
import re

def reverse_polish(op_list):
    # op_list.p()
    stack = []
    for cur in op_list:
        if type(cur) != int:
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack += cur(operand1, operand2),
        else:
            stack += cur,
    return stack[-1]


def get_possible_list(operands, operators):
    all_list = [operands[:2] + operators[:1]]
    # all_list.p()
    for i in range(1,len(operators)):
        new_list = []
        for l in all_list:
            for j in range(len(l), -1, -1):
                if j==len(l) or type(l[j]) != int:
                    new_l = l[:]
                    new_l.insert(j, operators[i])
                    new_l.insert(j, operands[i+1])
                    new_list += new_l,
                else:
                    break
        # new_list.p()
        all_list = new_list
    return all_list


class Solution(object):
    # using 52ms
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        operands, operators = [], []
        for s in re.split("([+-/*])", input):
            if s == "+":
                operators += add,
            elif s == "-":
                operators += sub,
            elif s == "*":
                operators += mul,
            else:
                operands += int(s),
        # results = []
        return [reverse_polish(l) for l in get_possible_list(operands, operators)]

    # dp, using 35ms
    def diffWaysToCompute(self, input):
        operands, operators = [], []
        for s in re.split("([+-/*])", input):
            if s == "+":
                operators += add,
            elif s == "-":
                operators += sub,
            elif s == "*":
                operators += mul,
            else:
                operands += int(s),
        # (operands, operators).p()
        n = len(operands)
        dp = [[None] * n for _ in range(n)]
        for l in range(n):
            for i in range(n-l):
                j = i + l
                if l == 0:
                    dp[i][j] = [operands[i]]
                # elif l == 1:
                #     dp[i][j] = [operators[i](operands[i],operands[j])]
                else:
                    # equals the below one line
                    # dp[i][j] = []
                    # for k in range(i,j):
                    #     for v1 in dp[i][k]:
                    #         for v2 in dp[k+1][j]:
                    #             dp[i][j] += operators[k](v1,v2),
                    dp[i][j] = [operators[k](v1,v2) for k in range(i,j) for v1 in dp[i][k] for v2 in dp[k+1][j]]
        dp.p()
        return dp[0][-1]



if __name__ == '__main__':
    from minitest import *

    with test(get_possible_list):
        get_possible_list([2,3,4],["*","+"]).must_equal([[2, 3, '*', 4, '+'], [2, 3, 4, '+', '*']])
        get_possible_list([2,3,4,5],["*","+","-"]).must_equal([
            [2, 3, '*', 4, '+', 5, '-'],
            [2, 3, '*', 4, 5, '-', '+'],
            [2, 3, 4, '+', '*', 5, '-'],
            [2, 3, 4, '+', 5, '-', '*'],
            [2, 3, 4, 5, '-', '+', '*']])

    with test(reverse_polish):
        reverse_polish([3,4,5,add,sub]).must_equal(-6)

    with test(Solution):
        result = Solution().diffWaysToCompute("2*3-4*5")
        result.sort()
        result.must_equal([-34, -14, -10, -10, 10])
