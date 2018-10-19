import sys
def solve(graph_grid, center_count):
    n = len(graph_grid)
    if n == 0: return 0
    if center_count < 1: return -1
    centers = [0]
    while len(centers) < center_count:
        pre_center = centers[-1]
        max_dist, next_center = max((graph_grid[pre_center][i],i) 
                for i in range(n) if i != pre_center)
        centers += next_center,
    return centers

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        # only gurantee that the min_max_distance is <= 2a
        # in this case optimal is choose 2,3 then a == 6
        # but this sovle would be 0,1, and min_max_distance == 7
        # but 7 < 12, so it is ok.
        graph_grid = [
            [0, 10, 7, 6],
            [10, 0, 8, 5],
            [7, 8, 0, 12],
            [6, 5, 12, 0]
        ]
        solve(graph_grid, 2).must_equal([0,1])

