class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        max_area = 0
        for i in range(m):
            pre = matrix[i]
            for i2 in range(i,m):
                if i2 == i:
                    cur = matrix[i2]
                else:
                    cur = matrix[i2][:]
                    for j in range(n):
                        if pre[j] != "1":
                            cur[j] = "0"
                    pre = cur

                cur_sum, max_s = 0, 0
                for j in range(n):
                    if cur[j] == "1":
                        cur_sum += 1
                        max_s = max(cur_sum, max_s)
                    else:
                        cur_sum = 0
                max_area = max(max_area, max_s*(i2-i+1))
                # (i,i2, cur, max_s, max_area).p()
        return max_area
    # the version I figured out
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        h_list = [0] * n
        left_list = [0] * n
        right_list = [n-1] * n
        max_v = 0
        for i in range(m):
            cur_row = matrix[i]
            for j in range(n):
                if cur_row[j] == "1":
                    h_list[j] += int(cur_row[j])
                else:
                    h_list[j] = 0
            closed_0 = 0 if cur_row[0] == "0" else -1
            for j in range(1, n):
                if cur_row[j] == "0":
                    left_list[j] = 0
                    closed_0 = j
                else:
                    if h_list[j] > h_list[j-1]:
                        left_list[j] = j
                    # else:
                    #     left_list[j] = left_list[j-1]
                    elif h_list[j] == h_list[j-1]:
                        left_list[j] = left_list[j-1]
                    else:
                        # if i-1 >= 0 and matrix[i-1][j] == "0":
                        #     left_list[j] = closed_0 + 1
                        left_list[j] = max(closed_0 + 1, left_list[j])

            closed_0 = n-1 if cur_row[-1] == "0" else n
            for j in range(n-2, -1, -1):
                if cur_row[j] == "0":
                    right_list[j] = n-1
                    closed_0 = j
                else:
                    if h_list[j] > h_list[j+1]:
                        right_list[j] = j
                    # else:
                    #     right_list[j] = right_list[j+1]
                    elif h_list[j] == h_list[j+1]:
                        right_list[j] = right_list[j+1]
                    else:
                        # if i-1 >= 0 and matrix[i-1][j] == "0":
                        right_list[j] = min(closed_0 -1,right_list[j]) 
            for j in range(n):
                v = (right_list[j] + 1 - left_list[j]) * h_list[j]
                max_v = max(max_v, v)
            # (i, h_list, right_list, left_list, max_v).p()
        return max_v                    
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        right = [n] * n
        left, height = [0] * n, [0] * n
        max_area = 0
        for i in range(m):
            cur_left, cur_right = 0, n
            for j in range(n-1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j
            for j in range(n):
                if matrix[i][j] == "1":
                    left[j] = max(left[j], cur_left)
                    height[j] += 1
                else:
                    left[j] = 0
                    cur_left = j + 1
                    height[j] = 0
                max_area = max(max_area, (right[j]-left[j])*height[j])
        return max_area

## review
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        h = [0] * n
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    h[j] += 1
                else:
                    h[j] = 0
            for j in range(n):
                w = 1
                for k in range(j-1,-1,-1):
                    if h[k] >= h[j]:
                        w += 1
                    else:
                        break
                for k in range(j+1,n):
                    if h[k] >= h[j]:
                        w += 1
                    else:
                        break
                area = w * h[j]
                res = max(res, area)
        return res

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        if m == 0: return 0
        n = len(matrix[0])
        h = [0] * n
        l, r = [0] * n, [n-1] * n
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == "1":
                    h[j] += 1
                else:
                    h[j] = 0
            k = n
            for j in range(n-1,-1,-1):
                if matrix[i][j] == "0":
                    k = j
                    r[j] = n-1
                else:
                    r[j] = min(r[j], k-1)

            k = -1
            for j in range(n):
                if matrix[i][j] == "0":
                    k = j
                    l[j] = 0
                else:
                    l[j] = max(l[j], k+1)
                area = (r[j]-l[j]+1) * h[j]
                # (i,j,h[j],r[j],l[j],area).p()
                res = max(res, area)
        return res
             
                
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        ma = [  ["1","0","1","0","0"],
                ["1","0","1","1","1"],
                ["1","1","1","1","1"],
                ["1","0","0","1","0"]]
        Solution().maximalRectangle(ma).must_equal(6)
        # ma = [["1","0","1","1","1"],["0","1","0","1","0"],["1","1","0","1","1"],["1","1","0","1","1"],["0","1","1","1","1"]]
        # Solution().maximalRectangle(ma).must_equal(6)
        # ma = [
        #         ["0","0","0","1","0","0","0"],
        #         ["0","0","1","1","1","0","0"],
        #         ["0","1","1","1","1","1","0"]]
        # Solution().maximalRectangle(ma).must_equal(6)

