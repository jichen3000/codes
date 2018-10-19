def simple_permutations(the_list):
    n = len(the_list)
    indeces = range(n)
    dp = [ [[0]] for i in range(n)]
    for i in range(1, n):
        dp[i] = []
        for cur_list in dp[i-1]:
            for j in range(len(cur_list), -1, -1):
                cur = cur_list[:]
                cur.insert(j, i)
                dp[i] += cur,
    return [[the_list[i] for i in cur_list] for cur_list in dp[-1]]

def permutations(iterable, r=None):
    # permutations('ABCD', 2) --> AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) --> 012 021 102 120 201 210
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = range(n)
    cycles = range(n, n-r, -1)
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
if __name__ == '__main__':
    from minitest import *

    with test(simple_permutations):
        # simple_permutations(range(4)).p()
        list(permutations(range(5),3)).p()



