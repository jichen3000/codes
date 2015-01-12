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

    def depth_first_search_with_depth(self,depth=0):
        results = []
        results.append((self,depth))
        depth += 1
        for child in self.children:  
            results += child.depth_first_search_with_depth(depth)
        return results

    def breadth_first_search(self, first=True):
        result_list = []
        if first:
            result_list.append(self)
        map(result_list.append, self.children)
        for child in self.children:  
            result_list += child.breadth_first_search(False)
        return result_list

    def __repr__(self):
        return "TreeNode('{0}')".format(self.value)
    def __eq__(self, other):
        return self.value == other.value

def get_leafs_with_depth(tree_node, depth=0):
    leafs = []
    if len(tree_node.children) == 0:
        leafs.append((tree_node, depth))
    else:
        depth += 1
        for child in tree_node.children:
            leafs += get_leafs_with_depth(child, depth) 
    return leafs

def is_balanced(tree_node):
    import operator
    # get all leafs with depth
    leafs_with_depth_list = get_leafs_with_depth(tree_node)
    depths = map(operator.itemgetter(1), leafs_with_depth_list)
    # compare the min and max depth of leafs
    return max(depths)-min(depths)<=1

def flat(lst):
    return [item for sub_list in lst for item in sub_list]

def generate_binary_tree_by_sorted_list(sorted_list):
    ''' Given a sorted (increasing order) array, 
    write an algorithm to create a binary tree with minimal height. '''
    if len(sorted_list) == 1:
        return TreeNode(sorted_list[0])
    if len(sorted_list) == 2:
        return TreeNode(sorted_list[1]).add_child(sorted_list[0])
    middle = len(sorted_list) / 2
    cur_node = TreeNode(sorted_list[middle])
    cur_node.add_child(generate_binary_tree_by_sorted_list(sorted_list[0:middle]))
    cur_node.add_child(generate_binary_tree_by_sorted_list(sorted_list[middle+1:]))
    return cur_node

def depth_first_search_with_depth2(the_node, depth=0):
    results = [(the_node, depth)]
    for child in the_node.children:
        results += depth_first_search_with_depth2(child, depth+1)
    return results


def depth_first_search_recurtive(the_node):
    results = [the_node]
    for child in the_node.children:
        results += depth_first_search_recurtive(child)
    return results


if __name__ == '__main__':
    from minitest import *

    #       A
    #      /|\
    #     B C D
    #    / / \ \
    #   E F   G H
    #   |     |
    #   I     J
    with test('print node list reversely'):
        a_node = TreeNode('a')
        a_node.add_child('b').add_child('e').add_child('i')
        c_node = a_node.add_child('c')
        c_node.add_child('f')
        c_node.add_child('g').add_child('j')
        a_node.add_child('d').add_child('h')

        node_list = a_node.depth_first_search_with_depth()
        def get_key(item):
            return item[1]
        sorted_list = sorted(node_list, key=get_key, reverse=True)
        # sorted_list.pp()
        cur_depth = sorted_list[0][1]
        def print_one(item):
            global cur_depth
            if cur_depth != item[1]:
                print "\n"
                cur_depth = item[1]
            print item[0].value,
        map(print_one, sorted_list)

        a_node.breadth_first_search().pp()

    with test(get_leafs_with_depth):
        get_leafs_with_depth(a_node).must_equal(
            [(TreeNode('i'), 3),
             (TreeNode('f'), 2),
             (TreeNode('j'), 3),
             (TreeNode('h'), 2)]
        )

    with test(is_balanced):
        is_balanced(a_node).must_true()
        # is_balanced(a_node).must_false()

    with test(flat):
        flat([[1,2,3],[4,5],[9,0]]).must_equal([1,2,3,4,5,9,0])

    with test(generate_binary_tree_by_sorted_list):
        generate_binary_tree_by_sorted_list(range(10)).pp()

    with test(depth_first_search_with_depth2):
        the_list = depth_first_search_with_depth2(a_node).pp()
        depth_dict = {}
        for cur_node, cur_depth in the_list:
            if depth_dict.get(cur_depth) == None:
                depth_dict[cur_depth] = []
            depth_dict[cur_depth].append(cur_node)
        depth_dict.pp()