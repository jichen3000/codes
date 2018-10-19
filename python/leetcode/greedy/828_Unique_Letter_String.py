class Solution:
    def uniqueLetterString(self, s):
        """
        :type s: str
        :rtype: int
        """
        mem = {}
        pre = 0
        sum_v, res = 0, 0
        for i,c in enumerate(s):            
            if c in mem:
                pi = mem[c][1]
                cur = 1 + pre + i - 1 - mem[c][1]
                # cur.p()
                # # if mem[c][0] == 1:
                # #     cur -= mem[c][1] + 1
                # # else:
                # (mem[c][1] - mem[c][0] ).p()
                cur -= mem[c][1] - mem[c][0] 
                mem[c] += i,
                mem[c].pop(0)
            else:
                cur = 1 + pre + i
                mem[c] = [-1,i]
            # (i,c,cur).p()
            sum_v += cur
            pre = cur
        return sum_v % (10**9 + 7)
        
        
        
if __name__ == '__main__':
    from minitest import *

    with test("Solution"):
        Solution().uniqueLetterString("abc").must_equal(10)
        Solution().uniqueLetterString("aba").must_equal(8)
        Solution().uniqueLetterString("aaa").must_equal(3)
        Solution().uniqueLetterString("aaaa").must_equal(4)
