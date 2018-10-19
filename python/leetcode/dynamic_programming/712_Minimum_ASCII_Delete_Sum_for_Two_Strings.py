def cal_value(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    if s1 == s2: return 0
    if n1 == 0: return sum(ord(c) for c in s2)
    j = 0
    results = ""
    for i in range(n1):
        j = i + len(results)
        if j >= n2:
            return -1
        while s1[i] != s2[j]:
            results += s2[j]
            j += 1
            if j >= n2: 
                return -1
    # i.p()
    if j < n2-1:
        results += s2[j+1:]
    if len(results) > 0:
        return sum(ord(c) for c in results)
    else:
        return 0

class Solution(object):
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        level = False
        results = []
        queue = [s1]
        visited = {s1:True}

        while queue:
            cur = queue.pop(0)
            cur_v = cal_value(cur, s2)
            # (cur, cur_v).p()
            if cur_v >= 0:
                results += cur_v + cal_value(cur, s1),
                # results.p()
                level = True
            if level: 
                continue
            for i in range(len(cur)):
                new_s = cur[:i] + cur[i+1:]
                if new_s not in visited:
                    queue.append(new_s) 
                    visited[new_s] = True
        if results:
            return min(results)
        else: return None

    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        def cal_s(s):
            return sum(ord(c) for c in s) 
        n1 = len(s1)
        n2 = len(s2)
        if s1 == s2: return 0
        if n1 == 0: return sum(ord(c) for c in s2)
        if n2 == 0: return sum(ord(c) for c in s1)
        dp = [ [0] * n2 for _ in range(n1)]
        j = 0
        for i in range(n1):
            if s2[j] == s1[i]:
                dp[i][j] = cal_s(s1[:i+1]) - ord(s2[j])
            else:
                dp[i][j] = cal_s(s1[:i+1]) + ord(s2[j])
        i = 0
        for j in range(n2):
            if s1[i] in s2[:j+1]:
                dp[i][j] = cal_s(s2[:j+1]) - ord(s1[i])
            else:
                dp[i][j] = cal_s(s2[:j+1]) + ord(s1[i])

        for i in range(1,n1):
            for j in range(1,n2):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+ord(s1[i]), dp[i][j-1]+ord(s2[j]))
        # dp.p()
        return dp[-1][-1]
                        
        
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        def cal_s(s):
            return sum(ord(c) for c in s) 
        n1 = len(s1)
        n2 = len(s2)
        if s1 == s2: return 0
        if n1 == 0: return sum(ord(c) for c in s2)
        if n2 == 0: return sum(ord(c) for c in s1)
        dp = [ [0] * n2 for _ in range(n1)]
        e1, e2 = False, False
        if s1[0] == s2[0]:
            e1, e2 = True, True
        else:
            dp[0][0] = ord(s1[0]) + ord(s2[0])
        j = 0
        for i in range(1,n1):
            if not e1 and s1[i] == s2[j]:
                dp[i][j] = dp[i-1][j] - ord(s1[i])
                e1 = True
            else:
                dp[i][j] = dp[i-1][j] + ord(s1[i])
        i = 0
        for j in range(1,n2):
            if not e2 and s1[i] == s2[j]:
                dp[i][j] = dp[i][j-1] - ord(s2[j])
                e2 = True
            else:
                dp[i][j] = dp[i][j-1] + ord(s2[j])

        for i in range(1,n1):
            for j in range(1,n2):
                if s1[i] == s2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+ord(s1[i]), dp[i][j-1]+ord(s2[j]))
        # dp.p()
        return dp[-1][-1]
    def minimumDeleteSum(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: int
        """
        dp = [ [0] * (len(s2)+1) for _ in range(len(s1)+1)]
        j = 0
        for i in range(1,len(dp)):
            dp[i][j] = dp[i-1][j] + ord(s1[i-1])
        i = 0
        for j in range(1,len(dp[0])):
            dp[i][j] = dp[i][j-1] + ord(s2[j-1])
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j]+ord(s1[i-1]), dp[i][j-1]+ord(s2[j-1]))
        return dp[-1][-1]



if __name__ == '__main__':
    from minitest import *
    # with test(cal_value):
    #     cal_value("let","leet").p()
    #     cal_value("lete","leet").p()
    #     cal_value("let","delete").p()
    #     cal_value("ea","sea").p()
    #     cal_value("k","yaybzvxitky").p()
    #     cal_value("k","rpnuskcphiw").p()
    #     cal_value("i","yaybzvxitky").p()
    #     cal_value("i","rpnuskcphiw").p()
    #     cal_value("","rpnuskcphiw").p()

    with test(Solution):
        Solution().minimumDeleteSum("sea","eat").must_equal(231)
        Solution().minimumDeleteSum("delete","leet").must_equal(403)
        Solution().minimumDeleteSum("yaybzvxitky","rpnuskcphiw").must_equal(2246)




        
        