class Solution(object):
    def ipToCIDR(self, ip, n):
        """
        :type ip: str
        :type n: int
        :rtype: List[str]
        """
        def get_ip(num, mask):
            res = []
            for i in range(4):
                v = num & 255
                num >>= 8
                res += str(v),
            return ".".join(res[::-1])+"/"+str(mask)
        num, i = 0, 0
        res = []
        for v in reversed(ip.split(".")):
            num += int(v) * (256 ** i)
            i += 1
        while n > 0:
            # get the rightest 1
            step = num & -num
            count, mask = 1, 32
            while count <= min(step,n):
                count *= 2
                mask -= 1
            if count > 1:
                # count.p()
                count //= 2
                mask += 1
            # (count, mask).p()
            res += get_ip(num, mask),
            num += count
            n -= count
        return res

if __name__ == '__main__':
    from minitest import *

    with test("Solution"):
        Solution().ipToCIDR("117.145.102.62",8).must_equal(["117.145.102.62/31","117.145.102.64/30","117.145.102.68/31"])
