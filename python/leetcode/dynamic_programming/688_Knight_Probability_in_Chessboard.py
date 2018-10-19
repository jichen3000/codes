# 48mins
class Solution(object):
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        dirs = [(-2,+1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
        def count_in(K, r, c):
            if K == 0: return 1
            count = 0
            for dx,dy in dirs:
                nx = r + dx
                ny = c + dy
                if nx >= 0 and nx < N and ny >= 0 and ny < N:
                    count += count_in(K-1, nx, ny)
            return count
        count =  count_in(K, r, c)
        print count
        return float(count) / (8 ** K)
    def knightProbability(self, N, K, r, c):
        """
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        if K == 0: return 1
        if N <= 2: return 0
        dirs = [(-2,+1),(-1,2),(1,2),(2,1),(2,-1),(1,-2),(-1,-2),(-2,-1)]
        def get_next(r, c):
            results = []
            for dx,dy in dirs:
                nx = r + dx
                ny = c + dy
                if nx >= 0 and nx < N and ny >= 0 and ny < N:
                    results += (nx,ny),
            return results
        dp = [ [ [0] * N for _ in range(N)] for _ in range(K)]
        for k in range(K):
            for x in range(N):
                for y in range(N):
                    if k == 0:
                        dp[k][x][y] = len(get_next(x,y))
                    else:
                        dp[k][x][y] = sum(dp[k-1][nx][ny] for nx,ny in get_next(x,y))
        print dp[-1][r][c]
        return float(dp[-1][r][c])/(8 ** K)

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().knightProbability(3,2,0,0).must_equal(0.0625)
        Solution().knightProbability(1,0,0,0).must_equal(1)

        