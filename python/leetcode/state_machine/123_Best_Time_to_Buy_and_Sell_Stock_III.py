# see 121_Best_Time_to_Buy_and_Sell_Stock.py firstly, then you will understand this snswer.
# two transactions
import math
import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1: return 0
        for i in range(n-2,0,-1):
            if prices[i] == prices[i+1] or (math.copysign(1, prices[i+1]-prices[i]) 
                    == math.copysign(1, prices[i]-prices[i-1])):
                del prices[i]
        n = len(prices)
        if n <= 1: return 0
        def inner(prices):
            n = len(prices)
            if n <= 1: return 0
            max_p = prices[-1]
            max_profit = 0
            for i in range(n-2,-1,-1):
                max_p = max(max_p, prices[i])
                max_profit = max(max_profit, max_p - prices[i])
            return max_profit
        the_max = 0
        for i in range(n):
            the_max = max(the_max, inner(prices[:i])+inner(prices[i:]))
        return the_max
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        hold1, hold2 = -sys.maxint, -sys.maxint
        sell1, sell2 = 0, 0
        for p in prices:
            sell2 = max(sell2, hold2 + p)
            hold2 = max(hold2, sell1 - p)
            sell1 = max(sell1, hold1 + p)
            hold1 = max(hold1,  - p)
            # (p, sell2, hold2, sell1, hold1).p()
        return sell2


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().maxProfit([7, 1, 5, 3, 6, 4]).must_equal(7)
        # Solution().maxProfit([2,1,2,0,1]).must_equal(2)
        # Solution().maxProfit([3,3,5,0,0,3,1,4]).must_equal(6)
        # Solution().maxProfit([1,2,4,2,5,7,2,4,9,0]).must_equal(13)
        # Solution().maxProfit([1,2,4,2,5,7,2,4,9,0,9]).must_equal(17)
