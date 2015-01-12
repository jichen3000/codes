import tree

def has_routes(start_node, end_node):
    visted_list=[]
    doing_list = [start_node]
    while len(doing_list)>0:
        cur_node = doing_list.pop()
        visted_list.append(cur_node)
        for child in cur_node.children:
            # child.pp()
            if child == end_node:
                return True
            if  child not in visted_list:
                doing_list.append(child)
    return False

def breadth_first_search(the_node):
    results = [the_node]
    doing_list = [the_node]
    while len(doing_list) > 0:
        cur_node = doing_list.pop()
        for child in cur_node.children:
            doing_list.append(child)
            results.append(child)
    return results


if __name__ == '__main__':
    from minitest import *

    with test(has_routes):
        #       A
        #      /|\
        #     B C D
        #    /|/ \ \
        #   E F   G H
        #   |     |
        #   I     J
        a_node = tree.TreeNode('a')
        b_node = a_node.add_child('b')
        i_node = b_node.add_child('e').add_child('i')
        c_node = a_node.add_child('c')
        f_node = c_node.add_child('f')
        j_node = c_node.add_child('g').add_child('j')
        a_node.add_child('d').add_child('h')

        # b_node.add_child(f_node)

        # z_node = tree.TreeNode('z')

        # has_routes(a_node, i_node).pp()
        # has_routes(a_node, z_node).pp()

    with test(breadth_first_search):
        breadth_first_search(a_node).pp()