import sys
# A utility function to find the vertex with minimum distance value, from
# the set of vertices not yet included in shortest path tree
def find_min_key(vertex_count, vertex_weights, handled):

    # Initilaize min value
    min_value = sys.maxint

    for v in range(vertex_count):
        if vertex_weights[v] < min_value and handled[v] == False:
            min_value = vertex_weights[v]
            min_index = v

    return min_index
# Function to construct and print MST for a graph represented using
# adjacency matrix representation
def solve(graph_grid):
    vertex_count = len(graph_grid)
    if vertex_count ==0: return None
    #Key values used to pick minimum weight edge in cut
    vertex_weights = [sys.maxint] * vertex_count
    # Array to store constructed MST
    parents = [None] * vertex_count
    handled = [False] * vertex_count
    # Make key 0 so that this vertex is picked as first vertex
    vertex_weights[0] = 0
    # First node is always the root of  
    parents[0] = -1

    for _ in range(vertex_count):
        # Pick the minimum distance vertex from the set of vertices not
        # yet processed. u is always equal to src in first iteration
        src = find_min_key(vertex_count, vertex_weights, handled)

        # Put the minimum distance vertex in the shortest path tree
        handled[src] = True
        # Update dist value of the adjacent vertices of the picked vertex
        # only if the current distance is greater than new distance and
        # the vertex in not in the shotest path tree
        for dst in range(1,vertex_count):
            # graph[src][dst] is non zero only for adjacent vertices of m
            # handled[dst] is false for vertices not yet included in MST
            # Update the key only if graph[src][dst] is smaller than key[dst]
            if graph_grid[src][dst] > 0 and handled[dst] == False and \
                    vertex_weights[dst] > graph_grid[src][dst]:
                vertex_weights[dst] = graph_grid[src][dst]
                parents[dst] = src  
    return [(parents[i],i) for i in range(1,vertex_count)]

# I simplized a little
def solve(graph_grid):
    vertex_count = len(graph_grid)
    weights = [sys.maxint] * vertex_count
    handled = [False] * vertex_count
    parents = [-1] * vertex_count
    # set start vertex
    weights[0] = 0

    for _ in range(vertex_count):
        # find_min_vertex
        _, src = min((weight,v) for v, weight in enumerate(weights) 
                if not handled[v])
        handled[src] = True

        # update the weights related to src
        for dst in range(vertex_count):
            if src != dst and graph_grid[src][dst] > 0 and not handled[dst] \
                    and graph_grid[src][dst] < weights[dst]:
                weights[dst] = graph_grid[src][dst]
                parents[dst] = src
    return [(parents[v],v, weights[v]) for v in range(1,vertex_count)]

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        graph_grid = [ 
            [0, 2, 0, 6, 0],
            [2, 0, 3, 8, 5],
            [0, 3, 0, 0, 7],
            [6, 8, 0, 0, 9],
            [0, 5, 7, 9, 0],
           ]
        solve(graph_grid).must_equal([(0, 1, 2), (1, 2, 3), (0, 3, 6), (1, 4, 5)])
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
        solve(graph_grid).must_equal([
                (0, 1, 4),
                (1, 2, 8),
                (2, 3, 7),
                (3, 4, 9),
                (2, 5, 4),
                (5, 6, 2),
                (6, 7, 1),
                (2, 8, 2)])

