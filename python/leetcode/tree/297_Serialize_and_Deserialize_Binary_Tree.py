# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        q = [root]
        res = []
        while q:
            cur = q.pop(0)
            if cur!=None:
                res += str(cur.val),
                q += cur.left,
                q += cur.right,
            else:
                res += "n",
        while res and res[-1] == "n":
            res.pop()
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if data == "": return None
        values = data.split(",")
        if not values: return None
        root = TreeNode(int(values.pop(0)))
        is_left = True
        parents = [root]
        for v in values:
            cur = None
            if v != "n":
                cur = TreeNode(int(v))
                parents += cur,
            if is_left:
                parents[0].left = cur
                is_left = False
            else:
                parents[0].right = cur
                is_left = True
                parents.pop(0)
        return root
                
            
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))