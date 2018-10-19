from collections import defaultdict
from itertools import permutations
class Solution(object):
    # tle 13mins
    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # if k == 0 or k == n * (n-1) /2:
        #     return 1
        counts = defaultdict(lambda: 0)
        for l in permutations(range(n)):
            count = 0
            for i in range(n-1):
                for j in range(i+1, n):
                    if l[i] > l[j]:
                        count += 1
            counts[count] += 1
        counts.p()
        return counts[k]


    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1:
            if k == 0: return 1
            return 0
        mid = n * (n-1) /2
        if k > mid: return 0
        if k == 0 or k == mid:
            return 1
        if k > (mid+1) / 2:
            k = mid - k
        if k == 1:
            return n - 1
        mem = [1,1]
        for i in range(3, n+1):
            new_mem = [0] * (i * (i-1) / 2 + 1)
            # len(new_mem).p()
            for j in range(min(k+1, len(mem))):
                v = mem[j]
                for ni in range(j,min(k+1,i+j)):
                    new_mem[ni] += v
            mem = new_mem
        # (n,k,mem[k],mem).p()
        return mem[k]

    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0: return 0
        if n == 1:
            if k == 0: return 1
            return 0
        total = n * (n-1) /2
        if k > total: return 0
        if k == 0 or k == total:
            return 1
        # (k, (total+1) / 2).p()
        if k >= (total+1) / 2:
            k = total - k
        # k.p()
        if k == 1:
            return n - 1
        mem = [0] * (k+1)
        mem[0],mem[1] = 1, 1
        modulo = 10 ** 9 + 7
        for i in range(3, n+1):
            pre = mem[:]
            total = i * (i-1) / 2
            mid = (total + 1) / 2
            for j in range(1, min(k+1, mid+1)):
                # if j>=n: pre[j-n].p()
                mem[j] = (mem[j-1] + pre[j] - (pre[j-i] if j>=i else 0)) % modulo
                # (j,n, (pre[j-n] if j>=n else 0)).p()
            for j in range(mid+1, k+1):
                # (i,j,total-j).p()
                mem[j] = mem[total-j]
            # (i, mem).p()
        return mem[-1]





if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().kInversePairs(2,2).must_equal(0)
        Solution().kInversePairs(4,3).must_equal(6)
        Solution().kInversePairs(5,5).must_equal(22)
        Solution().kInversePairs(5,8).must_equal(9)
        Solution().kInversePairs(6,7).must_equal(101)
        Solution().kInversePairs(7,11).must_equal(573)
        Solution().kInversePairs(1000,1000).must_equal(663677020)

        # 4:{0: 1, 1: 3, 2: 5, 3: 6, 4: 5, 5: 3, 6: 1}
        # 5:{0: 1, 1: 4, 2: 9, 3: 15, 4: 20, 5: 22, 6: 20, 7: 15, 8: 9, 9: 4, 10: 1}
        # 6:{0: 1, 1: 5, 2: 14, 3: 29, 4: 49, 5: 71, 6: 90, 7: 101, 8: 101, 9: 90, 10: 71, 11: 49, 12: 29, 13: 14, 14: 5, 15: 1}
        # 7:{0: 1, 1: 6, 2: 20, 3: 49, 4: 98, 5: 169, 6: 259, 7: 359, 8: 455, 9: 531, 10: 573, 11: 573, 12: 531, 13: 455, 14: 359, 15: 259, 16: 169, 17: 98, 18: 49, 19: 20, 20: 6, 21: 1}