class Solution:
    def isNStraightHand(self, hand, w):
        """
        :type hand: List[int]
        :type W: int
        :rtype: bool
        """
        if len(hand) % w != 0:
            return False
        m = len(hand) // w
        hand.sort()
        mem = []
        group_num = 0
        for v in hand:
            for first, cur_set in mem:
                if v - first < w and v not in cur_set:
                    cur_set.add(v)
                    break
            else:
                if group_num < m:
                    mem += [v, {v}],
                    group_num += 1
                else:
                    return False
            if len(mem[0][1]) == w:
                mem.pop(0)
            # (v, mem).p()
        return True
        

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().isNStraightHand([1,2,3,6,2,3,4,7,8],3).must_equal(True)
        Solution().isNStraightHand([1,2,3,5],2).must_equal(False)
        Solution().isNStraightHand([1,2,3,4,5,6],2).must_equal(True)
        Solution().isNStraightHand([5,1],1).must_equal(True)
        Solution().isNStraightHand([1,1,2,2,3,3],2).must_equal(False)
