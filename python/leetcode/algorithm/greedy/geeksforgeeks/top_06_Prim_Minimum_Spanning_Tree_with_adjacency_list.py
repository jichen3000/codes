# http://www.geeksforgeeks.org/greedy-algorithms-set-5-prims-mst-for-adjacency-list-representation/
import sys
from Queue import PriorityQueue
from collections import defaultdict
def solve(edges):
    graph = defaultdict(list)
    max_vertex = 0
    for src, dst, weight in edges:
        max_vertex = max(max_vertex, src, dst)
        graph[src] += (weight, dst),
        graph[dst] += (weight, src),
    vertex_count = max_vertex + 1

    parents = [-1] * vertex_count
    handled = [False] * vertex_count
    weights = [sys.maxint] * vertex_count
    min_heap = PriorityQueue()
    weights[0] = 0
    min_heap.put((weights[0], 0))

    while not min_heap.empty():
        _weight, src = min_heap.get()
        if handled[src]: continue
        handled[src] = True

        for weight, dst in graph[src]:
            if not handled[dst] and weight < weights[dst]:
                weights[dst] = weight
                parents[dst] = src
                min_heap.put((weight, dst))
    return [(parents[v],v, weights[v]) for v in range(1, vertex_count)]



if __name__ == '__main__':
    from minitest import *

    with test(solve):
        edges = [
            (7, 6, 1),
            (8, 2, 2),
            (6, 5, 2),
            (0, 1, 4),
            (2, 5, 4),
            (8, 6, 6),
            (2, 3, 7),
            (7, 8, 7),
            (0, 7, 8),
            (1, 2, 8),
            (3, 4, 9),
            (5, 4, 10),
            (1, 7, 11),
            (3, 5, 14),
        ]
        spanning_tree = solve(edges)
        spanning_tree.must_equal([
                (0, 1, 4),
                (1, 2, 8),
                (2, 3, 7),
                (3, 4, 9),
                (2, 5, 4),
                (5, 6, 2),
                (6, 7, 1),
                (2, 8, 2)])
        