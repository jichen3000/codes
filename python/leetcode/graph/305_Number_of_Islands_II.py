class Solution:
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        parents = [[None] * n for _ in range(m)]
        res = []
        dirs = [(0,1),(1,0),(0,-1),(-1,0)]
        def get_nexts(i, j):
            res = []
            for di, dj in dirs:
                ni, nj = di + i, dj + j
                if ni >= 0 and ni < m and nj >= 0 and nj < n and parents[ni][nj]:
                    res += (ni, nj),
            return res

        count = 0
        def find(si, sj):
            ci, cj = si, sj
            while (si, sj) != parents[si][sj]:
                si, sj = parents[si][sj]
            # path compression
            parents[ci][cj] = (si, sj)
            return (si, sj)
        def union(src, dst):
            si, sj = src
            di, dj = dst
            parents[si][sj] = (di, dj)

        for i, j in positions:
            if not parents[i][j]:
                parents[i][j] = (i, j)
                src_parent = (i, j)
            else:
                src_parent = find(i, j)
            count += 1

            for ni, nj in get_nexts(i, j):
                dst_parent = find(ni, nj)
                if src_parent != dst_parent:
                    count -= 1
                    union(src_parent, dst_parent)
                    src_parent = dst_parent
            res += count,
        return res


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().numIslands2(3,3,[[0,0],[0,1],[1,2],[2,1]]).must_equal([1,1,2,3])


        

