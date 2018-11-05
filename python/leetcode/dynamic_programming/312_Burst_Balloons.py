
class Solution(object):
    # 30mins backtracking solution, TLE Time Limit Exceeded at 13/70
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)        
        if n == 0: return 0
        max_value = [0]
        def dfs(nums, value):
            # (nums, value).p()
            if len(nums) <= 1:
                max_value[0] = max(max_value[0], value+nums[0])
                return
            for i in range(len(nums)):
                cur_v = (1 if i-1<0 else nums[i-1]) * (1 if i+1==len(nums) else nums[i+1]) * nums[i]
                # (i,nums,cur_v).p()
                dfs(nums[:i]+nums[i+1:],value+cur_v)
        dfs(nums, 0)
        return max_value[0]

    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        n = len(nums)        
        if n < 3: return 0
        dp = [[0] * n for _ in range(n)]
        for l in range(2,n):
            for i in range(n-l):
                j = i + l
                dp[i][j] = max(dp[i][k] + dp[k][j] +\
                    nums[i]*nums[k]*nums[j] \
                    for k in range(i+1,j))
        return dp[0][-1]

    def maxCoins(self, nums):
        '''
            physical meaning: 
                choose k as the last one, add nums[i]*nums[k]*nums[j] as last
                dp[i][j] means from i to j, the maxCoins
            key points, 
                1. add 1 in the head and tail, this one is most easy one
                2. choose one as last one, and add nums[i]*nums[k]*nums[j] as last
                    this is hardest one
                    use i and j to multiple j, means i and j is the last left one from sides
                3. dp[i][i+1] = 0
        '''
        nums = [1] + nums + [1]
        n = len(nums)        
        if n < 3: return 0
        dp = [[0] * n for _ in range(n)]
        for l in range(2, n):
            for i in range(n-l):
                j = i + l
                dp[i][j] = max(dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j] for k in range(i+1, j))
        return dp[0][n-1]


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        nums = [3,1,5,8]

        Solution().maxCoins(nums).must_equal(167)
