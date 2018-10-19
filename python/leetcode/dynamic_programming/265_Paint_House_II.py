class Solution:
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        O(n k)
        """
        if not costs or not costs[0]:
            return 0
        n, kn = len(costs), len(costs[0])
        # m1 is the most min one, m2 is the second min in the current costs
        m1, m2, i1 = 0, 0, -1
        for i in range(n):
            pre_m1, pre_m2, pre_i1 = m1, m2, i1
            m1 = m2 = float("inf")
            i1 = -1
            for j in range(kn):
                v = costs[i][j] + (pre_m1 if j != pre_i1 else pre_m2)
                if v < m1:
                    m2, m1, i1 = m1, v, j
                elif v < m2:
                    m2 = v
            # print(i1, m1, m2)
        return m1
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        house_count, color_count = len(costs), len(costs[0])
        # dp = costs[0][::]
        min_i, min_v, min_v2 = 0, 0, 0
        for i in range(house_count):
            cur_i, cur_v, cur_v2 = 0, float("inf"), float("inf")
            for j in range(color_count):
                cur = costs[i][j] + (min_v if j != min_i else min_v2)
                if cur < cur_v:
                    cur_v2, cur_v, cur_i = cur_v, cur, j
                elif cur < cur_v2:
                    cur_v2 = cur
            min_i, min_v, min_v2 = cur_i, cur_v, cur_v2
            # print(min_i, min_v, min_v2)
        return  min_v        
    # dp
    # base case: dp[0] = costs[0]
    # recursion rule: dp[i][j] = min(dp[i-1][k] for k in range(n) if k != j) + costs[i][j]
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        dp = costs[0]
        m, n = len(costs), len(costs[0])
        for i in range(1, m):
            pre = dp[::]
            for j in range(n):
                dp[j] = min(pre[k] for k in range(n) if k != j) + costs[i][j]
        return min(dp)
    # follow up:
    # 1, 5, 3
    # 2, 9, 4
    # only need record last min_v and min_j, and second_min
    # so if j != min_j, dp[j] = min_v
    #    else dp[j] = second_min
    # 3, 1
    # 1, 3
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        min_v, min_j, second_min = 0, 0, 0
        m, n = len(costs), len(costs[0])
        for i in range(m):
            pre_min_v, pre_min_j, pre_second_min = min_v, min_j, second_min
            min_v, second_min = float("inf"), float("inf")
            for j in range(n):
                cur = costs[i][j] + (pre_min_v if j != pre_min_j else pre_second_min)
                if cur < min_v:
                    second_min = min_v
                    min_v = cur
                    min_j = j
                elif cur < second_min:
                    second_min = cur
        return min_v        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().minCostII([[1,5,3],[2,9,4]]).must_equal(5)