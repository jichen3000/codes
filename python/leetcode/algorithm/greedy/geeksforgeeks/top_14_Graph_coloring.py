# http://www.geeksforgeeks.org/graph-coloring-set-2-greedy-algorithm/
# 1. Color first vertex with first color.
# 2. Do following for remaining V-1 vertices.
#           a) Consider the currently picked vertex and color it with the 
#              lowest numbered color that has not been used on any previously
#              colored vertices adjacent to it. If all previously used colors 
#              appear on vertices adjacent to v, assign a new color to it.
# memory the result pictures: small fish change tail
from collections import defaultdict
def solve(edges):
    if len(edges) == 0: return 0
    adjs = defaultdict(list)
    vertex_count = 0
    for src, dst in edges:
        adjs[src] += dst,
        adjs[dst] += src,
        vertex_count = max(src, dst, vertex_count)
    vertex_count += 1

    color_availabes = [True] * vertex_count
    results = [-1] * vertex_count
    results[0] = 0
    max_color = 0
    for src in range(1,vertex_count):

        for dst in adjs[src]:
            if results[dst] > -1:
                color_availabes[results[dst]] = False

        for min_color in range(vertex_count):
            if color_availabes[min_color]:
                break
        results[src] = min_color
        max_color = max(min_color, max_color)

        for dst in adjs[src]:
            if results[dst] > -1:
                color_availabes[results[dst]] = True                
    return results

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        edges = [
            (0, 1),
            (0, 2),
            (1, 2),
            (1, 3),
            (2, 3),
            (3, 4),
        ]
        solve(edges).must_equal([0, 1, 2, 0, 1])
        edges = [
            (0, 1),
            (0, 2),
            (1, 2),
            (1, 4),
            (2, 4),
            (4, 3),
        ]
        solve(edges).must_equal([0, 1, 2, 0, 3])
