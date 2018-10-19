# http://stackoverflow.com/questions/33140000/how-to-feed-caffe-multi-label-data-in-hdf5-format

import h5py, os
import numpy as np

def write_to_file(file_name):
    f = h5py.File(file_name, 'w')
    count = 3
    # 1200 data, each is a 128-dim vector
    f.create_dataset('data', (count, 4, 5, 5), dtype='f')
    # Data's labels, each is a 4-dim vector
    f.create_dataset('label', (count, ), dtype='i')

    # Fill in something with fixed pattern
    # Regularize values to between 0 and 1, or SigmoidCrossEntropyLoss will not work
    for i in range(count):
        f['data'][i] = np.random.random((4,5,5))
        f['label'][i] = i % 2

    f.close()

if __name__ == '__main__':
    write_to_file("train.h5")