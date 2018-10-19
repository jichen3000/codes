from __future__ import print_function, division, absolute_import, unicode_literals

import numpy as np

# handle the data from 3d_lasagne test
def _process_data(the_array):
    # all value must be larger than or equal 0
    min_value = np.amin(the_array)
    if min_value < 0:
        raise Exception("all values must be larger than or equal 0")
    the_array -= min_value
    the_array /= np.amax(the_array)
    return the_array

# handle the data from 3d_lasagne test
def _process_data_std(the_array):
    # all value must be larger than or equal 0
    all_data = the_array
    mean = np.mean(all_data)  # mean for data centering
    # notice, this is different with 3d_net
    std = np.std(all_data)  # std for data normalization

    all_data -= mean
    all_data /= std

    # min_value = np.amin(all_data)
    # all_data -= min_value
    # all_data /= np.amax(all_data)
    return all_data


def _process_labels_o(the_array):
    # only support n_class == 2
    # nx = the_array.shape[1]
    # ny = the_array.shape[0]
    the_shape = the_array.shape
    new_shape = list(the_shape[:-1]) + [2]
    new_labels = np.zeros(new_shape, dtype=np.float32)
    # import ipdb; ipdb.set_trace()
    new_labels[..., 1] = the_array[..., 0]
    new_labels[..., 0] = 1-the_array[..., 0]
    return new_labels 

def _process_labels(the_array):
    return the_array

class NumpyDataProvider(object):
    channels = 1
    n_class = 2
    
    def __init__(self, data_array, label_array):
        self.processed_data = _process_data_std(data_array)
        self.processed_labels = _process_labels_o(label_array)
        self.index = 0
        if self.processed_data.shape[0] != self.processed_labels.shape[0]:
            raise Exception("the data and label array must have same count!")
        self.count = self.processed_data.shape[0]
        self.new_indexs = np.arange(self.count)
        # np.random.seed(123)
        # np.random.shuffle(self.new_indexs)
        
    def __call__(self,n):
        self.index += n
        if self.index > self.count:
            raise Exception("index exceed {} the range {}".format(self,index, self.count))
        cur_indexs = self.new_indexs[self.index-n:self.index]
        cur_indexs.p()
        return self.processed_data[cur_indexs], self.processed_labels[cur_indexs]
    # def __call__(self,n):
    #     # np.random.seed(123)
    #         # replace = False, not same
    #     ids = np.random.choice(len(self.processed_data), n, replace=False)
    #     return self.processed_data[ids], self.processed_labels[ids]
   
if __name__ == '__main__':
       from minitest import *
       import os
   
       with test(NumpyDataProvider):
            data_path = "../../../data/colin_unet/3d_lasagne/"
            the_data = np.load(os.path.join(data_path,"data.npy")).astype('float32')
            the_labels = np.load(os.path.join(data_path,"target.npy")).astype('uint8')
            the_labels[the_labels>0]=1


            t_data = np.transpose(the_data, (0,2,3,4,1))
            t_labels = np.transpose(the_labels, (0,2,3,4,1))

            a_labels = _process_labels(t_labels)
            import ipdb;ipdb.set_trace()

            data_provider = NumpyDataProvider(t_data, t_labels)
            x,y = data_provider(4)
            x.shape.p()
            y.shape.p()
            x1,y1 = data_provider(4)
            x1.shape.p()
            y1.shape.p()
            # import ipdb; ipdb.set_trace()
            (x1==x).p()
