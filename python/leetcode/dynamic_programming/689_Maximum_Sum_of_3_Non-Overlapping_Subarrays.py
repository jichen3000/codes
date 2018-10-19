import sys
class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        ln = n - 3 * k
        groups = [[] for _ in range(4)]
        indeces = []
        min_left_sum = [sys.maxint]
        max_indeces = [[]]
        def get_nexts(groups, indeces, index):
            result = []
            if len(indeces) == 0:
                result.append(0)
                if len(groups[3]) < ln:
                    result.append(3)
            else:
                gi = len(indeces) - 1
                if len(groups[gi]) < k:
                    result.append(gi)
                else:
                    result.append(gi+1)
                    if gi+1 != 3 and len(groups[3]) < ln:
                        result.append(3)
            return result                
        def dfs(groups, indeces, index):
            # index.p()
            if index == n:
                # groups.pp()
                # indeces.p()
                sum_v = sum(groups[3])
                # (min_left_sum[0], sum_v).p()
                if min_left_sum[0] > sum_v:
                    min_left_sum[0] = sum_v
                    max_indeces[0] = indeces[:]
                return
            next_group_indeces = get_nexts(groups, indeces, index)
            # (index,next_group_indeces).p()
            if len(next_group_indeces) == 0:
                return
            # next_group_indeces.p()
            for i in next_group_indeces:
                if i < 3 and len(groups[i]) == 0:
                    indeces.append(index)
                groups[i].append(nums[index])
                dfs(groups, indeces, index+1)
                groups[i].pop()
                if i < 3 and len(groups[i]) == 0:
                    indeces.pop()
        dfs(groups, indeces, 0)
        return max_indeces[0]

    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        m = n - 3 * k + 1
        sums = [0] * (n+1)
        for i in range(n): 
            sums[i+1] = sums[i] + nums[i]

        left = [0] * m
        right = [0] * m
        result = None
        total = 0
        for i in range(m):
            cur_sum = sums[k+i] - sums[i]
            if cur_sum > total:
                left[i] = i
                total = cur_sum
            else:
                left[i] = left[i-1]

        total = 0
        for i in range(m):
            cur_sum = sums[n-i] - sums[n-i-k]
            if cur_sum > total:
                right[i] = n-i-k
                total = cur_sum
            else:
                right[i] = right[i-1]
        # left.p()
        # right.p()

        total = 0
        for i in range(m):
            middle_i, left_i, right_i = k+i, left[i], right[m-1-i]
            cur_sum = sums[k+middle_i] - sums[middle_i] +\
                    sums[k+left_i] - sums[left_i] +\
                    sums[k+right_i] - sums[right_i]
            # (left_i, middle_i, right_i, cur_sum).p()
            if cur_sum > total:
                result = [left_i, middle_i, right_i]
                total = cur_sum
        return result





if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().maxSumOfThreeSubarrays([1,2,1,2,6,7,5,1], 2).must_equal(
                [0,3,5])
        # nums,k = [7,13,20,19,19,2,10,1,1,19],3
        # Solution().maxSumOfThreeSubarrays(nums,k).must_equal(
        #         [1,4,7])


