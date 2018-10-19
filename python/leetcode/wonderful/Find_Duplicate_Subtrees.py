# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findDuplicateSubtrees(self, root):
        def tuplify(root):
            if root:
                tuple = root.val, tuplify(root.left), tuplify(root.right)
                trees[tuple].append(root)
                return tuple
        trees = collections.defaultdict(list)
        tuplify(root)
        print(trees)
        return [roots[0] for roots in trees.values() if roots[1:]]        
        