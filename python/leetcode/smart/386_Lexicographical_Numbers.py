class Solution(object):
    def lexicalOrder_time(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        # a = map(str, range(1,n+1))
        # a.sort()
        # return map(int, a)
        def down(n):
            return 10 ** (len(str(n))-1) - 1
        if n == 0:
            return []
        if n < 10:
            return range(1,n+1)
        acc = [1]
        results = []
        visited = {}
        while len(acc) > 0:
            cur = acc.pop()
            results += cur,
            if cur * 10 <= n:
                if not visited.get((cur+1),False):
                    if len(acc) == 0  or (len(acc) > 0 and str(acc[-1]) > str(cur+1)):
                        acc += cur + 1,
                acc += cur * 10,
                visited[cur*10] = True
            else:
                if cur + 1 <= n:
                    if len(acc) == 0  or (len(acc) > 0 and str(acc[-1]) > str(cur+1)):
                        acc += cur+1,
                else:
                    down_n = down(n)
                    if down_n != n / 10:
                        n = down_n
                        # print("new n:",n)
                    else:
                        break
        return results
    def lexicalOrder(self, n):
        ans = [1]
        while len(ans) < n:
            new = ans[-1] * 10
            while new > n:
                new /= 10
                new += 1
                while new % 10 == 0:    # deal with case like 199+1=200 when we need to restart from 2.
                    new /= 10
            ans.append(new)    
        return ans        
        
        