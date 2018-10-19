# Given a list of words (without duplicates), please write a program that returns all concatenated words in the given list of words.

# A concatenated word is defined as a string that is comprised entirely of at least two shorter words in the given array.

# Example:
# Input: ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]

# Output: ["catsdogcats","dogcatsdog","ratcatdogcat"]

# Explanation: "catsdogcats" can be concatenated by "cats", "dog" and "cats"; 
#  "dogcatsdog" can be concatenated by "dog", "cats" and "dog"; 
# "ratcatdogcat" can be concatenated by "rat", "cat", "dog" and "cat".
# Note:
# The number of elements of the given array will not exceed 10,000
# The length sum of elements in the given array will not exceed 600,000.
# All the input string will only include lower case letters.
# The returned elements order does not matter.
class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        fib = [1,2]
        n = int(log(num,2))
        # n.p()
        for i in range(2,n+1):
            fib += fib[i-1] + fib[i-2],

        def dfs(num):
            if num == 0:
                return 1
            elif num == 1:
                return 2
            elif num == 2 or num == 3:
                return 3
            n = int(log(num,2))
            new_num = num - 2 ** n
            if new_num >= 2 ** (n-1):
                return fib[n] + fib[n-1]
            else:
                return fib[n] + dfs(new_num)

        return dfs(num)

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().findIntegers(5).must_equal(5)
        Solution().findIntegers(6).must_equal(5)
        # Solution().findIntegers(16).must_equal(9)