# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def find(parent, node):
            if not node: return None, None
            if node.val == key:
                return parent, node
            if node.val > key:
                return find(node, node.left)
            else:
                return find(node, node.right)
        def leftest(node):
            if node.left:
                return leftest(node.left)
            return node
        parent, the_node = find(None, root)
        if not the_node: return root
        result = the_node.right
        if the_node.left:
            if the_node.right:
                right_lestest = leftest(the_node.right)
                right_lestest.left = the_node.left
                result =  the_node.right
            else:
                result = the_node.left
        if parent == None:
            if the_node.left:
                if the_node.right:
                    right_lestest = leftest(the_node.right)
                    right_lestest.left = the_node.left
                    return the_node.right
                else:
                    return the_node.left
            else:
                return the_node.right
        if parent.left == the_node:
            if the_node.left:
                if the_node.right:
                    right_lestest = leftest(the_node.right)
                    right_lestest.left = the_node.left
                    parent.left = the_node.right
                else:
                    parent.left = the_node.left
            else:
                parent.left = the_node.right
        else:
            if the_node.left:
                if the_node.right:
                    right_lestest = leftest(the_node.right)
                    right_lestest.left = the_node.left
                    parent.right = the_node.right
                else:
                    parent.right = the_node.left
            else:
                parent.right = the_node.right
        return root
            
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def find(parent, node):
            if not node: return None, None
            if node.val == key:
                return parent, node
            if node.val > key:
                return find(node, node.left)
            else:
                return find(node, node.right)
        def leftest(node):
            if node.left:
                return leftest(node.left)
            return node
        parent, the_node = find(None, root)
        if not the_node: return root
        result = the_node.right
        if the_node.left:
            if the_node.right:
                right_lestest = leftest(the_node.right)
                right_lestest.left = the_node.left
            else:
                result = the_node.left
        if parent == None:
            return result
        if parent.left == the_node:
            parent.left = result
        else:
            parent.right = result
        return root        
                
