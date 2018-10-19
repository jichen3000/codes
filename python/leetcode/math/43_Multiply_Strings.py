class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        mem = {}
        def add_list(long_list, short_list):
            carry = 0
            results = []
            ln, sn = len(long_list), len(short_list)
            for i in range(ln-1, -1, -1):
                j = sn - (ln - i)
                short_v = short_list[j] if j >=0 else 0
                cur = carry+ long_list[i] + short_v
                if cur >= 10:
                    carry = 1
                    cur -= 10
                else:
                    carry = 0
                results += cur,
            if carry == 1:
                results += 1,
            # results.p()
            return results[::-1]
        def cal(n1, nums):
            if n1 in mem:
                return mem[n1][::]
            i = 0
            sums1 = [0]
            for n2 in reversed(nums):
                res = n1 * n2
                # res.p()
                res = list(str(res))
                res = map(int, res)
                res += [0] * i
                sums1 = add_list(res, sums1)
                # (n1, n2, res, sums1).p()
                i += 1
            mem[n1] = sums1
            return sums1[::]
        if num1 == "0" or num2 == "0":
            return "0"
        sums=[0]
        i = 0
        nums1 = map(int, num1)
        nums2 = map(int, num2)
        for n1 in reversed(nums1):
            res = cal(n1, nums2)
            res += [0] * i
            sums = add_list(res, sums)
            # (n1, nums2, res, sums).p()
            i += 1
        return "".join(map(str, sums))
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"
        n1, n2 = len(num1), len(num2)
        nums1 = map(lambda x: ord(x) - 48, num1)
        # nums1.p()
        nums2 = map(lambda x: ord(x) - 48, num2)
        # nums2.p()
        res = [0] * (n1+n2)
        for i in range(n1-1, -1, -1):
            # c1 = ord(num1[i]) - 48
            c1 = nums1[i]
            for j in range(n2-1, -1, -1):
                # c2 = ord(num2[j]) - 48
                # c2.p()
                c2 = nums2[j]
                # c2.p()
                k = i + j
                sum_v = c1 * c2 + res[k+1]
                res[k] += sum_v / 10
                res[k+1] = sum_v % 10
        if res[0] == 0:
            res.pop(0)
        return "".join(map(str,res))
            
            

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().multiply("0","0").must_equal("0")
        Solution().multiply("0","9999").must_equal("0")
        Solution().multiply("227","345").must_equal("78315")
        Solution().multiply("123","456").must_equal("56088")
