class Solution(object):
    # TLE 20mins
    def orderOfLargestPlusSign(self, n, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        mine_set = set()
        for m in mines:
            mine_set.add(tuple(m))
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]
        def check(i,j,k):
            for di, dj in dirs:
                ni = i + di * k
                nj = j + dj * k
                if not (ni >= 0 and ni < n and nj >= 0 and nj < n and (ni,nj) not in mine_set):
                    return False
            return True
        max_n = (n+1)/2
        result = 0
        for i in range(n):
            for j in range(n):
                cur = 0
                for k in range(max_n+1):
                    if check(i,j,k):
                        cur += 1
                    else:
                        break
                result = max(cur, result)
                if result == max_n:
                    return result
        return result
    def orderOfLargestPlusSign(self, n, mines):
        """
        :type N: int
        :type mines: List[List[int]]
        :rtype: int
        """
        mine_set = set()
        for m in mines:
            mine_set.add(tuple(m))
        pre_row = [[None, None] for _ in range(n)]
        pre_one = [None, None]
        result = 0
        for i in range(n):
            cur_row = [[None, None] for _ in range(n)]
            pre_one = [None, None]
            for j in range(n):
                if (i,j) not in mine_set:
                    # (i,j).p()
                    min_i, min_j = 1, 1
                    if pre_row[j][0]:
                        pi, li = pre_row[j][0]
                        min_i = min(i-pi, li-i) + 1
                        cur_row[j][0] = pre_row[j][0]
                    else:
                        ii = i
                        for ii in range(i+1, n):
                            if (ii, j) in mine_set:
                                break
                        else:
                            ii = n
                        cur_row[j][0] = (i, ii-1)
                    if pre_one[1]:
                        pj, lj = pre_one[1]
                        min_j = min(j-pj, lj-j) + 1
                        cur_row[j][1] = pre_one[1]
                    else:
                        jj = j
                        for jj in range(j+1, n):
                            if (i, jj) in mine_set:
                                break
                        else:
                            jj = n
                        cur_row[j][1] = (j, jj-1)
                    # (i,j,cur_row[j], min_i, min_j).p()
                    result = max(result, min(min_i, min_j))
                pre_one = cur_row[j][:]
            pre_row = [cur_row[j][:] for j in range(n)]
        return result

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().orderOfLargestPlusSign(5, [[4,2]]).must_equal(2)
        Solution().orderOfLargestPlusSign(2, []).must_equal(1)
        Solution().orderOfLargestPlusSign(1, [[0,0]]).must_equal(0)
        Solution().orderOfLargestPlusSign(2, [[0,0],[0,1],[1,0]]).must_equal(1)
        Solution().orderOfLargestPlusSign(3, [[0,0]]).must_equal(2)
