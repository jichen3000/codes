class Solution:
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """
        h, m = time.split(":")
        nums = list(set(map(int, h+m)))
        nums.sort()
        n = len(nums)
        nexts = {str(nums[i]):(nums[i+1] if i+1<n else None) for i in range(n)}
        # print(nexts,m[1])
        if nexts[m[1]] != None:
            m = m[0] + str(nexts[m[1]])
            return "{}:{}".format(h, m)
        else:
            m = m[0] + str(nums[0])
        if nexts[m[0]] != None and int(str(nexts[m[0]])+m[1]) <= 59:
            m = str(nexts[m[0]]) + m[1]
            return "{}:{}".format(h, m)
        else:
            m = str(nums[0]) + m[1]
        if nexts[h[1]] != None and int(h[0]+str(nexts[h[1]])) < 24:
            h = h[0] + str(nexts[h[1]])
            return "{}:{}".format(h, m)
        else:
            h = h[0] + str(nums[0])
        if nexts[h[0]] != None and int(str(nexts[h[0]])+h[1]) < 24:
            h = str(nexts[h[0]]) + h[1]
            return "{}:{}".format(h, m)
        else:
            h = str(nums[0]) + h[1]
            return "{}:{}".format(h, m)
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().nextClosestTime("22:26").must_equal("22:22")