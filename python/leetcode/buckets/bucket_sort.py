# https://www.geeksforgeeks.org/bucket-sort-2/
# O is almost n
def solve(small_ones):
    n = len(small_ones)
    buckets = [ [] for _ in range(n)]
    for f in small_ones:
        i = int(n * f)
        buckets[i] += f,

    results = []
    for l in buckets:
        # if all numbers are uniformly distributed, it take O(n)
        # according CLRS book
        l.sort()
        for f in l:
            results += f,

    return results

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        solve([0.897, 0.565, 0.656, 0.1234, 0.665, 0.3434]).must_equal(
                [0.1234, 0.3434, 0.565, 0.656, 0.665, 0.897])