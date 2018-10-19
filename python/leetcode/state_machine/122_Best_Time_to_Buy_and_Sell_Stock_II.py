class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1: return 0
        max_p = prices[-1]
        total_profit, pre_profit = 0, None
        for i in range(n-2,-1,-1):
            if prices[i] >= prices[i+1]:
                max_p = prices[i]
                if pre_profit: total_profit += pre_profit
                pre_profit = None
            else:
                pre_profit = max_p - prices[i]
        if pre_profit: total_profit += pre_profit
        return total_profit


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().maxProfit([7, 1, 5, 3, 6, 4]).must_equal(7)
        Solution().maxProfit([2,1,2,0,1]).must_equal(2)
