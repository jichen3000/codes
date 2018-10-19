from __future__ import print_function
import keras
from keras.models import Sequential
from keras_contrib.layers import Deconvolution3D as Conv3DTranspose
from keras import backend as K
import numpy as np


def data_provider(batch_size, input_shape):
    return np.zeros([batch_size]+list(input_shape)+[1], dtype=np.float32)

def main():

    # x_train, y_train = data_provider(10)

    input_shape = (24, 24, 24)
    kernel_size = (3, 3, 3)
    pool_size=(2, 2, 2)
    batch_size = 2
    features = 4

    x_train = data_provider(batch_size, input_shape)
    x_train = x_train + 1
    np.unique(x_train, return_counts=True)

    output_shape = [None] +  [i*2 for i in input_shape] + [features]
    model = Sequential()
    model.add(Conv3DTranspose(features, kernel_size, output_shape=output_shape,
            strides=pool_size, padding='same', activation='relu',input_shape=x_train.shape[1:]))

    predict_value = model.predict(x_train)
