# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def printTree_has_issue(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        def inner(root):
            if root == None or root.val == None:
                return [[""]]
            if root.left == None and root.right==None:
                return [[str(root.val)]]
            left_part = inner(root.left)
            right_part = inner(root.right)
            # print("left_part",left_part)
            # print("right_part",right_part)
            left_row_count = len(left_part)
            left_col_count = len(left_part[0])
            right_row_count = len(right_part)
            right_col_count = len(right_part[0])
            max_row_count = max(left_row_count, right_row_count)
            max_col_count = max(left_col_count, right_col_count)
            fc = max_col_count * 2 + 1
            fr = max_row_count + 1
            result = [[""]*fc for i in xrange(fr)]
            result[0][max_col_count] = str(root.val)
            # for left part
            start_j = 0
            if left_col_count < max_col_count:
                start_j += (max_col_count-left_col_count)/2
            for i in xrange(left_row_count):
                real_i = i + 1
                for j in xrange(left_col_count):
                    result[real_i][start_j+j] = left_part[i][j]
            # for right part
            start_j = max_col_count + 1
            if right_col_count < max_col_count:
                start_j += (max_col_count-right_col_count)/2
            for i in xrange(right_row_count):
                real_i = i + 1
                for j in xrange(right_col_count):
                    result[real_i][start_j+j] = right_part[i][j]
            return result
        
        return inner(root) 

    def printTree(self, root):
        if root == None or root.val == None:
            return [[""]]
        # if root.left == None and root.right==None:
        #     return [[str(root.val)]]
        mem = []
        acc = [(0,0,root)]
        while len(acc) > 0:
            cur_level, i_in_level, cur_node = acc.pop(0)
            # if len(mem) == cur_level:
            #     mem.append([])
            mem.append((cur_level, i_in_level, cur_node))
            if cur_node.left: acc.append((cur_level+1, i_in_level*2+0, cur_node.left))
            if cur_node.right: acc.append((cur_level+1, i_in_level*2+1, cur_node.right))
        level_count = mem[-1][0] + 1
        col_count = 2 ** level_count - 1
        result = [[""]*col_count for i in xrange(level_count)]
        for cur_level, i_in_level, cur_node in mem:
            cur_level_start_index = 2**(level_count - cur_level - 1)-1
            cur_level_index_interval = 2**(level_count - cur_level)
            j = cur_level_start_index + i_in_level * (cur_level_index_interval)
            result[cur_level][j] = cur_node.val
        return result




if __name__ == '__main__':
      from minitest import *
  
      with test():
          pass  