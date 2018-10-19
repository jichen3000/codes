
from __future__ import division, print_function
import sys
import os
from collections import OrderedDict
import logging
import shutil

import numpy as np
import tensorflow as tf
# import minitest

sys.path.append("..")
# from tf_unet import util

# tf.nn.conv3d [batch, in_depth, in_height, in_width, in_channels]
# https://www.tensorflow.org/api_docs/python/tf/nn/conv3d
# 2d w [filter_height, filter_width, in_channels, out_channels]
# 3d w [filter_depth, filter_height, filter_width, in_channels, out_channels]

# lasagne.layers.dnn.Conv3DDNNLayer 
# (batch_size, num_input_channels, input_depth, input_rows, input_columns)
# http://lasagne.readthedocs.io/en/latest/modules/layers/dnn.html
# 2d w (num_filters, num_input_channels, filter_rows, filter_columns)
# 3d w (num_filters, num_input_channels, filter_depth, filter_rows, filter_columns)

def crop_and_concat3d(x1,x2):
    x1_shape = tf.shape(x1)
    x2_shape = tf.shape(x2)
    # offsets for the top left corner of the crop
    offsets = [0, (x1_shape[1] - x2_shape[1]) // 2, 
            (x1_shape[2] - x2_shape[2]) // 2, 
            (x1_shape[3] - x2_shape[3]) // 2, 0]
    size = [-1, x2_shape[1], x2_shape[2], x2_shape[3], -1]
    x1_crop = tf.slice(x1, offsets, size)
    # change for tf 1.0
    # return tf.concat(3, [x1_crop, x2])
    return tf.concat([x1_crop, x2], 4)

def create_3d_unet(channels, n_class, **kwargs):
    features_root = kwargs.get("features_root", 32)
    layers = kwargs.get("layers", 4)
    filter_size = kwargs.get("filter_size", 3)
    pool_size = kwargs.get("pool_size", 2)
    summaries = kwargs.get("summaries", True)

    # Remove nodes from graph or reset entire default graph
    tf.reset_default_graph()

    x = tf.placeholder(tf.float32, name="x-input",
            shape=[None, None, None, None, channels])
    y = tf.placeholder(tf.float32, name="y-input",
            shape=[None, None, None, None, n_class])

    keep_prob = tf.placeholder(tf.float32)


    in_node = tf.reshape(x, tf.stack(
            [-1,tf.shape(x)[1],tf.shape(x)[2],tf.shape(x)[3],channels]))
    batch_size = tf.shape(in_node)[0]
 
    weights = []
    biases = []
    # convs = []
    # pools = OrderedDict()
    # deconv = OrderedDict()
    dw_h_convs = OrderedDict()
    up_h_convs = OrderedDict()

    features = features_root

    # in_node = tf.contrib.layers.batch_norm(in_node, center=True, scale=True)
    # down layers
    for layer in range(0, layers):
        stddev = np.sqrt(2 / (filter_size**2 * features))
        # layer.p()
            
        if layer == 0:
            w1 = tf.Variable(tf.truncated_normal([filter_size, filter_size, 
                    filter_size, channels, features], stddev=stddev))
        else:
            w1 = tf.Variable(tf.truncated_normal([filter_size, filter_size, 
                    filter_size, features, features], stddev=stddev))
        b1 = tf.Variable(tf.constant(0.1, shape=[features]))

        conv1 = tf.nn.conv3d(in_node, w1, strides=[1, 1, 1, 1, 1], padding='SAME')
        # in the paper, it didn't mention the dropout
        conv1_dropout = tf.nn.dropout(conv1, keep_prob)
        tmp_h_conv = tf.nn.relu(conv1_dropout + b1)

        features = features*2
        w2 = tf.Variable(tf.truncated_normal([filter_size, filter_size, 
                filter_size, features//2, features], stddev=stddev))
        b2 = tf.Variable(tf.constant(0.1, shape=[features]))
        
        conv2 = tf.nn.conv3d(tmp_h_conv, w2, strides=[1, 1, 1, 1, 1], padding='SAME')
        conv2_dropout = tf.nn.dropout(conv2, keep_prob)
        dw_h_convs[layer] = tf.nn.relu(conv2_dropout + b2)
        
        weights.append((w1, w2))
        biases.append((b1, b2))
        # convs.append((conv1_dropout, conv2_dropout))
        
        if layer < layers-1:
            # print("some:",layer)P
            in_node = tf.nn.max_pool3d(dw_h_convs[layer], 
                    ksize=[1, pool_size, pool_size, pool_size, 1], 
                    strides=[1, pool_size, pool_size, pool_size, 1], 
                    padding='SAME')
        
    in_node = dw_h_convs[layers-1]

    # up layers
    for layer in range(layers-2, -1, -1):
        layer.p()
        # features = 2**(layer+1)*features_root
        stddev = np.sqrt(2 / (filter_size**2 * features))
        
        wd = tf.Variable(tf.truncated_normal([pool_size, pool_size, pool_size, features, features], stddev=stddev))
        bd = tf.Variable(tf.constant(0.1, shape=[features]))


        x_shape = tf.shape(in_node)
        output_shape = tf.stack([x_shape[0], x_shape[1]*2, x_shape[2]*2, x_shape[3]*2, x_shape[4]])
        h_deconv = tf.nn.conv3d_transpose(in_node, wd, output_shape, 
                strides=[1, pool_size, pool_size, pool_size, 1], padding='SAME')
        h_deconv_relu = tf.nn.relu(h_deconv + bd)
        h_deconv_concat = crop_and_concat3d(dw_h_convs[layer], h_deconv_relu)
        # deconv[layer] = h_deconv_concat
        
        features = features//2
        w1 = tf.Variable(tf.truncated_normal([filter_size, filter_size, 
                filter_size, features*3, features], stddev=stddev))
        w2 = tf.Variable(tf.truncated_normal([filter_size, filter_size, 
                filter_size, features, features], stddev=stddev))
        b1 = tf.Variable(tf.constant(0.1, shape=[features]))
        b2 = tf.Variable(tf.constant(0.1, shape=[features]))
        
        conv1 = tf.nn.conv3d(h_deconv_concat, w1, strides=[1, 1, 1, 1, 1], padding='SAME')
        conv1_dropout = tf.nn.dropout(conv1, keep_prob)
        h_conv = tf.nn.relu(conv1_dropout + b1)

        conv2 = tf.nn.conv3d(h_conv, w2, strides=[1, 1, 1, 1, 1], padding='SAME')
        conv2_dropout = tf.nn.dropout(conv2, keep_prob)
        in_node = tf.nn.relu(conv2_dropout + b2)
        up_h_convs[layer] = in_node
    
        weights.append((w1, w2))
        biases.append((b1, b2))

    # Output Map
    weight = tf.Variable(tf.truncated_normal([1, 1, 1, features, n_class], stddev=stddev))
    bias = tf.Variable(tf.constant(0.1, shape=[n_class]))
    conv = tf.nn.conv3d(in_node, weight, strides=[1, 1, 1, 1, 1], padding='SAME')
    conv_dropout = tf.nn.dropout(conv, tf.constant(1.0))
    output_map = tf.nn.relu(conv_dropout + bias)

    variables = []
    for w1,w2 in weights:
        variables.append(w1)
        variables.append(w2)
        
    for b1,b2 in biases:
        variables.append(b1)
        variables.append(b2)

    # import ipdb; ipdb.set_trace()
    return {"logits":output_map,"weights_biases":variables,
            "x":x, "y":y, "keep_prob":keep_prob}

# change for dropout and BatchNorm
def create_3d_unet_01(channels, n_class, **kwargs):
    features_root = kwargs.get("features_root", 32)
    layers = kwargs.get("layers", 4)
    filter_size = kwargs.get("filter_size", 3)
    pool_size = kwargs.get("pool_size", 2)
    summaries = kwargs.get("summaries", True)

    # Remove nodes from graph or reset entire default graph
    tf.reset_default_graph()

    x = tf.placeholder(tf.float32, name="x-input",
            shape=[None, None, None, None, channels])
    y = tf.placeholder(tf.float32, name="y-input",
            shape=[None, None, None, None, n_class])

    keep_prob = tf.placeholder(tf.float32)


    in_node = tf.reshape(x, tf.stack(
            [-1,tf.shape(x)[1],tf.shape(x)[2],tf.shape(x)[3],channels]))
    batch_size = tf.shape(in_node)[0]
 
    weights = []
    biases = []
    # convs = []
    # pools = OrderedDict()
    # deconv = OrderedDict()
    dw_h_convs = OrderedDict()
    up_h_convs = OrderedDict()

    features = features_root
    in_node = tf.contrib.layers.batch_norm(in_node, center=True, scale=True)
    # down layers
    for layer in range(0, layers):
        stddev = np.sqrt(2 / (filter_size**2 * features))
        layer.p()
            
        if layer == 0:
            w1 = tf.Variable(tf.truncated_normal([filter_size, filter_size, 
                    filter_size, channels, features], stddev=stddev))
        else:
            w1 = tf.Variable(tf.truncated_normal([filter_size, filter_size, 
                    filter_size, features, features], stddev=stddev))
        b1 = tf.Variable(tf.constant(0.1, shape=[features]))

        conv1 = tf.nn.conv3d(in_node, w1, strides=[1, 1, 1, 1, 1], padding='SAME')
        # in the paper, it didn't mention the dropout
        # conv1_dropout = tf.nn.dropout(conv1, keep_prob)
        # tmp_h_conv = tf.nn.relu(conv1_dropout + b1)
        tmp_h_conv = tf.nn.relu(conv1 + b1)

        features = features*2
        w2 = tf.Variable(tf.truncated_normal([filter_size, filter_size, 
                filter_size, features//2, features], stddev=stddev))
        b2 = tf.Variable(tf.constant(0.1, shape=[features]))
        
        conv2 = tf.nn.conv3d(tmp_h_conv, w2, strides=[1, 1, 1, 1, 1], padding='SAME')
        # conv2_dropout = tf.nn.dropout(conv2, keep_prob)
        # dw_h_convs[layer] = tf.nn.relu(conv2_dropout + b2)
        dw_h_convs[layer] = tf.nn.relu(conv2 + b2)
        
        weights.append((w1, w2))
        biases.append((b1, b2))
        # convs.append((conv1_dropout, conv2_dropout))
        
        if layer < layers-1:
            # print("some:",layer)P
            in_node = tf.nn.max_pool3d(dw_h_convs[layer], 
                    ksize=[1, pool_size, pool_size, pool_size, 1], 
                    strides=[1, pool_size, pool_size, pool_size, 1], 
                    padding='SAME')
        
    in_node = dw_h_convs[layers-1]
    in_node = tf.nn.dropout(in_node, keep_prob)

    # up layers
    for layer in range(layers-2, -1, -1):
        layer.p()
        # features = 2**(layer+1)*features_root
        stddev = np.sqrt(2 / (filter_size**2 * features))
        
        wd = tf.Variable(tf.truncated_normal([pool_size, pool_size, pool_size, features, features], stddev=stddev))
        bd = tf.Variable(tf.constant(0.1, shape=[features]))


        x_shape = tf.shape(in_node)
        output_shape = tf.stack([x_shape[0], x_shape[1]*2, x_shape[2]*2, x_shape[3]*2, x_shape[4]])
        h_deconv = tf.nn.conv3d_transpose(in_node, wd, output_shape, 
                strides=[1, pool_size, pool_size, pool_size, 1], padding='SAME')
        h_deconv_relu = tf.nn.relu(h_deconv + bd)
        h_deconv_concat = crop_and_concat3d(dw_h_convs[layer], h_deconv_relu)
        # deconv[layer] = h_deconv_concat
        
        features = features//2
        w1 = tf.Variable(tf.truncated_normal([filter_size, filter_size, 
                filter_size, features*3, features], stddev=stddev))
        w2 = tf.Variable(tf.truncated_normal([filter_size, filter_size, 
                filter_size, features, features], stddev=stddev))
        b1 = tf.Variable(tf.constant(0.1, shape=[features]))
        b2 = tf.Variable(tf.constant(0.1, shape=[features]))
        
        conv1 = tf.nn.conv3d(h_deconv_concat, w1, strides=[1, 1, 1, 1, 1], padding='SAME')
        # conv1_dropout = tf.nn.dropout(conv1, keep_prob)
        # h_conv = tf.nn.relu(conv1_dropout + b1)
        h_conv = tf.nn.relu(conv1 + b1)

        conv2 = tf.nn.conv3d(h_conv, w2, strides=[1, 1, 1, 1, 1], padding='SAME')
        # conv2_dropout = tf.nn.dropout(conv2, keep_prob)
        # in_node = tf.nn.relu(conv2_dropout + b2)
        in_node = tf.nn.relu(conv2 + b2)
        up_h_convs[layer] = in_node
    

        weights.append((w1, w2))
        biases.append((b1, b2))

    # Output Map
    weight = tf.Variable(tf.truncated_normal([1, 1, 1, features, n_class], stddev=stddev))
    bias = tf.Variable(tf.constant(0.1, shape=[n_class]))
    conv = tf.nn.conv3d(in_node, weight, strides=[1, 1, 1, 1, 1], padding='SAME')
    # conv_dropout = tf.nn.dropout(conv, tf.constant(1.0))
    # output_map = tf.nn.relu(conv_dropout + bias)
    output_map = tf.nn.relu(conv + bias)

    variables = []
    for w1,w2 in weights:
        variables.append(w1)
        variables.append(w2)
    # variables.append(wd)
    # variables.append(weight)
        
    for b1,b2 in biases:
        variables.append(b1)
        variables.append(b2)
    # variables.append(bd)
    # variables.append(bias)

    # import ipdb; ipdb.set_trace()
    return {"logits":output_map,"weights_biases":variables,
            "x":x, "y":y, "keep_prob":keep_prob}

# follow the keras version
def create_3d_unet_02(channels, n_class, **kwargs):
    features_root = kwargs.get("features_root", 32)
    layers = kwargs.get("layers", 4)
    filter_size = kwargs.get("filter_size", 3)
    pool_size = kwargs.get("pool_size", 2)
    summaries = kwargs.get("summaries", True)

    # Remove nodes from graph or reset entire default graph
    tf.reset_default_graph()

    x = tf.placeholder(tf.float32, name="x-input",
            shape=[None, None, None, None, channels])
    y = tf.placeholder(tf.float32, name="y-input",
            shape=[None, None, None, None, n_class])

    keep_prob = tf.placeholder(tf.float32)

    in_node = x
    # in_node = tf.reshape(x, tf.stack(
    #         [-1,tf.shape(x)[1],tf.shape(x)[2],tf.shape(x)[3],channels]))
    batch_size = tf.shape(in_node)[0]
 
    weights = []
    biases = []
    dw_h_convs = OrderedDict()
    up_h_convs = OrderedDict()

    features = features_root
    # in_node = tf.contrib.layers.batch_norm(in_node, center=True, scale=True)
    # down layers
    for layer in range(0, layers):
        stddev = np.sqrt(2 / (filter_size**2 * features))
        layer.p()
            
        if layer == 0:
            w1 = tf.Variable(tf.truncated_normal([filter_size, filter_size, 
                    filter_size, channels, features], stddev=stddev))
        else:
            w1 = tf.Variable(tf.truncated_normal([filter_size, filter_size, 
                    filter_size, features, features], stddev=stddev))
        b1 = tf.Variable(tf.constant(0.1, shape=[features]))

        conv1 = tf.nn.conv3d(in_node, w1, strides=[1, 1, 1, 1, 1], padding='SAME')
        # in the paper, it didn't mention the dropout
        # conv1_dropout = tf.nn.dropout(conv1, keep_prob)
        # tmp_h_conv = tf.nn.relu(conv1_dropout + b1)
        tmp_h_conv = tf.nn.relu(conv1 + b1)

        features = features*2
        w2 = tf.Variable(tf.truncated_normal([filter_size, filter_size, 
                filter_size, features//2, features], stddev=stddev))
        b2 = tf.Variable(tf.constant(0.1, shape=[features]))
        
        conv2 = tf.nn.conv3d(tmp_h_conv, w2, strides=[1, 1, 1, 1, 1], padding='SAME')
        # conv2_dropout = tf.nn.dropout(conv2, keep_prob)
        # dw_h_convs[layer] = tf.nn.relu(conv2_dropout + b2)
        dw_h_convs[layer] = tf.nn.relu(conv2 + b2)
        
        weights.append((w1, w2))
        biases.append((b1, b2))
        # convs.append((conv1_dropout, conv2_dropout))
        
        if layer < layers-1:
            # print("some:",layer)P
            in_node = tf.nn.max_pool3d(dw_h_convs[layer], 
                    ksize=[1, pool_size, pool_size, pool_size, 1], 
                    strides=[1, pool_size, pool_size, pool_size, 1], 
                    padding='SAME')
        
    in_node = dw_h_convs[layers-1]
    # in_node = tf.nn.dropout(in_node, keep_prob)

    # up layers
    for layer in range(layers-2, -1, -1):
        layer.p()
        # features = 2**(layer+1)*features_root
        stddev = np.sqrt(2 / (filter_size**2 * features))
        
        wd = tf.Variable(tf.truncated_normal([pool_size, pool_size, pool_size, features, features], stddev=stddev))
        bd = tf.Variable(tf.constant(0.1, shape=[features]))


        x_shape = tf.shape(in_node)
        output_shape = tf.stack([x_shape[0], x_shape[1]*2, x_shape[2]*2, x_shape[3]*2, x_shape[4]])
        h_deconv = tf.nn.conv3d_transpose(in_node, wd, output_shape, 
                strides=[1, pool_size, pool_size, pool_size, 1], padding='SAME')
        h_deconv_relu = tf.nn.relu(h_deconv + bd)
        h_deconv_concat = crop_and_concat3d(dw_h_convs[layer], h_deconv_relu)
        # deconv[layer] = h_deconv_concat
        
        features = features//2
        w1 = tf.Variable(tf.truncated_normal([filter_size, filter_size, 
                filter_size, features*3, features], stddev=stddev))
        w2 = tf.Variable(tf.truncated_normal([filter_size, filter_size, 
                filter_size, features, features], stddev=stddev))
        b1 = tf.Variable(tf.constant(0.1, shape=[features]))
        b2 = tf.Variable(tf.constant(0.1, shape=[features]))
        
        conv1 = tf.nn.conv3d(h_deconv_concat, w1, strides=[1, 1, 1, 1, 1], padding='SAME')
        # conv1_dropout = tf.nn.dropout(conv1, keep_prob)
        # h_conv = tf.nn.relu(conv1_dropout + b1)
        h_conv = tf.nn.relu(conv1 + b1)

        conv2 = tf.nn.conv3d(h_conv, w2, strides=[1, 1, 1, 1, 1], padding='SAME')
        # conv2_dropout = tf.nn.dropout(conv2, keep_prob)
        # in_node = tf.nn.relu(conv2_dropout + b2)
        in_node = tf.nn.relu(conv2 + b2)
        up_h_convs[layer] = in_node
    

        weights.append((w1, w2))
        biases.append((b1, b2))

    # Output Map
    weight = tf.Variable(tf.truncated_normal([1, 1, 1, features, n_class], stddev=stddev))
    bias = tf.Variable(tf.constant(0.1, shape=[n_class]))
    conv = tf.nn.conv3d(in_node, weight, strides=[1, 1, 1, 1, 1], padding='SAME')
    # conv_dropout = tf.nn.dropout(conv, tf.constant(1.0))
    # output_map = tf.nn.relu(conv_dropout + bias)
    output_map = tf.nn.relu(conv + bias)

    variables = []
    for w1,w2 in weights:
        variables.append(w1)
        variables.append(w2)
    # variables.append(wd)
    # variables.append(weight)
        
    for b1,b2 in biases:
        variables.append(b1)
        variables.append(b2)
    # variables.append(bd)
    # variables.append(bias)

    # import ipdb; ipdb.set_trace()
    return {"logits":output_map,"weights_biases":variables,
            "x":x, "y":y, "keep_prob":keep_prob}

if __name__ == '__main__':
    from minitest import *

    with test(create_3d_unet):
        channels = 1
        n_class = 10
        create_3d_unet(channels, n_class)
        pass