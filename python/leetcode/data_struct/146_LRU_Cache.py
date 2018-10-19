class DoubleLinkedNode(object):
    def __init__(self, obj):
        self.obj = obj
        self.prev = None
        self.next = None

class DoubleLinkedList(object):
    def __init__(self):
        self.head = DoubleLinkedNode(None)
        self.tail = DoubleLinkedNode(None)
        self.head.next = self.tail
        self.tail.prev = self.head
    def front(self):
        return self.head.next
    def back(self):
        return self.tail.prev
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

    def move_to_last(self, move_node):
        if move_node.next == self.tail:
            return self
        self.remove(move_node)
        self.insert(self.tail, move_node)
        return self




class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.nodes = {}
        self.recents = DoubleLinkedList()
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.nodes:
            cur_node = self.nodes[key]
            self.recents.move_to_last(cur_node)
            return cur_node.obj[1]
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.nodes:
            cur_node = self.nodes[key]
            cur_node.obj[1] = value
            self.recents.move_to_last(cur_node)
        else:
            if len(self.nodes) < self.capacity:
                new_node = DoubleLinkedNode([key,value])
                self.recents.insert(self.recents.tail, new_node)
                self.nodes[key] = new_node
            else:
                first_node = self.recents.front()
                del self.nodes[first_node.obj[0]]
                first_node.obj = [key,value]
                self.recents.move_to_last(first_node)
                self.nodes[key] = first_node
        