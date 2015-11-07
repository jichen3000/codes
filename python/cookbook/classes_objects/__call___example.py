# __call__ let the instance become callable
class Factorial(object):
    def __init__(self):
        self.cache = {}
    def __call__(self, n):
        if n not in self.cache:
            if n == 0:
                self.cache[n] = 1
            else:
                self.cache[n] = n * self.__call__(n-1)
        return self.cache[n]



# for i in xrange(10):                                                             
#     print("{}! = {}".format(i, fact(i)))

class MyCall(object):
    # def __init__(self):
    #     pass
    def __call__(self):
        print "in __call___"

class NoInstances(type):
    def __call__(self, *args, **kwargs):
        raise TypeError("Can't instantiate directly")
# Example
class Spam(object): 
    __metaclass__ = NoInstances
    @staticmethod
    def grok(x): 
        print('Spam.grok')

if __name__ == '__main__':
    from minitest import *

    with test(MyCall):
        fact = Factorial()
        fact(3).must_equal(6)

        mc = MyCall()
        # mc()

        (lambda : Spam()).must_raise(
                TypeError,"Can't instantiate directly")