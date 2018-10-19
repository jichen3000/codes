# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    ## memory issue
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums: return None
        m = len(nums) // 2
        root = TreeNode(nums[m])
        root.left = self.sortedArrayToBST(nums[:m])
        root.right = self.sortedArrayToBST(nums[m+1:])
        return root
        
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def inner(i,j):
            if i == j: return None
            m = i + (j-i) // 2
            root = TreeNode(nums[m])
            root.left = inner(i, m)
            root.right = inner(m+1, j)
            return root
        return inner(0, len(nums))
            
        