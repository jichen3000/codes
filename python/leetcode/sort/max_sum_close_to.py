# get the cloest sum to specified value
import bisect, sys

def max_sum_close_to(nums, k):
    pre_sum, pre_list = 0, []
    max_sum = -sys.maxint
    for v in nums:
        bisect.insort(pre_list, pre_sum)
        pre_sum += v
        i = bisect.bisect_left(pre_list, pre_sum - k)
        max_sum = max(max_sum, pre_sum - pre_list[i])
    return max_sum

if __name__ == '__main__':
    from minitest import *

    with test(max_sum_close_to):
        nums = [ 1, 2, -3, 4, 5 ]
        max_sum_close_to(nums,8).must_equal(8)
        max_sum_close_to(nums,9).must_equal(9)
        max_sum_close_to(nums,6).must_equal(6)
        max_sum_close_to(nums,5).must_equal(5)
        max_sum_close_to(nums,20).must_equal(9)
