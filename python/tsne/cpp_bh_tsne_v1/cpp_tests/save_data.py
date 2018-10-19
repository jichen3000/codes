import os
import numpy
import struct

def save_maxtrix():
    samples = numpy.arange(10,dtype='float64').reshape(5,2)
    with open(os.path.join(".", 'data.dat'), 'wb') as data_file:
        # Then write the data
        for sample in samples:
            data_file.write(struct.pack('{}d'.format(len(sample)), *sample))

save_maxtrix()
