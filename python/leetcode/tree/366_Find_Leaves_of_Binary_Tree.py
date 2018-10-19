# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import defaultdict
        if not root: return []
        mem = defaultdict(list)
        max_level = [0]
        def dfs(node):
            left_level = 0
            right_level = 0
            if node.left:
                left_level = dfs(node.left) + 1
            if node.right:
                right_level = dfs(node.right) + 1
            level = max(left_level, right_level)
            max_level[0] = max(max_level[0], level)
            mem[level].append(node.val)
            print(node.val, level, left_level, right_level)
            return level
        dfs(root)
        print(max_level, mem)
        return [mem[i] for i in range(max_level[0]+1)]
            
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().maxPoints(create_points(
        #         [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]])).must_equal(4)
        # Solution().maxPoints(create_points(
        #         [[1,1],[1,1],[2,3]])).must_equal(3)
        Solution().maxPoints(create_points(
                [[3,1],[12,3],[3,1],[-6,-1]])).must_equal(4)


        