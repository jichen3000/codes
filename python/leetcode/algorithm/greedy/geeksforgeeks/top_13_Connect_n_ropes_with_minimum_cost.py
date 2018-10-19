from Queue import PriorityQueue
def solve(ropes):
    if len(ropes) <= 1: return 0
    min_heap = PriorityQueue()
    for i in ropes:
        min_heap.put(i)
    total = 0
    while min_heap.qsize() > 1:
        cost = min_heap.get() + min_heap.get()
        total += cost
        min_heap.put(cost)
    return total

if __name__ == '__main__':
    from minitest import *

    with test(solve):
        solve([4,3,2,6]).must_equal(29)

