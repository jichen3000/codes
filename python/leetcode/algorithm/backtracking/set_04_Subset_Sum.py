def solve(nums, target):
    n = len(nums)
    if target == 0 or n == 0: 
        return []
    results = []
    all_mask = 1 << n
    for mask in xrange(all_mask):
        l = []
        for i in xrange(n):
            if mask >> i & 1:
                l += nums[i],
        if sum(l) == target:
            results += l,
    return results

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        nums = [10, 7, 5, 18, 12, 20, 15]
        solve(nums, 35).pp()

            