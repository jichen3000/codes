# Definition for a  binary tree node
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def in_order(root):
    if root == None:
        return []
    acc = [root]
    results = []
    while acc:
        cur = acc.pop()
        if type(cur) == TreeNode:
            if cur.right: acc += cur.right,
            if cur.left == None and cur.right == None:
                results += cur.val,
            else:
                acc += cur.val,
            if cur.left: acc += cur.left,
        else:
            results += cur,
    return results
# class BSTIterator(object):
#     def __init__(self, root):
#         """
#         :type root: TreeNode
#         """
#         self.root = root
#         self.post_order_list = in_order(root)
#         print(self.post_order_list)

#     def hasNext(self):
#         """
#         :rtype: bool
#         """
#         return self.post_order_list
        

#     def next(self):
#         """
#         :rtype: int
#         """
#         return self.post_order_list.pop(0)
class BSTIterator:
    # @param root, a binary search tree's root node
    def __init__(self, root):
        self.stack = list()
        self.pushAll(root)

    # @return a boolean, whether we have a next smallest number
    def hasNext(self):
        return self.stack

    # @return an integer, the next smallest number
    def next(self):
        tmpNode = self.stack.pop()
        self.pushAll(tmpNode.right)
        return tmpNode.val
        
    def pushAll(self, node):
        while node is not None:
            self.stack.append(node)
            node = node.left   
            
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        if root:
            self.acc = [(root, 0)]
            self.cur = self.find_next()
        else:
            self.cur = None
    def find_next(self):
        while self.acc:
            cur, i = self.acc.pop()
            if i == 0:
                if cur.right:
                    self.acc += (cur.right, 0),
                if cur.left:
                    self.acc += (cur, 1),
                    self.acc += (cur.left, 0),
                else:
                    return cur
            else:
                return cur


    def hasNext(self):
        """
        :rtype: bool
        """
        return self.cur != None
        

    def next(self):
        """
        :rtype: int
        """
        pre = self.cur
        if pre:
            self.cur = self.find_next()
            return pre.val
class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.acc = []
        self.push_all_lefts(root)
        
    def push_all_lefts(self, node):
        while node:
            self.acc += node,
            node = node.left

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.acc) > 0
        

    def next(self):
        """
        :rtype: int
        """
        pre = self.acc.pop()
        self.push_all_lefts(pre.right)
        return pre.val        

# Your BSTIterator will be called like this:
# i, v = BSTIterator(root), []
# while i.hasNext(): v.append(i.next())