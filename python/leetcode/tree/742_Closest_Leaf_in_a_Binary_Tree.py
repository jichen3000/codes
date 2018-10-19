## median

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findClosestLeaf(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: int
        """
        closest_leaf = None
        closest_path = 0
        parent_path = 0
        target_parent = None
        acc = [root]
        def is_leaf(node):
            return node.left == None and node.right == None
        while acc:
            cur = acc.pop()
            if getattr(cur, 'added', False) or is_leaf(cur):
                if is_leaf(cur):
                    setattr(cur,'path', 0)
                    setattr(cur, 'path_node', cur.val)
                else:
                    if cur.left == None:
                        setattr(cur,'path', cur.right.path)
                        setattr(cur, 'path_node', cur.right.path_node)
                    elif cur.right == None:
                        setattr(cur,'path', cur.left.path)
                        setattr(cur, 'path_node', cur.left.path_node)
                    else:
                        if cur.left.path < cur.right.path:
                            setattr(cur,'path', cur.left.path)
                            setattr(cur, 'path_node', cur.left.path_node)
                        else:
                            setattr(cur,'path', cur.right.path)
                            setattr(cur, 'path_node', cur.right.path_node)
                if cur.val == target:
                    min_path = cur.path
                    closest_leaf = cur.path_node
                    parent_path = 1
                    target_parent = cur
                    if parent_path >= min_path:
                        return closest_leaf
                if target_parent and  (cur.left == target_parent or cur.right == target_parent):
                    if cur.path + parent_path < min_path:
                        min_path = cur.path + parent_path
                        closest_leaf = cur.path_node
                    parent_path += 1
                    target_parent = cur
                    if parent_path >= min_path:
                        return closest_leaf
            else:
                setattr(cur, 'added', True)
                acc.append(cur)
                if cur.right: acc.append(cur.right)
                if cur.left: acc.append(cur.left)
        return closest_leaf

