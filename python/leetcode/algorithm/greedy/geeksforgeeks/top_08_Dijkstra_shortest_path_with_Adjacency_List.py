import sys
from collections import defaultdict
from Queue import PriorityQueue

def solve(edges, start_vertex):
    max_vertex = 0
    graph = defaultdict(list)
    for src, dst, weight in edges:
        graph[src] += (weight, dst),
        graph[dst] += (weight, src),
        max_vertex = max(max_vertex, src, dst)
    vertex_count = max_vertex + 1

    handled = [False] * vertex_count
    distances = [sys.maxint] * vertex_count
    min_heap = PriorityQueue()
    distances[start_vertex] = 0
    min_heap.put((distances[start_vertex], start_vertex))

    while not min_heap.empty():
        dist, src = min_heap.get()
        if handled[src]: continue
        handled[src] = True
        distances[src] = dist

        for weight, dst in graph[src]:
            if not handled[dst] and distances[dst] > distances[src] + weight:
                min_heap.put((distances[src] + weight, dst))
    return distances


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
        spanning_tree = solve(edges, 0)
        spanning_tree.must_equal([0, 4, 12, 19, 21, 11, 9, 8, 14])
