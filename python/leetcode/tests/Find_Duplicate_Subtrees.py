# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def get_preorder_list(self,root):
        acc = [root]
        result = []
        while len(acc) > 0:
            cur_node = acc.pop()
            result.append(cur_node)
            if cur_node.right: acc.append(cur_node.right)
            if cur_node.left: acc.append(cur_node.left)
        return result
    def get_inorder_val_str(self,root):
        acc = []
        if root: acc.append(root) 
        cur_node = None
        result = []
        while len(acc)>0:
            cur_node = acc.pop()
            if type(cur_node) == TreeNode:
                if cur_node.right!=None: 
                    acc.append(cur_node.right)
                else:
                    acc.append(str(cur_node.val)+"r")
                if cur_node.left == None and cur_node.right == None:
                    result.append(str(cur_node.val))
                else:
                    acc.append(cur_node.val)
                if cur_node.left!=None: 
                    acc.append(cur_node.left)
                else:
                    acc.append(str(cur_node.val)+"l")

            else:
                result.append(str(cur_node))
        return "".join(result)


            
    def findDuplicateSubtrees_time(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        if root == None:
            return []
        preorder_list = self.get_preorder_list(root)
        memory_hash = {}
        result = []
        added_hash  = {}
        # print("preorder_list",[i.val for i in preorder_list])
        for i in xrange(len(preorder_list)):
            for j in xrange(i+1, len(preorder_list)):
                if preorder_list[i].val == preorder_list[j].val:
                    if i not in memory_hash:
                        memory_hash[i] = self.get_inorder_val_str(preorder_list[i])
                    if j not in memory_hash:
                        memory_hash[j] = self.get_inorder_val_str(preorder_list[j])
                    if  added_hash.get(memory_hash[i], False)==False and memory_hash[i] == memory_hash[j]:
                        result.append(preorder_list[i])
                        
                        added_hash[memory_hash[i]] =True
        # print("res", )
        return result
        
        

