# Introduction-to-algorithm-3rdEdition chapter greedy P452

from heapq import heappush, heappop
from Queue import PriorityQueue
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def tree_node_cmp(self, other):
    return cmp(self.val, other.val)

setattr(TreeNode, "__cmp__", tree_node_cmp)

def construct_huffman_tree(freqs):
    pq = PriorityQueue()
    for i in freqs:
        pq.put(TreeNode(i))
    for i in xrange(len(freqs)-1):
        left = pq.get()
        right = pq.get()
        # (left.val,right.val).p()
        node = TreeNode(left.val+right.val)
        node.left, node.right = left, right
        pq.put(node)
    return pq.get()

if __name__ == '__main__':
    from minitest import *

    with test(construct_huffman_tree):
        tree = construct_huffman_tree([5,9,12,13,16,45])
        tree.val.must_equal(100)
        tree.left.val.must_equal(45)
        tree.right.val.must_equal(55)

    

