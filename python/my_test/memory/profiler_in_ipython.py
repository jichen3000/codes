# http://stackoverflow.com/questions/3372444/profile-memory-allocation-in-python-with-support-for-numpy-arrays
import numpy

%memit numpy.zeros(1e7)

for i in range(10):
    %memit numpy.zeros(1e7)
