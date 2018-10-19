from bisect import bisect
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.l = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        self.l.insert(bisect(self.l, num), num)
        

    def findMedian(self):
        """
        :rtype: float
        """
        n = len(self.l)
        if n % 2 == 0:
            return float(self.l[n/2-1]+self.l[n/2])/2
        else:
            return float(self.l[n/2])
        
from heapq import heappush, heappop
class MedianFinder(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.smalls = []
        self.larges = []
        

    def addNum(self, num):
        """
        :type num: int
        :rtype: void
        """
        if len(self.smalls) == 0 and len(self.larges) == 0:
            heappush(self.smalls, -num)
            return
        if num <= -self.smalls[0]:
            if len(self.smalls) > len(self.larges):
                heappush(self.smalls, -num)
                heappush(self.larges, -heappop(self.smalls))
            else:
                heappush(self.smalls, -num)
            # print "small", num, self.smalls, self.larges
        else:
            if len(self.larges) > len(self.smalls):
                heappush(self.larges, num)
                heappush(self.smalls, -heappop(self.larges))
            else:
                heappush(self.larges, num)
            # print "large", num, self.smalls, self.larges

    def findMedian(self):
        """
        :rtype: float
        """
        if len(self.smalls) > len(self.larges):
            return float(-self.smalls[0])
        elif len(self.smalls) < len(self.larges):
            return float(self.larges[0])
        else:
            return float(-self.smalls[0]+self.larges[0]) / 2

