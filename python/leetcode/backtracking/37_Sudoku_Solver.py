class Solution:
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        n = 9
        def cal_range_i(i,j):
            return (i//3) * 3 + j // 3

        def inner():    
            def set_v_sets(i,j, v):
                ri = cal_range_i(i,j)
                rows[i].add(v)
                cols[j].add(v)
                ranges[ri].add(v)
            rows = [set() for _ in range(n)]
            cols = [set() for _ in range(n)]
            ranges = [set() for _ in range(n)]
            n_set = set(i+1 for i in range(n))
            empty_set, handled_set = set(), set()
            for i in range(n):
                for j in range(n):
                    if board[i][j] == ".":
                        empty_set.add((i,j))
                    else:
                        set_v_sets(i,j,int(board[i][j]))
            while empty_set:
                temp_set = set()
                for i, j in empty_set:
                    ri = cal_range_i(i,j)
                    lefts = n_set - rows[i] - cols[j] - ranges[ri]
                    if len(lefts) == 0:
                        # (i,j,False,len(handled_set)).p()
                        for ni, nj in handled_set:
                            board[ni][nj] = "."
                        return False
                    if len(lefts) == 1:
                        temp_set.add((i,j))
                        v = lefts.pop()
                        set_v_sets(i,j,v)
                        board[i][j] = str(v)
                        handled_set.add((i,j))
                if len(temp_set) == 0:
                    # must guess
                    guess_list = []
                    for i, j in empty_set:
                        ri = cal_range_i(i,j)
                        lefts = n_set - rows[i] - cols[j] - ranges[ri]
                        if len(lefts) == 2:
                            guess_list = [(2, lefts, i,j,ri)]
                            break
                        guess_list += (len(lefts), lefts, i,j,ri),
                    guess_list.sort()
                    _, lefts, i, j, ri = guess_list.pop(0)
                    for v in lefts:
                        rows[i].add(v)
                        cols[j].add(v)
                        ranges[ri].add(v)
                        board[i][j] = str(v)
                        if inner():
                            # "inner".p()
                            return True
                        rows[i].discard(v)
                        cols[j].discard(v)
                        ranges[ri].discard(v)
                        board[i][j] = "."
                    for ni, nj in handled_set:
                        board[ni][nj] = "."
                    return False
                empty_set -= temp_set
            return True
        inner()
        
        
if __name__ == '__main__':
    from minitest import *

    with test("Solution"):
        # Solution().largestIsland([[1,1],[1,0]]).must_equal(4)
        # Solution().largestIsland([[0,1],[1,0]]).must_equal(3)
        board = [[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
        Solution().solveSudoku(board)
        board.must_equal([])
