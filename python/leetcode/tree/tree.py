class TreeNode(object):
    def __init__(self, value):
        super(TreeNode,self).__init__()
        self.value = value
        self.children = []

    def add_child(self, value):
        child = TreeNode(value)
        self.children.append(child)
        return child

    def __repr__(self):
        # return '\'{0}\''.format(self.value)
        return repr(self.value)

    def __eq__(self, value):
        return value == self.value

    def depth_first_list_recursively(self):
        result = [self]
        for child in self.children:
            result += child.depth_first_list_recursively()
        return result

    # def breadth_first_list_recursively(self, is_root=True):
    #     ''' has an issue '''
    #     result = []
    #     if is_root: result.append(self)
    #     result += self.children
    #     for child in self.children:
    #         result += child.breadth_first_list_recursively(False)
    #     return result


    def breadth_first_list(self):
        result = []
        acc = [self]
        while len(acc) > 0:
            current = acc.pop(0)
            result.append(current)
            acc += current.children
        return result

    def depth_first_list(self):
        result = []
        acc = [self]
        while len(acc) > 0:
            current = acc.pop()
            result.append(current)
            acc += current.children[::-1]
        return result

    def breadth_first_list_with_level(self):
        result = []
        cur_queue = [self]
        next_queue = []
        while len(cur_queue) > 0:
            current = cur_queue.pop(0)
            result.append(current)
            next_queue += current.children
            if len(cur_queue) == 0:
                cur_queue, next_queue = next_queue, cur_queue
                result.append("\n")
        return result



TREE_EXAMPLE = TreeNode("a")
b_node = TREE_EXAMPLE.add_child("b")
c_node = TREE_EXAMPLE.add_child("c")

d_node = b_node.add_child("d")
e_node = b_node.add_child("e")

f_node = c_node.add_child("f")
g_node = c_node.add_child("g")

h_node = d_node.add_child("h")
i_node = d_node.add_child("i")

j_node = e_node.add_child("j")
k_node = e_node.add_child("k")

l_node = h_node.add_child("l")
m_node = h_node.add_child("m")


if __name__ == '__main__':
    from minitest import *

    '''
              a
            b    c
          d   e f g
         h i j k
        l m
                
    '''
    with test(TreeNode):

        TREE_EXAMPLE.must_equal("a")

        TREE_EXAMPLE.depth_first_list_recursively().must_equal(
            ['a', 'b', 'd', 'h', 'l', 'm', 'i', 'e', 'j', 'k', 'c', 'f', 'g'])

        # TREE_EXAMPLE.breadth_first_list_recursively().pp()

        TREE_EXAMPLE.breadth_first_list().must_equal(
            ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm'])
        TREE_EXAMPLE.depth_first_list().must_equal(
            ['a', 'b', 'd', 'h', 'l', 'm', 'i', 'e', 'j', 'k', 'c', 'f', 'g'])

        TREE_EXAMPLE.breadth_first_list_with_level().must_equal(
            ['a', '\n', 'b', 'c', '\n', 'd', 'e', 'f', 'g', 
             '\n', 'h', 'i', 'j', 'k', '\n', 'l', 'm', '\n'])

