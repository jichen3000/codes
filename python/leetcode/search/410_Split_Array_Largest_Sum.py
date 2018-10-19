import sys
# 25mins
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        if m == 1: return sum(nums)
        groups = [[nums[0]]]
        max_len = n - m + 1
        min_max = [sys.maxint]
        def get_nexts():
            cur_i = len(groups) - 1
            result = []
            if len(groups[cur_i]) < max_len:
                result += cur_i,
            if cur_i + 1 < m:
                result += cur_i + 1,
            return result

        def dfs(index):
            if index == n:
                if len(groups) != m:
                    return
                # (index, groups).p()
                max_sum = max(sum(g) for g in groups)
                min_max[0] = min(min_max[0], max_sum)
                return
            next_group_indexs = get_nexts()
            if len(next_group_indexs) == 0:
                return
            for i in next_group_indexs:
                if i == len(groups):
                    groups.append([nums[index]])
                    dfs(index + 1)
                    groups.pop()
                else:
                    groups[i].append(nums[index])
                    dfs(index+1)
                    groups[i].pop()
        dfs(1)
        return min_max[0]


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        n = len(nums)
        if m == 1: return sum(nums)
        all_sum = 0
        max_num = nums[0]
        for i in range(n):
            all_sum += nums[i]
            max_num = max(nums[i], max_num)
        l, r = max_num, all_sum
        def is_valid(target):
            total, group_count = 0, 1
            for i in range(n):
                total += nums[i]
                if total > target:
                    total = nums[i]
                    group_count += 1
                    if group_count > m:
                        return False
            return True
        while l < r:
            mid = (l + r) / 2
            if is_valid(mid):
                r = mid
            else:
                l = mid+1
        return l
        

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().splitArray([7,2,5,10,8],2).must_equal(18)
        # Solution().splitArray([1,2147483646],1).must_equal(2147483647)
        # Solution().splitArray([2,3,1,2,4,3],5).must_equal(4)
        # Solution().splitArray([5,2,4,1,3,6,0],4).must_equal(6)
        nums = [5334,6299,4199,9663,8945,3566,9509,3124,6026,6250,7475,5420,9201,9501,38,5897,4411,6638,9845,161,9563,8854,3731,5564,5331,4294,3275,1972,1521,2377,3701,6462,6778,187,9778,758,550,7510,6225,8691,3666,4622,9722,8011,7247,575,5431,4777,4032,8682,5888,8047,3562,9462,6501,7855,505,4675,6973,493,1374,3227,1244,7364,2298,3244,8627,5102,6375,8653,1820,3857,7195,7830,4461,7821,5037,2918,4279,2791,1500,9858,6915,5156,970,1471,5296,1688,578,7266,4182,1430,4985,5730,7941,3880,607,8776,1348,2974,1094,6733,5177,4975,5421,8190,8255,9112,8651,2797,335,8677,3754,893,1818,8479,5875,1695,8295,7993,7037,8546,7906,4102,7279,1407,2462,4425,2148,2925,3903,5447,5893,3534,3663,8307,8679,8474,1202,3474,2961,1149,7451,4279,7875,5692,6186,8109,7763,7798,2250,2969,7974,9781,7741,4914,5446,1861,8914,2544,5683,8952,6745,4870,1848,7887,6448,7873,128,3281,794,1965,7036,8094,1211,9450,6981,4244,2418,8610,8681,2402,2904,7712,3252,5029,3004,5526,6965,8866,2764,600,631,9075,2631,3411,2737,2328,652,494,6556,9391,4517,8934,8892,4561,9331,1386,4636,9627,5435,9272,110,413,9706,5470,5008,1706,7045,9648,7505,6968,7509,3120,7869,6776,6434,7994,5441,288,492,1617,3274,7019,5575,6664,6056,7069,1996,9581,3103,9266,2554,7471,4251,4320,4749,649,2617,3018,4332,415,2243,1924,69,5902,3602,2925,6542,345,4657,9034,8977,6799,8397,1187,3678,4921,6518,851,6941,6920,259,4503,2637,7438,3893,5042,8552,6661,5043,9555,9095,4123,142,1446,8047,6234,1199,8848,5656,1910,3430,2843,8043,9156,7838,2332,9634,2410,2958,3431,4270,1420,4227,7712,6648,1607,1575,3741,1493,7770,3018,5398,6215,8601,6244,7551,2587,2254,3607,1147,5184,9173,8680,8610,1597,1763,7914,3441,7006,1318,7044,7267,8206,9684,4814,9748,4497,2239]
        Solution().splitArray(nums,9).must_equal(194890)
