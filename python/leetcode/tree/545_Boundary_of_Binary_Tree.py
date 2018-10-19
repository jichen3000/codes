# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root: return res
        res += root.val,
        def add_left_boundary(node):
            if not node or (not node.left and not node.right):
                return
            res.append(node.val)
            if node.left: add_left_boundary(node.left)
            else: add_left_boundary(node.right)
        def add_right_boundary(node):
            if not node or (not node.left and not node.right):
                return
            if node.right: add_right_boundary(node.right)
            else: add_right_boundary(node.left)
            res.append(node.val)
        def add_leaves(node):
            if not node: return
            if not node.left and not node.right:
                res.append(node.val)
            else:
                add_leaves(node.left)
                add_leaves(node.right)
            
        add_left_boundary(root.left)
        add_leaves(root.left)
        add_leaves(root.right)
        add_right_boundary(root.right)
        return res
        
        