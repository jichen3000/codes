def solve(edges, start_vertix):
    if len(edges) == 0:
        return 0
    n_list = set()
    for u,v,w in edges:
        n_list.add(u)
        n_list.add(v)
    n = max(n_list) + 1
    inf = float("inf")
    dist = [inf] * n
    dist[start_vertix] = 0
    for u,v,w in edges:
        dist[v] = min(dist[u] + w, dist[v])
    for u,v,w in edges:
        if dist[u] + w < dist[v]:
            raise Exception("Has a negative cycle!")
    return dist


if __name__ == '__main__':
    from minitest import *

    with test(solve):
        edges = [
            (0, 1, -1),
            (0, 2, 4),
            (1, 2, 3),
            (1, 3, 2),
            (1, 4, 2),
            (3, 2, 5),
            (3, 1, 1),
            (4, 3, -3),
        ]
        solve(edges,0).must_equal([0, -1, 2, -2, 1])
        # add (2,0,-3),  will let 0->2 has a negative cycle
        edges = [
            (0, 1, -1),
            (0, 2, 4),
            (1, 2, 3),
            (1, 3, 2),
            (1, 4, 2),
            (2,0,-3),
            (3, 2, 5),
            (3, 1, 1),
            (4, 3, -3),
        ]
        (lambda : solve(edges,0)).must_raise(Exception, "Has a negative cycle!")
             
