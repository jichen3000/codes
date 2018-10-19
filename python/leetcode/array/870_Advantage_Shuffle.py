class Solution():
    def advantageCount(self, a, b):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        bb = [(v, i) for i, v in enumerate(b)]
        res = [0] * len(b)
        bb.sort()
        a.sort()
        while bb:
            if a[0] > bb[0][0]:
                v,i = bb.pop(0)
                res[i] = a.pop(0)
            else:
                v,i = bb.pop()
                res[i] = a.pop(0)
        return res
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().advantageCount([2,7,11,15], [1,10,4,11]).must_equal([2,11,7,15])
        Solution().advantageCount([12,24,8,32],[13,25,32,11]).must_equal([24,32,8,12])
        Solution().advantageCount([2,0,4,1,2], [1,3,0,0,2]).must_equal([2, 0, 1, 2, 4])


