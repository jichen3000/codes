from itertools import permutations, combinations

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