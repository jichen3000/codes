# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sort_list_to_bst(self,the_list):
        '''
            change to list
        '''
        if len(the_list) == 0:
            return None
        elif len(the_list) == 1:
            return TreeNode(the_list[0].val)
        else:
            root_index = len(the_list)/2
            root = TreeNode(the_list[root_index].val)
            root.left = self.sort_list_to_bst(the_list[0:root_index])
            root.right = self.sort_list_to_bst(the_list[root_index+1:])
            return root
            

    
    def sortedListToBST_to_list(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        the_list =  []
        cur_node = head
        while cur_node:
            the_list.append(cur_node)
            cur_node = cur_node.next
        return self.sort_list_to_bst(the_list)
        
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        acc = [root]
        result = []
        while len(acc) > 0:
            cur_node = acc.pop()
            if type(cur_node) == TreeNode:
                if cur_node.right:
                    acc.append(cur_node.right)
                acc.append(cur_node.val)
                if cur_node.left:
                    acc.append(cur_node.left)
            else:
                cur_value = cur_node
                if len(result)>0 and cur_value <= result[-1]:
                    return False
                else:
                    result.append(cur_value)
        return True

        