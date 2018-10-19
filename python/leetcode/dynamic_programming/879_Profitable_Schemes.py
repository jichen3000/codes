'''
Example 1:

Input: G = 5, P = 3, group = [2,2], profit = [2,3]
Output: 2
Explanation: 
To make a profit of at least 3, the gang could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.

Example 2:

Input: G = 10, P = 5, group = [2,3,5], profit = [6,7,8]
Output: 7
Explanation: 
To make a profit of at least 5, the gang could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).


good solution
https://leetcode.com/problems/profitable-schemes/discuss/154636/C++-O(PGn)-top-down-DP-solution
so basic idea of all posible from a 0-1 list, choose or not choose, every item only can choose once
that's the key of knapsack essential.

in this quiz
must satisfied: dfs(k, other_value) = dfs(k-1, other_value) + dfs(k-1, other_value - values[k])
k is the index of elements, values are list of value for elements.
first part means if not choose k element, using same value, how many posible solutions
second part equals if choose k element, how many posible solutions
there is no overlap in these two parts
'''


class Solution:
    def profitableSchemes(self, g_count, min_p, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        gp = list(zip(group, profit))
        gp.sort()
        res = []
        for g, p in gp:
            if g > g_count:
                break
            n = len(res)
            for i in range(n):
                cg, cp = res[i]
                if cg + g <= g_count:
                    res.append([cg + g, cp + p])
            res.append([g, p])
        count = 0
        for g, p in res:
            if p >= min_p:
                count += 1
        return count
    def profitableSchemes(self, g_count, min_p, group, profit):
        """
        :type G: int
        :type P: int
        :type group: List[int]
        :type profit: List[int]
        :rtype: int
        """
        from heapq import heappush, heappop
        gp = list(zip(group, profit))
        gp.sort()
        res = []
        for g, p in gp:
            if g > g_count:
                break
            temp = res[::]
            while temp:
                cg, cp = heappop(temp)
                if cg + g > g_count:
                    break
                heappush(res, [cg + g, cp + p])
            heappush(res, [g, p])
        count = 0
        while res:
            g, p = heappop(res)
            if p >= min_p:
                count += 1
        return count    

    def profitableSchemes(self, max_people, min_profit, group, profits):
        M = 1000000007
        def dfs(k, max_people, min_profit):
            # (k, max_people, min_profit).p()
            if k == 0:
                return 1 if min_profit <= 0 else 0
            if max_people < 0:
                return 0
            if min_profit < 0:
                min_profit = 0
            if dp[k][max_people][min_profit] != -float("inf"):
                return dp[k][max_people][min_profit]
            res = dfs(k-1, max_people, min_profit)
            if max_people >= group[k-1]:
                res += dfs(k-1, max_people-group[k-1], min_profit-profits[k-1])
            res %= M
            dp[k][max_people][min_profit] = res
            return res

        dp = [[[-float("inf")] * (min_profit + 1) for _ in range(max_people + 1)] for _ in range(len(group) + 1)]
        
        res = dfs(len(group), max_people, min_profit)
        # dp.pp()
        return res

if __name__ == '__main__':
    from minitest import *

    with test("some"):
        Solution().profitableSchemes(5, 3, [2,2], [2,3]).must_equal(2)
        Solution().profitableSchemes(10, 5, [2,3,5], [6,7,8]).must_equal(7)