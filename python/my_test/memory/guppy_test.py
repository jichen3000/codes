# it seems not work for numpy
# this is why http://stackoverflow.com/questions/6018986/memory-profiler-for-numpy
from guppy import hpy
h = hpy()
print h.heap()
