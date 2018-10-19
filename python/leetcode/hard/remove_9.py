class Solution(object):
    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        real_n = n
        m = [0] * 10
        for k in xrange(10):
            m[k] = real_n / (9 * (10**k))
            #(real_n,k,m[k]).p()
            if m[k] > 0:
                real_n += m[k] * (10 ** k)
            else:
                break
        return real_n