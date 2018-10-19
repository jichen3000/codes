# pip install git+git://github.com/Theano/Theano.git --upgrade
from __future__ import print_function
import keras
# from keras import backend as K
from keras.layers import Conv3D
from keras.engine import InputSpec
from keras.utils import conv_utils
from keras_contrib import backend as K

class Conv3DTranspose(Conv3D):
    def __init__(self, filters,
                 kernel_size,
                 strides=(1, 1, 1),
                 padding='valid',
                 data_format=None,
                 activation=None,
                 use_bias=True,
                 kernel_initializer='glorot_uniform',
                 bias_initializer='zeros',
                 kernel_regularizer=None,
                 bias_regularizer=None,
                 activity_regularizer=None,
                 kernel_constraint=None,
                 bias_constraint=None,
                 **kwargs):
        super(Conv3DTranspose, self).__init__(
            filters,
            kernel_size,
            strides=strides,
            padding=padding,
            data_format=data_format,
            activation=activation,
            use_bias=use_bias,
            kernel_initializer=kernel_initializer,
            bias_initializer=bias_initializer,
            kernel_regularizer=kernel_regularizer,
            bias_regularizer=bias_regularizer,
            activity_regularizer=activity_regularizer,
            kernel_constraint=kernel_constraint,
            bias_constraint=bias_constraint,
            **kwargs)
        self.input_spec = InputSpec(ndim=5)

    def call(self, inputs):
        # print("in call")
        kernel_shape = K.get_value(self.kernel).shape
        input_shape = K.shape(inputs)
        output_shape = self.compute_output_shape(input_shape)
        output_shape = [None]+list(output_shape[1:])
        print("output_shape:{}".format(output_shape))
        print("kernel_shape:{}".format(kernel_shape))
        outputs = K.deconv3d(inputs, self.kernel, output_shape,
                            strides=self.strides,
                            padding=self.padding,
                            data_format=self.data_format,
                            filter_shape=kernel_shape)
        if self.bias:
            outputs = K.bias_add(
                outputs,
                self.bias,
                data_format=self.data_format)
        if self.activation is not None:
            return self.activation(outputs)
        return outputs

    def compute_output_shape(self, input_shape):
        if self.data_format == 'channels_first':
            h_axis, w_axis, d_axis = 2, 3, 4
        else:
            h_axis, w_axis, d_axis = 1, 2, 3

        height, width, depth = input_shape[h_axis], input_shape[w_axis], input_shape[d_axis]
        kernel_h, kernel_w, kernel_d = self.kernel_size
        stride_h, stride_w, stride_d = self.strides

        batch_size = input_shape[0]
        # Infer the dynamic output shape:
        out_height = conv_utils.deconv_length(
                height, stride_h, kernel_h, self.padding)
        out_width = conv_utils.deconv_length(
                width, stride_w, kernel_w, self.padding)
        out_depth = conv_utils.deconv_length(
                depth, stride_d, kernel_d, self.padding)
        if self.data_format == 'channels_first':
            output_shape = (batch_size, self.filters, out_height, out_width, out_depth)
        else:
            output_shape = (batch_size, out_height, out_width, out_depth, self.filters)
        # print("in compute_output_shape")
        # print("output_shape:{}".format(output_shape))
        return output_shape

    def get_config(self):
        config = super(Conv3DTranspose, self).get_config()
        config.pop('dilation_rate')
        return config

if __name__ == '__main__':
    from keras.models import Sequential
    import numpy as np
    from minitest import *

    def data_provider(batch_size, input_shape):
        return np.zeros([batch_size]+list(input_shape)+[1], dtype=np.float32)

    with test(Conv3DTranspose):
        input_shape = (12, 12, 12)
        kernel_size = (3, 3, 3)
        pool_size=(2, 2, 2)
        batch_size = 2
        features = 4

        x_train = data_provider(batch_size, input_shape)
        x_train = x_train + 1
        np.unique(x_train, return_counts=True)

        output_shape = [None] +  [i*2 for i in input_shape] + [features]
        model = Sequential()
        model.add(Conv3DTranspose(features, kernel_size,
                strides=pool_size, padding='same', activation='relu',input_shape=x_train.shape[1:]))

        predict_value = model.predict(x_train)
        print(predict_value.shape)
        print(np.unique(predict_value[...,0], return_counts=True))


