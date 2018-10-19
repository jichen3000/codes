# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        acc = [(0, root)]
        pq_parents = []
        parents = []
        while acc:
            times, cur = acc.pop()
            # print(times, cur.val)
            if times == 0:
                acc += (1, cur),
                parents += cur.val,
                if cur.right:
                    acc += (0, cur.right),
                if cur.left:
                    acc += (0, cur.left),
            else:
                if cur == p or cur == q:
                    pq_parents += parents[::],
                    if len(pq_parents) == 2:
                        break
                parents.pop()
        first, second = pq_parents[0], pq_parents[1]
        # print(pq_parents)
        for i in range(max(len(first), len(second))):
            if i == min(len(first), len(second)) or first[i] != second[i]:
                break
        return first[i-1]

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        acc = [(0, root)]
        encount = 0
        parents = []
        while acc:
            times, cur = acc.pop()
            # print(times, cur.val)
            if times == 0:
                acc += (1, cur),
                parents += (encount, cur.val),
                if cur.right:
                    acc += (0, cur.right),
                if cur.left:
                    acc += (0, cur.left),
            else:
                if cur == p or cur == q:
                    if encount == 0:
                        encount += 1
                    else:
                        break
                parents.pop()
        for times, val in reversed(parents):
            if times == 0:
                return val
                