class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        pre_r = ratings[0] - 1
        pre_c = 0
        total_c = 0
        ratings.append(ratings[-1]+1)
        stack = []
        for i in range(len(ratings)-1):
            cur_r, next_r = ratings[i], ratings[i+1]
            if   pre_r <  cur_r and cur_r >  next_r:
                stack.append(pre_c)
            elif pre_r <  cur_r and cur_r <= next_r:
                pre_c += 1
                total_c += pre_c
            elif pre_r >= cur_r and cur_r >  next_r:
                stack.append(0)
            elif pre_r >= cur_r and cur_r <= next_r:
                pre_c = 1
                total_c += pre_c
                stack_cur_c = pre_c
                while stack:
                    stack_pre_c = stack.pop()
                    stack_cur_c = max(stack_cur_c, stack_pre_c) + 1
                    total_c += stack_cur_c
            pre_r = cur_r
        return total_c


if __name__ == '__main__':
    from minitest import *


    with test(Solution):
        Solution().candy([0]).must_equal(1)
        Solution().candy([2,2]).must_equal(2)
        Solution().candy([1,2]).must_equal(3)
        Solution().candy([1,2,2]).must_equal(4)
        Solution().candy([2,3,2]).must_equal(4)
        Solution().candy([2,1]).must_equal(3)
        Solution().candy([1,0,2]).must_equal(5)
        Solution().candy([1,3,5]).must_equal(6)
        Solution().candy([5,3,1]).must_equal(6)
        