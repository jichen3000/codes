# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:

    # Input: root = [4,2,5,1,3], target = 3.714286, and k = 2

    #     4
    #    / \
    #   2   5
    #  / \
    # 1   3
    #    / \
    #  2.5 3.5
    # 2.2 2.7
    # small_stack = [2, 3, 3.5]
    # large_stack = [4]
    # 3.5, not left node
    # 4,  put 5 in stack [5]
    # 3, less than target, means all its right node has been handled,
    # so put 3 in res, put its left node 2.5 in small stack, and loop its all right node 
    # to small stack [2, 2.5, 2.7]
    # so idea is using two stacks, one for larger, one for smaller
    # first find the closest node, in the same time, put the node on the path to two stacks
    # then from two stacks, move the closest value one to result
    # if the node come from small stack, put its left node, and its left node's all right nodes
    # to small stack
    # if the node come from large stack, put its right node, and its right node's all left nodes
    # to large stack
    # time is O(n), space is O(n)
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        def find_closest(node):
            if node == None:
                return
            if node.val > target:
                large_stack.append(node)
                find_closest(node.left)
            elif node.val < target:
                small_stack.append(node)
                find_closest(node.right)
            else:
                large_stack.append(node)
        def put_all_right(node):
            while node:
                small_stack.append(node)
                node = node.right
        def put_all_left(node):
            while node:
                large_stack.append(node)
                node = node.left
        if k <= 0: return []
        large_stack, small_stack = [], []
        find_closest(root)
        res = []
        while len(res) < k:
            if len(large_stack) > 0 and (len(small_stack) == 0 or large_stack[-1].val - target <= target - small_stack[-1].val):
                node = large_stack.pop()
                res.append(node.val)
                if node.val == target:
                    put_all_right(node.left)
                put_all_left(node.right)
            else:
                node = small_stack.pop()
                res.append(node.val)
                put_all_right(node.left)
        return res


    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        if not root: return []
        cur = root
        largers, smallers, larger_values, smaller_values, res = [], [], [], [], []
        while cur:
            if cur.val < target:
                smallers += cur,
                print("smallers",cur.val)
                cur = cur.right
            elif cur.val > target:
                largers += cur,
                print("largers",cur.val)
                cur = cur.left
        # print(smallers, largers)
        def small_first(node):
            if node.left: 
                if small_first(node.left):
                    return True
            larger_values.append(node.val)
            if len(larger_values) >= k:
                return True
            if node.right: small_first(node.right)
        def large_first(node):
            if node.right: 
                if large_first(node.right):
                    return True
            smaller_values.append(node.val)
            if len(smaller_values) >= k:
                return True
            if node.left: large_first(node.left)
        for cur in largers[::-1]:
            temp_left, cur.left = cur.left, None
            small_first(cur)
            cur.left = temp_left
        for cur in smallers[::-1]:
            temp_right, cur.right = cur.right, None
            large_first(cur)
            cur.right = temp_right
        print(smaller_values, larger_values)
        while len(res)<k:
            small_v = smaller_values[0] if smaller_values else float("inf")
            large_v = larger_values[0] if larger_values else float("inf")
            if target - small_v <= large_v - target:
                val = smaller_values.pop(0)
            else:
                val = larger_values.pop(0)
            res += val,
        return res