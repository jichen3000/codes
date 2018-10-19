# Given a binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to 
# any node in the tree along the parent-child connections. 
# The path must contain at least one node and does not need to go through the root.


# For example:
# Given the below binary tree,

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import sys
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if node.left == None and node.right == None:
                return [node.val, node.val]
            left_max_v, left_max_p = -sys.maxint, -sys.maxint
            if node.left:
                left_max_v, left_max_p = dfs(node.left)
            right_max_v, right_max_p = -sys.maxint, -sys.maxint
            if node.right:
                right_max_v, right_max_p = dfs(node.right)
            max_v = max(left_max_v, right_max_v,
                    node.val + left_max_p + right_max_p,
                    node.val, node.val + left_max_p, node.val + right_max_p,
                    right_max_p, left_max_p)
            max_p = max(left_max_p, right_max_p, 0) + node.val
            return [max_v, max_p]
        return dfs(root)[0]

