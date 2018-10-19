class Solution:
    def kEmptySlots(self, s, k):
        """
        :type s: List[int]
        :type k: int
        :rtype: int
        """
        if not s: return -1
        n = len(s)
        ss = [1] * n
        for i, v in enumerate(s):
            j = v - 1
            ss[j] = 0
            if j+k+1 < n and ss[j+k+1] == 0:
                res = all(ss[m]>0 for m in range(j+1, j+k+1))
                if res: return i + 1
            if j - k - 1 >= 0 and ss[j-k-1] == 0:
                res = all(ss[m]>0 for m in range(j-k, j))
                if res: return i + 1
            # (i, v, j, ss).p()
        return -1
    
    # wonderful idea
    # The idea is to use an array days[] to record each position's flower's blooming day. 
    # That means days[i] is the blooming day of the flower in position i+1. 
    # We just need to find a subarray days[left, left+1,..., left+k, right] which satisfies: 
    # for any i = left+1,..., left+k-1, we can have days[left] < days[i] && days[right] < days[i]. 
    # Then, the result is max(days[left], days[right]).
    # think reversely
    def kEmptySlots(self, s, k):
        """
        :type s: List[int]
        :type k: int
        :rtype: int
        """
        if not s: return -1
        n = len(s)
        days = [0] * n
        for i in range(n):
            days[s[i]-1] = i + 1
        left, right, res = 0, k + 1, n + 1
        if right >= n: return -1
        # to find subset
        for i in range(n):
            # print(i)
            if days[i] > max(days[left], days[right]):
                continue
            if i == right:
                res = min(res, max(days[left], days[right]))
            left = i
            right = i + k + 1
            if right >= n: break
        res = -1 if res == n+1 else res
        return res
            
class Solution:
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        if not flowers: 
            return -1
        n = len(flowers)
        days = [0] * n
        for i,v in enumerate(flowers):
            days[v-1] = i + 1
        # days.p()
        left, right, i = 0, k + 1, 1
        res = n + 1
        while right < n:
            if i < right and days[i] > days[left] and days[i] > days[right]:
                i += 1
                continue
            # (left, right, i, days[left], days[right]).p()
            if i == right:
                res = min(res, max(days[left], days[right]))
            left, right = i, i + k + 1
            i += 1
        return res if res < n + 1 else -1
            


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().kEmptySlots([1,3,2],1).must_equal(2)
        # Solution().kEmptySlots([1,2,3],1).must_equal(-1)
        # Solution().kEmptySlots([6,5,8,9,7,1,10,2,3,4],2).must_equal(8)
        # Solution().kEmptySlots([3,9,2,8,1,6,10,5,4,7], 1).must_equal(6)
        Solution().kEmptySlots([10,1,6,4,2,8,9,7,5,3], 1).must_equal(4)

