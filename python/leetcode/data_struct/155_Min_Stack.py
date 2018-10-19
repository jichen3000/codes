class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min_v = None
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.min_v == None:
            self.min_v = x
            self.stack += 0,
        else:
            self.stack += x - self.min_v,
            if self.min_v > x:
                self.min_v = x
        

    def pop(self):
        """
        :rtype: void
        """
        if self.stack[-1] < 0:
            self.min_v -= self.stack[-1]
        self.stack.pop()
        if len(self.stack) == 0:
            self.min_v = None
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack[-1] >= 0:
            return self.stack[-1] + self.min_v
        else:
            return self.min_v
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_v
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()