from itertools import permutations, combinations

def combinations_i(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

if __name__ == '__main__':
    from minitest import *

    with test(permutations):
        items = range(3)
        list(permutations(items)).must_equal(
                [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)])
        list(permutations(items,2)).must_equal(
                [(0, 1), (0, 2), (1, 0), (1, 2), (2, 0), (2, 1)])

    with test(combinations):
        list(combinations(items, 3)).must_equal(
                [(0, 1, 2)])
        list(combinations(items, 2)).must_equal(
                [(0, 1), (0, 2), (1, 2)])

    with test(combinations_i):
        items = "ABCD"
        list(combinations_i(items, 2)).p()