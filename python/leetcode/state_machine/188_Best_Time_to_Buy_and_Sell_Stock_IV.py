import sys
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if k == 0 or n == 0: return 0
        if k < n / 2:
            sells = [0] * k
            holds = [-sys.maxint] * k
            # print n, k
            for p in prices:
                for j in range(k-1,0,-1):
                    sells[j] = max(sells[j], holds[j] + p)
                    holds[j] = max(holds[j], sells[j-1] - p)
                sells[0] = max(sells[0], holds[0] + p)
                holds[0] = max(holds[0], -p)
            return sells[-1]
        else:
            profit = 0
            for i in range(1, n):
                if prices[i] > prices[i-1]:
                    profit += prices[i] - prices[i-1]
            return profit
                
        
        