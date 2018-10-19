import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1: return 0
        max_p = prices[-1]
        max_profit = 0
        for i in range(n-2,-1,-1):
            max_p = max(max_p, prices[i])
            max_profit = max(max_profit, max_p - prices[i])
        return max_profit
    # this method is really important, since it also work in 123        
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold1, sell1 = -sys.maxint, 0
        for p in prices:
            # The maximum if we've just sold stock so far.
            sell1 = max(sell1, hold1 + p)
            # The maximum if we've just buy  stock so far        
            hold1 = max(hold1,  - p)
            # (p, sell2, hold2, sell1, hold1).p()
        return sell1
    # state machine
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy, sell = -float("inf"), 0
        for p in prices:
            buy = max(buy, -p)
            sell = max(sell, buy+p)
        return sell

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().maxProfit([7, 1, 5, 3, 6, 4]).must_equal(5)
