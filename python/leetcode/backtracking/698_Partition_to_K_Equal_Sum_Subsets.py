class Solution:
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        from itertools import permutations
        t, r = divmod(sum(nums), k)
        if r != 0: return False
        def dfs(nums, ck):
            visited = set()
            if ck == 1:
                return sum(nums) == t
            for ll in range(1, len(nums)):
                for l in permutations(nums, ll):
                    if tuple(l) in visited:
                        continue
                    visited.add(tuple(l))
                    if sum(l) == t:
                        left_nums = nums.copy()
                        for v in l:
                            left_nums.remove(v)
                        res = dfs(left_nums, ck-1)
                        if res: return True
            return False
        return dfs(nums, k)
    # time: k ^ n, more pricisely, (k-1)! * k ^ (n-k)
    # space: k + n
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        buckets = [0] * k
        target, remain = divmod(sum(nums), k)
        if remain != 0: return False
        n = len(nums)
        nums.sort(reverse=True)
        
        def dfs(i):
            if i == n:
                return len(set(buckets)) == 1
            for j in range(k):
                buckets[j] += nums[i]
                if buckets[j] <= target and dfs(i+1):
                    return True
                buckets[j] -= nums[i]
                # for the num > target
                if buckets[j] == 0:
                    break
            return False
        return dfs(0)
                