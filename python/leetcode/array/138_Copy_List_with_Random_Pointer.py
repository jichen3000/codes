# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        new_head = RandomListNode(0)
        cur, pre = head, new_head
        mem = {}
        while cur:
            if cur not in mem:
                mem[cur] = RandomListNode(cur.label)
            pre.next = mem[cur]
            if cur.random and cur.random not in mem:
                mem[cur.random] = RandomListNode(cur.random.label)
            if cur.random:
                mem[cur].random = mem[cur.random]
            pre, cur = mem[cur], cur.next
        return new_head.next