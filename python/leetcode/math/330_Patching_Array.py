import bisect
class Solution(object):
    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        patch_count = 0
        if len(nums) > 0:
            i = bisect.bisect_left(nums, n+1)
            nums = nums[:i]
        if n > 100:
            cur = n / 2
            while cur >= nums[-1]:
                patch_count += 1
                cur /= 2
            n = cur  + 1
        # n.p()
        sums = []
        for mask in range(1, 1 << len(nums)):
            cur = 0
            for i in range(len(nums)):
                if mask >> i & 1:
                    cur += nums[i]
            sums += cur,
        ps = [False] * (n+1)
        ps[0] = True
        for v in sums:
            if v < n+1:
                ps[v] = True
        index = 1
        while index < n + 1:
            while ps[index]:
                index += 1
                if index == n+1:
                    return patch_count
            patch_count += 1
            for i in range(n, index, -1):
                if ps[i-index]:
                    ps[i] = True
            ps[index] = True
            # index.p()
            index += 1
        return patch_count


    def minPatches(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: int
        """
        nn = len(nums)
        count = 0
        cur_sum, index, cur_v = 0, 0, 1
        while cur_v <= n:
            if index < nn and cur_v >= nums[index]:
                while index < nn and cur_v >= nums[index]:
                    cur_sum += nums[index]
                    cur_v = cur_sum+1
                    index += 1
            else:
                count += 1
                # cur_v.p()
                cur_sum += cur_v
                cur_v = cur_sum+1
        return count 



if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().minPatches([1, 3],6).must_equal(1)
        Solution().minPatches([],7).must_equal(3)
        Solution().minPatches([],8).must_equal(4)
        Solution().minPatches([1, 5, 10],20).must_equal(2)
        Solution().minPatches([1, 2, 2],5).must_equal(0)
        Solution().minPatches([1, 2,3,5],40).must_equal(2)
        Solution().minPatches([1,2,31,33],100).must_equal(4)
        Solution().minPatches([10,30,36,42,50,76,87,88,91,92],54).must_equal(5)

        Solution().minPatches([1,2,31,33], 2147483647).must_equal(28)
        Solution().minPatches([1,2,3], 2147483647).must_equal(29)
        Solution().minPatches([1,3], 2147483647).must_equal(30)
