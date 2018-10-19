def optimal_bst(p_list, q_list):
    # notice, p_list from 0 to n-1, but in book from 1 to n
    # so p[i] in book, will be p_list[i-1] here
    n = len(p_list)
    e_matrix = [[0 for j in xrange(n+1)] for i in xrange(n+2)]
    w_matrix = [[0 for j in xrange(n+1)] for i in xrange(n+2)]
    # root_matrix is not a tree, but it can build a tree
    root_matrix = [[0 for j in xrange(n+1)] for i in xrange(n+1)]
    for i in xrange(1,n+2):
        e_matrix[i][i-1] = q_list[i-1]
        w_matrix[i][i-1] = q_list[i-1]
    for l in xrange(1,n+1):
        for i in xrange(1,n-l+1+1):
            j = i + l - 1
            e_matrix[i][j] = float("inf")
            w_matrix[i][j] = w_matrix[i][j-1] + p_list[j-1] + q_list[j]
            for r in xrange(i,j+1):
                cur_value = e_matrix[i][r-1] + e_matrix[r+1][j] + w[i,j]
                if cur_value < e_matrix[i][j]:
                    e_matrix[i][j] = cur_value
                    root_matrix[i][j] = r
    # return optimal value
    return e_matrix[1][n+1]
