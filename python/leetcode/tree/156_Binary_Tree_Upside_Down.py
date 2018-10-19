# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return
        def dfs(node, parent):
            # print(node.val)
            res = None
            if node.left:
                # print(node.left.val, node.val)
                res = dfs(node.left, node)
                # print(res.val)
            if parent:
                r = parent.right
                node.left = r
                node.right = parent
                ## must add these two, otherwise, the origin root would not change
                parent.left = None
                parent.right = None
            if res:
                return res
            return node
        return dfs(root, None)                
        