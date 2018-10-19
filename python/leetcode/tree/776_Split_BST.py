# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def splitBST(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[TreeNode]
        """
        res = [None, None]
        if root == None:
            return res
        if root.val < target:
            res[0] = root
            res[0].right, res[1] = self.splitBST(root.right, target)
        else:
            res[1] = root
            res[0],res[1].left = self.splitBST(root.left, target)
        return res
