WHITE = 1
GRAY  = 2
DARK  = 3

class Vertex(object):
    def __init__(self, key, color=WHITE):
        self.key = key
        self.color = color
        self.distance = float("inf")
        self.parent = None
    def __repr__(self):
        return str(self.key)

def breadth_first_search(adjacency_list, start_key):
    # color means
    # WHITE no visted
    # GRAY adjacency vertex to the visited one
    # DARK visited
    # but in this method, only need to have DARK and WHITE
    vertex_list = [Vertex(key) for key in xrange(len(adjacency_list))]
    start_vertex = vertex_list[start_key]
    start_vertex.color = GRAY
    start_vertex.distance = 0
    result_vertex_list = []

    acc = [start_vertex]
    while len(acc) > 0:
        cur_vertex = acc.pop(0)
        for key in adjacency_list[cur_vertex.key]:
            adj_vertex = vertex_list[key]
            if adj_vertex.color == WHITE:
                adj_vertex.color = GRAY
                adj_vertex.distance = cur_vertex.distance + 1
                adj_vertex.parent = cur_vertex
                acc.append(adj_vertex)
        cur_vertex.color = DARK
        result_vertex_list.append(cur_vertex)
    return result_vertex_list


# cannot handle the isolated vertex
def breadth_first_search_simple(adjacency_list, start_key):
    cached_list = [False] * len(adjacency_list)
    result_list = []
    acc = [start_key]
    cached_list[start_key] = True
    while len(acc) > 0:
        cur_key = acc.pop(0)
        result_list.append(cur_key)
        for adj_key in adjacency_list[cur_key]:
            if cached_list[adj_key] == False:
                acc.append(adj_key)
                cached_list[adj_key] = True
    return result_list

def breadth_first_search_simple_full(adjacency_list):
    cached_list = [False] * len(adjacency_list)
    result_list = []
    for start_key in xrange(len(adjacency_list)):
        if cached_list[start_key] == False:
            acc = [start_key]
            cached_list[start_key] = True
            while len(acc) > 0:
                cur_key = acc.pop(0)
                result_list.append(cur_key)
                for adj_key in adjacency_list[cur_key]:
                    if cached_list[adj_key] == False:
                        acc.append(adj_key)
                        cached_list[adj_key] = True
    return result_list

# cannot handle the isolated vertex
def depth_first_search_simple(adjacency_list, start_key):
    cached_list = [False] * len(adjacency_list)
    result_list = []
    acc = [start_key]
    cached_list[start_key] = True
    while len(acc) > 0:
        cur_key = acc.pop()
        result_list.append(cur_key)
        for adj_key in reversed(adjacency_list[cur_key]):
            if cached_list[adj_key] == False:
                acc.append(adj_key)
                cached_list[adj_key] = True
    return result_list

def depth_first_search_simple_full(adjacency_list):
    cached_list = [False] * len(adjacency_list)
    result_list = []
    for start_key in xrange(len(adjacency_list)):
        if cached_list[start_key] == False:
            acc = [start_key]
            cached_list[start_key] = True
            while len(acc) > 0:
                cur_key = acc.pop()
                result_list.append(cur_key)
                for adj_key in reversed(adjacency_list[cur_key]):
                    if cached_list[adj_key] == False:
                        acc.append(adj_key)
                        cached_list[adj_key] = True
    return result_list

def gen_adjacency_list(number_vertexes, edges):
    adjacencies = [[] for _ in xrange(number_vertexes)]
    for i,j in edges:
        adjacencies[i].append(j)
    return adjacencies

if __name__ == '__main__':
    from minitest import *

    with test(gen_adjacency_list):
        edges = [
                (0,1),
                (0,2),
                (1,2),
                (2,0),
                (2,3),
                (3,3),
                (4,4)
                ]
        adjacency_list = gen_adjacency_list(5, edges)
        adjacency_list.must_equal([[1, 2], [2], [0, 3], [3],[4]])

    with test(breadth_first_search):
        str(breadth_first_search(adjacency_list, 2)).must_equal(
            '[2, 0, 3, 1]')
        str(breadth_first_search(adjacency_list, 0)).must_equal(
            '[0, 1, 2, 3]')

    with test(breadth_first_search_simple):
        breadth_first_search_simple(adjacency_list, 2).must_equal([2, 0, 3, 1])
        breadth_first_search_simple(adjacency_list, 0).must_equal([0, 1, 2, 3])
    with test(depth_first_search_simple):
        depth_first_search_simple(adjacency_list, 2).must_equal([2, 0, 1, 3])
        depth_first_search_simple(adjacency_list, 0).must_equal([0, 1, 2, 3])
    with test(breadth_first_search_simple_full):
        breadth_first_search_simple_full(adjacency_list).must_equal([0, 1, 2, 3, 4])
    with test(depth_first_search_simple_full):
        depth_first_search_simple_full(adjacency_list).must_equal([0, 1, 2, 3, 4])

        




