# Introduction-to-algorithm-3rdEdtition.pdf page 412 
from collections import defaultdict
def solve_consecutive(s1, s2):
    '''
        this is for consecutive subsequence
    '''
    max_len = 0
    start_i = -1
    if len(s1) >= len(s2):
        long_s,short_s = s1, s2
    else:
        long_s,short_s = s2, s1
    if len(short_s) == 0:
        return start_i,max_len
    m = defaultdict(list)
    for i in xrange(len(long_s)-1):
        for j in xrange(i, len(long_s)):
            ij_len = j-i+1
            if ij_len == 1:
                for k in xrange(len(short_s)):
                    if short_s[k] == long_s[i]:
                        m[(i,j)].append(k)
                        if ij_len > max_len:
                            max_len =  ij_len
                            start_i = i
            else:
                for k in m[(i,j-1)]:
                    if k + ij_len - 1 < len(short_s):
                        if short_s[k + ij_len - 1] == long_s[j]:
                            m[(i,j)].append(k)
                            if ij_len > max_len:
                                max_len =  ij_len
                                start_i = i
    return start_i,max_len

def solve_topdown(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return ""
    def inner(s1, s2):
        if len(s1) >= len(s2):
            long_s,short_s = s1, s2
        else:
            long_s,short_s = s2, s1
        if len(short_s) == 1:
            if short_s[0] in long_s:
                return short_s[0]
            else:
                return ""
        if short_s[-1] == long_s[-1]:
            return inner(long_s[:-1], short_s[:-1])+short_s[-1]
        else:
            result1 = inner(long_s, short_s[:-1])
            result2 = inner(long_s[:-1], short_s)
            if len(result1) > len(result2):
                return result1
            else:
                return result2
    return inner(s1,s2)

def solve_topdown_memory(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return ""
    m = {}
    def inner(s1, s2):
        if len(s1) == 1:
            if s1 in s2:
                m[(1,len(s2))] =  s1
            else:
                m[(1,len(s2))] =  ''
            return m[(1,len(s2))]
        if len(s2) == 1:
            if s2 in s1:
                m[(len(s1),1)] =  s2
            else:
                m[(len(s1),1)] =  ''
            return m[(len(s1),1)]

        if s2[-1] == s1[-1]:
            if (len(s1)-1,len(s2)-1) not in m:
                m[(len(s1)-1,len(s2)-1)] = inner(s1[:-1], s2[:-1])
            
            m[(len(s1),len(s2))] = m[(len(s1)-1,len(s2)-1)] +s1[-1]
        else:
            if (len(s1),len(s2)-1) not in m:
                m[(len(s1),len(s2)-1)] = inner(s1, s2[:-1])
            if (len(s1)-1,len(s2)) not in m:
                m[(len(s1)-1,len(s2))] = inner(s1[:-1], s2)
            if len(m[(len(s1),len(s2)-1)]) > len(m[(len(s1)-1,len(s2))]):
                m[(len(s1),len(s2))] = m[(len(s1),len(s2)-1)]
            else:
                m[(len(s1),len(s2))] = m[(len(s1)-1,len(s2))] 
        return m[(len(s1),len(s2))]
    return inner(s1,s2)

def solve_bottomup(s1, s2):
    if len(s1) == 0 or len(s2) == 0:
        return ""
    if len(s1) >= len(s2):
        long_s,short_s = s1, s2
    else:
        long_s,short_s = s2, s1
    if len(short_s) == 1:
        if short_s[0] in long_s:
            return short_s[0]
        else:
            return ""
    m = [['' for j in xrange(len(s2))] for i in xrange(len(s1))]
    for i in xrange(1,len(s1)):
        for j in xrange(1,len(s2)):
            if s1[i] == s2[j]:
                m[i][j] = m[i-1][j-1] + s1[i]
            else:
                if len(m[i][j-1]) > len(m[i-1][j]):
                    m[i][j] = m[i][j-1]
                else:
                    m[i][j] = m[i-1][j]
    return m[len(s1)-1][len(s2)-1]


if __name__ == '__main__':
    from minitest import *

    # with test(solve_consecutive):
    #     s1 = "ABCDEFG"
    #     s2 = "MMMEFGM"
    #     solve_consecutive(s1,s2).must_equal((4, 3))
    #     s1 = "ABCDEFG"
    #     s2 = "LLLL"
    #     solve_consecutive(s1,s2).must_equal((-1, 0))
    #     s1 = "ABCDEFGMMMM"
    #     s2 = "MMMEFGM"
    #     solve_consecutive(s1,s2).must_equal((4, 4))
    #     s1 = "ABCDEFGMMMM"
    #     s2 = "EZ"
    #     solve_consecutive(s1,s2).must_equal((4, 1))
    with test(solve_topdown):
        s1 = "ABCDEFGXXXY"
        s2 = "MMMEFGMY"
        solve_topdown(s1,s2).must_equal('EFGY')
        s1 = "ABCDEFG"
        s2 = "LLLL"
        solve_topdown(s1,s2).must_equal('')
        s1 = "ABCDEFGMMMM"
        s2 = "MMMEFGM"
        solve_topdown(s1,s2).must_equal('EFGM')
        s1 = "ABCDEFGMMMM"
        s2 = "E"
        solve_topdown(s1,s2).must_equal('E')


    with test(solve_topdown_memory):
        s1 = "ABCDEFGXXXY"
        s2 = "MMMEFGMY"
        solve_topdown_memory(s1,s2).must_equal('EFGY')
        s1 = "ABCDEFG"
        s2 = "LLLL"
        solve_topdown_memory(s1,s2).must_equal('')
        s1 = "ABCDEFGMMMM"
        s2 = "MMMEFGM"
        solve_topdown_memory(s1,s2).must_equal('EFGM')
        s1 = "ABCDEFGMMMM"
        s2 = "E"
        solve_topdown_memory(s1,s2).must_equal('E')

    with test(solve_bottomup):
        s1 = "ABCDEFGXXXY"
        s2 = "MMMEFGMY"
        solve_bottomup(s1,s2).must_equal('EFGY')
        s1 = "ABCDEFG"
        s2 = "LLLL"
        solve_bottomup(s1,s2).must_equal('')
        s1 = "ABCDEFGMMMM"
        s2 = "MMMEFGM"
        solve_bottomup(s1,s2).must_equal('EFGM')
        s1 = "ABCDEFGMMMM"
        s2 = "E"
        solve_bottomup(s1,s2).must_equal('E')





