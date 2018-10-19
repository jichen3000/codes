class Solution:
    def __init__(self):
        self.mem = {}
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) <= 1: 
            return 0
        if len(cost) in self.mem:
            return self.mem[len(cost)]
        res = min(cost[0]+self.minCostClimbingStairs(cost[1:]),
                  cost[1]+self.minCostClimbingStairs(cost[2:]))
        self.mem[len(cost)] = res
        return res
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        if len(cost) <= 1: 
            return 0
        p1, p2 = cost.pop(0), cost.pop(0)
        for cur in cost:
            p = min(p1, p2) + cur
            p2, p1 = p, p2
        return min(p1, p2)
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        if n <= 1: return 0
        dp = [0] * (n+1)
        for i in range(2,n+1):
            dp[i] = min(dp[i-1]+cost[i-1], dp[i-2]+cost[i-2])
        return dp[-1]
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        n = len(cost)
        if n <= 1: return 0
        pre1, pre2, cur = 0, 0, 0
        for i in range(2,n+1):
            cur = min(pre1+cost[i-1], pre2+cost[i-2])
            pre1, pre2 = cur, pre1
        return cur        
        