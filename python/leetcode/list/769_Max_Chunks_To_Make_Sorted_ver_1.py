class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        if n == 1: return 1
        n_list = range(n)
        result = 1
        cur = None
        for i in range(n):
            n_list.remove(arr[i])
            if cur == None:
                cur = arr[i]
                if arr[i] == 0:
                    result += 1
            else:
                if arr[i] > cur:
                    cur = arr[i]
                if n_list and n_list[0] > cur:
                    result += 1
        return result

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().maxChunksToSorted([4,3,2,1,0]).must_equal(1)
        Solution().maxChunksToSorted([1,0,2,3,4]).must_equal(4)
        Solution().maxChunksToSorted([2,0,1]).must_equal(1)
        Solution().maxChunksToSorted([0,1]).must_equal(2)
        Solution().maxChunksToSorted([0]).must_equal(1)
