# Enter your code here. Read input from STDIN. Print output to STDOUT

def get_full_matrix(row_count, col_count):
    return [["O" for j in xrange(col_count)] for i in xrange(row_count)]

def get_detonated_matrix(row_count, col_count, matrix):
    for i in xrange(row_count):
        for j in xrange(col_count):
            #print(i,j,matrix[i][j])
            if matrix[i][j] == "O":
                matrix[i][j] = "+"
                if i - 1 >=0 and matrix[i-1][j] == ".":
                    matrix[i-1][j] = "+"
                if i + 1 <row_count and matrix[i+1][j] == ".":
                    matrix[i+1][j] = "+"
                if j - 1 >=0 and matrix[i][j-1] == ".":
                    matrix[i][j-1] = "+"
                if j + 1 <col_count and matrix[i][j+1] == ".":
                    matrix[i][j+1] = "+"
    #for cur_row in matrix:
    #    print("".join(cur_row))

    for i in xrange(row_count):
        for j in xrange(col_count):
            if matrix[i][j] == ".":
                matrix[i][j] = "O"
            else:
                matrix[i][j] = "."
    return matrix

          



    
def main(row_count, col_count, the_second, matrix):
    if the_second < 2:
        return matrix
    elif the_second % 2 == 0:
        return get_full_matrix(row_count, col_count)
    if the_second == 3:
        first_detonated_matrix = get_detonated_matrix(row_count, col_count, matrix)
        return first_detonated_matrix
    if the_second == 5: 
        first_detonated_matrix = get_detonated_matrix(row_count, col_count, matrix)
        new_origin_matrix = get_detonated_matrix(row_count, col_count, first_detonated_matrix)
        return new_origin_matrix
    #if the_second > 4:
    first_detonated_matrix = get_detonated_matrix(row_count, col_count, matrix)
    new_origin_matrix = get_detonated_matrix(row_count, col_count, first_detonated_matrix)
    if (the_second-1) % 4 == 0:
        return new_origin_matrix
    elif (the_second+1) % 4 == 0:
        return get_detonated_matrix(row_count, col_count, new_origin_matrix)

row_count, col_count, the_second = map(int, raw_input().strip().split(" "))
matrix = []
for i in xrange(row_count):
    #print(i)
    #print(raw_input().strip())
    one_row = list(raw_input().strip())
    matrix.append(one_row)
    
for cur_row in main(row_count, col_count, the_second, matrix):
    print("".join(cur_row))
    

