from __future__ import division, print_function
import sys
import os
from collections import OrderedDict
import logging
import shutil

import numpy as np
import tensorflow as tf
import minitest

sys.path.append("..")
from tf_unet import image_gen
from tf_unet import util

from tf_unet.plain_unet import Trainer, predict, create_unet

%load_ext autoreload
%autoreload 2

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

def pixel_wise_softmax_2(output_map):
    exponential_map = tf.exp(output_map)
    sum_exp = tf.reduce_sum(exponential_map, 3, keep_dims=True)
    tensor_sum_exp = tf.tile(sum_exp, tf.stack([1, 1, 1, tf.shape(output_map)[3]]))
    return tf.div(exponential_map,tensor_sum_exp)

nx = 572
ny = 572
generator = image_gen.GrayScaleDataProvider(nx, ny, cnt=20)
x_test, y_test = generator(4)
# generator.channels 1
# generator.n_class 2
test_x, test_y = generator(1)

unet_hash = create_unet(channels=generator.channels, 
    n_class=generator.n_class, layers=3, features_root=16)
train_kwargs = {"output_path":"./unet_trained", 
    "n_class":generator.n_class,
    "cost_options":{"type":"cross_entropy"},
    "optimizer_options":{"type":"momentum"},
    "epochs":1
    }

logits = unet_hash["logits"]
weights_biases = unet_hash["weights_biases"]
x = unet_hash["x"]
y = unet_hash["y"]
keep_prob = unet_hash["keep_prob"]

init = tf.global_variables_initializer()
# with tf.Session() as sess:
sess = tf.Session()
sess.run(init)
        
predicter = tf.nn.softmax(logits)
pred_mm = pixel_wise_softmax_2(logits)
logits_value, predicter_value, pred_mm_value = sess.run((logits, predicter, pred_mm),
        feed_dict={x: test_x, keep_prob: 1.})
np.unique(predicter_value[...,0], return_counts=True)
np.unique(pred_mm_value[...,0], return_counts=True)
np.unique(logits_value, return_counts=True)

### 
predicter = Trainer.do(unet_hash, generator, **train_kwargs)
prediction = predict(predicter, unet_hash, x_test, 
        generator.n_class, "./unet_trained/model.cpkt")