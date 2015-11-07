# https://leetcode.com/problems/course-schedule/
# use Topological Sort
# http://stackoverflow.com/questions/4168/graph-serialization/4577#4577


def find_start_nodes(edge_list):
    in_nodes = set([edge[1] for edge in edge_list])
    out_nodes = set([edge[0] for edge in edge_list])
    return out_nodes - in_nodes
    
def cal_node_depend_hash(start_nodes, node_edge_hash):
    return {node:cal_node_depend_nodes(node,node_edge_hash) 
            for node in start_nodes}

def cal_node_depend_nodes(node, node_edge_hash):
    '''not support the cycle'''
    acc = [node]
    result = []
    while len(acc) > 0:
        cur_node = acc.pop(0)
        # cur_node.pp()
        if cur_node not in result:
            result.append(cur_node)
        if cur_node not in node_edge_hash:
            continue
        for in_node, out_node in node_edge_hash[cur_node]:
            if out_node not in result and out_node not in acc:
                acc.append(out_node)
    result.pop(0)
    return result


def gen_node_edge_hash(edge_list):
    result = {}
    for edge in edge_list:
        cur = result.get(edge[0], [])
        cur.append(edge)
        result[edge[0]] = cur
    return result

def find_suitable_course(course_edge_list, count):
    start_nodes = find_start_nodes(course_edge_list)
    node_edge_hash = gen_node_edge_hash(course_edge_list)
    cource_depend_hash = cal_node_depend_hash(
            start_nodes, node_edge_hash)
    return [(c, v ) for c,v in cource_depend_hash.items() if len(v) < count]

if __name__ == '__main__':
    from minitest import *

    edge_list = [(1,2),(2,1),(3,4),(5,6),(5,9),(4,7),(6,10),(8,9),(9,10),(3,10)]
    with test(find_start_nodes):
        find_start_nodes(edge_list).must_equal(set([3, 5, 8]))

    with test(gen_node_edge_hash):
        edge_hash = {1: [(1, 2)],
                     2: [(2, 1)],
                     3: [(3, 4), (3, 10)],
                     4: [(4, 7)],
                     5: [(5, 6), (5, 9)],
                     6: [(6, 10)],
                     8: [(8, 9)],
                     9: [(9, 10)]}
        gen_node_edge_hash(edge_list).must_equal(edge_hash)

    with test(cal_node_depend_nodes):
        cal_node_depend_nodes(5, edge_hash).must_equal([6, 9, 10])

    with test(find_suitable_course):
        find_suitable_course(edge_list,3).pp()

