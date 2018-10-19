class Solution:
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        if not people: return 0
        res = 0
        people.sort(reverse=True)
        # people.p()
        count = 0
        while people:
            cur = 0
            count = 0
            while count < 2 and people and cur + people[0] <= limit:
                cur += people.pop(0)
                count += 1
            while count < 2 and people and cur + people[-1] <= limit:
                cur += people.pop()
                count += 1
            res += 1
            # (cur, res, people).p()
        return res

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().numRescueBoats([1,2],3).must_equal(1)
        # Solution().numRescueBoats([3,2,2,1],3).must_equal(3)
        Solution().numRescueBoats([3,2,3,2,2],6).must_equal(3)
