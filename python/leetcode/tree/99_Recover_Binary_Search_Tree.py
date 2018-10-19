# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution(object):
    # the first the one larger than next one
    # the second is the second one smaller than before one if not, choose the first's next one
    # pass the self to left child, give the parent to right one, but how about root?
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        first_error = None
        acc = [(root, False)]
        inorders = []
        while acc:
            cur, second_visited = acc.pop()
            if (cur.left == None and cur.right == None) or second_visited:
                inorders += cur,
                continue
            if cur.right:
                acc.append((cur.right,False))
            acc.append((cur,True))
            if cur.left:
                acc.append((cur.left,False))
        n = len(inorders)

        for i in range(n-1):
            if inorders[i].val > inorders[i+1].val:
                break
        for j in range(i+2, n):
            if inorders[j].val < inorders[j-1].val:
                inorders[j].val, inorders[i].val = inorders[i].val, inorders[j].val
                break
        else:
            inorders[i+1].val, inorders[i].val = inorders[i].val, inorders[i+1].val

    # the first error node is the first one smaller than the before, the before one.
    # the second error node is the second smaller than the before, 
    #     if is not, is the next node of first error node.
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        errors = [None, None]
        pre = [None]
        found = [False]
        def inorder(cur):
            if found[0]: return
            if cur.left: inorder(cur.left)
            if pre[0] and cur.val < pre[0].val:
                if errors[0] == None:
                    errors[0] = pre[0]
                    errors[1] = cur
                else:
                    errors[1] = cur
                    found[0] = True
                    return
            pre[0] = cur
            if cur.right: inorder(cur.right)
        inorder(root)
        errors[0].val, errors[1].val = errors[1].val, errors[0].val





                
                
        
                
                
        
# 3 2 1
# 1 3 2
# 1 2 3 6 5 4 7
if __name__ == '__main__':
    from minitest import *

    with test():
        pass                

