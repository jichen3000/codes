# this is for leetcode 432_All_O_one_Data_Structure.py
# https://github.com/kamyu104/LeetCode/blob/master/Python/all-oone-data-structure.py

class Node(object):
    def __init__(self, value, keys):
        self.value = value
        self.keys = keys
        self.prev = None
        self.next = None

class DoubleLinkedList(object):
    def __init__(self):
        self.head = Node(0, None)
        self.tail = Node(0, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, pre_node, cur_node):
        cur_node.next = pre_node.prev
        cur_node.prev = pre_node
        pre_node.next.prev = cur_node
        pre_node.next = cur_node

    def remove(self, cur_node):
        cur_node.prev.next = cur_node.next
        cur_node.next.prev = cur_node.prev
        del cur_node

    def is_empty(self):
        # just like self.head.next == self.tail
        return self.head.next is self.tail

    # def begin(self):
    #     return self.head

    # def end(self):
    #     return self.tail

    def front(self):
        return self.head.next
    def back(self):
        return self.tail.prev

if __name__ == '__main__':
    from minitest import *

    with test(DoubleLinkedList):
        dll = DoubleLinkedList()
        dll.is_empty().must_equal(True)
        n1 = Node(1,None)
        dll.insert(dll.head, n1)
        dll.head.next.must_equal(n1)
