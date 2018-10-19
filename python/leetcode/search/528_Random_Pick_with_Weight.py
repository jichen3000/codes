from random import randint
from bisect import bisect_left
class Solution:

    def __init__(self, w):
        """
        :type w: List[int]
        """
        s = 0
        self.mem = []
        for v in w:
            s += v
            self.mem += s,
        
        

    def pickIndex(self):
        """
        :rtype: int
        """
        i = randint(1, self.mem[-1])
        return bisect_left(self.mem, i)
        
        
        
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()