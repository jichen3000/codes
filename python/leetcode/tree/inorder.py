# http://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
# 94. Binary Tree Inorder Traversal
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal2(self, root):
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
            if type(cur_node) == TreeNode:
                if cur_node.right!=None: acc.append(cur_node.right)
                if cur_node.left == None and cur_node.right == None:
                    result.append(cur_node.val)
                else:
                    acc.append(cur_node.val)
                if cur_node.left!=None: acc.append(cur_node.left)
            else:
                result.append(cur_node)
        return result
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def put_all_left(node):
            while node:
                stack.append(node)
                node.left
        stack = [root]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            put_all_left(node.right)
        return res
        
    def recursive(self,root):
        result = []
        if root == None: return result
        def inner(node, result):
            if node.left: inner(node.left, result)
            result += node,
            if node.right: inner(node.right, result)
        inner(root, result)
        return result
        