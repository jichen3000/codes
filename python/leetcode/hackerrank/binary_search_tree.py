class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, 
                self.data)

class BST(object):
    def __init__(self,root_data=None):
        if root_data:
            self.root = Node(root_data)
        else:
            self.root = None

    def add(self, node_data):
        if self.root == None:
            self.root = Node(node_data)
            return self.root
        acc = [self.root]
        while len(acc) > 0:
            cur_node = acc.pop()
            if node_data == cur_node.data:
                return cur_node
            elif node_data > cur_node.data:
                if cur_node.right:
                    acc.append(cur_node.right)
                else:
                    cur_node.right = Node(node_data)
                    return cur_node.right
            else:
                if cur_node.left:
                    acc.append(cur_node.left)
                else:
                    cur_node.left = Node(node_data)
                    return cur_node.left

    def pre_order_list(self):
        result = []
        acc = [self.root]
        while len(acc) > 0:
            cur_node = acc.pop()
            result.append(cur_node)
            if cur_node.right: acc.append(cur_node.right)
            if cur_node.left: acc.append(cur_node.left)
        return result



    def is_in(node_data):
        pass

if __name__ == '__main__':
    from minitest import *

    with test(BST):
        n_list  = [8, 10, 5,3,7,9,1,11]
        tree = BST()
        map(tree.add, n_list)
        tree.pre_order_list().pp()
