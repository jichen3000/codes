from bst_with_parent import TreeNode, Tree

BLACK, RED = 0,1
class BlackRedNode(TreeNode):
    def __init__(self,value):
        super(self.__class__, self).__init__(value)
        self.color = None

class BlackRedTree(Tree):
    def __init__(self, root):
        super(self.__class__, self).__init__(root)

    # node a and c do not change,
    # node x, y and b will change
    #
    #       |                    |
    #       y     left R         x
    #      / \      <==         / \
    #     x   c                a   y
    #    / \      righ R          / \
    #   a   b       ==>          b   c
    def left_rotate(self,x_node):
        y_node = x_node.right
        # b node
        x_node.right = y_node.left
        if x_node.right != None:
            x_node.right.parent = x_node
        # x parent
        if x_node.parent == None:
            self.root = y_node
        elif x_node.parent.left == x_node:
            x_node.parent.left = y_node
        elif x_node.parent.right == x_node:
            x_node.parent.right = y_node

        y_node.parent = x_node.parent
        y_node.left = x_node
        x_node.parent = y_node
        return y_node

    def right_rotate(self,y_node):
        x_node = y_node.left
        # b node
        y_left = x_node.right
        if y_left != None:
            y_left.parent = y_node
        # y parent
        if y_node.parent == None:
            self.root = x_node
        elif y_node.parent.left == y_node:
            y_node.parent.left = x_node
        elif y_node.parent.right == y_node:
            y_node.parent.right = x_node

        x_node.parent = y_node.parent
        x_node.right = y_node
        y_node.parent = x_node
        return x_node

    def insert(self, new_node):
        super(self.__class__, self).insert(new_node)
        new_node.color = RED
        self.insert_fixup(new_node)
        return new_node

    def insert_fixup(self, new_node):
        z_node = new_node
        while z_node.parent.color == RED:
            if z_node.parent == z_node.parent.parent.left:
                y_node = z_node.parent.parent.right
                if y_node.color == RED:
                    # case 1
                    z_node.parent.color = BLACK
                    y_node.color = BLACK
                    z_node.parent.parent.color = RED
                    z_node = z_node.parent.parent
                elif z_node == z_node.parent.right:
                    # case 2
                    z_node = z_node.parent
                    self.left_rotate(z_node)
                    # case 3
                    z_node.parent.color = BLACK
                    z_node.parent.parent.color = RED
                    self.right_rotate(z_node.parent.parent)
            else:
                y_node = z_node.parent.parent.left
                if y_node.color == RED:
                    # case 1
                    z_node.parent.color = BLACK
                    y_node.color = BLACK
                    z_node.parent.parent.color = RED
                    z_node = z_node.parent.parent
                elif z_node == z_node.parent.left:
                    # case 2
                    z_node = z_node.parent
                    self.right_rotate(z_node)
                    # case 3
                    z_node.parent.color = BLACK
                    z_node.parent.parent.color = RED
                    self.left_rotate(z_node.parent.parent)
        self.root.color = BLACK
        return new_node





if __name__ == '__main__':
    from minitest import *

    #         15
    #      /     \
    #     6       18
    #    / \     /  \
    #   3   7   17  20
    #  / \   \
    # 2   4   13
    #        /
    #       9
    preorder = [15,6,3,2,4,7,13,9,18,17,20]
    inorder =  [2,3,4,6,7,9,13,15,17,18,20]
    with test("left_rotate"):
        root_node = BlackRedNode.build_with_preorder_inorder(
            preorder[:],inorder[:])
        root_node.get_inorder_list().must_equal(inorder)
        br_tree = BlackRedTree(root_node)
        node_6 = root_node.search_by_preorder(6)
        node_6.value.must_equal(6)


        node_6.parent.value.must_equal(15)
        node_7 = br_tree.left_rotate(node_6)
        node_7.value.must_equal(7)
        node_6.parent.value.must_equal(7)
        node_7.parent.value.must_equal(15)
        node_7.left.value.must_equal(6)
        # node_7.parent.value.must_equal(15)

    with test("right_rotate"):
        root_node = BlackRedNode.build_with_preorder_inorder(
            preorder[:],inorder[:])
        root_node.get_inorder_list().must_equal(inorder)
        br_tree = BlackRedTree(root_node)
        root_node.value.must_equal(15)

        br_tree.right_rotate(root_node)
        br_tree.root.value.must_equal(6)



