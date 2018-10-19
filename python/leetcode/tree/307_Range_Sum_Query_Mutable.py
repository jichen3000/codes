# binary indexed tree
# http://www.hawstein.com/posts/binary-indexed-trees.html
# with original nums
class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        # self.nums = nums
        n = len(nums)
        self.bit = [0] * (n+1)
        for i in range(1, n+1):
            self._update(i, nums[i-1])
        # print self.bit
    
    def _update(self, i, diff):
        index = i
        while index < len(self.bit):
            self.bit[index] += diff
            index += index & (-index)
    
    def _get_sum(self, i):
        index = i
        res = 0
        while index > 0:
            res += self.bit[index]
            index -= index&(-index)
        return res

    def _read_origin(self, i):
        index = i
        # index.p()
        res = self.bit[index]
        if index > 0:
            end_i = index - (index & (-index))
            (end_i,index).p()
            index -= 1
            while index != end_i:
                index.p()
                res -= self.bit[index]
                index -= index & -index
        return res
    
        

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self._read_origin(i+1)
        self._update(i+1, diff)
        # self.nums[i] = val
            
        

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self._get_sum(j+1) - self._get_sum(i)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

if __name__ == '__main__':
    from minitest import *

    with test("Solution"):
        # obj = NumArray([1,3,5])
        # obj.sumRange(0,2).must_equal(9)
        # obj.update(1,2)
        # obj.sumRange(0,2).must_equal(8)

        obj = NumArray([1]*8)
        obj.bit.p()
        obj._read_origin(5).p()
        obj._read_origin(6).p()