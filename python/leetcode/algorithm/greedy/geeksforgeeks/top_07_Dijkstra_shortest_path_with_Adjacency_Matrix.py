# just like Prim
import sys

def solve(graph_grid, start_vertex):
    vertex_count = len(graph_grid)
    if vertex_count == 0: return None
    handled = [False] * vertex_count
    distances = [sys.maxint] * vertex_count

    distances[start_vertex] = 0

    for _ in xrange(vertex_count):
        _, src = min((w, i) for i, w in enumerate(distances) if not handled[i])
        # src.p()
        handled[src] = True

        for dst in xrange(vertex_count):
            if src != dst and not handled[dst] \
                    and graph_grid[src][dst] > 0 \
                    and distances[dst] > distances[src] + graph_grid[src][dst]:
                distances[dst] = distances[src] + graph_grid[src][dst]
    return distances

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        graph_grid = [ 
                [0, 4, 0, 0, 0, 0, 0, 8, 0],
                [4, 0, 8, 0, 0, 0, 0, 11, 0],
                [0, 8, 0, 7, 0, 4, 0, 0, 2],
                [0, 0, 7, 0, 9, 14, 0, 0, 0],
                [0, 0, 0, 9, 0, 10, 0, 0, 0],
                [0, 0, 4, 14, 10, 0, 2, 0, 0],
                [0, 0, 0, 0, 0, 2, 0, 1, 6],
                [8, 11, 0, 0, 0, 0, 1, 0, 7],
                [0, 0, 2, 0, 0, 0, 6, 7, 0],
           ]
        solve(graph_grid, 0).must_equal([0, 4, 12, 19, 21, 11, 9, 8, 14])
