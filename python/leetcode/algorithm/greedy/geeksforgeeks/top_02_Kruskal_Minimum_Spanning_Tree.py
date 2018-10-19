# http://www.geeksforgeeks.org/greedy-algorithms-set-2-kruskals-minimum-spanning-tree-mst/
# using union-find
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.children = []
    def add(self,child):
        self.children += child,

def my_solve(weight_edges):
    '''
        one edge, weight, src, dst
    '''
    # sort by weight
    n = len(weight_edges)
    if n == 0: return None
    # max_vertex = 1
    # for weight, src, dst in weight_edges:
    #     max_vertex = max(max_vertex, src, dst)
    node_dict = {}
    weight_edges.sort()
    weight, src, dst = weight_edges.pop(0)
    root = TreeNode(src)
    cur = TreeNode(dst)
    root.add(cur)
    node_dict[src] = root
    node_dict[dst] = cur 
    # cannot handle the isolated node
    while len(weight_edges)>0:
        temp = []
        found = False
        while not found and len(weight_edges)>0:
            weight, src, dst = weight_edges.pop(0)
            # (weight, src, dst).p()
            if node_dict.get(src, None)!=None and node_dict.get(dst, None)!=None:
                # there is a cycle if add this edge
                pass
            elif node_dict.get(src, None)==None and node_dict.get(dst, None)==None:
                temp += (weight, src, dst),
            else:
                if node_dict.get(dst, None)!=None:
                    src, dst = dst, src
                parent = node_dict.get(src)
                cur = TreeNode(dst)
                parent.add(cur)
                node_dict[dst] = cur
                found = True
            # temp.p()
            # found.p()

        weight_edges = temp + weight_edges
    # len(node_dict).p()
    return root

def union_find_cycle(edges):
    parents = {}
    def find(vertex):
        if parents[vertex][0] != vertex:
            parents[vertex][0] = find(parents[vertex][0])
        return parents[vertex][0]
    def union(src, dst):
        if parents[src][1] < parents[dst][1]:
            parents[dst][0] = src
        elif parents[src][1] > parents[dst][1]:
            parents[src][0] = dst
        else:
            parents[src][0] = dst
            parents[dst][1] += 1 
    for src, dst in edges:
        if src not in parents:
            parents[src] = [src,0]
        if dst not in parents:
            parents[dst] = [dst,0]
        src_root = find(src)
        dst_root = find(dst)
        if src_root == dst_root:
            return True
        union(src_root,dst_root)
    return False

def solve(weight_edges):
    weight_edges.sort()
    spanning_tree = []
    while len(weight_edges) > 0:
        weight, src, dst = edges.pop(0)
        spanning_tree += (src, dst),
        if union_find_cycle(spanning_tree):
            spanning_tree.pop()
    return spanning_tree


def solve(weight_edges):
    parents = {}
    def find(vertex):
        if parents[vertex][0] != vertex:
            parents[vertex][0] = find(parents[vertex][0])
        return parents[vertex][0]
    def union(src, dst):
        if parents[src][1] < parents[dst][1]:
            parents[dst][0] = src
        elif parents[src][1] > parents[dst][1]:
            parents[src][0] = dst
        else:
            parents[src][0] = dst
            parents[dst][1] += 1 
    weight_edges.sort()
    spanning_tree = []
    while len(weight_edges) > 0:
        weight, src, dst = edges.pop(0)
        if src not in parents:
            parents[src] = [src,0]
        if dst not in parents:
            parents[dst] = [dst,0]
        src_root = find(src)
        dst_root = find(dst)
        if src_root != dst_root:
            spanning_tree += (src, dst),
            union(src_root, dst_root)
    return spanning_tree


if __name__ == '__main__':
    from minitest import *

    with test(my_solve):
        # weight, src, dst
        edges = [
            (1, 7, 6),
            (2, 8, 2),
            (2, 6, 5),
            (4, 0, 1),
            (4, 2, 5),
            (6, 8, 6),
            (7, 2, 3),
            (7, 7, 8),
            (8, 0, 7),
            (8, 1, 2),
            (9, 3, 4),
            (10, 5, 4),
            (11, 1, 7),
            (14, 3, 5),
        ]
        root = my_solve(edges)
        root.val.must_equal(7)
        root.children[0].val.must_equal(6)
        root.children[1].val.must_equal(0)
    with test(solve):
        edges = [
            (1, 7, 6),
            (2, 8, 2),
            (2, 6, 5),
            (4, 0, 1),
            (4, 2, 5),
            (6, 8, 6),
            (7, 2, 3),
            (7, 7, 8),
            (8, 0, 7),
            (8, 1, 2),
            (9, 3, 4),
            (10, 5, 4),
            (11, 1, 7),
            (14, 3, 5),
        ]
        spanning_tree = solve(edges)
        spanning_tree.must_equal([(7, 6), (6, 5), (8, 2), (0, 1), (2, 5), (2, 3), (0, 7), (3, 4)])
    with test(union_find_cycle):
        edges = [(1,2),(2,3),(3,1)]
        union_find_cycle(edges).must_equal(True)



