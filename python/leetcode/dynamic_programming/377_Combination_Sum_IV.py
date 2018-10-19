from itertools import permutations
from collections import Counter
from math import factorial

class Solution(object):
    def combinationSum4_time(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        dp = [[] for i in xrange(target+1)]
        count = 0
        for i in range(n):
            for j in range(target, 0, -1):
                v = nums[i]
                if j > v:
                    k = 1
                    while k * v < j:
                        dp[j] += [ l+[v]*k for l in dp[j-v*k] ]
                        k += 1
                if j % v == 0:
                    dp[j] += [v] * (j/v),
        print dp[target]
        def cal_permutation_count(l):
            n = len(l)
            if n == 1:
                return 1
            counter = Counter(l)
            num = factorial(n)
            for k,v in counter.items():
                if v > 1:
                    num = num / factorial(v)
            return num
            
        # print [len(set(permutations(l))) for l in dp[target]]
        return sum(cal_permutation_count(l) for l in dp[target])
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def cal_new_t(count, number, k):
            new_number = number + k
            new_count = count
            for i in xrange(new_number, number, -1):
                new_count *= i
            new_count /= factorial(k)
            # if count == 1:
            #     new_count /= factorial(number)
            return (new_count, new_number)
        n = len(nums)
        dp = [[] for i in xrange(target+1)]
        count = 0
        for i in range(n):
            for j in range(target, 0, -1):
                v = nums[i]
                if j > v:
                    k = 1
                    while k * v < j:
                        # dp[j] += [ l+[v]*k for l in dp[j-v*k] ]
                        dp[j]+=[cal_new_t(count, number,k) for count, number in dp[j-v*k]]
                        k += 1
                if j % v == 0:
                    dp[j] += (1, j/v),
        print dp[target]
        # print dp
        # print [len(set(permutations(l))) for l in dp[target]]
        return sum(count for count, number in dp[target])
    def combinationSum4(self, nums, target):
        nums, combs = sorted(nums), [0] * (target+1)
        for i in range(target + 1):
            for num in nums:
                if num  > i: (i,num,combs[i]).p();break
                if num == i: combs[i] += 1
                if num  < i: combs[i] += combs[i - num]
                (i,num,combs[i]).p()
        
        return combs[target]
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().combinationSum4_time([1,2,3],6).p()
        # Solution().combinationSum4([1,2,3],6).p()        
        # Solution().combinationSum4_time([1,2,3],8).p()
        # Solution().combinationSum4([1,2,3],4).p()
        Solution().combinationSum4([2,3,4],8).p()