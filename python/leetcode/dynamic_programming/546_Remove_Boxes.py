class Solution(object):
    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        n = len(boxes)
        def get_nexts(boxes):
            len_dict = {}
            for i in range(len(boxes)):
                v = boxes[i]
                if v in len_dict:
                    last = len_dict[v][-1]
                    if last[0] + last[1] == i:
                        last[1] += 1
                    else:
                        len_dict[v] += [i,1],
                else:
                    len_dict[v] = [[i,1]]
            min_len = len(boxes) + 1
            min_k = -1
            for k, v in len_dict.items():
                v_len = len(v)
                if v_len == 1:
                    return v
                else:
                    v_len = sum(l for i,l in v)
                    if min_len > v_len:
                        min_len = v_len
                        min_k = k
            return len_dict[min_k]                    
        max_count = [0]
        def dfs(boxes, count):
            if len(boxes) == 0:
                max_count[0] = max(max_count[0], count) 
                return
            next_moves = get_nexts(boxes)
            for i, l in next_moves:
                dfs(boxes[:i]+boxes[i+l:], count + l ** 2)
        dfs(boxes,0)
        return max_count[0]

    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        n = len(boxes)
        mem = {}
        def get_nexts(boxes):
            len_dict = {}
            for i in range(len(boxes)):
                v = boxes[i]
                if v in len_dict:
                    last = len_dict[v][-1]
                    if last[0] + last[1] == i:
                        last[1] += 1
                    else:
                        len_dict[v] += [i,1],
                else:
                    len_dict[v] = [[i,1]]
            # len_dict.pp()
            # exit(0)
            result = []
            for k, v in len_dict.items():
                v_len = len(v)
                if v_len == 1:
                    return v
                else:
                    result += v
            return result                 
        max_count = [0]
        def dfs(boxes, count):
            ti = tuple(boxes)
            # ti.p()
            if ti in mem:
                return mem[ti]
            # boxes.p()
            if len(boxes) == 0:
                # max_count[0] = max(max_count[0], count) 
                return count
            next_moves = get_nexts(boxes)
            result = max(dfs(boxes[:i]+boxes[i+l:], count + l ** 2) for i, l in next_moves)
            mem[ti] = result
            return mem[ti]
                
        return dfs(boxes,0)
        # return max_count[0]

    def removeBoxes(self, boxes):
        """
        :type boxes: List[int]
        :rtype: int
        """
        n = len(boxes)
        if n == 0: return 0
        dp = [[[0] * n  for _ in range(n)] for _ in range(n)]
        l = 0
        for i in range(n):
            j = i + l
            for k in range(i+1):
                dp[i][j][k] = (k+1) ** 2

        for l in range(1,n):
            for i in range(n-l):
                j = i + l
                for k in range(i+1):
                    dp[i][j][k] = (k+1)**2 + dp[i+1][j][0]
                    for m in range(i+1, j+1):
                        if boxes[i] == boxes[m]:
                            dp[i][j][k] = max(dp[i][j][k], dp[i+1][m-1][0]+dp[m][j][k+1])
        return dp[0][-1][0]



if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # boxes = [1, 3, 2, 2, 2, 3, 4, 3, 1]
        # Solution().removeBoxes(boxes).must_equal(23)
        Solution().removeBoxes([1,2,1,2,1]).must_equal(11)

        # Solution().removeBoxes([6, 10, 1, 7, 1, 3, 10, 2, 1, 3]).must_equal(16)
        boxes = [3,8,8,5,5,3,9,2,4,4,6,5,8,4,8,6,9,6,2,8,6,4,1,9,5,3,10,5,3,3,9,8,8,6,5,3,7,4,9,6,3,9,4,3,5,10,7,6,10,7]
        Solution().removeBoxes(boxes).must_equal(136)