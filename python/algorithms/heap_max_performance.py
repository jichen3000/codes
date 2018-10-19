import heapq
import numpy
import sortedcontainers

def heap_min_one(the_array):
    the_heap = []
    index = 0
    for i in the_array:
        heapq.heappush(the_heap,(i,index))
        index += 1
    return [heapq.heappop(the_heap) for i in range(len(the_array))]

def heap_max_one(the_array):
    the_heap = []
    index = 0
    for i in the_array:
        heapq.heappush(the_heap,(-i,index))
        index += 1
    result = []
    for i in range(len(the_array)):
        item = heapq.heappop(the_heap)
        result.append((-item[0],item[1]))
    return result

import timeit
numpy.random.seed(2)
the_array = numpy.random.rand(1e6)

heap_max_timer = timeit.Timer(lambda: heap_max_one(the_array))
print "heap_max_timer:"
print heap_max_timer.timeit(number=1)

heap_min_timer = timeit.Timer(lambda: heap_min_one(the_array))
print "heap_min_timer:"
print heap_min_timer.timeit(number=1)
