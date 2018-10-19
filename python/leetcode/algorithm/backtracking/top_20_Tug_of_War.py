import sys
def solve(nums):
    n = len(nums)
    if n % 2 == 0:
        limits = [n / 2, n / 2]
    else:
        limits = [n/2+1, n/2]
    results = [sys.maxint, []]
    def dfs(group, index):
        if index == n:
            abs_v = abs(sum(group[0])-sum(group[1]))
            # abs_v.p()
            # results[0].p()
            if abs_v < results[0]:
                # [abs_v, group].p()
                results[0] = abs_v
                results[1] = [group[0][:],group[1][:]]
            return 
        for i in range(2):
            if len(group[i]) == limits[i]:
                continue
            group[i].append(nums[index])
            dfs(group, index+1)
            group[i].pop()
    dfs([[nums[0]],[] ], 1)
    return results

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        solve([23, 45, -34, 12, 0, 98, -99, 4, 189, -1, 4]).must_equal(
                [1, [[23, 0, -99, 4, 189, 4], [45, -34, 12, 98, -1]]])
