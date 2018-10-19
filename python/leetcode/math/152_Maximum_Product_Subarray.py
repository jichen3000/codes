class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)
        dp = [ [0] * n for _ in range(n) ]
        def mul(i, j):
            res = nums[j]
            for k in range(i, j):
                res *= nums[k]
            return res
        for l in range(0, n):
            for i in range(n-l):
                j = i + l
                if l == 0:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1], mul(i,j))
        return dp[0][-1]
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        n = len(nums)
        dp = nums[::]
        muls = nums[::]
        for l in range(1, n):
            # temp = [max(dp[i], dp[i+1], mul(i,i+l)) for i in range(n-l) ]
            temp1 = []
            temp2 = []
            for i in range(n-l):
                j = i + l
                temp1 += muls[i] * nums[j],
                temp2 += max(dp[i], dp[i+1], temp1[-1]),
            muls = temp1
            dp = temp2
        return dp[0]      
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        res = nums[0]
        cur = first_part = last_part = 1
        count = 0
        for v in nums:
            if v == 0:
                # (v, cur, first_part, last_part).p()
                if count > 1:
                    if cur > 0:
                        res = max(res, cur)
                    else:
                        res = max(res, cur // first_part, cur // last_part)
                # res.p()
                cur = first_part = last_part = 1
                count = 0
            else:
                cur *= v
                last_part *= v
                count += 1
                if first_part > 0:
                    first_part *= v
                if v < 0:
                    last_part = v
            res = max(res, v)
            # (v, res).p()
        if count > 1:
            if cur > 0:
                res = max(res, cur)
            else:
                res = max(res, cur // first_part, cur // last_part)
        return res
