# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        acc = [(root, None)]
        node_parent_list = []
        while len(acc) > 0:
            cur_node, cur_parent = acc.pop(0)
            setattr(cur_node, 'sum', cur_node.val)
            node_parent_list.append((cur_node, cur_parent))
            if cur_node.left: acc.append((cur_node.left,cur_node))
            if cur_node.right: acc.append((cur_node.right,cur_node))
        for cur_node, cur_parent in reversed(node_parent_list):
            if cur_parent:
                cur_parent.sum += cur_node.sum
        for cur_node, cur_parent in node_parent_list:
            if cur_node.left and cur_node.left.sum==cur_node.val:
                return True
            if cur_node.right and cur_node.right.sum==cur_node.val:
                return True

            if cur_node.left and cur_node.right:
                if cur_node.val + cur_node.left.sum == cur_node.right.sum:
                    return True
                if cur_node.val + cur_node.right.sum == cur_node.left.sum:
                    return True
        return False

            
            
            