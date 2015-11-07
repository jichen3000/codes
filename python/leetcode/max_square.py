# 1 0 1 0 0
# 1 0 1 1 1
# 1 1 1 1 1
# 1 0 0 1 0
def find_square(matrix, row_start, col_start, row_count, col_count):
    # min(row_count-row_start, col_count-col_start).p()
    for square_index in range(1, min(row_count-row_start, col_count-col_start)):
        if matrix[row_start+square_index][col_start+square_index] == 0:
            return square_index
        else:
            for j in range(col_start, col_start+square_index+1):
                if matrix[row_start+square_index][j] == 0:
                    return square_index
            for i in range(row_start, row_start+square_index+1):
                if matrix[i][col_start+square_index] == 0:
                    return square_index

    return min(row_count-row_start, col_count-col_start)

def find_max(matrix, row_count, col_count):
    max_value = 1
    point = None
    for i in range(row_count):
        for j in range(col_count):
            if matrix[i][j] != 0:
                max_index = find_square(matrix, i, j, row_count, col_count)
                if max_index > max_value:
                    max_value = max_index
                    point = (i,j)
    return (point, max_value)

if __name__ == '__main__':
    from minitest import *

    with test(find_square):
        matrix = [  [1, 0, 1, 0, 0, 0, 0, 0, 0],
                    [1, 0, 1, 1, 1, 1, 1, 1, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 0],
                    [1, 0, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 1, 0, 0, 1, 1, 1, 1]]
        # find_square(matrix, 0, 0, len(matrix), len(matrix[0])).p()
        find_square(matrix, 1, 2, len(matrix), len(matrix[0])).p()
        find_square(matrix, 2, 5, len(matrix), len(matrix[0])).p()

    with test(find_max):
        find_max(matrix, len(matrix), len(matrix[0])).p()
        pass

