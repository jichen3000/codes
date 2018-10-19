
class Solution(object):
    # first coins, then amount
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        m = len(coins)
        if amount==0: return 1
        if m == 0: return 0
        dp = [[0]*(amount+1) for _ in xrange(m)]
        for i in range(m):
            for j in range(1,amount+1):
                dp[i][j] = dp[i-1][j]
                if j >= coins[i]:
                    if coins[i] % j == 0:
                        dp[i][j] += 1
                    dp[i][j] += dp[i][j-coins[i]]
        # dp.pp()
        return dp[-1][-1]
    # first coins, then amount
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount==0: return 1
        dp = [0]*(amount+1)
        for i in range(len(coins)):
            for j in range(coins[i],amount+1):
            # for j in range(amount,coins[i]-1,-1):
                if coins[i] % j == 0:
                    dp[j] += 1
                dp[j] += dp[j-coins[i]]
        return dp[-1]

    # first amount, then coins, in this method, 
    # cannot using only one array on dp
    # if using array for amount, the coins loop cannot add correct value
    # if using array for coins, cannot get the previouse amount
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if amount==0: return 1
        if len(coins) == 0: return 0
        dp = [[1] * len(coins) for _ in xrange(amount+1)]
        for i in xrange(1,amount + 1):
            for j in xrange(len(coins)):
                no_cur_coin = dp[i][j-1] if j>0 else 0
                no_cur_value = dp[i-coins[j]][j] if i >= coins[j] else 0
                dp[i][j] = no_cur_coin + no_cur_value
        # dp.pp()
        return dp[-1][-1]




if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().change(0,[]).must_equal(1)
        # Solution().change(0,[7]).must_equal(1)
        # Solution().change(7,[]).must_equal(0)
        # Solution().change(10,[1,2,5]).must_equal(10)
        Solution().change(4,[1,2,5]).must_equal(3)
        # Solution().change(5,[1,2,5]).must_equal(4)
        # Solution().change(7,[1,2,5]).must_equal(6)
        # Solution().change(10,[1,2,5]).must_equal(10)
        # Solution().change(100,[1,2,5]).must_equal(541)
