# http://www.geeksforgeeks.org/partition-set-k-subsets-equal-sum/
def solve(nums, group_count):
    n = len(nums)
    all_sum = sum(nums)
    if all_sum % group_count != 0:
        return False
    target_sum = all_sum / group_count

    results = []
    def dfs(addeds, groups):
        if len(addeds) == n:
            # groups.p()
            if all(sum(l)==target_sum for l in groups):
                results.append(groups)
                return True
            else:
                return False
        i = len(addeds)
        for j in range(group_count):
            groups[j].append(nums[i])
            addeds.append(nums[i])
            if dfs(addeds, groups):
                return True
            groups[j].pop()
            addeds.pop()
        return False
    addeds = []
    groups = [[] for _ in range(group_count)]
    result = dfs(addeds, groups)
    # results.pp()
    return result
    

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        solve([2,1,4,5,3,3], 3).must_equal(True)
        # solve([2,1,4,5,9], 3).must_equal(False)
