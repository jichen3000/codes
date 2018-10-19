# http://stackoverflow.com/questions/33140000/how-to-feed-caffe-multi-label-data-in-hdf5-format

import h5py, os
import numpy as np

def read_to_file(file_name):
    f = h5py.File(file_name)
    print(f.keys())
    print("data len:",f['data'].len())
    print("data label:",f['label'].len())

    print(f['data'][0])
    for i in f['label']:
        print(i)


if __name__ == "__main__":
    file_name = "train.h5"
    read_to_file(file_name)
