# http://www.geeksforgeeks.org/searching-for-patterns-set-2-kmp-algorithm/
# https://en.wikipedia.org/wiki
# O(n+k)
def kmp(txt, pattern):
    n = len(txt)
 
    # values for pattern
    j = 0 # index for pattern[]
 
    # Preprocess the pattern (calculate lps[] array)
    lps = longest_prefix_suffix(pattern)
    # lps.p()
    results = []
    i = 0 # index for txt[]
    while i < n:
        if pattern[j] == txt[i]:
            i += 1
            j += 1
        if j == len(pattern):
            # print "Found pattern at index " + str(i-j)
            # return i-j
            results += i-j,
            j = lps[j-1]
 
        # mismatch after j matches
        elif i < n and pattern[j] != txt[i]:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
    return results

# another version of kmp, same as longest_prefix_suffix
def kmp(s, p):
    sn, pn = len(s), len(p)
    lps = longest_prefix_suffix(p)
    # lps.p()
    i, j = 0, 0
    res = []
    count = 0
    while i < sn and count < 30:
        # (i,j,s[i],p[j],res).p()
        if s[i] == p[j]:
            i += 1
            j += 1
            if j == pn:
                res += i - pn,
                j -= 1
        else:
            if j > 0:
                j = lps[j-1]
            else:
                i += 1
        count += 1
    return res 
    
def longest_prefix_suffix(pattern):
 
    lps = [0] * len(pattern)
    i = 1
    # length of the previous longest prefix suffix
    j = 0 
 
    # the loop calculates lps[i] for i = 1 to M-1
    while i < len(pattern):
        if pattern[i]==pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar 
            # to search step.
            if j != 0:
                # Also, note that we do not increment i here
                j = lps[j-1]
            else:
                lps[i] = 0
                i += 1
    return lps
 
if __name__ == '__main__':
    from minitest import *

    with test(longest_prefix_suffix):
        longest_prefix_suffix("ababbbabbaba#ababbabbbaba").must_equal([0, 0, 1, 2, 0, 0, 1, 2, 0, 1, 2, 3, 0, 1, 2, 3, 4, 5, 1, 2, 0, 0, 1, 2, 3])
        longest_prefix_suffix("ABABCABAB").must_equal([0, 0, 1, 2, 0, 1, 2, 3, 4])
        longest_prefix_suffix("AAACAAAA").must_equal([0, 1, 2, 0, 1, 2, 3, 3])
        longest_prefix_suffix("abababab").must_equal([0, 0, 1, 2,3,4,5,6])
    with test(kmp):
        kmp("ABABDABACDABABCABAB", "ABABCABAB").must_equal([10])
        kmp("AAAAABAAABA", "AAAA").must_equal([0,1])
        kmp("ABC ABCDAB ABCDABCDABDE", "ABCDABD").must_equal([15])