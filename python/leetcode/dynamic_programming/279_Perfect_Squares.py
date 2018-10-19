class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        ss = []
        for i in xrange(1,n+1):
            v = i * i
            if v < n:
                ss += v,
            elif v == n:
                return 1
            else:
                break
        # ss.p()
        # min_v = n
        dp = [[0] * (n+1) for _ in range(len(ss))]
        for i in range(len(ss)):
            s = ss[i]
            for j in range(1, n+1):
                if s > j:
                    dp[i][j] = dp[i-1][j]
                elif s == j:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i][j-ss[k]]+1 for k in range(0,i+1))
                # if j == n:
                #     min_v = min(min_v, dp[i][j])
                # (i,j,dp[i][j]).p()
        return dp[-1][-1]

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        ss = []
        for i in xrange(1,n+1):
            v = i * i
            if v < n:
                ss += v,
            elif v == n:
                return 1
            else:
                break
        dp = [[0] * len(ss) for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(len(ss)):
                s = ss[j]
                if s > i:
                    dp[i][j] = dp[i][j-1]
                elif s == i:
                    dp[i][j] = 1
                else:
                    dp[i][j] = min(dp[i-s][j]+1, dp[i][j-1] if j > 0 else n)
        return dp[-1][-1]
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        ss = []
        for i in xrange(1,n+1):
            v = i * i
            if v < n:
                ss += v,
            elif v == n:
                return 1
            else:
                break
        dp = [0] * (n+1)
        for i in range(1, n+1):
            for j in range(len(ss)):
                if ss[j] <= i:
                    dp[i] = min(dp[i-ss[j]]+1, dp[i] if j > 0 else n)
        return dp[-1]

## best one, bfs, tree
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares= []
        for i in range(1, n+1):
            cur = i * i
            if cur < n:
                squares += cur,
            elif cur == n:
                return 1
            else:
                break
        count = 0
        check_set = {n}
        while check_set:
            count += 1
            temp = set()
            for v in check_set:
                for s in squares:
                    if v == s:
                        return count
                    elif v < s:
                        break
                    temp.add(v-s)
            check_set = temp
        return count

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().numSquares(1).must_equal(1)
        Solution().numSquares(3).must_equal(3)
        Solution().numSquares(12).must_equal(3)
        Solution().numSquares(13).must_equal(2)
        Solution().numSquares(43).must_equal(3)
        Solution().numSquares(6922).must_equal(2)
