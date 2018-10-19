from itertools import product, permutations

OPERATIONS = ["+","-","*","/"]

def cal_reverse_polish(tokens):
    stack = []
    for token in tokens:
        if token in OPERATIONS:
            operand2 = stack.pop()
            operand1 = stack.pop()
            v = eval(operand1+token+operand2)
            stack += str(v),
        else:
            stack += token,
    return int(stack[0])



def solution(nums, target):
    nums_permuations = list(permutations(nums))
    operation_product = list(product(OPERATIONS, repeat=len(nums)-1))
    results = []

    for cur_nums in nums_permuations:
        for cur_opes in operation_product:
            cur_stack = [str(cur_nums[0])]
            for i in xrange(len(cur_opes)):
                cur_stack += str(cur_nums[i+1]),
                cur_stack += cur_opes[i],
            cur_stack.p()
            try:
                if cal_reverse_polish(cur_stack) == target:
                    results += cur_stack,
            except Exception as e:
                # raise
                print e
                pass
    return results

if __name__ == '__main__':
    from minitest import *

    with test(solution):
        solution([9,3,0,8], 3).p()

