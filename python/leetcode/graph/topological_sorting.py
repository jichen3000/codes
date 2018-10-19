# http://www.geeksforgeeks.org/topological-sorting/

def topological_sort(number_vertexes, edges):
    reversed_links = [[] for _ in xrange(number_vertexes)]
    for i, j in edges:
        if j > i:
            reversed_links[j].append(i)

    visited =[False] * number_vertexes
    result =[]
    acc = [i for i in xrange(number_vertexes)]
    while len(acc) > 0:
        cur_vertex = acc.pop()
        if visited[cur_vertex] == False:

            new_added = False
            for i in reversed_links[cur_vertex]:
                if visited[i] == False:
                    if not new_added:
                        acc.append(cur_vertex)
                    new_added = True
                    acc.append(i)
            if new_added:
                continue

            visited[cur_vertex] = True
            result.append(cur_vertex)
    return result


if __name__ == '__main__':
    from minitest import *

    with test(topological_sort):
        edges = [
                (5, 2),
                (5, 0),
                (4, 0),
                (4, 1),
                (2, 3),
                (3, 1),
        ]
        topological_sort(6, edges).p()
