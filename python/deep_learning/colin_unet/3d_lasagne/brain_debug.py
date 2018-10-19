## wget https://www.dropbox.com/s/h4no2pm970im82k/data.npy
## wget https://www.dropbox.com/s/2vjan6mbcf2fsit/target.npy
import os 
import minitest
import numpy as np
import lasagne
import theano.tensor as T
import theano
from sklearn.metrics import roc_auc_score
import time

import Unet

%load_ext autoreload
%autoreload 2

def get_data_set():
    CUR_DIR = os.getcwd()
    data_path = CUR_DIR.replace("work","data")
    data_path.p()

    origin_data = np.load(os.path.join(data_path,"data.npy")).astype('float32')
    origin_labels = np.load(os.path.join(data_path,"target.npy")).astype('uint8')

    all_labels = origin_labels
    all_labels[all_labels>0]=1

    all_data = origin_data
    mean = np.mean(all_data)  # mean for data centering
    # notice, this is different with 3d_net
    std = np.std(all_data)  # std for data normalization

    all_data -= mean
    all_data /= std

    return all_data[0:200], all_labels[0:200], all_data[200:], all_labels[200:]

train_data, train_labels, valid_data, valid_labels = get_data_set()

BATCH_SIZE = 1
PATCH_SIZE = 128
net = Unet.build_UNet(n_input_channels=1, BATCH_SIZE=BATCH_SIZE, num_output_classes=2, pad='same',
         nonlinearity=lasagne.nonlinearities.elu, input_dim=(PATCH_SIZE, PATCH_SIZE),depth=128,
         base_n_filters=24,kernel_size=3, do_dropout=True)

#Point network's output layer to output_layer_for_loss parameter parameter for later use
output_layer_for_loss = net["output_flattened"]


print "Started experiment"

def batch_generator(data, target, BATCH_SIZE, shuffle=False):
    if shuffle:
        np.random.seed(123)
        while True:
            ids = np.random.choice(len(data), BATCH_SIZE)
            yield data[ids], target[ids]
    else:
        for idx in range(0, len(data), BATCH_SIZE):
            ids = slice(idx, idx + BATCH_SIZE)
            yield data[ids], target[ids]

x_sym = T.TensorType('float32',(False,)*5) ('inputs') #Input tensor (i.e. images)
seg_output = lasagne.layers.get_output(net["output_segmentation"], x_sym, deterministic=True)
get_segmentation = theano.function([x_sym], seg_output)

train_generator = batch_generator(train_data, train_labels, BATCH_SIZE, shuffle=False)


data, label = train_generator.next()
seg_output_value = get_segmentation(data.astype(np.float32))
np.unique(seg_output_value, return_counts=True)
