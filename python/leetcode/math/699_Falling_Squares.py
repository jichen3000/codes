class Solution(object):
    # has issue
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        from bisect import bisect_left, bisect_right
        heights = []
        res = []
        for left, size in positions:
            right = left + size - 1
            li = bisect_right(heights, left)
            ri = bisect_left(heights, right)
            left_part = heights[:li]
            right_part = heights[ri:]
            if left_part:
                if left_part[-1][0] == left:
                    left_part[-1] = [left, max(right, left_part[-1][1]), left_part[-1][2] + size]
                elif left_part[-1][0] < left and left <= left_part[-1][1]:
                    left_part[-1][1] = left - 1
                    left_part += [left, right, left_part[-1][2] + size],
                elif left_part[-1][1] < left:
                    left_part += [left, right, size],
            else:
                left_part += [left, right, size],
            if right_part:
                if right_part[0][0] == right:
                    left_part[-1][2] = max(left_part[-1][2], right_part[0][2]+size)
                    if right_part[0][1] == right_part[0][2]:
                        right_part.pop(0)
                    else:
                        right_part[0][0] = right - 1
            res += left_part[-1][2],
            heights = left_part + right_part
        return res    
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        heights = []
        height_mem = {}
        max_h = 0
        for left, side_l in positions:
            height = max(height_mem[x] if x in height_mem else 0
                        for x in range(left, left+side_l))
            height += side_l
            max_h = max(max_h, height)
            for x in range(left, left+side_l):
                height_mem[x] = height
            heights += max_h,
        return heights
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        n = len(positions)
        heights = []
        height_mem = {}
        max_h = 0
        def is_cover(left_i, right_i, left_j, right_j):
            if left_j <= right_i and right_i <= right_j:
                return True
            if left_j <= left_i and left_i <= right_j:
                return True
            if left_i <= left_j and right_j <= right_i:
                return True
            if left_j <= left_i and right_i <= right_j:
                return True
            return False
        for i in range(n):
            left_i, l_i = positions[i]
            right_i = left_i + l_i -1
            cur_h = 0
            for j in range(i-1, -1, -1):
                left_j, l_j = positions[j]
                right_j = left_j + l_j -1
                # (left_i, right_i, left_j, right_j).p()
                # is_cover(left_i, right_i, left_j, right_j).p()
                if is_cover(left_i, right_i, left_j, right_j) :
                    cur_h = max(cur_h, height_mem[(left_j, right_j)])
            cur_h += l_i
            # height_mem.p()
            # (left_i, l_i, cur_h).p()
            height_mem[(left_i, right_i)] = cur_h
            max_h = max(max_h, cur_h)
            heights += max_h,
        return heights

class Solution:
    '''
        just like the above one, but more simplized
        in python, there is not treemap, which
        get, containskey, next are all
        O(log n), datastruct using Red-black tree
    '''
    def fallingSquares(self, ps):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        def is_covered(p0, p1):
            if p0[0] > p1[0]:
                p0, p1 = p1, p0
            return p0[0]+p0[1]-1 >= p1[0]
        mem, res = {}, []
        for i in range(len(ps)):
            left, size = ps[i]
            cur_max = 0
            key = tuple(ps[i])
            for j in range(i-1, -1, -1):
                if is_covered(ps[j], ps[i]):
                    # print(ps[j], ps[i], mem)
                    cur_max = max(cur_max, mem[tuple(ps[j])])
            cur_max += size
            res += max(cur_max, res[-1] if res else 0),
            mem[tuple(ps[i])] = cur_max
            # print(mem)
        return res
        
class Solution:
    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        pre_list = []
        res = []
        max_h = 0
        for l, size in positions:
            r = l + size
            h = 0
            for pl, pr, ph in pre_list:
                # has intersection
                if not (r <= pl or l >= pr):
                    h = max(h, ph)
            h += size
            max_h = max(max_h, h)
            res += max_h,
            pre_list += (l, r, h),
        return res

if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().fallingSquares([[1,2],[2,3],[6,1]]).must_equal([2,5,5])
        Solution().fallingSquares([[6,1],[9,2],[2,4]]).must_equal([1,2,4])
