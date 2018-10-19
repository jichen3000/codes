class Solution(object):
    # pros: can handle any group number, 3 or 4 even more
    # cons: using recursive method
    def makesquare_dfs(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        group_n = 4
        if nums == None: return False
        n = len(nums)
        if n < group_n:
            return False
        nums.sort(reverse=True)
        sum_v = sum(nums)
        if sum_v % group_n != 0:
            return False
        target = sum_v / group_n
        for num in nums:
            if num > target:
                return False
        sums = [0] * group_n
        def dfs(index):
            if index == n:
                if all(s == target for s in sums):
                    return True
                else:
                    return False
            for i in xrange(group_n):
                if sums[i] + nums[index] > target:
                    continue
                sums[i] += nums[index]
                if dfs(index+1): return True
                sums[i] -= nums[index]
            return False
        return dfs(0)

    # pros: easy understand, no recursive
    # cons: cannot handle other goupr numbers, long time
    def makesquare(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        group_n = 4
        if nums == None: return False
        n = len(nums)
        if n < group_n:
            return False
        # nums.sort(reverse=True)
        sum_v = sum(nums)
        if sum_v % group_n != 0:
            return False
        target = sum_v / group_n
        for num in nums:
            if num > target:
                return False
        
        all_mask = (1 << n) -1
        mask_list = []
        half_subset_list = [False] * (all_mask+1)
        for mask in xrange(all_mask):
            subset_sum = 0
            for i in xrange(n):
                if ((mask >> i) & 1):
                    subset_sum += nums[i]
            if subset_sum == target:
                for pre_mask in mask_list:
                    # means they are exlude
                    if (pre_mask & mask) == 0:
                        half_subset_mask = (pre_mask | mask)
                        half_subset_list[half_subset_mask] = True
                        if half_subset_list[all_mask ^ half_subset_mask]:
                            # print(pre_mask, mask, half_subset_mask,all_mask ^ half_subset_mask)
                            return True
            mask_list += mask,
        return False



if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().makesquare([1,1,2,2,2]).must_true()
        Solution().makesquare([1,2,2,2,2]).must_false()
        Solution().makesquare([3,3,3,3,4]).must_false()
