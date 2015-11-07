
import weakref
class Node(object):
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []
    def __repr__(self):
        return 'Node({!r:})'.format(self.value)
        # property that manages the parent as a weak-reference
    @property
    def parent(self):
        return self._parent if self._parent is None else self._parent()
    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)
    def add_child(self, child): 
        self.children.append(child) 
        child.parent = self
    def __eq__(self, other):
        return repr(self) == repr(other)


if __name__ == '__main__':
    from minitest import *

    with test(Node):
        root = Node('parent')
        c1 = Node('child')
        root.add_child(c1)
        c1.parent.must_equal(root)
        del root
        c1.parent.must_equal(None)