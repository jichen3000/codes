class Solution(object):
    # most stupid one, 2 ** n time and space
    def countPalindromicSubsequences(self, s):
        """
        :type points: List[Point]
        :rtype: int
        """
        def is_p(ss):
            i, j = 0, len(ss) - 1
            while i < j:
                if ss[i] != ss[j]:
                    return False
                i += 1
                j -= 1
            return True
        cur_set = set()
        for i in range(len(s)):
            temp_set = {s[i]} | cur_set
            for item in cur_set:
                new_s = item+s[i]
                temp_set.add(new_s)
            cur_set = temp_set
        res = 0
        for item in cur_set:
            if is_p(item):
                res += 1
        return res 
    # dp, from top to bottom
    # dp(i, j) means including i and j at least one  
    # dp(i, j) = sum( (dp(i1, j1) + 2) if i1 != j1 else 1 for i1, j1 in pairs) 
    def countPalindromicSubsequences(self, s):
        mem={}
        def dfs(start, end):
            # (start, end, s[start:end]).p()
            if start >= end: return 0
            # if start + 1 == end: return 1
            if (start, end) in mem: return mem[(start, end)]
            
            count = 0
            ss = s[start:end+1]
            # ss.p()
            for x in 'abcd':
                # x.p()
                if x not in ss:
                    continue
                i = ss.index(x) + start
                j = ss.rindex(x) + start
                    
                res = (dfs(i+1, j-1) + 2) if i!=j else 1
                count += res
                # (x,i,j, res, count).p()
            mem[(start, end)] = count
            return mem[(start, end)]

        res = dfs(0, len(s)-1) % 1000000007
        # mem.p()
        return res

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().countPalindromicSubsequences("a").must_equal(1)
        # Solution().countPalindromicSubsequences("aba").must_equal(4)
        # Solution().countPalindromicSubsequences("aa").must_equal(2)
        # Solution().countPalindromicSubsequences("bccb").must_equal(6)
        Solution().countPalindromicSubsequences("cccc").must_equal(4)
        # Solution().countPalindromicSubsequences("abccba").must_equal(14)
