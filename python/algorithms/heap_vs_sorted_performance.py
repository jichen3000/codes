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

import timeit
numpy.random.seed(2)
the_array = numpy.random.rand(1e7)

heap_timer = timeit.Timer(lambda: heap_one(the_array))
print "heap_timer:"
print heap_timer.timeit(number=1)

sourted_timer = timeit.Timer(lambda: sourted_list_one(the_array))
print "sourted_timer:"
print sourted_timer.timeit(number=1)

# numpy.random.seed(2)
# the_array = numpy.random.rand(1e7)
# heap_timer:
# 7.02763104439
# sourted_timer:
# 94.38331604
