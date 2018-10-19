# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        res = []
        stack = [root]
        while stack and len(res) < k:
            cur = stack.pop()
            if type(cur) == TreeNode:
                if cur.right:
                    stack += cur.right,
                stack += cur.val,
                if cur.left:
                    stack += cur.left,
            else:
                res += cur,
        return res[-1]