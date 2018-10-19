# http://www.geeksforgeeks.org/depth-first-traversal-for-a-graph/
# Depth First Traversal (or Search) for a graph is similar to Depth First Traversal of a tree
# 

class Graph(object):
    def __init__(self, number_vertexes, edges):
        self.number_vertexes = number_vertexes
        # self.edges = edges
        self.adjacencies = [[] for _ in xrange(number_vertexes)]
        for i,j in edges:
            self.adjacencies[i].append(j)
        # self.adjacencies.p()

    def depth_first_search_r(self, visited, cur_vertex, result):
        visited[cur_vertex] = True
        result.append(cur_vertex)
        # print cur_vertex,

        for i in self.adjacencies[cur_vertex]:
            if visited[i] == False:
                self.depth_first_search_r(visited, i, result)

    def depth_first_search1(self, start_vertex=0):
        visited = [False] * self.number_vertexes
        result = []
        self.depth_first_search_r(visited, start_vertex, result)
        return result

def breadth_first_search(number_vertexes, edges, start_vertex=0):
    visited = [False] * number_vertexes
    adjacencies = [[] for _ in xrange(number_vertexes)]
    for i,j in edges:
        adjacencies[i].append(j)

    result = []
    acc = [start_vertex]
    while len(acc) > 0:
        cur_vertex = acc.pop(0)
        visited[cur_vertex] = True
        result.append(cur_vertex)
        for i in adjacencies[cur_vertex]:
            if visited[i] == False:
                acc.append(i)
    return result




if __name__ == '__main__':
    from minitest import *

    with test("depth_first_search1"):
        edges = [
                (0,1),
                (0,2),
                (1,2),
                (2,0),
                (2,3),
                (3,3)
                ]
        g = Graph(4,edges)
        g.depth_first_search1(2).must_equal([2, 0, 1, 3])
        # g.depth_first_search1(3).must_equal([2, 0, 1, 3])
        # depth_first_search(4, edges, 2).must_equal([2, 0, 1, 3])
        # depth_first_search(4, edges, 3).must_equal([2, 0, 3, 1])

