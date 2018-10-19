from heapq import heappop, heappush
class MaxStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.id = 0
        self.q = []
        self.l = []
        self.deleted_ids_q = set()
        self.deleted_ids_l = set()
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.id += 1
        self.l += (x, self.id),
        heappush(self.q, (-x, -self.id))
        # print(self.q, self.l)
        

    def pop(self):
        """
        :rtype: int
        """
        self.top()
        v, id = self.l.pop()
        self.deleted_ids_q.add(id)
        return v
        

    def top(self):
        """
        :rtype: int
        """
        while self.l[-1][1] in self.deleted_ids_l:
            v, id = self.l.pop()
            self.deleted_ids_l.discard(id)
        return self.l[-1][0]
            
        

    def peekMax(self):
        """
        :rtype: int
        """
        while -self.q[0][1] in self.deleted_ids_q:
            v, nid = heappop(self.q)
            self.deleted_ids_q.discard(-nid)
        return -self.q[0][0]
        
        

    def popMax(self):
        """
        :rtype: int
        """
        self.peekMax()
        v, nid = heappop(self.q)
        self.deleted_ids_l.add(-nid)
        return -v


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

