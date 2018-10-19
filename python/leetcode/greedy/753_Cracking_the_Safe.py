# 00, 01, 10, 11
# 00110

# 000, 001, 002
# 010, 011, 012
# 020, 021, 022

# 100, 101, 102
# 110, 111, 112
# 120, 121, 122

# 200, 201, 202
# 210, 211, 212
# 220, 221, 222

class Solution:
    # def crackSafe(self, n, k):
    #     from itertools import permutations
    #     all_set = {"".join(map(int, l)) for l in permutations(range(k), n)}
    #     res = "0" * n
    #     while all_set:
    def crackSafe(self, n, k):
        all_s = list(map(str,range(k)))
        def dfs(cur, used):
            cur.p()
            if len(used) == k**n - 1:
                return [True, cur]
            used.add(cur[-n:])
            for digit in all_s:
                new = cur + digit
                (new, digit, new[-n:]).p()
                if new[-n:] not in used:
                    temp = dfs(new, used)
                    if temp[0]:
                        return temp
            used.remove(cur[-n:])
            return [False, cur]
        return dfs('0'*n, set())[1]            
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        ints = list(map(str, range(k)))
        end_count = k ** n - 1
        used = set()
        def dfs(cur):
            # cur.p()
            if len(used) == end_count:
                return (True, cur)
            used.add(cur[-n:])
            for c in ints:
                new = cur + c
                if new[-n:] not in used:
                    res = dfs(new)
                    if res[0]:
                        return res
            used.discard(cur[-n:])
            return (False, cur)
        return dfs("0"*n)[1]  

class Solution:
    def crackSafe(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        visited, count = set(), k ** n
        def dfs(s):
            # s.p()
            if len(visited) == count:
                return s
            for i in range(k):
                new_s = s + str(i)
                # (new_s,new_s[-n:]).p()
                if new_s[-n:] not in visited:
                    visited.add(new_s[-n:])
                    result = dfs(new_s) 
                    if result: return result
                    visited.discard(new_s[-n:])
        return dfs("0" * (n-1))              
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().crackSafe(3,3).must_equal("00010020110120210221112122200")
        Solution().crackSafe(1,2).must_equal("01")
