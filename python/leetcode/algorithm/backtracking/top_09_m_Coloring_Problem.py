# borrow from greedy top_14_Graph_coloring
from collections import defaultdict

def solve(edges):
    adjs = defaultdict(list)
    max_vertex = 0
    for src, dst in edges:
        adjs[src] += dst,
        adjs[dst] += src,
        max_vertex = max(max_vertex, src, dst)
    vertex_count = max_vertex + 1

    available_colors = [True] * vertex_count

    def next_color(i):
        for adj in adjs[i]:
            if vertex_colors[adj] > -1:
                available_colors[vertex_colors[adj]] = False
        min_color = 0
        for j in range(i+1):
            if available_colors[j]:
                break
        for adj in adjs[i]:
            if vertex_colors[adj] > -1:
                available_colors[vertex_colors[adj]] = True
        return j


    vertex_colors = [-1] * vertex_count
    vertex_colors[0] = 0
    for i in range(1, vertex_count):
        vertex_colors[i] = next_color(i)
    vertex_colors.p()
    return vertex_colors

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
