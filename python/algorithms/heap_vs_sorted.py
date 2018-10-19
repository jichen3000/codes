import heapq
import numpy
import sortedcontainers

def heap_one(the_array):
    the_heap = []
    for i in the_array:
        heapq.heappush(the_heap,i)
    return [heapq.heappop(the_heap) for i in range(10)]

def sourted_list_one(the_array):
    the_list = sortedcontainers.SortedList()
    for i in the_array:
        the_list.add(i)
    return [the_list.pop() for i in range(10)]


if __name__ == '__main__':
    from minitest import *

    numpy.random.seed(2)
    the_array = numpy.random.rand(10)
    with test(heap_one):
        heap_one(the_array).pp()

    with test(sourted_list_one):
        sourted_list_one(the_array).pp()
