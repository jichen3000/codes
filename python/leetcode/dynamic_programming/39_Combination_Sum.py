class Solution(object):
    def combinationSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        n = len(nums)
        if n == 0:
            return []
        dp = [ [] for j in xrange(target+1)]
        for i in xrange(n):
            # from large to small to remove the duplicate one
            for j in xrange(target,0,-1):
                if j >= nums[i]:
                    # (i,j,nums[i]).p()
                    if j % nums[i] == 0:
                        dp[j] += [nums[i]] * (j/nums[i]),
                    for k in xrange(1, j/nums[i]+1):
                        dp[j] += [l+([nums[i]] * k) for l in dp[j-k*nums[i]] ]
        return dp[-1]

    ## dfs
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        mem = {}
        def dfs(n):
            if n in mem:
                return mem[n]
            if n == 0:
                mem[n] = [[]]
                return [[]]
            res = []
            for num in candidates:
                if n >= num:
                    res += [[num]+l for l in dfs(n-num) if len(l)==0 or num<=l[0]]
            mem[n] = res
            return res
        return dfs(target)                
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().combinationSum([2,3,6,7],7).must_equal([[2, 2, 3], [7]])
        Solution().combinationSum([1,2],4).must_equal([[1, 1, 1, 1], [2, 2], [1, 1, 2]])
