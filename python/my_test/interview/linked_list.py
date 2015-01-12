class LinkedNode(object):
    """docstring for LinkedNode"""
    def __init__(self, the_value):
        super(LinkedNode, self).__init__()
        self.the_value = the_value
        self.next_node = None

    def append(self, the_value):
        the_node = LinkedNode(the_value):
        # find the last one
        cur_node = self
        while cur_node:
            cur_node = cur_node.next
        cur_node.next_node = the_node
        return the_node

        