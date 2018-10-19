# Introduction-to-algorithm-3rdEdition chapter greedy
# pairs will sort by second element, actually, this is not useful for dp
def solve(pairs):
    # this is the dynamic programming
    n = len(pairs)
    if n == 0: return 0
    dp = [1] * n
    for i in xrange(1,n):
        dp[i] = max([dp[j] for j in xrange(i) if pairs[j][1]<=pairs[i][0]] + [0]) + 1
    return max(dp)


def solve(pairs):
    # this is greedy
    # the list must support sort
    def compare(o1, o2):
        if o1[1] == o2[1]:
            return cmp(o1[0], o2[0])
        else:
            return cmp(o1[1], o2[1])
    sorted(pairs, cmp=compare)
    n = len(pairs)
    if n == 0: return 0
    item = pairs[0]
    count = 1
    for i in xrange(1,n):
        if pairs[i][0] >= item[1]:
            item = pairs[i]
            count += 1
    return count

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        pairs = [(1,4),(3,5),(0,6),(5,7),(3,9),(5,9),(6,10),(8,11),(8,12),(2,14),(12,16)]
        solve(pairs).must_equal(4)