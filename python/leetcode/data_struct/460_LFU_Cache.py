class Node(object):
    def __init__(self, value, obj):
        self.value = value
        self.obj = obj
        self.prev = None
        self.next = None
    def __str__(self):
        return "Node(value: {0}, obj: {1})".format(
                self.value, str(self.obj))
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
        return self

    def remove(self, remove_node):
        remove_node.prev.next = remove_node.next
        remove_node.next.prev = remove_node.prev
        return self

    def front(self):
        return self.head.next
    def back(self):
        return self.tail.prev
    def is_empty(self):
        return self.head.next == self.tail

    def __str__(self):
        result = []
        cur = self.head.next
        while cur != self.tail:
            result += str(cur),
            cur = cur.next
        return "; ".join(result)
    def __repr__(self):
        return self.__str__()


class LFUCache(object):
    # freq_list
    #   +
    #   |
    #   +
    #  head +--> freq_0 +--> freq_1 +--> ... +--> tail
    #              +           +
    #              |           |
    #              +           +
    #            head        head
    #              +           +
    #              |           |
    #              |           |
    #              v           v
    #            node_a      node_c
    #              +           +
    #              |           |
    #              |           |
    #              v           v
    #            node_b      node_d
    #              +           +
    #              |           |
    #              |           |
    #              v           v
    #            tail        trail

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.freq_dict = {}
        self.node_dict = {}
        self.freq_list = DoubleLinkedList()

        

    def increase_freq(self, key):
        cur_freq = self.freq_dict[key]
        next_freq = cur_freq.next
        if next_freq == self.freq_list.tail or next_freq.value != cur_freq.value+1:
            next_freq = Node(cur_freq.value+1, DoubleLinkedList())
            self.freq_list.insert(cur_freq.next, next_freq)
        cur_node = self.node_dict[key]
        cur_freq.obj.remove(cur_node)
        if cur_freq.obj.is_empty():
            self.freq_list.remove(cur_freq)
        next_freq.obj.insert(next_freq.obj.tail, cur_node)
        return next_freq

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        # ("put",key,value).p()
        if self.capacity==0:
            return
        # try:
        if key in self.node_dict:
            next_freq = self.increase_freq(key)
            cur_node = self.node_dict[key]
            cur_node.value = value
        else:
            # remove one
            if self.capacity == len(self.node_dict):
                remove_in_freq = self.freq_list.front()
                remove_node = remove_in_freq.obj.front()
                remove_in_freq.obj.remove(remove_node)
                if remove_in_freq.obj.is_empty():
                    self.freq_list.remove(remove_in_freq)
                remove_key = remove_node.obj
                del self.freq_dict[remove_key]
                del self.node_dict[remove_key]
            next_freq = self.freq_list.front()
            # next_freq.p()
            if next_freq == self.freq_list.tail or next_freq.value != 0:
                # "in".p()
                next_freq = Node(0, DoubleLinkedList())
                self.freq_list.insert(self.freq_list.front(), next_freq)
            cur_node = Node(value, key)
            next_freq.obj.insert(next_freq.obj.tail, cur_node)
            # self.freq_list.front().p()
        self.node_dict[key] = cur_node
        self.freq_dict[key] = next_freq
            # self.freq_list.p()
        # except AttributeError as e:
        #     print("get",key)
        #     return -101

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # ("get",key).p()
        if self.capacity == 0:
            return -1
        # try:
        if key in self.node_dict:
            next_freq = self.increase_freq(key)
            self.freq_dict[key] = next_freq
            # self.freq_list.p()
            return self.node_dict[key].value
        # except AttributeError as e:
        #     print("get",key)
        #     return -100
        # self.freq_list.p()
        return -1


        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    from minitest import *

    with test(LFUCache):

        cache = LFUCache(2)

        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1).must_equal(1) 
        cache.put(3, 3)
        cache.get(2).must_equal(-1)   
        cache.get(3).must_equal(3)   
        cache.put(4, 4)
        cache.get(1).must_equal(-1)   
        cache.get(3).must_equal(3)   
        cache.get(4).must_equal(4) 

        cache = LFUCache(2)
        cache.put(2,1)
        cache.put(3,1)
        cache.put(2,2)
        cache.put(4,4)
        cache.get(2).must_equal(2)   

        cache = LFUCache(10)
        cache.put(10,13)
        cache.put(3,17)
        cache.put(6,11)
        cache.put(10,5)
        cache.put(9,10)
        cache.get(13)
        cache.put(2,19)
        cache.get(2)
        cache.get(3)
        cache.put(5,25)
        cache.get(8)
        cache.put(9,22)
        cache.put(5,5)
        cache.put(1,30)
        cache.get(11)
        cache.put(9,12)
        cache.get(7)
        cache.get(5)
        cache.get(8)
        cache.get(9)
        cache.put(4,30)
        cache.put(9,3)
        cache.get(9)
        cache.get(10)
        cache.get(10)
        cache.put(6,14)
        cache.put(3,1)
        cache.get(3)
        cache.put(10,11)
        cache.get(8)
        cache.put(2,14)
        cache.get(1)
        cache.get(5)
        cache.get(4)
        cache.put(11,4)
        cache.put(12,24)
        cache.put(5,18)
        cache.get(13)
        cache.put(7,23)
        cache.get(8)
        cache.get(12)
        cache.put(3,27)
        cache.put(2,12)
        cache.get(5)
        cache.put(2,9)
        cache.put(13,4)
        cache.put(8,18)
        cache.put(1,7)
        cache.get(6)
        cache.put(9,29)
        cache.put(8,21)
        cache.get(5)
        cache.put(6,30)
        cache.put(1,12)
        cache.get(10)
        cache.put(4,15)
        cache.put(7,22)
        cache.put(11,26)
        cache.put(8,17)
        cache.put(9,29)
        cache.get(5)
        cache.put(3,4)
        cache.put(11,30)
        cache.get(12)
        cache.put(4,29)
        cache.get(3)
        cache.get(9)
        cache.get(6)
        cache.put(3,4)
        cache.get(1)
        cache.get(10)
        cache.put(3,29)
        cache.put(10,28)
        cache.put(1,20)
        cache.put(11,13)
        cache.get(3)
        cache.put(3,12)
        cache.put(3,8)
        cache.put(10,9)
        cache.put(3,26)
        cache.get(8)
        cache.get(7)
        cache.get(5)
        cache.put(13,17)
        cache.put(2,27)
        cache.put(11,15)
        cache.get(12)
        cache.put(9,19)
        cache.put(2,15)
        cache.put(3,16)
        cache.get(1)
        cache.put(12,17)
        cache.put(9,1)
        cache.put(6,19)
        cache.get(4).must_equal(29)
        cache.get(5).p()
        # cache.get(5)
        # cache.put(8,1)
        # cache.put(11,7)
        # cache.put(5,2)
        # cache.put(9,28)
        # cache.get(1)
        # cache.put(2,2)
        # cache.put(7,4)
        # cache.put(4,22)
        # cache.put(7,24)
        # cache.put(9,26)
        # cache.put(13,28)
        # cache.put(11,26)
