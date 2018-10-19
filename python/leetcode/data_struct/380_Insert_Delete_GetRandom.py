from random import randint
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pos_dict = {}
        self.l = []

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos_dict:
            self.pos_dict[val] = len(self.l)
            self.l += val,
            return True
        return False
            
        
        

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos_dict:
            return False
        i = self.pos_dict[val]
        self.pos_dict[self.l[-1]] = i
        self.l[i], self.l[-1] = self.l[-1], self.l[i]
        del self.pos_dict[val]
        self.l.pop()
        return True
        

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        i = randint(0, len(self.l)-1)
        return self.l[i]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()