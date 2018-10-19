import numpy
import timeit
from minitest import *

# numpy.random.seed(2)
# a = numpy.random.rand(10)
# b = numpy.sort(a)
# c = sorted(a)
# a.p()
# b.p()
# c.p()

partition_timer = timeit.Timer("numpy.partition(a, 10000)",
        "import numpy;numpy.random.seed(2);"+
        "a = numpy.random.rand(10000000)")

print(partition_timer.timeit(10))

sort_timer = timeit.Timer("numpy.sort(a)",
        "import numpy;numpy.random.seed(2);"+
        "a = numpy.random.rand(10000000)")

print(sort_timer.timeit(10))

# sorted_timer = timeit.Timer("sorted(a)",
#         "import numpy;numpy.random.seed(2);"+
#         "a = numpy.random.rand(10000000)")
#
# print(sorted_timer.timeit(10))
