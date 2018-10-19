from operator import add, sub, truediv, mul
from itertools import permutations, product
OPS = [add, sub, mul, truediv]
## reverse polish
# https://en.wikipedia.org/wiki/Reverse_Polish_notation
def cal_reverse_polish(tokens):
    stack = []
    for token in tokens:
        if token in OPS:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = token(operand1, operand2)
            stack.append(result)
        else:
            stack.append(token)
    return stack[0]

def gen_validate_reverse_polish_list(operands, operators):
    '''
        using dp,
        the first one is [n0,n1,o0]
        then find the last operand index as pre_index, 
        loop from pre_index + 1 to new_length-1, insert the new operand,
                and append new operator at the last
    '''
    if len(operands) < 2:
        raise Exception("invalidate for operands lengths!")
    if len(operands) != len(operators) +1:
        raise Exception("invalidate for lengths of operands and operators!")
    pre_permutations = [ [(0,0),(0,1),(1,0)] ]
    cur_permutations = pre_permutations
    for i in xrange(1, len(operators)):
        insert_operator = (1,i)
        insert_operand  = (0,i+1)
        pre_operand = (0,i)
        cur_permutations = []
        for cur_list in pre_permutations:
            pre_index = cur_list.index(pre_operand)
            for j in xrange(pre_index+1, (i+1)*2):
                new_list = cur_list[:]
                new_list.insert(j,insert_operand)
                new_list.append(insert_operator)
                cur_permutations += new_list,
        pre_permutations = cur_permutations
    all_list = [operands, operators]
    return [[all_list[li][ii] for li, ii in cur_list] for cur_list in cur_permutations]

def judge_target(nums, target):
    n = len(nums)
    if n <= 1:
        return False
    # operand_permutations = permutations(nums)
    # operator_permutations = permutations(OPS,n-1)
    for operands in permutations(nums):
        for operators in product(OPS,repeat=n-1):
            for tokens in gen_validate_reverse_polish_list(operands, operators):
                # operands.p()
                # tokens.p()
                try:
                    value = cal_reverse_polish(tokens)
                    # value.p()
                    if abs(value - target) < 0.0001:
                        print(tokens)
                        return True
                except ZeroDivisionError as e:
                    # raise
                    pass
    return False


class Solution(object):
    def judgePoint24(self, nums):
        return judge_target(nums, 24)

if __name__ == '__main__':
    from minitest import *

    # with test(gen_validate_reverse_polish_list):
    #     gen_validate_reverse_polish_list([1,2],['+']).p()
    #     gen_validate_reverse_polish_list([1,2,3],['+','-']).p()
    #     gen_validate_reverse_polish_list([1,2,3,4],['+','-','*']).p()
    #     gen_validate_reverse_polish_list([1,2,3,4,5],['+','-','*','/']).size().p()
    #     gen_validate_reverse_polish_list([1,2,3,4,5,6],['+','-','*','/','+']).size().p()

    with test(cal_reverse_polish):
        cal_reverse_polish([1,2, add]).must_equal(3)
        cal_reverse_polish([1,2, truediv]).must_equal(0.5)

    with test(Solution):
        # Solution().judgePoint24([4, 1, 8, 7]).must_equal(True)
        # Solution().judgePoint24([9, 4, 8, 5]).must_equal(True)
        Solution().judgePoint24([1, 6, 9, 1]).must_equal(True)
