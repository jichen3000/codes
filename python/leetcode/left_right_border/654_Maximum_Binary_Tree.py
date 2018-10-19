# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # this actually is the second version, but slower the below one.
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def inner(start, end):
            if end == 0:
                return None
            max_v, max_i = nums[start], start
            for i in range(start+1, end):
                if nums[i] > max_v:
                    max_v, max_i = nums[i], i
            node = TreeNode(max_v)
            if max_i + 1 < end:
                node.right = inner(max_i+1, end)
            if max_i-1 >= start:
                node.left = inner(start, max_i)
            return node
        return inner(0, len(nums))
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def inner(nums):
            if len(nums) == 0:
                return None
            if len(nums) == 1:
                return TreeNode(nums[0])

            max_num = max(nums)
            root = TreeNode(max_num)
            max_index = nums.index(max_num)
            #print("nums[0:max_index]",nums[0:max_index])
            #print("nums[max_index+1:]",nums[max_index+1:])
            root.left = inner(nums[0:max_index])
            root.right = inner(nums[max_index+1:])
            return root
        return inner(nums)
    # brilliant
    # for i, in the left side, small than me, is my left child
    # in the right side, small than me, is my left child
    # larger than me, is my parent
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        stack = []
        for i in range(len(nums)):
            node = TreeNode(nums[i])
            while stack and stack[-1].val < nums[i]:
                node.left = stack.pop()
            if stack:
                stack[-1].right = node
            stack.append(node)
        return stack[0]
        

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().constructMaximumBinaryTree([3,2,1,6,0,5]).must_equal(False)

