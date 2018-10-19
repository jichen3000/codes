class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        chains = [[nums[0]]]
        max_len = 1
        for i in nums:
            added = False
            for chain_i in xrange(len(chains)):
                chain = chains[chain_i]
                if i > chain[-1]:
                    # if i - 1 > chain[-1]:
                    #     chains.append(chain[:])
                    chain.append(i)
                    added = True
                    max_len = max(len(chain), max_len)
                elif i < chain[-1]:
                    if len(chain) == 1:
                        chain[-1] = i
                        added = True
                    elif chain[-2] < i:
                        chain[-1] = i
                        added = True
            if not added:
                chains.append([i])
        return max_len
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return 0

        dp = [1] * n
        for i in xrange(1,len(nums)):
            for j in xrange(0,i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i],dp[j]+1)
        return max(dp)
            

                        
                
                        
                
        