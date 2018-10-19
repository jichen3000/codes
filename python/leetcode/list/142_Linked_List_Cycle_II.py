# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
    with O(n) time and O(1) space without modifying the list
    
    let n is total length of list,
        x is the length before entry of loop,
        l is the length, when slow meet the fast
        m is l - x as (set 4)
    then, when fast meet the slow,
        n + m = 2l + 1, and x + m = l(according set 4), so n - x = l + 1
    after meeting, slow still need to go x + 2 to entry of loop
    let fast start from head, it will go x + 1 to entry of loop
    example:
    1 -> 2 -> 3 -> 4 -> 5
              |         |
              |         6
              |         |
              9 <- 8 <- 7
    n = 9
    x = 2
    l = 6
    m = 4

    slow   fast
     1      3
     2      5
     3      7
     4      9
     5      4
     6      6

then slow = slow + 2, fast = 1
    slow   fast
     8      1
     9      2
     3      3

'''
class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None: return None
        slow = head
        fast = head.next
        if fast == None: return None
        fast = fast.next
        if fast == None: return None
        while slow.val != fast.val:
            slow = slow.next
            fast = fast.next
            if fast == None: return None
            fast = fast.next
            if fast == None: return None
        slow = slow.next.next
        fast = head
        while slow.val != fast.val:
            slow = slow.next
            fast = fast.next
        return slow