import sys
import os
# sys.path.append("..")

from numpy_data_provider import NumpyDataProvider
from unet_3d import create_3d_unet, create_3d_unet_01
from unet_trainer import Trainer, predict
import numpy as np

# cannot run in colin-d, gpu memory is not enough

from __future__ import division, print_function
from collections import OrderedDict
import logging
import shutil

import tensorflow as tf
import minitest

# sys.path.append("..")
# from tf_unet import image_gen
# from tf_unet import util

%load_ext autoreload
%autoreload 2

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def _pixel_wise_softmax_2(output_map):
    # np.divide(np.inf,np.inf) == np.nan
    exponential_map = tf.exp(output_map)
    sum_exp = tf.reduce_sum(exponential_map, 4, keep_dims=True)
    tensor_sum_exp = tf.tile(sum_exp, tf.stack([1, 1, 1, 1, tf.shape(output_map)[4]]))
    return tf.div(exponential_map,tensor_sum_exp)

def brain():
    # nx = 572
    # ny = 572
    # generator = image_gen.GrayScaleDataProvider(nx, ny, cnt=20)
    # x_test, y_test = generator(4)
    # generator.channels 1
    # generator.n_class 2
    data_path = "../../../data/colin_unet/3d_lasagne/"
    # the_data = np.load(os.path.join(data_path,"data.npy")).astype('float32')
    # the_labels = np.load(os.path.join(data_path,"target.npy")).astype('uint8')
    # the_labels[the_labels>0]=1
    # t_data = np.transpose(the_data, (0,2,3,4,1))
    # t_labels = np.transpose(the_labels, (0,2,3,4,1))
    t_data = np.load(os.path.join(data_path,"data_tf.npy")).astype('float32')
    t_labels = np.load(os.path.join(data_path,"labels_tf.npy")).astype('float32')
    data_provider = NumpyDataProvider(t_data, t_labels)
    x_test, y_test = data_provider(4)
    y_test[...,1],y_test[...,0]=y_test[...,0],y_test[...,1]
    print("NumpyDataProvider end")


    verification_batch_size = 1
    # test_x, test_y = data_provider(verification_batch_size)
    unet_hash = create_3d_unet_01(channels=data_provider.channels, 
        n_class=data_provider.n_class, 
        layers=3, features_root=16)
    print("create_3d_unet end")
    train_kwargs = {"output_path":"./unet_trained", 
        "n_class":data_provider.n_class,
        "cost_options":{
            "type":"cross_entropy",
            "class_weights":[1,1]
        },
        "optimizer_options":{"type":"momentum"},
        "epochs":1,
        "training_iters":10,
        "verification_batch_size":4
        }

    logits = unet_hash["logits"]
    weights_biases = unet_hash["weights_biases"]
    x = unet_hash["x"]
    y = unet_hash["y"]
    keep_prob = unet_hash["keep_prob"]

           
    n_class = 2
    flat_logits = tf.reshape(logits, [-1, n_class])
    flat_labels = tf.reshape(y, [-1, n_class])
    # flat_labels = tf.reshape(y[...,0].astype('int32'), [-1, ])
    # loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(
    #         logits=flat_logits,  labels=flat_labels))
    # loss = tf.nn.softmax_cross_entropy_with_logits(
    #         logits=flat_logits,  labels=flat_labels)
    loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(
            logits=flat_logits,  labels=tf.cast(flat_labels[...,0], tf.int32)))
    # logits_value, loss_value = sess.run((logits, loss),
    #         feed_dict={x: test_x, y: test_y, keep_prob: 1.})




    init_learning_rate = 0.001
    global_step = tf.Variable(0)
    # decay_rate = optimizer_options.pop("decay_rate", 0.95)
    decay_rate = 0.95
    training_iters = 1
    learning_rate_node = tf.train.exponential_decay(
            learning_rate=init_learning_rate, 
            global_step=global_step, 
            decay_steps=training_iters,  
            decay_rate=decay_rate, 
            staircase=True)
    learning_rate_node = tf.Variable(init_learning_rate)
    # cost = loss
    
    # optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate_node).minimize(loss,global_step=global_step)

    momentum = 0.2
    
    learning_rate_node = tf.train.exponential_decay(
            learning_rate=0.001, 
            global_step=global_step, 
            decay_steps=training_iters,  
            decay_rate=decay_rate, 
            staircase=True)
    
    optimizer = tf.train.MomentumOptimizer(learning_rate=learning_rate_node, 
            momentum=momentum).minimize(
            loss, global_step=global_step)
    # optimizer = tf.train.AdamOptimizer(learning_rate=learning_rate_node).compute_gradients(loss)
    pred = tf.nn.softmax(logits)

    if sess: sess.close()
    init = tf.global_variables_initializer()
    # with tf.Session() as sess:
    sess = tf.Session()
    sess.run(init)
 
    for i in range(10):
        test_x, test_y = data_provider(verification_batch_size)
        test_y[...,1],test_y[...,0]=test_y[...,0],test_y[...,1]
        logits_value, loss_value, optimizer_value, lr_value, pred_value, weight_value = sess.run(
                (logits, loss, optimizer, learning_rate_node, pred,weights_biases[0]),
                feed_dict={x: test_x, y: test_y, keep_prob: 1.})
        # logits_value, loss_value, lr_value, pred_value, weight_value = sess.run(
        #         (logits, loss, learning_rate_node, pred,weights_biases[0]),
        #         feed_dict={x: test_x, y: test_y, keep_prob: 1.})
        np.unique(logits_value,return_counts=True).p()
        [pred_value[...,1].max(),pred_value[...,1].min()].p()
        np.unique(pred_value[...,1],return_counts=True).p()
        loss_value.mean().p()
        lr_value.p()
        [weight_value.min(),weight_value.mean(),weight_value.max()].p()

    np.unique(test_y[...,1],return_counts=True).p()   
    a = pred_value[...,1]
    np.unique(a[a>0.5],return_counts=True).p()


    pred_sm = tf.nn.softmax(logits)
    pred_sm_value = sess.run(pred_sm, 
            feed_dict={x: x_test, keep_prob: 1.})
    logits_value,pred_sm_value = sess.run((logits,pred_sm), 
            feed_dict={x: x_test, keep_prob: 1.})


    exponential_map = tf.exp(logits)
    sum_exp = tf.reduce_sum(exponential_map, 4, keep_dims=True)
    my_pred = tf.div(exponential_map,sum_exp)
    pred_sm = tf.nn.softmax(logits)
    logits_value, exponential_map_value, sum_exp_value, my_pred_value, pred_sm_value = sess.run(
            (logits, exponential_map, sum_exp, my_pred, pred_sm),
            feed_dict={x: test_x, keep_prob: 1.})
    np.unique(aa, return_counts=True)
    np.unique(exponential_map_value, return_counts=True)
    np.unique(sum_exp_value, return_counts=True)
    np.unique(my_pred_value[...,1], return_counts=True)
    np.unique(pred_sm_value[...,1], return_counts=True)



    tensor_sum_exp = tf.tile(sum_exp, tf.stack([1, 1, 1, 1, tf.shape(output_map)[4]]))
    return tf.div(exponential_map,tensor_sum_exp)


# o 128
# 0 