# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def is_same(left, right):
            if left==None and right==None:
                return True
            if left==None or right==None or left.val != right.val:
                return False
            return is_same(left.left, right.right) and is_same(left.right, right.left)
        if not root: return True
        return is_same(root.left, root.right)
            
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root: return True
        left_q = [root.left]
        right_q = [root.right]
        while left_q:
            left = left_q.pop(0)
            right = right_q.pop(0)
            if left==None and right==None:
                continue
            if left==None or right==None or left.val != right.val:
                return False
            if left:
                left_q += left.left,
                left_q += left.right,
                right_q += right.right,
                right_q += right.left,
        return True
                
            
                