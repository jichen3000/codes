class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        max_count = 1
        count = 1
        nums = sorted(set(nums))
        # nums.sort()
        for i in range(1, len(nums)):
            if nums[i] ==  nums[i-1]+1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 1
        return max_count


    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        max_count = 1
        nums = set(nums)
        mem = {}
        for v in nums:
            in1 = (v, 1) in mem
            in2 = (v, -1) in mem
            if in1 and in2:
                pre = mem[(v, -1)]
                nex = mem[(v, 1)]
                pre[0] += 1 + nex[0]
                mem[(v-1, -1)] = pre
                mem[(v+1, 1)] = pre
                max_count = max(max_count, pre[0])
            elif in1:
                nex = mem[(v, 1)]
                nex[0] += 1
                del mem[(v, 1)]
                mem[(v+1, 1)] = nex
                max_count = max(max_count, nex[0])
            elif in2:
                pre = mem[(v, -1)]
                pre[0] += 1
                del mem[(v, -1)]
                mem[(v-1, -1)] = pre
                max_count = max(max_count, pre[0])
            else:
                cur = [1]
                mem[(v+1,  1)] = cur
                mem[(v-1, -1)] = cur
        return max_count

    # came form answer
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0: return 0
        max_count = 1
        mem = {}
        for v in nums:        
            if v not in mem:
                left = mem[v-1] if v-1 in mem else 0
                right = mem[v+1] if v+1 in mem else 0

                sum_v = left + 1 + right
                mem[v] = sum_v

                # the key, only maintain the boundry
                mem[v-left] = sum_v
                mem[v+right] = sum_v

                max_count = max(max_count, sum_v)
        return max_count


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().longestConsecutive([100, 4, 200, 1, 3, 2]).must_equal(4)
