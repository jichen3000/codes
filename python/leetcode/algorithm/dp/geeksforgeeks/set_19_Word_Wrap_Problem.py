# 35mins, get this recursive one
def solve(s, limit):
    if len(s) == 0: return 0
    if len(s) < limit:
        return (limit - len(s)) ^ 3
    words = s.split(" ")
    def inner(words):
        words.p()
        n = len(words)
        if n == 0:
            return 0
        for i in xrange(n-1,-1,-1):
            cur_l = len(" ".join(words[i:]))
            if cur_l <= limit:
                result += (limit-cur_l) ** 3 + inner(words[:i]),
            else:
                break
        return min(result)
    return inner(words)

# 60mins
def solve(s, limit):
    if len(s) == 0: return 0
    if len(s) < limit:
        return (limit - len(s)) ^ 3
    words = s.split(" ")
    n = len(words)
    if n == 0: return 0
    dp = [0] * (n+1)
    # dp[0] = (limit - len(words[0])) ** 3
    for i in xrange(1,n+1):
        values = []
        for j in xrange(i-1,-1,-1):
            l = len(" ".join(words[j:i]))
            if l <= limit:
                values += (limit - l) ** 3 + dp[j],
            else:
                break
        dp[i] = min(values)
    # dp.p()
    return dp[-1]
if __name__ == '__main__':
    from minitest import *

    with test(solve):
        solve("Geeks for Geeks presents word wrap problem", 15).p()
