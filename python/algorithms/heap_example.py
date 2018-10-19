import heapq

if __name__ == '__main__':
    from minitest import *

    with test("simpe int array"):
        a = []
        heapq.heappush(a, 8)
        heapq.heappush(a, 7)
        a.must_equal([7,8])
        heapq.heappush(a, 9)
        a.must_equal([7,8,9])
        heapq.heappop(a).must_equal(7)
        a.must_equal([8,9])

    with test("tuple"):
        a = []
        heapq.heappush(a, (8,"f"))
        heapq.heappush(a, (7,"s"))
        a.must_equal([(7, 's'), (8, 'f')])

    with test("max heap"):
        a = []
        listForTree = range(5)
        heapq.heapify(listForTree).p()
        listForTree.p()
        heapq._heapify_max(listForTree).p()
        listForTree.p()
