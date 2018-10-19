def c(up, down):
    if up == 0:
        return 1
    up_mul, down_mul = 1,1
    for i in range(up):
        up_mul *= down - i
        down_mul *= i+1
    return up_mul / down_mul

class Solution(object):
    # this can only for part of it.
    def numberOfArithmeticSlices(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if  n < 3: return 0
        step_mem = {}
        ari_list = []
        for i in range(1, n):
            for j in range(len(ari_list)-1,-1,-1):
                start, count, step, dup = ari_list[j]
                if nums[i] == start + count * step:
                    ari_list[j][1] += 1
                elif nums[i] == start + (count-1) * step:
                    ari_list[j][3] += 1
            # (i, nums[i], ari_list).p()
            for j in range(i):
                new_step = nums[i] - nums[j]
                if new_step == 0:
                    if 0 not in step_mem:
                        new_one = [nums[j], 2, new_step, 1]
                        step_mem[new_step] = [new_one]
                        ari_list += new_one,
                    break

                # new_step.p()
                for start, count, step, dup in step_mem.get(new_step, []):
                    # (start + count * step, nums[j]).p()
                    if start + (count-1) * step == nums[i] and  start != nums[j]:
                        break
                else:
                    new_one = [nums[j], 2, new_step, 1]
                    if new_step in step_mem:
                        if step_mem[new_step][-1][:-1] == new_one[:-1]:
                            step_mem[new_step][-1][-1] += 1
                        else:
                            step_mem[new_step] += new_one,
                            ari_list += new_one,
                    else:
                        step_mem[new_step] = [new_one]
                        ari_list += new_one,
        #     (i, ari_list).p()
        # ari_list.p()
        result = 0
        for start, count, step, dup in ari_list:
            if count > 2:
                if step != 0:
                    (start, count, step, dup).p()
                    result += (count-2)*(count-1) / 2 * dup
                else:
                    for j in range(count - 2):
                        result += c(j, count) * dup

        return result

    def numberOfArithmeticSlices(self, nums):
        res = 0
        n = len(nums)
        mem = [{} for _ in range(n)]
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                # for 2, 3, 3, 4
                same_count = mem[i].get(diff, 0)
                pre_count = mem[j].get(diff, 0)
                # now res add pre count, since it need 3 to count
                res += pre_count
                # plus one is for pre_count
                mem[i][diff] = same_count + pre_count + 1
                (i, nums[i], j, nums[j], diff, same_count + pre_count, mem[i][diff], res).p()
        return res
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().numberOfArithmeticSlices([1,2,3]).must_equal(1)
        Solution().numberOfArithmeticSlices([1,2,3,4]).must_equal(3)
        # Solution().numberOfArithmeticSlices([1,2,3,4,5]).must_equal(7)
        # Solution().numberOfArithmeticSlices([1,2,3,4,5,6]).must_equal(12)
        # Solution().numberOfArithmeticSlices([1,2,3,4,5,6,7]).must_equal(20)
        # Solution().numberOfArithmeticSlices([1,2,3,4,5,6,7,8]).must_equal(29)
        # Solution().numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9]).must_equal(41)
        # Solution().numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9, 10]).must_equal(55)
        # Solution().numberOfArithmeticSlices([2,2,3,4]).must_equal(2)
        # Solution().numberOfArithmeticSlices([0,1,2,2,2]).must_equal(4)
        # Solution().numberOfArithmeticSlices([0,2000000000,-294967296]).must_equal(0)
        # Solution().numberOfArithmeticSlices([1,1,1,1]).must_equal(5)
        # Solution().numberOfArithmeticSlices([1,1,1,1,1]).must_equal(16)
        # Solution().numberOfArithmeticSlices([79,20,64,28,67,81,60,58,97,85,92,96,82,89,46,50,15,2,36,44,54,2,90,37,7,79,26,40,34,67,64,28,60,89,46,31,9,95,43,19,47,64,48,95,80,31,47,19,72,99,28,46,13,9,64,4,68,74,50,28,69,94,93,3,80,78,23,80,43,49,77,18,68,28,13,61,34,44,80,70,55,85,0,37,93,40,47,47,45,23,26,74,45,67,34,20,33,71,48,96]).must_equal(
        #         1030)
