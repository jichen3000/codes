# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        acc = []
        if root: acc.append((0,root))
        result = []
        while len(acc)>0:
            cur_level, cur_node = acc.pop()
            next_level = cur_level+1
            if len(result) < next_level:
                result.append([cur_node.val])
            else:
                result[cur_level].append(cur_node.val)
            if cur_node.right: acc.append((next_level, cur_node.right))
            if cur_node.left: acc.append((next_level, cur_node.left))
        return result        