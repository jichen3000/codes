class Solution:
    def numberOfPatterns(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        jumps = {
            (1,7):4, (1,3):2, (1,9):5,
            (3,1):2, (3,9):6, (3,7):5,
            (7,9):8, (7,1):4, (7,3):5,
            (9,3):6, (9,7):8, (9,1):5,
            (2,8):5, (8,2):5,
            (6,4):5, (4,6):5,
        }
        res = 0
        def dfs(cur, size):
            count = 0
            if size >= m:
                count += 1
            if size == n:
                return count
            visited[cur] = True
            for nxt in range(1,10):
                jump = jumps.get((cur, nxt), None)
                if not visited[nxt] and (jump == None or visited[jump]):
                    count += dfs(nxt, size+1)
            visited[cur] = False
            return count
            
                
        visited = [False] * 10
        res += dfs(1, 1) * 4
        res += dfs(2, 1) * 4
        res += dfs(5, 1)
        return res
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().numberOfPatterns(1,1).must_equal(9)
        Solution().numberOfPatterns(2,2).must_equal(56)
        Solution().numberOfPatterns(1,2).must_equal(65)
        Solution().numberOfPatterns(3,3).must_equal(320)
        Solution().numberOfPatterns(1,3).must_equal(385)