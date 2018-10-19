# https://www.geeksforgeeks.org/segment-tree-set-1-sum-of-given-range/
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class NumArray:
    def __init__(self, arr):
        self.arr = arr
        self.tree = self._create_tree()
    def _cal_mid(self, l, r):
        return (l+r) // 2 + 1
    def _create_tree(self):
        if not self.arr: return
        def dfs(l, r):
            if l == r:
                return Node(self.arr[l])
            m = self._cal_mid(l, r)
            cur =  Node(0)
            cur.left = dfs(l, m-1)
            cur.right = dfs(m, r)
            cur.val = cur.left.val + cur.right.val
            return cur
        return dfs(0, len(self.arr)-1)

    def sumRange(self, i, j):
        def dfs(node, l, r):
            # if not node: return 0
            if i <=l and r <= j:
                return node.val
            if r < i or l > j:
                return 0
            m = self._cal_mid(l, r)
            return  dfs(node.left, l, m - 1) + \
                    dfs(node.right, m, r)
        return dfs(self.tree, 0, len(self.arr)-1)

    def update(self, i, val):
        diff = val - self.arr[i]
        def dfs(node, l, r):
            if l <= i <= r:
                node.val += diff
                if l == r: return
                m = self._cal_mid(l, r)
                dfs(node.left, l, m - 1)
                dfs(node.right, m, r)
        dfs(self.tree, 0, len(self.arr)-1)
        self.arr[i] = val



if __name__ == '__main__':
    from minitest import *

    with test(""):
        arr = [1,3,5,7,9,11]
        na = NumArray(arr)
        na.sumRange(2, 5).must_equal(32)
        na.sumRange(0, 5).must_equal(36)
        na.sumRange(1, 4).must_equal(24)

        na.update(2, 6)
        na.sumRange(2, 5).must_equal(33)
        na.sumRange(0, 5).must_equal(37)
        na.sumRange(1, 4).must_equal(25)        
        na.sumRange(1, 1).must_equal(3)        