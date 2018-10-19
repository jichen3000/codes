import print_helper
class Node(object):
    def __init__(self, data=None):
        self.data=data
        self.left = None
        self.right = None
    def __repr__(self):
        data_str = self.data
        if self.data: 
            data_str = "'{}'".format(self.data)
        return "{}(data={})".format(
                self.__class__.__name__, data_str)

    # pre order
    def depth_first_list(self):
        acc = [self]
        result = []
        count = 100
        index = 0
        while len(acc) > 0 and index < count:
            cur_node = acc.pop()
            result.append(cur_node)
            if cur_node.right: acc.append(cur_node.right)
            if cur_node.left: acc.append(cur_node.left)
            index += 1
        return result

# left root right
def in_order(root):
    acc = [root]
    cur_node = acc[-1]
    result = []
    # index = 0
    # while len(acc)>0 and index < 100:
    while len(acc)>0:
        # cur_node.p()
        # acc.p()
        if cur_node.left and cur_node.left.data not in result: 
            acc.append(cur_node.left)
            cur_node = acc[-1]
        else:
            cur_node = acc.pop()
            result.append(cur_node.data)
            if cur_node.right: 
                acc.append(cur_node.right)
            # cur_node = acc[-1]
            if len(acc) > 0:
                cur_node = acc[-1]
            else:
                cur_node = None
        # index += 1

    return result

def in_order_recursively(root):
    if root:
        in_order_recursively(root.left)
        print(root.data),
        in_order_recursively(root.right)

# left right root
def post_order(root):
    acc = [root]
    cur_node = acc[-1]
    result = []
    # index = 0
    while len(acc)>0:
        # cur_node.p()
        # acc.p()
        if cur_node.left and cur_node.left.data not in result: 
            acc.append(cur_node.left)
            cur_node = acc[-1]
        elif cur_node.right and cur_node.right.data not in result:
            acc.append(cur_node.right)
            cur_node = acc[-1]
        else:
            cur_node = acc.pop()
            result.append(cur_node.data)
            if len(acc) > 0:
                cur_node = acc[-1]
            else:
                cur_node = None
        # index += 1

    return result

# left right root
def post_order_recursively(root):
    if root:
        post_order_recursively(root.left)
        post_order_recursively(root.right)
        print(root.data),

# root left right
def pre_order_recursively(root):
    if root:
        print(root.data),
        pre_order_recursively(root.left)
        pre_order_recursively(root.right)

if __name__ == '__main__':
    from minitest import *

    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    root = node1
    root.right = node2
    node2.right = node5
    node5.left = node3
    node5.right = node6
    node3.right = node4
    with test(in_order):
        in_order(root).must_equal([1, 2, 3, 4, 5, 6])
        print("in_order_recursively:"),
        in_order_recursively(root)
        print("")
        post_order(root).must_equal([4, 3, 6, 5, 2, 1])
        print("post_order_recursively:"),
        post_order_recursively(root)
        print("")
        print("pre_order_recursively:"),
        pre_order_recursively(root)
        print("")
        [i.data for i in root.depth_first_list()].must_equal(
                [1, 2, 5, 3, 4, 6])


