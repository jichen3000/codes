class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, res):
            l, r, rt = 0
            if root.left:
                l = dfs(root.left, res)
                if root.left.val == root.val:
                    rt = l + 1
                    res[0] = max(res[0], l+1)
            if root.right:
                r = dfs(root.right, res)
                if root.right.val == root.val:
                    rt = max(rt, r+1)
                    res[0] = max(res[0], r+1)
                    if root.left and root.left.val == root.val:
                        res[0] = max(res[0], l+r+2)
            return rt
        if not root: return 0
        res = [0]
        dfs(root, res)
        return res[0]

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        res = [1]
        def inner(node):
            if not node: return 0
            # print(node.val)
            left_c = inner(node.left)
            right_c = inner(node.right)
            count = 1
            if left_c and node.left.val == node.val:
                count += left_c
            if right_c and node.right.val == node.val:
                count += right_c
            res[0] = max(res[0], count)
            # print(node.val, count, res[0])
            if left_c and node.left.val == node.val and right_c and node.right.val == node.val:
                count = max(1+left_c, 1+right_c)
            return count
        count = inner(root)
        res[0] = max(res[0], count)
        return res[0] - 1
        