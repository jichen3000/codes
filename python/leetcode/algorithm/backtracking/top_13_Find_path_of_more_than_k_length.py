from collections import defaultdict
def solve(edges, target_weight):
    max_vertex = 0
    adjs = defaultdict(list)
    for src, des, weight in edges:
        adjs[src] += (des, weight),
        adjs[des] += (src, weight),
        max_vertex = max(max_vertex, des, src)
    vertex_count = max_vertex + 1

    visited = [False] * vertex_count
    def get_nexts(cur_vertex, visited):
        return [(v,w) for v, w in adjs[cur_vertex] if not visited[v]]

    def dfs(path, weights, visited):
        if sum(weights) > target_weight:
            return True
        if len(path) == vertex_count:
            return False
        next_vertics = get_nexts(path[-1], visited)
        if len(next_vertics) == 0: 
            return False
        for v, w in next_vertics:
            path.append(v)
            weights.append(w)
            visited[v] = True
            if dfs(path, weights, visited):
                return True
            path.pop()
            weights.pop()
            visited[v] = False
    path, weights = [0], []
    dfs(path, weights, visited)
    return path

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        edges=[
                (0, 1, 4),
                (0, 7, 8),
                (1, 2, 8),
                (1, 7, 11),
                (2, 3, 7),
                (2, 8, 2),
                (2, 5, 4),
                (3, 4, 9),
                (3, 5, 14),
                (4, 5, 10),
                (5, 6, 2),
                (6, 7, 1),
                (6, 8, 6),
                (7, 8, 7),
        ]
        solve(edges, 62).must_equal([0])
        solve(edges, 60).must_equal([0, 7, 1, 2, 3, 4, 5, 6, 8])
        
