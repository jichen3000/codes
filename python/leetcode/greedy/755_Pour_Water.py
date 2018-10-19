class Solution(object):
    def pourWater(self, s, v, k):
        """
        :type heights: List[int]
        :type V: int
        :type K: int
        :rtype: List[int]
        """
        if not s: return
        n = len(s)
        def inner(v):
            if v <= 0: return
            min_i = k
            found = False
            for i in range(k-1, -1, -1):
                if s[min_i] > s[i]:
                    min_i = i
                    found = True
                if s[i] > s[min_i]:
                    break
            if not found:
                for i in range(k+1, n):
                    if s[min_i] > s[i]:
                        min_i = i
                    if s[i] > s[min_i]:
                        break
            s[min_i] += 1
            return inner(v-1)
        inner(v)
        return s

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().pourWater([1,2,3,4,3,2,1,2,3,4,3,2,1],
                2,5).must_equal([1,2,3,4,3,3,2,2,3,4,3,2,1])
        Solution().pourWater([1,2,3,4,3,2,1,2,3,4,3,2,1],
                10,2).must_equal([4,4,4,4,3,3,3,3,3,4,3,2,1])
