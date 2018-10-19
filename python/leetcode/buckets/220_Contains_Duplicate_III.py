class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        n = len(nums)
        if n == 0: return False
        for i in range(n-1):
            for j in range(i+1, min(n,i+k+1)):
                if abs(nums[j]-nums[i]) <= t:
                    return True
        return False
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        from bisect import bisect
        n = len(nums)
        if n == 0: return False
        sorted_tuples = []
        for i, v in enumerate(nums):
            sorted_tuples += (v, i),
        sorted_tuples.sort()
        sorted_tuples.p()
        for i in range(n):
            v, index = sorted_tuples[i]
            max_i = bisect(sorted_tuples, (v+t+1,))
            (i, v, index, max_i).p()
            for j in range(i+1, min(n,max_i)):
                (j, sorted_tuples[j][1], index, sorted_tuples[j][1] - index <= k).p()
                if abs(sorted_tuples[j][1] - index) <= k:
                    return True
        return False 
    # naive bucket sort  
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        from collections import defaultdict
        if t < 0: return False
        buckets = defaultdict(list)
        width = t + 1
        for i, v in enumerate(nums):
            bi = v / width
            buckets[bi] += (v, i),
        # buckets.p(0)
        for key in buckets.keys():
            for v, i in buckets[key]:
                for nv, ni in buckets.get(key-1,[]) + buckets[key] + buckets.get(key+1,[]):
                    # (v, i, nv, ni, t, k, abs(nv-v), abs(ni-i), (abs(nv-v) <= t and abs(ni-i) <= k)).p()
                    if abs(nv-v) <= t and abs(ni-i) <= k and ni != i:
                        return True
        return False
    # move buckets
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0: return False
        n = len(nums)
        buckets = {}
        w = t + 1
        for i in xrange(n):
            key = nums[i] / w
            if key in buckets:
                return True
            if key - 1 in buckets and abs(nums[i] - buckets[key - 1]) < w:
                return True
            if key + 1 in buckets and abs(nums[i] - buckets[key + 1]) < w:
                return True
            buckets[key] = nums[i]
            # the important part of this method
            # remove the previous index which small than k
            # so clever
            if i >= k: 
                del buckets[nums[i - k] / w]
        return False



if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().containsNearbyAlmostDuplicate([0,10,22,15,0,5,22,12,1,5], 3, 3).must_equal(False)
        Solution().containsNearbyAlmostDuplicate([-1,-1], 1, 0).must_equal(True)

