class BinaryTreeNode(object):
    """docstring for BinaryTreeNode"""
    def __init__(self, value):
        super(BinaryTreeNode, self).__init__()
        self.value = value
        self.children = []
        self.parent = None

    def add_child(self, node_value):
        if isinstance(node_value, BinaryTreeNode):
            new_node = node_value
        else: 
            new_node = BinaryTreeNode(node_value)
        self.children.append(new_node)
        new_node.parent = self
        return new_node

    def depth_first_search_recursively(self):
        result = [self]
        for child in self.children:
            result += child.depth_first_search()
        return result

    def depth_first_search(self):
        doing_stack = [self]
        acc = []
        while len(doing_stack) > 0:
            cur_node = doing_stack.pop()
            acc.append(cur_node)
            for child in reversed(cur_node.children):
                doing_stack.append(child)
        return acc


    def __repr__(self):
        return "BinaryTreeNode('{0}')".format(self.value)
    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.value == other.value

def find_closest_common_parent(a_node, b_node):
    if a_node == b_node:
        return a_node
    elif a_node.parent == b_node.parent:
        return a_node.parent
    elif a_node == b_node.parent:
        return a_node
    elif b_node == a_node.parent:
        return b_node
    if a_node.parent == None or b_node.parent == None:
        return None
    return find_closest_common_parent(a_node.parent, b_node.parent)

def match_tree_recursively(a_node, b_node):
    if a_node != b_node:
        return False
    if len(a_node.children) != len(b_node.children):
        return False
    for i in range(len(a_node.children)):
        if not match_tree_recursively(a_node.children[i], b_node.children[i]):
            return False
    return True

def match_tree_o(a_node, b_node):
    def is_equal(a_node, b_node):
        if a_node != b_node:
            return False
        if len(a_node.children) != len(b_node.children):
            return False
        return True
    a_stack = [a_node]
    b_stack = [b_node]
    while len(a_stack) > 0:
        cur_a = a_stack.pop()
        cur_b = b_stack.pop()
        if not is_equal(cur_a, cur_b):
            return False
        for i in range(len(cur_a.children)):
            a_stack.append(cur_a.children[i])
            b_stack.append(cur_b.children[i])
    return True


def is_sub_tree_recursively(big_tree, small_tree):
    if match_tree_recursively(big_tree, small_tree):
        return True
    for child in big_tree.children:
        if is_sub_tree_recursively(child, small_tree):
            return True
    return False

def is_sub_tree_o(big_tree, small_tree):
    doing_stack = [big_tree]
    while len(doing_stack) > 0:
        cur_tree = doing_stack.pop()
        if match_tree_o(cur_tree, small_tree):
            return True
        for child in cur_tree.children:
            doing_stack.append(child)
    return False

if __name__ == '__main__':
    from minitest import *

        #       A
        #      / \
        #     B   C
        #    /   / \
        #   E   F   G
        #  /       /
        # I       J
    with test('print node list reversely'):
        a_node = BinaryTreeNode('a')
        b_node = a_node.add_child('b')
        e_node = b_node.add_child('e')
        i_node = e_node.add_child('i')
        c_node = a_node.add_child('c')
        f_node = c_node.add_child('f')
        j_node = c_node.add_child('g').add_child('j')

        a_node.depth_first_search().must_equal(
            [BinaryTreeNode('a'),
             BinaryTreeNode('b'),
             BinaryTreeNode('e'),
             BinaryTreeNode('i'),
             BinaryTreeNode('c'),
             BinaryTreeNode('f'),
             BinaryTreeNode('g'),
             BinaryTreeNode('j')]
        )

    with test(find_closest_common_parent):
        find_closest_common_parent(b_node, c_node).must_equal(a_node)
        find_closest_common_parent(a_node, c_node).must_equal(a_node)
        find_closest_common_parent(e_node, c_node).must_equal(a_node)
        find_closest_common_parent(f_node, j_node).must_equal(c_node)
        find_closest_common_parent(i_node, j_node).must_equal(a_node)
        # BinaryTreeNode('a').value

    with test(match_tree_recursively):
        match_tree_recursively(e_node, e_node).must_true()
        e1_node = BinaryTreeNode('e')
        i1_node = e1_node.add_child('i')
        k1_node = e1_node.add_child('k')
        match_tree_recursively(e_node, e1_node).must_false()

    with test(is_sub_tree_recursively):
        is_sub_tree_recursively(a_node, e_node).must_true()
        is_sub_tree_recursively(a_node, e1_node).must_false()

    with test(match_tree_o):
        match_tree_o(e_node, e_node).must_true()
        match_tree_o(e_node, e1_node).must_false()

    with test(is_sub_tree_o):
        is_sub_tree_o(a_node, e_node).must_true()
        is_sub_tree_o(a_node, e1_node).must_false()

