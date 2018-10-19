class Solution:
    def asteroidCollision(self, a):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        q = []
        for i in range(len(a)):
            if a[i] < 0:
                finished = False
                while q and q[-1] > 0:
                    if q[-1] > -a[i]:
                        finished = True
                        break
                    elif q[-1] == -a[i]:
                        q.pop()
                        finished = True
                        break
                    else:
                        q.pop()
                if not finished:
                    q += a[i],
            else:
                q += a[i],
        return q
        
if __name__ == '__main__':
    from minitest import *

    with test(Solution):
        Solution().asteroidCollision([8,-8]).must_equal([])
        Solution().asteroidCollision([10,2,-5]).must_equal([10])
        Solution().asteroidCollision([-2, -1, 1, 2]).must_equal([-2, -1, 1, 2])