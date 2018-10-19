class Solution(object):
    def judgeCircle(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        result = [0,0]
        for cur_m in moves:
            if cur_m == "U":
                result[0] += 1
            elif cur_m == "D":
                result[0] -= 1
            elif cur_m == "L":
                result[1] += 1
            elif cur_m == "R":
                result[1] -= 1
        if result == [0,0]:
            return True
        else:
            return False
                
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().judgeCircle("UD").p()
        Solution().judgeCircle("LL").p()