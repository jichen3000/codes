# http://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
# 145. Binary Tree Postorder Traversal

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)
        
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        acc = []
        result = []
        if root: acc.append(root)
        while len(acc) > 0:
            cur_node = acc.pop()
            if type(cur_node) == TreeNode:
                if cur_node.left == None and cur_node.right == None:
                    result.append(cur_node.val)
                else:
                    acc.append(cur_node.val)
                if cur_node.right: acc.append(cur_node.right)
                if cur_node.left: acc.append(cur_node.left)
            else:
                result.append(cur_node)
                    
        return result

    def recursive(self, root):
        result = []
        if root == None: return result
        def inner(node, result):
            if node.left: inner(node.left, result)
            if node.right: inner(node.right, result)
            result += node,
        inner(root,result)
        return result

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        root = TreeNode(1)
        n2 = TreeNode(2)
        root.left = n2
        n3 = TreeNode(3)
        n2.left = n3
        n4 = TreeNode(4)
        root.right = n4
        n5 = TreeNode(5)
        n4.right = n5
        n6 = TreeNode(6)
        n5.right = n6
        Solution().postorderTraversal(root).p()
        Solution().recursive(root).p()


                