import heapq

a = [1, 4, 7, 10]
b = [2, 5, 6, 11]

if __name__ == '__main__':
    from minitest import *

    with test("merge"):
        list(heapq.merge(a,b)).must_equal(
                [1, 2, 4, 5, 6, 7, 10, 11])
