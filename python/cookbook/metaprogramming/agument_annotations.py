# cannot use in python2
class Spam:
    def bar(self, x:int, y:int):
        retrun ('Bar 1:', x, y)
    def bar(self, s:str, n:int = 0):
        return ('Bar 2:', s, n)

if __name__ == '__main__':
    from minitest import *

    with test(""):
        s = Spam()
        s.bar(2, 3).must_equal((1,2,3))
        s.bar('hello') # Prints Bar 2: hello 0