from collections import defaultdict
from random import randint
import random
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hash = {}
        self.count = 0
        self.all_single = True
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.count += 1
        if val in self.hash:
            self.hash[val] += 1
            self.all_single = False
            return False
        else:
            self.hash[val] = 1
            return True
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.hash:
            self.count -= 1
            if self.hash[val] > 1:
                self.hash[val] -= 1
            else:
                del self.hash[val]
            return True
        return False
        

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        index = randint(0, self.count-1)
        if self.all_single:
            return self.hash.keys()[index]
        for key in self.hash.keys():
            if index < self.hash[key]:
                return key
            index -= self.hash[key]

            
        
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.values = []
        self.indexes = {}
        

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        self.values.append(val)
        if val in self.indexes:
            self.indexes[val].append(len(self.values)-1)
            return False
        else:
            self.indexes[val] = [len(self.values)-1]
            return True
        

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.indexes:
            i = self.indexes[val][-1]
            self.indexes[self.values[-1]][-1] = i
            self.values[i], self.values[-1] = self.values[-1], self.values[i]
            self.values.pop()
            self.indexes[val].pop()
            return True
        return False


    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.values)
        
            


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
