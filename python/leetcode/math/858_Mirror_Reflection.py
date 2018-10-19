class Solution:
    def mirrorReflection(self, p, q):
        """
        :type p: int
        :type q: int
        :rtype: int
        """
        n = 1
        while n * q % p > 0:
            n += 1
        # n.p()
        if n % 2 == 0:
            return 2
        else:
            if (n * q // p) % 2 == 1:
                return 1
        return 0


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().mirrorReflection(2, 1).must_equal(2)
        Solution().mirrorReflection(3, 2).must_equal(0)
        Solution().mirrorReflection(4, 3).must_equal(2)
        Solution().mirrorReflection(3, 1).must_equal(1)
        Solution().mirrorReflection(4, 4).must_equal(1)


