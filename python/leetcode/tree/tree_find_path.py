# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    def __repr__(self):
        return str(self.val)

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        WHITE = 1
        BLACK = 2
        acc = [(root, WHITE)]
        cur_path = []
        two_paths = []
        while len(acc) > 0:
            cur_node, color = acc.pop()
            # print("cur_node,color",cur_node.val,color)
            # cur_node.p()
            if color == WHITE:
                if cur_node.left == None and cur_node.right == None:
                    if cur_node == p or cur_node == q:
                        two_paths.append(cur_path + [cur_node])
                        if len(two_paths) == 2:
                            break
                else:
                    acc.append((cur_node, BLACK))
                    if cur_node.right != None: acc.append((cur_node.right,WHITE))
                    if cur_node.left != None: acc.append((cur_node.left,WHITE))
                    cur_path.append(cur_node)
            else:
                cur_path.pop()
                if cur_node == p or cur_node == q:
                    two_paths.append(cur_path + [cur_node])
                    if len(two_paths) == 2:
                        break
        # two_paths.p()
        # print("two_paths",two_paths)
        the_index = min(len(two_paths[0]),len(two_paths[1])) - 1
        for i in xrange(the_index+1):
            if two_paths[0][i].val != two_paths[1][i].val:
                the_index = i-1
                break
        return two_paths[0][the_index]

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        node0 = TreeNode(0)
        node1 = TreeNode(1)
        node2 = TreeNode(2)
        node3 = TreeNode(3)
        node4 = TreeNode(4)
        node5 = TreeNode(5)
        node6 = TreeNode(6)
        node7 = TreeNode(7)
        node8 = TreeNode(8)
        node9 = TreeNode(9)
        node10 = TreeNode(10)

        root = node3
        node3.left = node5
        node3.right = node1
        node5.left = node6
        node5.right = node2
        node6.left = node9
        node6.right = node10
        node2.left = node7
        node2.right = node4
        node1.left = node0
        node1.right = node8

        # Solution().lowestCommonAncestor(root, node4, node8).must_equal(
        #         node3)

        node0 = TreeNode(0)
        node1 = TreeNode(1)
        node0.left = node1
        root = node0
        Solution().lowestCommonAncestor(root, node0, node1).must_equal(
                node0)

