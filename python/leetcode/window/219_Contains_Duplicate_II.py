class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        from collections import defaultdict
        if k == 0 or not nums:
            return False
        mem = defaultdict(lambda : 0)
        q = []
        for i in range(len(nums)):
            if nums[i] in mem:
                return True
            if len(q) == k:
                j = q.pop(0)
                mem[nums[j]] -= 1
                if mem[nums[j]] == 0:
                    del mem[nums[j]]
            q += i,
            mem[nums[i]] += 1
        return False
            
                

        
        
if __name__ == '__main__':
    from minitest import *

    with test("Solution"):
        Solution().containsNearbyDuplicate([1,2,1],1).must_equal(False)
