from tree import *

def invert_recursively_and_change_self(self):
    # self.children[0], self.children[1] = self.children[1], self.children[0]
    self.children = self.children[::-1]
    [c.invert_recursively_and_change_self() for c in self.children]
    return self

def invert_change_self(self):
    for c in self.breadth_first_list():
        c.children = c.children[::-1]
    return self

'''
          a
        b    c
      d   e f g
     h i j k
    l m
            
'''
TreeNode.invert_recursively_and_change_self = invert_recursively_and_change_self
TreeNode.invert_change_self = invert_change_self

if __name__ == '__main__':
    from minitest import *

    with test(invert_recursively_and_change_self):
        TREE_EXAMPLE.breadth_first_list().must_equal(
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'])
        TREE_EXAMPLE.invert_recursively_and_change_self().pp()
        TREE_EXAMPLE.breadth_first_list().must_equal(
            ['a', 'c', 'b', 'g', 'f', 'e', 'd', 'k', 'j', 'i', 'h', 'm', 'l'])

    with test(invert_change_self):
        TREE_EXAMPLE.breadth_first_list().pp()
        TREE_EXAMPLE.invert_change_self().breadth_first_list().pp()
