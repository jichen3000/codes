# http://www.geeksforgeeks.org/match-a-pattern-and-string-without-using-regular-expressions/
def solve(the_s, pattern):
    n = len(the_s)
    m = len(pattern)
    def inner(i, j):
        if i == n and j == m: return True
        if i == n or j == m: return False
        cur_p = pattern[j]
        if cur_p in memo:
            cur_len = len(memo[cur_p])
            if memo[cur_p] != the_s[i:i+cur_len]:
                return False
            return inner(i+cur_len, j+1)
        for cur_len in range(1, n-i+1):
            memo[cur_p] = the_s[i:i+cur_len]
            if inner(i+cur_len, j+1):
                return True
            del memo[cur_p]
    memo = {}
    inner(0,0)
    return memo

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        solve("GeeksforGeeks",'aba').pp()

