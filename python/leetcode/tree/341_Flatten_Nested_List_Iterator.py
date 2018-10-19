# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.nestedList = nestedList
        self.cur_list = self.nestedList
        self.stack = []
        self.next_one = None
        self.setNext()
        

    def next(self):
        """
        :rtype: int
        """
        # print("next",self.next_one)
        tmp = self.next_one
        self.setNext()
        return tmp
        

    def hasNext(self):
        """
        :rtype: bool
        """
        # print("has")
        return self.next_one != None
    
    def setNext(self):
        while len(self.cur_list) > 0 and self.cur_list[0].isInteger()==False:
            self.stack += self.cur_list,
            self.cur_list = self.cur_list.pop(0).getList()
        while self.stack and len(self.cur_list) == 0:
            self.cur_list = self.stack.pop()
        if len(self.cur_list) > 0 and self.cur_list[0].isInteger()==False:
            self.setNext()
            return
        if len(self.stack) == 0 and len(self.cur_list) == 0:
            self.next_one = None
        else:
            self.next_one = self.cur_list.pop(0)


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = [] 
        for i in reversed(nestedList):
            self.stack += i,
        self.next_one = self.getNext()

    def next(self):
        """
        :rtype: int
        return tmp
        """
        # print("next")
        pre = self.next_one
        self.next_one = self.getNext()
        # print pre
        return pre


    def hasNext(self):
        """
        :rtype: bool
        """
        # print "has"
        # print self.next_one
        return self.next_one != None

    def getNext(self):
        if not self.stack: return None
        cur = self.stack.pop()
        # print cur.isInteger()
        while not cur.isInteger():
            for i in reversed(cur.getList()):
                self.stack += i,
            if not self.stack: return None
            cur = self.stack.pop()
            # print cur.isInteger()
        # print cur.getInteger()
        return cur
        

