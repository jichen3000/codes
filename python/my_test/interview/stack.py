class LinkedNode(object):
    """docstring for LinkedNode"""
    def __init__(self, value):
        super(LinkedNode, self).__init__()
        self.value = value
        self.next = None

    def add_next(self, value):
        self.next = self.__class__(value)
        return self.next

    def __repr__(self):
        return self.__class__.__name__ +"('{}')".format(self.value)

    def __eq__(self, other):
        if not isinstance(other, self.__class__):
            return False
        return self.value == other.value

class Stack(object):
    def __init__(self):
        super(Stack, self).__init__()
        self.top = None

    def push(self, value):
        cur_node = LinkedNode(value)
        cur_node.next = self.top
        self.top = cur_node
        return self

    def pop(self):
        if self.top:
            result = self.top.value
            self.top = self.top.next
            return result
        return None

    def __iter__(self):
        return self
    def next(self):
        if self.top == None:
            raise StopIteration
        else:
            return self.pop()

def iter_stack(the_stack):
    current = the_stack.pop()
    while current:
        yield current
        current = the_stack.pop()

if __name__ == '__main__':
    from minitest import *

    with test("init"):
        a_node = LinkedNode("a")
        b_node = a_node.add_next("b")
        # b_node.pp()
        c_node = b_node.add_next("c")
        c_node.must_equal(LinkedNode('c'))

    with test(Stack):
        the_stack = Stack()
        the_stack.pop().must_equal(None)
        the_stack.push('a')
        the_stack.push('b')
        the_stack.pop().must_equal('b')
        the_stack.pop().must_equal('a')

        the_stack.push('a')
        the_stack.push('b')
        [i for i in the_stack].must_equal(['b', 'a'])

        the_stack.push('a')
        the_stack.push('b')
        [i for i in iter_stack(the_stack)].must_equal(['b', 'a'])
                       