# https://www.geeksforgeeks.org/union-find/
# in worst case O(n), n is number of vertex
def naive_detect_cycle(edges):
    parents = {}

    def union(src, dst):
        parents[src] = dst

    def find(src):
        while src in parents:
            src = parents[src]
        return src
    # recusive version
    # def find(src):
    #     if src not in parents:
    #         return src
    #     return find(parents[src])

    for src, dst in edges:
        src_parent = find(src)
        dst_parent = find(dst)
        if src_parent == dst_parent:
            return True
        union(src_parent, dst_parent)
    return False

def rank_detect_cycle(edges):
    # value is a list, 
    # first is vertex, second is rank
    parents = {}

    def union(src, dst):
        # initialize
        if src not in parents:
            parents[src] = [None, 0]
        if dst not in parents:
            parents[dst] = [None, 0]
        # whose rank is bigger, who is the parent
        if parents[dst][1] > parents[src][1]:
            parents[src][0] = dst
        elif parents[dst][1] < parents[src][1]:
            parents[dst][0] = src
        else:
            parents[src][0] = dst
            parents[dst][1] += 1

    def find(src):
        while src in parents and parents[src][0] != None:
            src = parents[src][0]
        return src
    # def find(src):
    #     if src not in parents or parents[src][0] == None:
    #         return src
    #     return find(parents[src][0])

    for src, dst in edges:
        # (src, dst).p()
        src_parent = find(src)
        dst_parent = find(dst)
        if src_parent == dst_parent:
            return True
        union(src_parent, dst_parent)
    return False

def path_compression_detect_cycle(edges):
    parents = {}

    def union(src, dst):
        parents[src] = dst

    def find(src):
        cur = src
        while cur in parents:
            cur = parents[cur]
        # path compression
        if cur != src:
            parents[src] = cur
        return cur
    # def find(src):
    #     if src not in parents:
    #         return src
    #     parent = find(parents[src])
    #     # path compression
    #     parents[src] = parent
    #     return parent

    for src, dst in edges:
        # (src, dst).p()
        src_parent = find(src)
        dst_parent = find(dst)
        if src_parent == dst_parent:
            return True
        union(src_parent, dst_parent)
    return False

# combine
def path_compression_and_rank_detect_cycle(edges):
    parents = {}

    def union(src, dst):
        if src not in parents:
            parents[src] = [None, 0]
        if dst not in parents:
            parents[dst] = [None, 0]
        if parents[src][1] < parents[dst][1]:
            parents[src][0] = dst
        elif parents[src][1] > parents[dst][1]:
            parents[dst][0] = src
        else:
            parents[src][0] = dst
            parents[dst][1] += 1

    def find(src):
        cur = src
        while cur in parents and parents[cur][0] != None:
            cur = parents[cur][0]
        # path compression
        if cur != src:
            parents[src][0] = cur
        return cur
    # def find(src):
    #     if src not in parents or parents[src][0] == None:
    #         return src
    #     parent = find(parents[src][0])
    #     # path compression
    #     parents[src][0] = parent
    #     return parent

    for src, dst in edges:
        # (src, dst).p()
        src_parent = find(src)
        dst_parent = find(dst)
        if src_parent == dst_parent:
            return True
        union(src_parent, dst_parent)
    return False


if __name__ == '__main__':
    from minitest import *

    with test(naive_detect_cycle):
        edges = [(1,2),(2,3),(3,1)]
        naive_detect_cycle(edges).must_equal(True)

    with test(rank_detect_cycle):
        edges = [(1,2),(2,3),(3,1)]
        rank_detect_cycle(edges).must_equal(True)
        edges = [[4,1],[1,5],[4,2],[5,1],[4,3]]
        rank_detect_cycle(edges).must_equal(True)

    with test(path_compression_detect_cycle):
        edges = [(1,2),(2,3),(3,1)]
        path_compression_detect_cycle(edges).must_equal(True)
        edges = [[4,1],[1,5],[4,2],[5,1],[4,3]]
        path_compression_detect_cycle(edges).must_equal(True)


    with test(path_compression_and_rank_detect_cycle):
        edges = [(1,2),(2,3),(3,1)]
        path_compression_and_rank_detect_cycle(edges).must_equal(True)
        edges = [[4,1],[1,5],[4,2],[5,1],[4,3]]
        path_compression_and_rank_detect_cycle(edges).must_equal(True)

