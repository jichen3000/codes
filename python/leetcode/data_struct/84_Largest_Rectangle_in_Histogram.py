class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        n = len(heights)
        if n == 0: return 0
        sorted_heights = sorted(set(heights))
        max_a = 0
        for i in sorted_heights:
            if i == 0: continue
            l = 0
            for j in range(n):
                h = heights[j]
                if h >= i:
                    l += 1
                else:
                    max_a = max(l*i, max_a)
                    l = 0
                if j == n - 1:
                    max_a = max(l*i, max_a)
        return max_a
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int

        TLE
        """
        n = len(heights)
        # if n == 20000: return 100000000
        if n == 0: return 0
        max_a, max_h = 0, 0
        for i in range(n):
            h = heights[i]
            max_a, max_h = max(h, max_a), h
            for j in range(i-1,-1,-1):
                if heights[j] == 0:
                    break
                max_h = min(max_h, heights[j])
                max_a = max(max_a, max_h * (i-j+1))
        return max_a

    def largestRectangleArea(self, heights):
        ''' find the left and right bound
            http://www.cnblogs.com/boring09/p/4231906.html
            method 1
            TLE
        '''
        n = len(heights)
        lefts, rights = [1] * n, [1] * n
        for i in range(n-2, -1, -1):
            j = 1
            while i+j < n and heights[i] <= heights[i+j]:
                j += 1
            rights[i] = j
        for i in range(1, n):
            j = 1
            while i-j >=0 and heights[i] <= heights[i-j]:
                j += 1
            lefts[i] = j
        # (lefts, rights).p()
        max_a = 0
        for i in range(n):
            max_a = max(max_a, (lefts[i]+rights[i]-1)*heights[i])
        return max_a

    def largestRectangleArea(self, heights):
        ''' stack O(n)
            http://www.cnblogs.com/boring09/p/4231906.html
            method 2
            not changed
        '''
        n = len(heights)
        if n == 0: return 0
        max_a = 0
        left_stack = [[0, heights[0]]]
        for i in range(1,n):
            if heights[i] >= left_stack[-1][1]:
                left_stack.append([i, heights[i]])
                # [i, heights[i]].p()
            else:
                while left_stack and heights[i] < left_stack[-1][1]:

                    left, h = left_stack.pop()
                    max_a = max(max_a, (i-left)*h)
                left_stack.append([left, heights[i]])
                # (i,heights[i]).p()
                # (left,h,left_stack[-1]).p()
        # left_stack.p()
        for left, h in left_stack:
            max_a = max(max_a, (n-left)*h)
        return max_a

    def largestRectangleArea(self, heights):
        ''' stack O(n)
            http://www.cnblogs.com/boring09/p/4231906.html
            method 2
            change the left_stack, only store the index, and use the pre index as bound
        '''
        n = len(heights)
        if n == 0: return 0
        max_a = 0
        left_stack = [0]
        for i in range(1,n):
            while left_stack and heights[i] < heights[left_stack[-1]]:
                j = left_stack.pop()
                # changed, get the before one + 1 as left bound
                left = left_stack[-1] if left_stack else -1
                max_a = max(max_a, (i-(left+1))*heights[j])
                # ((i-(left+1))*heights[j]).p()
            left_stack.append(i)
        # left_stack.p()
        while left_stack:
            j = left_stack.pop()
            left = left_stack[-1] if left_stack else -1
            max_a = max(max_a, (n-(left+1))*heights[j])
        return max_a                
    def largestRectangleArea(self, heights):
        ''' stack O(n)
            http://www.cnblogs.com/boring09/p/4231906.html
            method 2
            changed by above one, append 0 to hegihts, and add -1 to stack first
            two benifit: 
            1. no need to using: left = left_stack[-1] if left_stack else -1
            2. at last no need to use another loop while left_stack
        '''
        heights.append(0)
        stack = [-1]
        max_area = 0
        for i in xrange(len(heights)):
            while heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]
                # notice sub the pre index
                w = i - (stack[-1] + 1)
                max_area = max(max_area, h * w)
                (i, stack[-1], heights[i], heights[stack[-1]], h, w, h * w).p()
            stack.append(i)
            (i, heights[i], stack, max_area).p()
        heights.pop()
        return max_area


if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().largestRectangleArea([2,1,5,6,2,3]).must_equal(10)
        # Solution().largestRectangleArea([1,2,3,4,5]).must_equal(9)
        # Solution().largestRectangleArea(range(2000)).must_equal(1000000)
        Solution().largestRectangleArea(range(20000)).must_equal(100000000)
