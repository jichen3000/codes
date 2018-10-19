class Solution(object):
    def coinChange_recursively(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        def inner(amount):
            if amount == 0:
                return 0

            min_n = 99999
            for i in xrange(len(coins)):
                if amount >= coins[i]:
                    result = 1 + inner(amount-coins[i])
                    if result >   0:
                        min_n  = min(result, min_n)

            if min_n == 99999:
                return -1
            else:
                return min_n
        return inner(amount)
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        mem_hash = [0] * (amount+1)
        for m in xrange(1,amount+1):
            # mem_hash[m].p()
            min_r = 99999
            for i in xrange(len(coins)):
                if m>=coins[i] and mem_hash[m-coins[i]] >= 0:
                    min_r = min(min_r, mem_hash[m-coins[i]]+1)
            if min_r == 99999:
                mem_hash[m] = -1
            else:
                mem_hash[m] = min_r
            # mem_hash[m].p()
        # mem_hash.p()
        return mem_hash[amount]
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        coins.sort()
        dp = [0] * (amount + 1)
        for j in range(1, amount + 1):
                dp[j] = j // coins[0] if j % coins[0] == 0 else float("inf")
        for i in range(1, len(coins)):
            for j in range(coins[i], amount + 1):
                dp[j] = min(dp[j-coins[i]] + 1, dp[j])
        # print(dp)
        if dp[-1] == float("inf"):
            return -1
        return dp[-1]
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().coinChange([1],0).must_equal(0)
        Solution().coinChange([1,2,5],11).must_equal(3)
        # Solution().coinChange([2],3).must_equal(-1)