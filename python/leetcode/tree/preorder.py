# http://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
# 94. Binary Tree Inorder Traversal
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)

class Solution(object):
    def preorder_traversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        acc = []
        if root: acc.append(root) 
        cur_node = None
        result = []
        while len(acc)>0:
            cur_node = acc.pop()
            result.append(cur_node)
            if cur_node.right!=None: acc.append(cur_node.right)
            if cur_node.left!=None: acc.append(cur_node.left)
        return result
    def preorder_traversal_with_none(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        acc = []
        if root: acc.append(root) 
        cur_node = None
        result = []
        while len(acc)>0:
            cur_node = acc.pop()
            result.append(cur_node)
            if cur_node != None:
                acc.append(cur_node.right)
                acc.append(cur_node.left)
        return result

    def preorder_recursive(self,root):
        result = []
        if root == None: return result
        def inner(node, result):
            result += node,
            if node.left: inner(node.left, result)
            if node.right: inner(node.right, result)
        inner(root, result)
        return result


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        root = TreeNode(1)
        n2 = TreeNode(2)
        root.left = n2
        n3 = TreeNode(3)
        n2.left = n3
        n4 = TreeNode(4)
        root.right = n4
        n5 = TreeNode(5)
        n4.right = n5
        n6 = TreeNode(6)
        n5.right = n6
        Solution().preorder_traversal(root).p()
        Solution().preorder_traversal_with_none(root).p()
        Solution().preorder_recursive(root).p()


        