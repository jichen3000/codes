import math
from operator import methodcaller
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return 'Point({!r:},{!r:})'.format(self.x, self.y)
    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)
    def __eq__(self,other):
        return repr(self) == repr(other)

if __name__ == '__main__':
    from minitest import *

    with test("getattr"):
        p = Point(2,3)
        getattr(p, 'distance')(0,0).must_equal(3.605551275463989)
    
    with test(methodcaller):
        p = Point(2,3)
        methodcaller("distance", 0,0)(p).must_equal(3.605551275463989)
        points = [
            Point(1, 2),
            Point(3, 0),
            Point(10, -3),
            Point(-5, -7),
            Point(-1, 8),
            Point(3, 2)
        ]
        points.sort(key=methodcaller("distance", 0,0))
        points.must_equal(
            [Point(1,2), Point(3,0), Point(3,2), Point(-1,8), 
            Point(-5,-7), Point(10,-3)])
