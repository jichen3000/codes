class Solution(object):
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        visited = [[[[False] * 10 for _ in range(10)] for _ in range(10)] for _ in range(10)]
        for deadend in deadends:
            i1, i2, i3, i4 = map(int, deadend)
            visited[i1][i2][i3][i4] = True
        if visited[0][0][0][0]:
            return -1
        visited[0][0][0][0] = True
        target_list = tuple(map(int, target))
        dirs = [(0,0,0,1),(0,0,0,-1),(0,0,1,0),(0,0,-1,0),(0,1,0,0),(0,-1,0,0), (1,0,0,0),(-1,0,0,0)]
        queue = [(0,0,0,0,0)]
        cur_count = 0
        while queue:
            i1, i2, i3, i4, count = queue.pop(0)
            if (i1, i2, i3, i4) == target_list:
                return count
            for d1, d2, d3, d4 in dirs:
                ni1 = (i1 + d1) % 10
                ni2 = (i2 + d2) % 10
                ni3 = (i3 + d3) % 10
                ni4 = (i4 + d4) % 10
                if not visited[ni1][ni2][ni3][ni4]:
                    visited[ni1][ni2][ni3][ni4] = True
                    queue.append((ni1, ni2, ni3, ni4, count+1))

        return -1


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().openLock(["0201","0101","0102","1212","2002"], "0202").must_equal(6)
        Solution().openLock(["1002","1220","0122","0112","0121"], "1200").must_equal(3)
        Solution().openLock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888").must_equal(-1)
        Solution().openLock(["0000"], "8888").must_equal(-1)
