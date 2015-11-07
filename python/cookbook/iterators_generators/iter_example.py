import itertools

class Node:
    def __init__(self, value):
            self._value = value
            self._children = []
    def __repr__(self):
        return "'Node({!r})'".format(self._value)
    def add_child(self, node): 
        self._children.append(node)
        return self
    def __iter__(self):
        return iter(self._children)
    def __eq__(self, other):
        return repr(self) == repr(other)
    # yield from only work in python 3
    # def depth_first(self):
    #     yield self
    #     for c in self:
    #         yield from c.depth_first()

if __name__ == '__main__':
    from minitest import *

    with test(iter):
        root = Node(0)
        child1 = Node(1) 
        child2 = Node(2) 
        root.add_child(child1) 
        root.add_child(child2) 
        list(root).must_equal(["Node(1)", "Node(2)"])
        [ch for ch in root].must_equal(["Node(1)", "Node(2)"])
        list(itertools.islice(root,1,2)).must_equal(["Node(2)"])
        [ch for ch in itertools.islice(root,1,2)].must_equal(["Node(2)"])
        # itertools.dropwhile

        # [ch for ch in root.depth_first].must_equal(["Node(1)", "Node(2)"])
