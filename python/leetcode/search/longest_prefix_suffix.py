def get_lps(s):
    if len(s) == 0: return []
    lps = [0]
    i, j = 1, 0
    while i < len(s):
        if s[i] == s[j]:
            j += 1
            lps += j,
            i += 1
        else:
            if j > 0:
                # if j = lps[j-1], will not stop at "AAACAAAA"
                j = lps[j-1]
            else:
                lps += 0,
                i += 1
    return lps
        

if __name__ == '__main__':
    from minitest import *

    with test("Solution"):
        get_lps("AAACAAAA").must_equal([0, 1, 2, 0, 1, 2, 3, 3])
        
