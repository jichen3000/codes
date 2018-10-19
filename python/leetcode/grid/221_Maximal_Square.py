class Solution(object):
    # naive solution
    def maximalSquare(self, g):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not g or not g[0]:
            return 0
        res = 0
        # visited = set()
        m, n = len(g), len(g[0])
        for i in range(m):
            for j in range(n):
                if g[i][j] == "1":
                    # visited.add((i,j))
                    l = 0
                    for l in range(1, min(m-i, n-j)+1):
                        if j + l >= n or i + l >= m:
                            break
                        is_all = True
                        nj = j + l
                        for ni in range(i, i+l+1):
                            # visited.add((ni,nj))
                            if g[ni][nj] != "1":
                                is_all = False
                                break
                        ni = i + l
                        for nj in range(j, j+l):
                            # visited.add((ni,nj))
                            # (ni, nj).p()
                            if g[ni][nj] != "1":
                                is_all = False
                                break
                        if not is_all: 
                            break
                    res = max(res, 1, l**2)
        return res
    ## Maximal Rectangle
    def maximalSquare(self, g):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not g or not g[0]:
            return 0
        res = 0
        m, n = len(g), len(g[0])
        h, l, r = [0] * n, [0] * n, [n-1] * n
        for i in range(m):
            # for heights
            for j in range(n):
                if g[i][j] == "1":
                    h[j] += 1
                else:
                    h[j]  = 0

            # for lefts
            leftest = n-1
            for j in range(n):
                if g[i][j] == "1":
                    leftest = min(j, leftest)
                    l[j] = max(leftest, l[j])
                else:
                    leftest = n-1
                    l[j] = 0
            # for rights
            rightest = 0
            for j in range(n-1, -1, -1):
                if g[i][j] == "1":
                    rightest = max(j, rightest)
                    r[j] = min(rightest, r[j])
                else:
                    rightest  = 0
                    r[j] = n-1

            # (i,h).p()
            # (i,l).p()
            # (i,r).p()
            for j in range(n):
                w = r[j] + 1 - l[j]
                w = min(w, h[j])
                res = max(res, w*w)
        return res        
    # Maximal Rectangle
    def maximalSquare(self, g):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not g or not g[0]:
            return 0
        res = 0
        m, n = len(g), len(g[0])
        h, l, r = [0] * n, [0] * n, [n-1] * n
        for i in range(m):
            # for heights
            for j in range(n):
                if g[i][j] == "1":
                    h[j] += 1
                else:
                    h[j]  = 0

            # for lefts
            closest_0 = -1
            for j in range(n):
                if g[i][j] == "1":
                    l[j] = max(closest_0+1, l[j])
                else:
                    l[j] = 0
                    closest_0 = j
            # for rights
            closest_0 = n
            for j in range(n-1, -1, -1):
                if g[i][j] == "1":
                    r[j] = min(closest_0-1, r[j])
                else:
                    r[j] = n-1
                    closest_0 = j

            # (i,h).p()
            # (i,l).p()
            # (i,r).p()
            for j in range(n):
                w = r[j] + 1 - l[j]
                w = min(w, h[j])
                res = max(res, w*w)
        return res


                    

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().maximalSquare([
                ["1","1"],
                ["1","1"]]).must_equal(4)

        Solution().maximalSquare([
                ["1","0","1","0","0"],
                ["1","0","1","1","1"],
                ["1","1","1","1","1"],
                ["1","0","0","1","0"]
                ]).must_equal(4)

        Solution().maximalSquare([
                ["0","1","1","0","1"],
                ["1","1","0","1","0"],
                ["0","1","1","1","0"],
                ["1","1","1","1","0"],
                ["1","1","1","1","1"],
                ["0","0","0","0","0"]
                ]).must_equal(9)


