class Solution:
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type H: int
        :rtype: int
        """
        def diff(value):
            return sum(math.ceil(v/value) for v in piles) <= h
        sum_v = sum(piles)
        l = math.ceil(sum_v / h)
        r = max(piles)+1
        while l < r:
            m = (l+r)//2
            v = diff(m)
            # print(m,v)
            if v:
                r = m
            else:
                l = m + 1
        return l
            
        