class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        self.matrix = matrix
        if self.matrix and self.matrix[0]:
            self.bit = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]
            for x in range(1,len(matrix)+1):
                for y in range(1,len(matrix[0])+1):
                    self.__update(x,y, self.matrix[x-1][y-1])
        
    def __update(self, x, y, diff):
        while x < len(self.bit):
            tempy = y
            while tempy < len(self.bit[0]):
                self.bit[x][tempy] += diff
                tempy += tempy & -tempy
            x += x & -x

    def __get_sum(self, x, y):
        res = 0
        while x > 0:
            tempy = y
            while tempy > 0:
                # tempy.p()
                res += self.bit[x][tempy]
                tempy -= tempy & -tempy
            x -= x & -x
        return res

    def update(self, row, col, val):
        """
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        diff = val - self.matrix[row][col]
        self.__update(row+1, col+1, diff)
        self.matrix[row][col] = val
        
        

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        # self.__get_sum(row1, col1).p()
        return self.__get_sum(row2+1, col2+1) - \
                self.__get_sum(row2+1, col1) - \
                self.__get_sum(row1, col2+1) + \
                self.__get_sum(row1, col1)

if __name__ == '__main__':
    from minitest import *

    with test(""):
        matrix = [[3,0,1,4,2],[5,6,3,2,1],[1,2,0,1,5],[4,1,0,1,7],[1,0,3,0,5]]
        obj = NumMatrix(matrix)
        obj.sumRegion(2,1,4,3).must_equal(8)
        obj.update(3,2,2)
        obj.sumRegion(2,1,4,3).must_equal(10)

        matrix = [[1]]
        obj = NumMatrix(matrix)
        obj.sumRegion(0,0,0,0).must_equal(1)
        obj.update(0,0,-1)
        obj.sumRegion(0,0,0,0).must_equal(-1)
