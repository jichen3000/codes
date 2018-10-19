# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        # print("preorder, inorder",preorder, inorder)
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) > 1:
            inorder_root_index = inorder.index(root.val)
            inorder_left_part = inorder[0:inorder_root_index]
            inorder_right_part = inorder[inorder_root_index+1:]
            
            preorder_left_last_index = len(inorder_left_part)
            # print("preorder_left_last_index",preorder_left_last_index)
            preorder_left_part = preorder[1:preorder_left_last_index+1]
            preorder_right_part = preorder[preorder_left_last_index+1:]
            root.left = self.buildTree(preorder_left_part, inorder_left_part)
            root.right = self.buildTree(preorder_right_part, inorder_right_part)


        return root
        