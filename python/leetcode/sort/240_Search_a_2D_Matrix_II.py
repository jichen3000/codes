class Solution:
    def searchMatrix(self, matrix, target):
        """
        O(m log n)
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        from bisect import bisect_left
        m = len(matrix)
        if m == 0: return False
        n = len(matrix[0])
        if n == 0: return False
        for i in range(m):
            if target < matrix[i][0]:
                return False
            if matrix[i][0] <= target and target <= matrix[i][-1]:
                j = bisect_left(matrix[i], target)
                if j < n and matrix[i][j] == target:
                    return True
        return False

    def searchMatrix(self, matrix, target):
        """
        O(m+n)
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or len(matrix[0]) == 0:
            return False
        i, j = 0, len(matrix[0])-1
        while i < len(matrix) and j >= 0:
            if target == matrix[i][j]:
                return True
            elif target > matrix[i][j]:
                i += 1
            else:
                j -= 1
        return False

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 5).must_equal(True)
        Solution().searchMatrix([[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], 20).must_equal(False)