# this is for leetcode 432_All_O_one_Data_Structure.py
# https://github.com/kamyu104/LeetCode/blob/master/Python/all-oone-data-structure.py

class Node(object):
    def __init__(self, value, keys):
        self.value = value
        self.keys = keys
        self.prev = None
        self.next = None
    def __str__(self):
        return "value: {0}, keys: {1}".format(
                self.value, ",".join(self.keys))
    def __repr__(self):
        return self.__str__()

class DoubleLinkedList(object):
    def __init__(self):
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, pos_node, insert_node):
        insert_node.prev = pos_node.prev
        insert_node.next = pos_node
        pos_node.prev.next = insert_node
        pos_node.prev = insert_node

    def remove(self, cur_node):
        cur_node.prev.next = cur_node.next
        cur_node.next.prev = cur_node.prev
        del cur_node

    def is_empty(self):
        # just like self.head.next == self.tail
        return self.head.next is self.tail

    # def begin(self):
    #     return self.head.next

    # def end(self):
    #     return self.tail

    def front(self):
        return self.head.next
    def back(self):
        return self.tail.prev
    def __str__(self):
        result = []
        cur = self.head.next
        while cur != self.tail:
            result += str(cur),
            cur = cur.next
        return "; ".join(result)
    def __repr__(self):
        return self.__str__()

class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        # the key is the key, the value is the node in the double linked list
        self.nodes = {}
        self.count_list = DoubleLinkedList()
        

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        if key not in self.nodes:
            # ("not in", key).p()
            if self.count_list.front().value != 1:
                cur_node = Node(1, {key})
                self.count_list.insert(self.count_list.front(), cur_node)
            else:
                cur_node = self.count_list.front()
                cur_node.keys.add(key)
            self.nodes[key] = cur_node
            # cur_node.p()
        else:
            # ("in", key).p()
            cur_node, next_node = self.nodes[key], self.nodes[key].next
            if next_node == self.count_list.tail or next_node.value != cur_node.value + 1:
                next_node = Node(cur_node.value + 1, {key})
                self.count_list.insert(cur_node.next, next_node)
            else:
                next_node.keys.add(key)
            self.nodes[key] = next_node
            cur_node.keys.discard(key)
            if len(cur_node.keys) == 0:
                self.count_list.remove(cur_node)
        # self.count_list.p()

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        if key in self.nodes:
            cur_node, pre_node = self.nodes[key], self.nodes[key].prev
            if cur_node.value > 1:
                if pre_node.value == self.count_list.head or pre_node.value != cur_node.value - 1:
                    pre_node = Node(cur_node.value - 1, {key})
                    self.count_list.insert(cur_node, pre_node)
                else:
                    pre_node.keys.add(key)
                self.nodes[key] = pre_node
            else:
                del self.nodes[key]

            cur_node.keys.discard(key)
            if len(cur_node.keys) == 0:
                self.count_list.remove(cur_node)


        

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        if self.count_list.back() != self.count_list.head:
            for k in  self.count_list.back().keys:
                return k
        return ""

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        if self.count_list.front() != self.count_list.tail:
            for k in  self.count_list.front().keys:
                return k
        return ""

if __name__ == '__main__':
    from minitest import *

    with test(AllOne):
        ao = AllOne()
        ao.inc("a")
        ao.inc("b")
        ao.inc("c")
        ao.inc("d")
        ao.inc("a")
        ao.inc("b")
        ao.inc("c")
        ao.inc("d")
        ao.inc("c")
        ao.inc("d")
        ao.inc("d")
        ao.inc("a")
        ao.getMinKey().must_equal("b")

        ao = AllOne()
        ao.inc("a")
        ao.inc("b")
        ao.inc("b")
        ao.inc("c")
        ao.inc("c")
        ao.inc("c")
        ao.inc("c")
        ao.dec("b")
        ao.dec("b")
        ao.getMinKey().must_equal("a")

        ao.dec("a")
        ao.getMaxKey().must_equal("c")
        ao.getMinKey().must_equal("c")


