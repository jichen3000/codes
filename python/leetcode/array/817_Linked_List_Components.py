# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def numComponents(self, head, g):
        """
        :type head: ListNode
        :type g: List[int]
        :rtype: int
        """
        mem = set(g)
        cur = head
        res, cur_count = 0, 0
        while cur:
            if cur.val in mem:
                cur_count += 1
            else:
                if cur_count > 0:
                    res += 1
                cur_count = 0
            cur = cur.next
        if cur_count > 0:
            res += 1
        return res
            
        