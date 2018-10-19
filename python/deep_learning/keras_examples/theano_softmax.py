from __future__ import print_function
from keras.backend import theano_backend 
from theano import tensor as T
from keras import backend as K




def multi_dims_softmax(x):
    print("in multi_dims_softmax")
    if len(theano_backend.int_shape(x)) > 2:
        origin_shape = theano_backend.shape(x)
        new_shape = (-1,origin_shape[-1])
        reshaped = theano_backend.reshape(x,new_shape)
        reshaped_softmax = T.nnet.softmax(reshaped)
        return theano_backend.reshape(reshaped_softmax,origin_shape)
    else:
        return T.nnet.softmax(x)

setattr(theano_backend, "softmax", multi_dims_softmax)
if K.backend()=="theano":
    setattr(K,"softmax", multi_dims_softmax)

if __name__ == '__main__':
    from minitest import *

    from keras.models import Sequential
    from keras.layers import Activation 
    import numpy as np

    def data_provider(batch_size, input_shape):
        return np.zeros([batch_size]+list(input_shape), dtype=np.float32)

    with test(multi_dims_softmax):
        batch_size = 1
        input_shape = (12, 12, 12, 2)

        x_train = data_provider(batch_size, input_shape)
        x_train = x_train + 1
        print("x_train.shape:{}".format(x_train.shape))

        # theano_backend["softmax"] = multi_dims_softmax

        model = Sequential()
        model.add(Activation(K.softmax,input_shape=input_shape))

        predict_value = model.predict(x_train)
