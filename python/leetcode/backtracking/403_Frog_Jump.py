class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        n = len(stones)
        for i in range(n-1, 5, -1):
            dist = stones[i] - stones[i-1]
            if dist > stones[i-1]:
                return False
        def get_nexts(index, pre_unit):
            result = []
            for i in range(index+1, n):
                next_unit = stones[i] - stones[index]
                if next_unit >= pre_unit-1 and next_unit <= pre_unit+1:
                    result.insert(0,i)
                if next_unit > pre_unit+1:
                    break
            return result
        mem = {}
        def dfs(index, pre_unit):
            # (index, stones[index],pre_unit).p()
            key = (index, pre_unit)
            if key in mem:
                return mem[key]
            if index == n-1:
                mem[key] = True
                return mem[key]
            next_moves = get_nexts(index, pre_unit)
            # next_moves.p()
            if len(next_moves) == 0:
                return False
            for next_i in next_moves:
                if dfs(next_i, stones[next_i]-stones[index]):
                    mem[(next_i, stones[next_i]-stones[index])] = True
                    return True
            return False
        return dfs(0,0)

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().canCross([0,1,3,5,6,8,12,17]).must_equal(True)
        Solution().canCross([0,1,2,3,4,8,9,11]).must_equal(False)
