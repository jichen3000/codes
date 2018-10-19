class Solution:
    def minSwap(self, a, b):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        # a = [-float("inf")] + a + [float("inf")]
        # b = [-float("inf")] + b + [float("inf")]
        res = 0
        n = len(a)
        for i in range(n-1):
            if a[i] >= a[i+1] or b[i] >= b[i+1]:
                if (b[i-1] if i >= 1 else -float("inf"))  < a[i] < (b[i+1] if i+1 < n else float("inf")) and \
                        (a[i-1] if i >= 1 else -float("inf")) < b[i] < (a[i+1] if i+1 < n else float("inf")):
                    a[i], b[i] = b[i], a[i]
                    v1 = self.minSwap(a[i:], b[i:]) + 1
                    a[i], b[i] = b[i], a[i]
                    if i+1 < n:
                        a[i+1], b[i+1] = b[i+1], a[i+1]
                        v2 = self.minSwap(a[i+1:], b[i+1:]) + 1
                        a[i+1], b[i+1] = b[i+1], a[i+1]
                    else:
                        v2 = n
                    return min(v1, v2)
                res += 1
        return res
        
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(A)
        pre = [0, 1]
        for i in range(1, n):
            cur = [n,n]
            if A[i]>A[i-1] and B[i]>B[i-1]:
                cur[0] = min(cur[0], pre[0])
                cur[1] = min(cur[1], pre[1]+1)
            if A[i]>B[i-1] and B[i]>A[i-1]:
                cur[0] = min(cur[0], pre[1])
                cur[1] = min(cur[1], pre[0]+1)
            pre = cur
        return min(pre) 

    def minSwap(self, a, b):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        n = len(a)
        pre_change, pre_no = 1, 0
        for i in range(1,n):
            change, no = n, n
            if a[i] > a[i-1] and b[i] > b[i-1]:
                no = min(no, pre_no)
                change = min(change, pre_change+1)
            if a[i] > b[i-1] and b[i] > a[i-1]:
                no = min(no, pre_change)
                change = min(change, pre_no+1)
            pre_change, pre_no = change, no
        return min(pre_change, pre_no) 
                      
if __name__ == '__main__':
    from minitest import *

    with test("Solution"):
        Solution().minSwap([1,3,5,4],[1,2,3,7]).must_equal(1)
        Solution().minSwap([3,3,8,9,10],[1,7,4,6,8]).must_equal(1)
        Solution().minSwap([0,7,8,10,10,11,12,13,19,18],[4,4,5,7,11,14,15,16,17,20]).must_equal(4)
        
