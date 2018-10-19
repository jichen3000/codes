# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        def reverse(head):
            cur = head
            pre = None
            while cur:
                nn = cur.next
                cur.next = pre
                pre = cur
                cur = nn
            return pre
                
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        if n <= 1:
            return True
        half = n // 2
        cur = head
        for i in range(half):
            cur = cur.next
        tail = reverse(cur)
        res = True
        ct, cur = tail, head
        for i in range(half):
            if ct.val != cur.val:
                res = False
                break
            ct, cur = ct.next, cur.next
        reverse(tail)
        return res
        
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        pre, slow, fast = None, head, head
        while fast and fast.next:
            fast = fast.next.next
            slow.next, slow, pre = pre, slow.next, slow
        res = True
        back, pre = pre, slow
        if fast: slow = slow.next
        while back:
            res = res and back.val == slow.val
            back.next, back, pre = pre, back.next, back
            slow = slow.next
        return res