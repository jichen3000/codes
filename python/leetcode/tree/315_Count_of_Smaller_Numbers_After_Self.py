class Node(object):
    def __init__(self, v):
        self.v = v
        self.left = None
        self.right = None
        self.small_count = 0
        self.left_count = 0
        self.dup_count = 1
    def add(self, child):
        # (self.v, self.small_count, self.dup_count).p()
        # (child.v, child.small_count, child.dup_count).p()
        # child.small_count = self.small_count
        if child.v > self.v:
            child.small_count += self.dup_count + self.left_count
            if self.right:
                self.right.add(child)
            else:
                self.right = child
        elif child.v < self.v:
            self.left_count += 1
            if self.left:
                self.left.add(child)
            else:
                self.left = child
        else:
            child.small_count += self.left_count
            self.dup_count += 1

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        counts = []
        for i in range(n):
            count = 0
            for j in range(i+1, n):
                if nums[j] < nums[i]:
                    count += 1
            counts += count,
        return counts
    
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n == 0: return []
        if n == 1: return [0]
        root = Node(nums[n-1])
        counts = [0] * n
        for i in range(n-2, -1, -1):
            cur = Node(nums[i])
            root.add(cur)
            counts[i] = cur.small_count
        return counts

class Solution(object):
    ## merge sort
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) == 0: return []
        res = [0] * len(nums)
        num_pos_arr = [(v,i) for i,v in enumerate(nums)]
        def merge_sort(left, right):
            # (left, right).p()
            new = []
            i, j = 0, 0
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    res[left[i][1]] += j
                    # res[left[i][1]].p()
                    new += left[i],
                    i += 1
                else:
                    new += right[j],
                    j += 1
            if i == len(left):
                new += right[j:]
            else:
                for k in range(i, len(left)):
                    res[left[k][1]] += j
                new += left[i:]
            return new
        def inner(l):
            n = len(l)
            if n == 1: 
                return l
            elif n == 2:
                if l[0][0] > l[1][0]:
                    res[l[0][1]] += 1
                    # res[l[0][1]].p()
                    l[0],l[1] = l[1],l[0]
                return l
            left_l = inner(l[:n/2])
            right_l = inner(l[n/2:])
            return merge_sort(left_l, right_l)
        inner(num_pos_arr)
        return res


if __name__ == '__main__':
    from minitest import *

    with test(Solution):

        # Solution().countSmaller([30,100,51,51,21,100,41]).must_equal([1,4,2,2,0,1,0])
        # Solution().countSmaller([2,0,1]).must_equal([2,0,0])
        # Solution().countSmaller([99,8,21,65,100,41]).must_equal([4,0,0,1,1,0])
        # Solution().countSmaller([5,2,6,1]).must_equal([2,1,1,0])
        # Solution().countSmaller([5,2,2,6,1]).must_equal([3,1,1,1,0])
        # nums = [83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]
        # results = [17,9,19,12,14,6,12,5,12,3,0,10,0,7,8,4,0,0,4,3,2,0,1,0]
        # Solution().countSmaller(nums).must_equal(results)
        nums = [26,78,27,100,33,67,90,23,66,5,38,7,35,23,52,22,83,51,98,69,81,32,78,28,94,13,2,97,3,76,99,51,9,21,84,66,65,36,100,41]
        results = [10,27,10,35,12,22,28,8,19,2,12,2,9,6,12,5,17,9,19,12,14,6,12,5,12,3,0,10,0,7,8,4,0,0,4,3,2,0,1,0]
        Solution().countSmaller(nums).must_equal(results)
