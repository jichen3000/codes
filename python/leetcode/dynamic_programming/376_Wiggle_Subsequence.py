class Solution(object):
    # 39 mins
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def sign(v):
            if v == 0:
                return 0
            return v/abs(v)
        if nums == None:
            return 0
        n = len(nums)
        if n <= 1:
            return n
        max_len = 1
        pre_sign = 0
        # choose the first which not equal to the pre
        for j in xrange(1,n):
            pre_sign = sign(nums[j]-nums[j-1])
            if pre_sign != 0:
                max_len = 2
                pre_index = j
                break
        for i in xrange(j+1,n):
            # cannot just choose the last one, but need to loop
            for k in xrange(pre_index, i):
                cur_sign = sign(nums[i]-nums[k])
                if cur_sign != pre_sign and cur_sign != 0:
                    max_len += 1
                    pre_index = i
                    pre_sign = cur_sign
                    break
        return max_len
        
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().wiggleMaxLength([0,0]).must_equal(1)
        Solution().wiggleMaxLength([0,0,0]).must_equal(1)
        Solution().wiggleMaxLength([12,64,50,41,39,35,40]).must_equal(4)


