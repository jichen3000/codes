def solve(graph_grid):
    n = len(graph_grid)
    if n < 2: return []
    # sums is the key of this algorithm
    sums = [0] * n
    for i in xrange(n):
        for j in xrange(n):
            if i != j:
                sums[i] -= graph_grid[i][j]
                sums[j] += graph_grid[i][j]
    sums = [(value,i) for i, value in enumerate(sums) if value != 0]
    if len(sums) == 0: return []
    sums.sort()
    # sums.p()
    first_v, first_i = sums.pop(0)
    last_v, last_i = sums.pop()
    results = []
    while len(sums) > 0 or last_v != 0:
        # (first_v, first_i, last_v, last_i).p()
        cur_sum = first_v + last_v
        if cur_sum > 0:
            # (first_i, last_i, -first_v).p()
            results += (first_i, last_i, -first_v),
            first_v, first_i = sums.pop(0)
            last_v = cur_sum
        elif cur_sum < 0:
            # (first_i, last_i, last_v).p()
            results += (first_i, last_i, last_v),
            last_v, last_i = sums.pop()
            first_v = cur_sum
        else:
            # (first_i, last_i, last_v).p()
            results += (first_i, last_i, last_v),
            if len(sums) == 0: break
            first_v, first_i = sums.pop(0)
            last_v, last_i = sums.pop()
    return results

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        graph_grid = [
            [0, 1000, 2000],
            [0, 0, 5000],
            [0, 0, 0]
        ]
        solve(graph_grid).must_equal([(1, 2, 4000), (0, 2, 3000)])
        graph_grid = [
            [0, 100, 200, 0, 0, 0],
            [0, 0, 500, 50, 0, 0],
            [0, 0, 0, 0, 650, 0],
            [0, 50, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 150],
            [0, 0, 0, 0, 0, 0],
        ]
        solve(graph_grid).must_equal(
                [(1, 4, 400), (0, 4, 100), (0, 5, 150), (0, 2, 50)])



