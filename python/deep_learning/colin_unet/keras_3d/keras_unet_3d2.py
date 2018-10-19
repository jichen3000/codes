# not just keras
# https://github.com/farizrahman4u/keras-contrib
# sudo pip install git+https://www.github.com/farizrahman4u/keras-contrib.git

from __future__ import print_function
from __future__ import absolute_import
import keras
from keras.models import Model
from keras.layers import Input, Dropout, Conv3D, MaxPooling3D
from keras.layers import Activation, Reshape 

from keras.layers import Concatenate, concatenate
from keras import backend as K
from keras.layers.convolutional import Conv3D

import sys
import os
# sys.path.append("..")

# from keras_contrib.layers import Deconvolution3D as Conv3DTranspose
from conv_3d_transpose import Conv3DTranspose
import theano_multi_dims_softmax

import numpy as np

import minitest

%load_ext autoreload
%autoreload 2

# keras.backend.backend()

def build_3d_unet(input_shape, class_count, layer_count=3, features_root=16):    
    # class_count = 2
    # layer_count = 3
    # features_root=16
    # input_shape = (128, 128, 128, 1)
    kernel_size = (3, 3, 3)
    pool_size=(2, 2, 2)


    cur_layer = Input(shape=input_shape)
    the_net = {"input":cur_layer}

    
    # down, layer = 0, 1, 2
    down_layers = {}
    for layer in range(0, layer_count):
        features = features_root * (2**layer)
        cur_layer = Conv3D(features, kernel_size=kernel_size,
                padding='same', activation='relu')(cur_layer)
        cur_layer = Conv3D(features * 2, kernel_size=kernel_size,
                padding='same', activation='relu')(cur_layer)
        down_layers[layer] = cur_layer
        if layer < layer_count-1:
            cur_layer = MaxPooling3D(pool_size=pool_size)(cur_layer)

    # up, layer = 1, 0
    for layer in range(layer_count-2, -1, -1):
        features = features_root * (2**layer)

        cur_layer = Conv3DTranspose(features * 4, kernel_size,
                strides=pool_size, padding='same', activation='relu')(cur_layer)
        cur_layer = concatenate([down_layers[layer], cur_layer])

        cur_layer = Conv3D(features * 2, kernel_size=kernel_size,
                padding='same', activation='relu')(cur_layer)
        cur_layer = Conv3D(features * 2, kernel_size=kernel_size,
                padding='same', activation='relu')(cur_layer)

    cur_layer = Conv3D(class_count, kernel_size=kernel_size,
            padding='same', activation='relu')(cur_layer)
    the_net["predict"] = cur_layer

    cur_layer = Activation(K.softmax)(cur_layer)
    the_net["train"] = cur_layer

    return the_net

def get_data_set():
    CUR_DIR = os.getcwd()
    # data_path = CUR_DIR.replace("work","data")
    data_path = "/home/jichen3000/data/colin_unet/3d_lasagne/"
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

train_data, train_labels, valid_data, valid_labels = get_data_set()
train_data = np.transpose(train_data, (0,2,3,4,1))
train_labels = np.transpose(train_labels, (0,2,3,4,1))

x_test = train_data[0:4]
y_test = _process_labels_o(train_labels[0:4])
x_train = train_data[10:20]
y_train = _process_labels_o(train_labels[10:20])
x_predict = train_data[100:101]
y_predict = _process_labels_o(train_labels[100:101])

def main():
    # data_path = "../../../data/colin_unet/3d_lasagne/"
    # # the_data = np.load(os.path.join(data_path,"data.npy")).astype('float32')
    # # the_labels = np.load(os.path.join(data_path,"target.npy")).astype('uint8')
    # # the_labels[the_labels>0]=1
    # # t_data = np.transpose(the_data, (0,2,3,4,1))
    # # t_labels = np.transpose(the_labels, (0,2,3,4,1))
    # t_data = np.load(os.path.join(data_path,"data_tf.npy")).astype('float32')
    # t_labels = np.load(os.path.join(data_path,"labels_tf.npy")).astype('float32')
    # data_provider = NumpyDataProvider(t_data, t_labels)
    # x_test, y_test = data_provider(4)

    class_count = 2
    layer_count = 3
    features_root=16
    # input_shape = x_test.shape[1:]
    input_shape = (128, 128, 128, 1)
    net = build_3d_unet(input_shape, class_count, layer_count, features_root)

    model = Model(inputs=net["input"], outputs=net["train"])

    model.compile(loss=keras.losses.categorical_crossentropy,
                  optimizer=keras.optimizers.Adadelta(),
                  metrics=['accuracy'])

    # x_train, y_train = data_provider(10)
    batch_size = 1
    epochs = 1
    model.fit(x_train, y_train,
              batch_size=batch_size,
              epochs=epochs,
              verbose=1,
              validation_data=(x_test, y_test))


    # x_predict, y_predict = data_provider(1)
    # predict_model = Model(inputs=net["input"], outputs=net["train"])
    predict_value = model.predict(x_predict)

    np.unique(predict_value[...,0], return_counts=True)
    np.sum(predict_value[...,0]<=0.5)

# Train on 10 samples, validate on 4 samples
# Epoch 1/1
# 10/10 [==============================] - 122s - loss: 0.2508 - acc: 0.9214 - val_loss: 0.0615 - val_acc: 0.9852
# Out[5]: <keras.callbacks.History at 0x7f5dad3fba50>

# In [6]:     predict_value = model.predict(x_predict)
#    ...: 

# In [7]: np.unique(predict_value[...,0], return_counts=True)
# Out[7]: 
# (array([ 0.30468601,  0.3049407 ,  0.30699229, ...,  0.99999976,
#          0.99999988,  1.        ], dtype=float32),
#  array([    1,     1,     1, ..., 19667,  7104,  1015]))

# In [8]: np.sum(predict_value[...,0]>0.5)
# Out[8]: 2096693

# In [9]: np.sum(predict_value[...,0]<=0.5)
# Out[9]: 459
