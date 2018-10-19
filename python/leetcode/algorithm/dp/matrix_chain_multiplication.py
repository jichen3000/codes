# code see set_8_Matrix_Chain_Multiplication.py
# Introduction-to-algorithm-3rdEdtition.pdf page 400
def solve(shape_list):
    n = len(shape_list)
    if n <=1:
        return 0
    p = [c for r,c in shape_list]
    p.insert(0,shape_list[0][0])
    # p.p()
    m = [[0 for _ in xrange(n+1)] for _ in xrange(n+1)]
    # s = [[0 for _ in xrange(n+1)] for _ in xrange(n+1)]
    # for i in xrange(1,n+1):
    #     m[i][i] = 0
    for l in xrange(2, n+1):
        for i in xrange(1,n-l+1+1):
            j = i + l -1
            m[i][j] = float('inf')
            for k in xrange(i,j):
                q = m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                (l,i,j,k,q).p()
                if q < m[i][j]:
                    m[i][j] = q
                    # s[i][j] = k
    m.pp()
    # s.pp()
    return m[1][n]

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        shape_list=[(30,35),(35,15),(15,5),(5,10),(10,20),(20,25)]
        solve(shape_list).p()

