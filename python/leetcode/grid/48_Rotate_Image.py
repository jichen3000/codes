class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = matrix
        n = len(matrix)
        for i in range(n//2):
            for j in range(i,n-1-i):
                # print(i,j)
                m[j][n-1-i],m[n-1-i][n-1-j],m[n-1-j][i],m[i][j] = \
                        m[i][j], m[j][n-1-i],m[n-1-i][n-1-j],m[n-1-j][i]
                        
        