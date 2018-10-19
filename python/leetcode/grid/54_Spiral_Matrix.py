class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m = len(matrix)
        if m == 0: return []
        n = len(matrix[0])
        res = []
        min_v = min(m,n)
        for l in range(min_v):
            i = l
            for j in range(l, n-1-l):
                res += matrix[i][j],
            j = n - 1 - l
            for i in range(l, m-1-l):
                res += matrix[i][j],
            i = m - 1 - l
            for j in range(n-1-l, l, -1):
                res += matrix[i][j],
            j = l
            for i in range(m-1-l, l, -1):
                res += matrix[i][j],
        if min_v % 2 == 1:
            l = min_v / 2
            if m <= n:
                i = l
                for j in range(l, n-1-l):
                    res += matrix[i][j],
            else:
                j = l
                for i in range(l, m-1-l):
                    res += matrix[i][j],
        return res
        
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # if matrix:
        #     return list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])
        # else:
        #     return []
        return matrix and list(matrix.pop(0)) + self.spiralOrder(zip(*matrix)[::-1])


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]]).must_equal(
                [1,2,3,6,9,8,7,4,5])
        Solution().spiralOrder([[]]).must_equal(
                [])
