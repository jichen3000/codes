class Solution(object):
    def maxProfit_hard(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit1 = profit2 = 0
        for i in xrange(1, len(prices)):
            pre_profit1 = profit1
            profit1 = max(profit1+prices[i]-prices[i-1], profit2)
            profit2=max(pre_profit1,profit2)
        return max(profit1, profit2)
    def maxProfit_dp(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        using dp, https://soulmachine.gitbooks.io/algorithm-essentials/java/dp/best-time-to-buy-and-sell-stock-with-cooldown.html
        """
        n = len(prices)
        if n <= 1:
            return 0
        hold = [0] * n
        sell = [0] * n
        hold[0] = 0-prices[0]
        for i in xrange(1,n):
            hold[i] = max(hold[i-1], sell[i-2]-prices[i])
            sell[i] = max(sell[i-1], hold[i-1]+prices[i])
        return sell[n-1]
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        using dp, https://soulmachine.gitbooks.io/algorithm-essentials/java/dp/best-time-to-buy-and-sell-stock-with-cooldown.html
        """
        n = len(prices)
        if n <= 1:
            return 0
        pre_hold = 0-prices[0]
        pre_sell1 = pre_sell2 = 0
        sell = 0
        for i in xrange(1,n):
            hold = max(pre_hold, pre_sell2-prices[i])
            sell = max(pre_sell1, pre_hold+prices[i])
            pre_hold = hold
            pre_sell2,pre_sell1 = pre_sell1, sell
        return sell

# review
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0: return 0
        dp = [[0]*n for _ in xrange(n)]
        for l in range(1, n):
            for i in range(n-l):
                j = i + l
                dp[i][j] = max((dp[i][k-1] if k-1>i else 0) + (dp[k+1][j] if k+1 < j else 0) for k in range(i,j+1))
                dp[i][j] = max(dp[i][j], prices[j]-prices[i])
                # (i,j,prices[i], prices[j],dp[i][j]).p()
        return dp[0][-1]

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0: return 0
        # last index
        last_sell_i = -10
        dp = [0] * n
        for i in range(1,n):
            should_sell = False
            cur = prices[i] - prices[i-1]
            dp[i] = dp[i-1]
            if cur > 0:
                if i - last_sell_i <= 2:
                    dp[i] = max(dp[i-3] + cur, dp[i-2] + prices[i] - prices[i-2], dp[i-1])
                    if dp[i-3] + cur > dp[i-1] or dp[i-2] + prices[i] - prices[i-2] > dp[i-1]:
                        should_sell = True
                else:
                    dp[i] = dp[i-1] + cur
                    should_sell = True
                # (i, prices[i], cur, last_sell_i, dp[i]).p()
                if i + 1 < n and prices[i] > prices[i+1] and should_sell:
                    last_sell_i = i
        return dp[-1]
    # wonderful idea
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1: return 0
        sell = [0] * n
        buy = [0] * n
        buy[0] = -prices[0]
        rest = [0] * n
        for i in range(1,n):
            sell[i] = max(sell[i-1], buy[i-1]+prices[i])
            buy[i] = max(buy[i-1], rest[i-1]-prices[i])
            rest[i] = max(rest[i-1], sell[i-1], buy[i-1])
        return sell[-1]

    # wonderful idea 2
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1: return 0
        sell, pre_sell = 0, 0
        buy, pre_buy = 0, -prices[0]
        rest = 0
        for i in range(1,n):
            sell = max(pre_sell, pre_buy+prices[i])
            buy = max(pre_buy, rest-prices[i])
            rest = max(rest, pre_sell, pre_buy)
            pre_sell, pre_buy = sell, buy
        return sell
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().maxProfit([6,1,3,2,4,7]).must_equal(6)