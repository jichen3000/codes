class Solution:
    def canIWin(self, max_i, target):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        def dfs(l, sum_v):
            (l, sum_v).p()
            if not l or sum_v >=target: return False
            if l[-1] + sum_v >= target:
                return True
            for i in range(len(l)):
                ll = l[:i]+l[i+1:]
                cur_v = sum_v+l[i]
                res = all(dfs(ll[:j]+ll[j+1:], cur_v + ll[j]) for j in range(len(ll)))
                # res.p()
                if res:
                    return res
            return False
        if target <= 0: return True
        return dfs(list(range(1,max_i+1)), 0)

    def canIWin(self, max_i, target):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        changed, found this one is the next one lose
        """
        mem = {}
        def dfs(s, t):
            # (s, t).p()
            key = tuple(s)
            if key in mem:
                return mem[key]
            if not s or t <= 0: 
                mem[key] = False
                return False
            for v in s:
                cur_t = t-v
                if cur_t <= 0: 
                    mem[key] = True
                    return True
                if not dfs(s-{v}, cur_t):
                    mem[key] = True
                    return True

            mem[key] = False
            return False
        if target <= 0: return True
        if (max_i+1) * max_i / 2 < target: return False
        return dfs(set(range(1,max_i+1)), target)

    def canIWin(self, max_i, target):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        mem = {}
        used = [False] * max_i
        def dfs(t):
            # if t <= 0: return False
            key = tuple(used)
            if key in mem:
                return mem[key]
            for v in range(max_i):
                if used[v]:
                    continue
                used[v] = True
                if t-v-1 <= 0:
                    used[v] = False
                    mem[key] = True
                    return True                    
                if not dfs(t-v-1):
                    used[v] = False
                    mem[key] = True
                    return True
                used[v] = False

            mem[key] = False
            return False
        if target <= 0: return True
        if (max_i+1) * max_i / 2 < target: return False
        return dfs(target)

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().canIWin(10, 1).must_equal(True)
        Solution().canIWin(5, 50).must_equal(False)
        Solution().canIWin(10, 11).must_equal(False)
        Solution().canIWin(10, 40).must_equal(False)
