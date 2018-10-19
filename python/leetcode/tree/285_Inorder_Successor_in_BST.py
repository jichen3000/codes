# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        res = []
        index = [None]
        def inorder(cur):
            if cur.left: inorder(cur.left)
            res.append(cur)
            if cur == p:
                index[0] = len(res) - 1
            if cur.right: inorder(cur.right)
        inorder(root)
        if index[0] + 1 < len(res):
            return res[index[0]+1]
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        found = [False]
        res = [None]
        def inorder(cur):
            if cur.left and cur.val > p.val: inorder(cur.left)
            if found[0]: res[0] = cur
            found[0] = (cur == p)
            if cur.right and not res[0]: inorder(cur.right)
        inorder(root)
        return res[0]       