# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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

class Solution(object):
    def deserialize(self, s):
        """
        :type s: str
        :rtype: NestedInteger
        """
        root = NestedInteger()
        cur = root
        cur_s = ""
        stack = []
        i = 0
        while i < len(s):
            c = s[i]
            if c == "[":
                if s[i+1] != "]":
                    new = NestedInteger()
                    cur.add(new)
                    stack += cur,
                    cur = new
                else:
                    i += 1
            elif c == "]":
                if i > 0 and s[i-1] != "]":
                    cur.setInteger(int(cur_s))
                cur_s = ""
                stack.pop()
            elif c == ",":
                if i > 0 and s[i-1] != "]":
                    cur.setInteger(int(cur_s))
                cur_s = ""
                new =  NestedInteger()
                stack[-1].add(new)
                cur = new
            else:
                cur_s += c
            i += 1
        if cur_s:
            cur.setInteger(int(cur_s))
        return root
        