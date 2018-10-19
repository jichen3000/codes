# 773. Sliding Puzzle 50mins
class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        possible_map = {
            0:[1,3],
            1:[0,2,4],
            2:[1,5],
            3:[0,4],
            4:[1,3,5],
            5:[2,4],
        }
        
        def exchange(s, i, j):
            smalli = min(i, j)
            bigi = max(i,j)
            return s[:smalli] + s[bigi] + s[smalli+1:bigi] + s[smalli] + s[bigi+1:]

        def get_moves(s):
            pre_i = s.index("0")
            res = set()
            for next_i in possible_map[pre_i]:
                new_s = exchange(s, pre_i, next_i)
                # (s, pre_i, next_i, new_s).p()
                if new_s not in visited:
                    res.add(new_s)
            return res

        b = [str(board[i][j]) for i in range(2) for j in range(3)]
        s = "".join(b)
        target = "123450"
        if s == target: return 0
        acc = {s}
        visited = set()
        count = 0
        while acc:
            # acc.p()
            visited |= acc
            count += 1
            nexts = set()
            for cur_s in acc:
                next_set = get_moves(cur_s)
                # (s, next_set).p()
                if target in next_set:
                    return count
                nexts |= next_set
            acc = nexts
        return -1





if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        # Solution().slidingPuzzle([[1,2,3],[4,0,5]]).must_equal(1)
        # Solution().slidingPuzzle([[1,2,3],[5,4,0]]).must_equal(-1)
        Solution().slidingPuzzle([[3,2,4],[1,5,0]]).must_equal(14)
