import sys
class ClosureInstance:
    def __init__(self, locals=None): 
        if locals is None:
            locals = sys._getframe(1).f_locals

        # Update instance dictionary with callables
        self.__dict__.update(
            (key,value) for key, value in locals.items() 
            if callable(value) )
    # Redirect special methods
    def __len__(self):
        return self.__dict__['__len__']()

# Example use
def Stack(): 
    items = []
    def push(item): 
        items.append(item)
    def pop():
        return items.pop()
    def __len__():
        return len(items)
    return ClosureInstance()

if __name__ == '__main__':
    from minitest import *

    with test(Stack):
        s = Stack()
        s.push(10)
        s.push(20)
        print s
        print type(s)
        len(s).must_equal(2)
        s.pop().must_equal(20)
        pass