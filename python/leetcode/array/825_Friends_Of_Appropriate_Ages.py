class Solution:
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        ages.sort()
        res = 0
        for i in range(len(ages)-1):
            for j in range(i+1, len(ages)):
                if ages[j] < 2 * ages[i] - 14:
                    res += 1 if ages[i] != ages[j] else 2
                else:
                    break
        return res 

    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        res = 0
        nums = [0] * 121
        for age in ages:
            nums[age] += 1
        for age in range(15, 121):
            if nums[age] > 0:
                if nums[age] > 1:
                    res += nums[age]*(nums[age]-1)
                range_age = age * 2 - 14
                res += sum(nums[age+1:range_age]) * nums[age]
                # (age, nums[age], range_age, res).p()
        return res

    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int
        """
        res = 0
        nums = [0] * 121
        for age in ages:
            nums[age] += 1
        v_sum, v_range = 0, 0
        for age in range(15, 121):
            if age == 16:
                v_range = 18
                v_sum = nums[17]
            elif age > 16:
                v_range += 2
                v_sum -= nums[age]
                if age <= 67:
                    v_sum += nums[v_range-2] + nums[v_range-1]
                elif age == 68:
                    v_sum += nums[120]
            if nums[age] > 0:
                if nums[age] > 1:
                    res += nums[age]*(nums[age]-1)
                range_age = age * 2 - 14
                res += v_sum * nums[age]
                # (age, nums[age], range_age, res).p()
        return res

    
        
if __name__ == '__main__':
    from minitest import *

    with test("Solution"):
        Solution().numFriendRequests([16,16]).must_equal(2)
        Solution().numFriendRequests([16,16,16]).must_equal(6)
        Solution().numFriendRequests([16,17,18]).must_equal(2)
        Solution().numFriendRequests([20,30,100,110,120]).must_equal(3)
        Solution().numFriendRequests([8,85,24,85,69]).must_equal(4)
        Solution().numFriendRequests([49,110,13,39,45,104,9,114,86,72,13,24,10,77,103,85,9,21,66,25]).must_equal(47)
        