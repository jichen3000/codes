def f1(n):
    if n < 2:
        return 1
    return n*f1(n-1)

def f2(n):
    if n < 2:
        return 1
    x = f2(n-1)
    result = n * x 
    return result


def f3(n, acc=1):
    if n < 2:
        return 1 * acc
    return acc*n*f3(n-1)

def f_tail_call(n, acc=1):
    if n < 2:
        return acc
    return f_tail_call(n-1, n * acc)

f4 = f_tail_call

def f5(n, acc=1):
    while True:
        if n < 2:
            return acc
        return f5(n-1, n * acc)
        break

def f6(n, acc=1):
    while True:
        if n < 2:
            return acc
        n, acc = (n-1, n * acc)
        continue
        break

def f_iterative(n, acc=1):
    while n > 1:
        n, acc = (n-1, n * acc)
        continue
    return acc

class TreeNode(object):
    """docstring for TreeNode"""
    def __init__(self, value):
        super(TreeNode, self).__init__()
        self.value = value
        self.children = []

    def add_child(self, node_value):
        if isinstance(node_value, TreeNode):
            new_node = node_value
        else: 
            new_node = TreeNode(node_value)
        self.children.append(new_node)
        return new_node

    def __repr__(self):
        return "TreeNode('{0}')".format(self.value)

    def __eq__(self, other):
        return self.value == other.value

def depth_first_search_recurtively(the_node):
    results = [the_node]
    for child in the_node.children:
        results += depth_first_search_recurtively(child)
    return results

def depth_first_search_1(the_node, acc=[]):
    results = [the_node]
    for child in the_node.children:
        results += depth_first_search_1(child)
    return results + acc

def depth_first_search_2(the_node, acc=[]):
    acc.append(the_node)
    for child in the_node.children:
        depth_first_search_2(child, acc)
    return acc

def depth_first_search_3(the_node, acc=[]):
    acc.append(the_node)
    while True:
        for child in the_node.children:
            depth_first_search_3(child, acc)
        return acc
        break

def depth_first_search_4(the_node):
    acc = []
    doing_queue = [the_node]
    while len(doing_queue) > 0:
        cur_node = doing_queue.pop()
        for child in reversed(cur_node.children):
            doing_queue.append(child)
        acc.append(cur_node)
    return acc

import Queue
def depth_first_search_5(the_node):
    acc = []
    doing_queue = Queue.Queue()
    doing_queue.put(the_node)
    while doing_queue.qsize > 0:
        cur_node = doing_queue.get()
        for child in reversed(cur_node.children):
            doing_queue.put(child)
        acc.append(cur_node)
    return acc


if __name__ == '__main__':
    from minitest import *

    with test(f1):
        f1(5).must_equal(120)

    with test(f2):
        f2(5).must_equal(120)

    with test(f3):
        f3(5).must_equal(120)

    with test(f_tail_call):
        f_tail_call(5).must_equal(120)

    with test(f5):
        f5(5).must_equal(120)

    with test(f6):
        f6(5).must_equal(120)

    with test(f_iterative):
        f_iterative(5).must_equal(120)

    a_node = TreeNode('a')
    a_node.add_child('b').add_child('e').add_child('i')
    c_node = a_node.add_child('c')
    c_node.add_child('f')
    c_node.add_child('g').add_child('j')
    a_node.add_child('d').add_child('h')

    depth_first_list = [ TreeNode('a'),
                         TreeNode('b'),
                         TreeNode('e'),
                         TreeNode('i'),
                         TreeNode('c'),
                         TreeNode('f'),
                         TreeNode('g'),
                         TreeNode('j'),
                         TreeNode('d'),
                         TreeNode('h')]

    with test(depth_first_search_recurtively):
        depth_first_search_recurtively(a_node).must_equal(depth_first_list)

    with test(depth_first_search_1):
        depth_first_search_1(a_node).must_equal(depth_first_list)

    with test(depth_first_search_2):
        depth_first_search_2(a_node).must_equal(depth_first_list)

    with test(depth_first_search_3):
        depth_first_search_3(a_node).must_equal(depth_first_list)

    with test(depth_first_search_4):
        depth_first_search_4(a_node).must_equal(depth_first_list)

    with test(depth_first_search_5):
        depth_first_search_5(a_node).must_equal(depth_first_list)

    # with test(depth_first_search_3):
    #     depth_first_search_3(a_node).must_equal(depth_first_list)

    # with test(depth_first_search_3):
    #     depth_first_search_3(a_node).must_equal(depth_first_list)

    # with test(depth_first_search_3):
    #     depth_first_search_3(a_node).must_equal(depth_first_list)


