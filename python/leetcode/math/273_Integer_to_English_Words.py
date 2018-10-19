class Solution(object):
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        map_big = {
            0:"",
            1:"Thousand",
            2:"Million",
            3:"Billion"
        }
        map_00 = {
            "2":"Twenty",
            "3":"Thirty",
            "4":"Forty",
            "5":"Fifty",
            "6":"Sixty",
            "7":"Seventy",
            "8":"Eighty",
            "9":"Ninety",            
        }
        map_0 = {
            "1": "One",
            "2": "Two",
            "3": "Three",
            "4": "Four",
            "5": "Five",
            "6": "Six",
            "7": "Seven",
            "8": "Eight",
            "9": "Nine",
            "10":"Ten",
            "11":"Eleven",
            "12":"Twelve",
            "13":"Thirteen",
            "14":"Fourteen",
            "15":"Fifteen",
            "16":"Sixteen",
            "17":"Seventeen",
            "18":"Eighteen",
            "19":"Nineteen",
        }
        if num == 0:
            return "Zero"
        def to_words_3(nums):
            res = []
            if len(nums) == 3:
                if nums[0] != "0":
                    res = [map_0[nums[0]], "Hundred"]
                nums.pop(0)
            if len(nums) == 2:
                if nums[0] == "1":
                    res += map_0[nums[0]+nums[1]],
                    return " ".join(res)
                if nums[0] != "0":
                    res += map_00[nums[0]],
                nums.pop(0)
            if nums[0] != "0":
                res += map_0[nums[0]],
            return " ".join(res)
        nums = list(str(num))
        result = []
        big_i = 0
        while nums:
            i = max(0, len(nums) - 3)
            last_3 = to_words_3(nums[i:])
            # (i, last_3).p()
            if big_i > 0:
                if last_3:
                    result = [last_3, map_big[big_i]] + result
            else:
                result = [last_3]
            big_i += 1
            nums = nums[:i]
        return " ".join(result).strip()

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().numberToWords(1000).must_equal("One Thousand")
        Solution().numberToWords(10000).must_equal("Ten Thousand")
        Solution().numberToWords(1000000).must_equal("One Million")
        Solution().numberToWords(1000001).must_equal("One Million One")
        # Solution().numberToWords(0).must_equal("Zero")
        # Solution().numberToWords(123).must_equal("One Hundred Twenty Three")
        # Solution().numberToWords(12345).must_equal("Twelve Thousand Three Hundred Forty Five")
        # Solution().numberToWords(1234567).must_equal("One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")
        # Solution().numberToWords(1234567).must_equal("One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven")
        # Solution().numberToWords(2147483647).must_equal("Two Billion One Hundred Forty Seven Million Four Hundred Eighty Three Thousand Six Hundred Forty Seven")



