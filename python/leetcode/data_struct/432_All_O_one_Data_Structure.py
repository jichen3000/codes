class DoubleLinkedNode:
    def __init__(self, val=None):
        self.val = val
        self.key_set = set()
        self.prev, self.next = None, None
        
class DoubleLinkedList:
    def __init__(self):
        self.head = DoubleLinkedNode()
        self.tail = DoubleLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def insert(self, pos_node, cur_node):
        cur_node.prev = pos_node.prev
        cur_node.next = pos_node
        
        pos_node.prev.next = cur_node
        pos_node.prev = cur_node
        
    def delete(self, cur_node):
        cur_node.prev.next = cur_node.next
        cur_node.next.prev = cur_node.prev
        
    def front(self):
        return self.head.next
    def back(self):
        return self.tail.prev
    
    def move_to_front(self, cur_node):
        self.delete(cur_node)
        self.insert(self.front(), cur_node)
        
    def insert_front(self, cur_node):
        self.insert(self.front(), cur_node)
        
class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ddl = DoubleLinkedList()
        self.mem = {}
        self.v_nodes = {}
        

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: void
        """
        # print("inc", key)
        if key in self.mem:
            v = self.mem[key]
            cur = self.v_nodes[v]
            cur.key_set.discard(key)
            next_val = cur.val + 1
            self.mem[key] = next_val
            if next_val in self.v_nodes:
                self.v_nodes[next_val].key_set.add(key)
            else:
                new = DoubleLinkedNode(next_val)
                new.key_set.add(key)
                self.v_nodes[next_val] = new
                self.ddl.insert(cur.next, new)
                
            if len(self.v_nodes[v].key_set) == 0:
                self.ddl.delete(self.v_nodes[v])
                del self.v_nodes[v]
        else:
            next_val = 1
            self.mem[key] = next_val
            if next_val in self.v_nodes:
                self.v_nodes[next_val].key_set.add(key)
            else:
                new = DoubleLinkedNode(next_val)
                new.key_set.add(key)
                self.v_nodes[next_val] = new
                self.ddl.insert(self.ddl.front(), new)
            
        

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: void
        """
        # print("dec", key)
        if key not in self.mem: return
        v = self.mem[key]
        cur = self.v_nodes[v]
        cur.key_set.discard(key)
        if v > 1:
            prev_val = cur.val - 1
            self.mem[key] = prev_val
            if prev_val in self.v_nodes:
                self.v_nodes[prev_val].key_set.add(key)
            else:
                new = DoubleLinkedNode(prev_val)
                new.key_set.add(key)
                self.v_nodes[prev_val] = new
                self.ddl.insert(cur, new)
        else:
            del self.mem[key]

        if len(self.v_nodes[v].key_set) == 0:
            self.ddl.delete(self.v_nodes[v])
            del self.v_nodes[v]
        
        

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        cur = self.ddl.back()
        for key in cur.key_set:
            return key
        return ""
        

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        cur = self.ddl.front()
        for key in cur.key_set:
            return key
        return ""
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()