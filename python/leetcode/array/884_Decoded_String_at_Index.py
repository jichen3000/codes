class Solution:
    # MLE 7mins
    def decodeAtIndex(self, s, k):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        cur = ""
        for v in s:
            if v.isalpha():
               cur += v
            else:
                cur *= int(v)
            if len(cur) >= k:
                return cur[k-1]


    def decodeAtIndex(self, s, k):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        cur = ""
        total_size = size = 0
        count = 1
        stack = []
        pre = None
        for v in s:
            if v.isalpha():
                if pre and not pre.isalpha():
                    stack += (cur, count, size, total_size),
                    cur = ""
                    count = 1
                    size = total_size
                cur += v
                size += 1
                total_size += 1
            else:
                count *= int(v)
                total_size = count * size
            pre = v
            if total_size >= k:
                # stack.pp()
                # (cur, count, size, total_size).p()
                while k>=0:
                    # (v, k, cur, count, size, total_size).p()
                    if total_size == k:
                        return cur[-1]
                    left = k % size
                    if left == 0: left = size
                    # (left, stack[-1][3] if stack else 0).p()
                    if stack and stack[-1][3] >= left:
                        k = left
                        cur, count, size, total_size = stack.pop()
                    else:
                        return cur[left-1-(stack[-1][3] if stack else 0)]
    
    def decodeAtIndex(self, S, K):
        N = 0
        for i, c in enumerate(S):
            if c.isdigit():
                N *= int(c)
            else:
                N += 1
            if K <= N: break
        for j in range(i, -1, -1):
            c = S[j]
            if c.isdigit():
                N //= int(c)
                K %= N
            else:
                if K == N or K == 0: return c
                N -= 1
            # (j, c, N, K).p()
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().decodeAtIndex("leet2code3", 10).must_equal("o")
        # Solution().decodeAtIndex("a2345678999999999999999", 1).must_equal("a")
        # Solution().decodeAtIndex("leet2code3", 22).must_equal("o")
        # Solution().decodeAtIndex("leet2code3", 18).must_equal("e")
        # Solution().decodeAtIndex("leet2code3", 20).must_equal("t")
        # Solution().decodeAtIndex("leet2code3", 14).must_equal("e")
        # Solution().decodeAtIndex("vk6u5xhq9v", 554).must_equal("k")
        # Solution().decodeAtIndex("n2f7x7bv4l", 110).must_equal("x")
        # Solution().decodeAtIndex("y959q969u3hb22odq595",222280369).must_equal("y")
