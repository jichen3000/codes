# http://www.geeksforgeeks.org/find-maximum-sum-possible-equal-sum-three-stacks/
def solve(stack1, stack2, stack3):
    stacks = [stack1, stack2, stack3]
    sums = [sum(s) for s in stacks]
    min_sum = min(sums)
    while min_sum > 0:
        all_equal = True
        for i in range(3):
            if sums[i] > min_sum:
                sums[i] -= stacks[i].pop(0)
                min_sum = min(sums)
                all_equal = False
        if all_equal: break
    return min_sum

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        stack1 = [ 3, 2, 1, 1, 1 ]
        stack2 = [ 4, 3, 2 ]
        stack3 = [ 1, 1, 4, 1 ]
        solve(stack1, stack2, stack3).p()
        stack1 = [ 9, 3 ]
        stack2 = [ 10,4 ]
        stack3 = [ 11,5 ]
        solve(stack1, stack2, stack3).p()
