from itertools import product
class Solution(object):
    def change_t(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        coin_max_ranges = [xrange(amount / c + 1) for c in coins]
        all_posibles = product(*coin_max_ranges)
        result = 0
        for cur_p in all_posibles:
            # print("cur_p", cur_p)
            sum_v = sum(p*coins[i] for i,p in enumerate(cur_p))
            if sum_v == amount:
                result += 1
        return result
    # miss a little
    def change_less(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if len(coins) == 0 and amount==0:
            return 1
        cache = [[0 for c in coins] for i in xrange(amount+1)]
        for i in xrange(0,amount+1):
            cur_r = 0
            for  ci in xrange(len(coins)):
                cur_c = coins[ci]
                if ci == 0:
                    # if cur_c  == 1:
                    # else:
                    if i % cur_c == 0:
                        cache[i][ci] = 1
                    else:
                        cache[i][ci] = 0
                else:
                    max_n = i / cur_c
                    # print("i,ci,cur_c,max_n,",i,ci,cur_c,max_n)
                    for j in xrange(max_n):
                        # print("j,i-(j+1)*c,cache[i-(j+1)*c][:ci]",j,i-(j+1)*cur_c,cache[i-(j+1)*cur_c][:ci])
                        cache[i][ci] += sum(cache[i-(j+1)*cur_c][:ci])
            print("i,cache[i]",i,cache[i])
        return sum(cache[amount])

    #
    def change_two(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if len(coins) == 0 and amount==0:
            return 1
        dp = [[0 for i in xrange(amount+1)] for c in xrange(len(coins)+1)]
        dp[0][0] = 1
        for ci in xrange(1,len(coins)+1):
            dp[ci][0] = 1
            cur_c = coins[ci-1]
            for j in xrange(1,amount+1):
                pre = 0
                if j >= cur_c:
                    pre = dp[ci][j-cur_c]
                dp[ci][j] = dp[ci-1][j] + pre
        return dp[len(coins)][amount]

    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if len(coins) == 0 and amount==0:
            return 1
        dp = [0 for i in xrange(amount+1)]
        dp[0] = 1
        for ci in xrange(len(coins)):
            for j in xrange(1,amount+1):
            # dp[j] = 1
                if j >= coins[ci]:
                    dp[j] += dp[j-coins[ci]]
        return dp[amount]




                

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().change_less(10,[1,2,5]).must_equal(10)
        # Solution().change(4,[1,2,5]).must_equal(3)
        # Solution().change(5,[1,2,5]).must_equal(4)
        # Solution().change(7,[1,2,5]).must_equal(6)
        # Solution().change(10,[1,2,5]).must_equal(10)
        # Solution().change(100,[1,2,5]).must_equal(541)
        # Solution().change(500,[1,2,5]).must_equal(12701)
        # Solution().change(10,[10]).must_equal(1)
        # Solution().change(0,[]).must_equal(1)
        # Solution().change(10,[]).must_equal(0)
        # Solution().change(5000,[1,2]).must_equal(2501)
