class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
    def __repr__(self):
        return str(self.value)


    def get_inorder_list(self):
        acc = [self]
        result = []
        while len(acc) > 0:
            cur_node = acc.pop()
            if type(cur_node) == self.__class__:
                if cur_node.right: acc.append(cur_node.right)
                acc.append(cur_node.value)
                if cur_node.left: acc.append(cur_node.left)
            else:
                result.append(cur_node)
        return result

    def get_preorder_list(self):
        acc = [self]
        result = []
        while len(acc) > 0:
            cur_node = acc.pop()
            result.append(cur_node.value)
            if cur_node.right: acc.append(cur_node.right)
            if cur_node.left: acc.append(cur_node.left)
        return result

    def search_by_preorder(self, search_value):
        acc = [self]
        while len(acc) > 0:
            cur_node = acc.pop()
            if cur_node.value == search_value:
                return cur_node
            if cur_node.right: acc.append(cur_node.right)
            if cur_node.left: acc.append(cur_node.left)
        return None

    def get_min_node(self):
        cur_node = self
        while cur_node.left:
            cur_node = cur_node.left
        return cur_node

    def get_max_node(self):
        cur_node = self
        while cur_node.right:
            cur_node = cur_node.right
        return cur_node

    def get_successor(self):
        if self.right:
            return self.right.get_min_node()
        cur_node = self
        parent = cur_node.parent
        while parent and parent.right == cur_node:
            cur_node = parent
            parent = cur_node.parent
        return parent

    def get_predecessor(self):
        if self.left:
            return self.left.get_max_node()
        cur_node = self
        parent = cur_node.parent
        while parent != None and parent.left == cur_node:
            cur_node = parent
            parent = cur_node.parent
        return parent



    @classmethod
    def build_with_preorder_inorder(cls,preorder,inorder):
        # pass None and []
        if inorder:
            root_index = inorder.index(preorder.pop(0))
            root = cls(inorder[root_index])
            root.left = cls.build_with_preorder_inorder(
                    preorder,inorder[0:root_index])
            root.right = cls.build_with_preorder_inorder(
                    preorder,inorder[root_index+1:])
            if root.left != None:
                root.left.parent = root
            if root.right != None:
                root.right.parent = root
            return root

class Tree(object):
    def __init__(self, root):
        self.root = root

    def insert(self, new_node):
        cur_node = self.root
        # pre_node as the trailing node
        pre_node = None
        while cur_node != None:
            pre_node = cur_node
            if new_node.value < cur_node.value:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        if pre_node == None:
            self.root = new_node
            return new_node
        new_node.parent = pre_node
        if pre_node.value < new_node.value:
            pre_node.left = new_node
        else:
            pre_node.right = new_node
        return new_node



    def delete(self, the_node):
        # z are the detele one
        def transplant(the_node, replace_node):
            the_parent = the_node.parent
            if the_parent == None:
                self.root = replace_node
            elif the_parent.left == the_node:
                the_parent.left = replace_node
            else:
                the_parent.right = replace_node
            if replace_node != None:
                replace_node.parent = the_parent
            return replace_node

        if the_node.left == None and the_node.right == None:
            transplant(the_node, the_node.right)
        elif the_node.left == None and the_node.right != None:
            transplant(the_node, the_node.right)
        elif the_node.left != None and the_node.right == None:
            transplant(the_node, the_node.left)
        elif the_node.left != None and the_node.right != None and the_node.right.left == None:
            replace_node = the_node.right
            pre_left = the_node.left
            transplant(the_node, replace_node)
            replace_node.left = pre_left
        else:
            successor = the_node.right.get_min_node
            transplant(successor, successor.right)
            transplant(the_node, successor)
            successor.right = the_node.right
            successor.left = the_node.left
        return the_node




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
    root    = TreeNode(15)
    node_6  = TreeNode(6)
    node_3  = TreeNode(3)
    node_2  = TreeNode(2)
    node_4  = TreeNode(4)
    node_7  = TreeNode(7)
    node_13 = TreeNode(13)
    node_9  = TreeNode(9)
    node_18 = TreeNode(18)
    node_17 = TreeNode(17)
    node_20 = TreeNode(20)

    root.left = node_6
    root.right = node_18
    node_6.left = node_3
    node_6.right = node_7
    node_3.left = node_2
    node_3.right = node_4
    node_7.right = node_13
    node_13.left = node_9
    node_18.left = node_17
    node_18.right = node_20

    node_6.parent = root
    node_3.parent = node_6
    node_7.parent = node_6
    node_2.parent = node_3
    node_4.parent = node_3
    node_7.parent = node_6
    node_13.parent = node_7
    node_9.parent = node_13
    node_18.parent = root
    node_17.parent = node_18
    node_20.parent = node_18

    preorder = [15,6,3,2,4,7,13,9,18,17,20]
    inorder =  [2,3,4,6,7,9,13,15,17,18,20]

    with test("get_inorder_list"):
        root.get_inorder_list().must_equal(inorder)
        root.get_preorder_list().must_equal(preorder)

    with test("build the tree"):
        new_root = TreeNode.build_with_preorder_inorder(preorder,inorder)
        new_root.get_inorder_list().must_equal(inorder)

    with test("search_by_preorder"):
        other_6 = root.search_by_preorder(6)
        other_6.value.must_equal(6)


    with test("get_min_node"):
        root.get_min_node().value.must_equal(2)
        node_18.get_min_node().value.must_equal(17)
        node_17.get_min_node().value.must_equal(17)

    with test("max"):
        root.get_max_node().value.must_equal(20)
        node_6.get_max_node().value.must_equal(13)
        node_18.get_max_node().value.must_equal(20)
        node_20.get_max_node().value.must_equal(20)

    with test("get_successor"):
        node_13.get_successor().value.must_equal(15)
        node_4.get_successor().value.must_equal(6)
        root.get_successor().value.must_equal(17)
        node_20.get_successor().must_equal(None)

    with test("get_predecessor"):
        root.get_predecessor().value.must_equal(13)
        node_17.get_predecessor().value.must_equal(15)

    with test("insert"):
        tree = Tree(root)
        new_node = tree.insert(TreeNode(12))
        new_node.value.must_equal(12)
        new_node.parent.value.must_equal(9)

        preorder1 = [12,5,2,9,18,15,17,19]
        inorder1 =  [2,5,9,12,15,17,18,19]
        new_root1 = TreeNode.build_with_preorder_inorder(preorder1,inorder1)
        tree1 = Tree(new_root1)
        new_node1 = tree1.insert(TreeNode(13))
        new_node1.parent.value.must_equal(15)



