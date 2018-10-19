from __future__ import division
def gcd(a, b):
    ''' greatest common divisor '''
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a,b)



class Solution:
    def nthMagicalNumber(self, n, a, b):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        a, b = min(a,b), max(a,b)
        i, j = 0, b - a
        v = a
        m = 1000000007
        if b % a == 0:
            return a * n % m
        # (i, j, v).p()
        while n > 1:
            n -= 1
            # (i, j).p()
            if i == 0 and j == 0:
                inc = a
                j = b - a
            elif i == 0 and j > 0:
                inc = min(a, j)
                i = a - inc
                j = j - inc
            else:
                inc = i
                j = b - i
                i = 0
            v += inc
            # (i, j, v).p()
        return v % m

    def nthMagicalNumber(self, n, a, b):
        """
        :type N: int
        :type A: int
        :type B: int
        :rtype: int
        """
        # a, b = min(a,b), max(a,b)
        lcm_v = lcm(a, b)
        m_set = set()
        for i in range(1, lcm_v // a + 1):
            m_set.add(i * a)
        for i in range(1, lcm_v // b+ 1):
            m_set.add(i * b)
        m_list = sorted(m_set)
        # m_list.p()
        d, m = divmod(n-1, len(m_list))
        res = d * lcm_v + m_list[m]
        return res % 1000000007