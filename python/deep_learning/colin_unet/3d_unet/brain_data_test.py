# http://stackoverflow.com/questions/34240703/difference-between-tensorflow-tf-nn-softmax-and-tf-nn-softmax-cross-entropy-with

import sys
import os
# sys.path.append("..")

from numpy_data_provider import NumpyDataProvider
from unet_3d import create_3d_unet, create_3d_unet_01
from unet_trainer import Trainer, predict
import numpy as np

%load_ext autoreload
%autoreload 2
# cannot run in colin-d, gpu memory is not enough
import logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')


def cal_class_weights(the_labels):
    #Class distribution between the two classes
    class_frequencies = np.array([np.sum(the_labels == 0) ,
                                  np.sum(the_labels == 1)  ])

    # We are taking the log here because we want the net to focus more on the foreground pixels but not too much (otherwise
    # it would not be penalized enough for missclassifying terrain pixels which results in too many false positives)
    class_weights = np.log(class_frequencies[[1,0]])
    class_weights = class_weights / np.sum(class_weights) * 2.
    class_weights = class_weights.astype(np.float32)
    return class_weights

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
    # np.save(os.path.join(data_path,"data_tf.npy"), t_data)
    # np.save(os.path.join(data_path,"labels_tf.npy"), t_labels)
    t_data = np.load(os.path.join(data_path,"data_tf.npy")).astype('float32')
    t_labels = np.load(os.path.join(data_path,"labels_tf.npy")).astype('uint8')
    data_provider = NumpyDataProvider(t_data, t_labels)
    print("NumpyDataProvider end")


    unet_hash = create_3d_unet_01(channels=data_provider.channels, 
        n_class=data_provider.n_class, 
        layers=3, features_root=16)
    print("create_3d_unet end")
    # class_weights = cal_class_weights(t_labels[...,0])
    # class_weights=[1,1]
    class_weights=None
    train_kwargs = {"output_path":"./unet_trained", 
        "n_class":data_provider.n_class,
        "cost_options":{
            "type":"cross_entropy",
            # "type":"dice_coefficient",
            "regularizer":1e-4,
            # "class_weights":class_weights
        },
        # "optimizer_options":{"type":"momentum"},
        "optimizer_options":{"type":"adam"},
        "epochs":2,
        "training_iters":10,
        "verification_batch_size":4
        }

    predicter = Trainer.do(unet_hash, data_provider, **train_kwargs)
    print("Trainer.do end")

    x_test, y_test = data_provider(4)
    prediction = predict(unet_hash, x_test, data_provider.n_class, "./unet_trained/model.cpkt")
    print("predict end")
    np.unique(prediction[...,0], return_counts=True)
    np.unique(prediction[...,1], return_counts=True)
    
    # cost     
    # loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=flat_logits, 
    # http://www.cnblogs.com/welhzh/p/6648907.html
    
    # the prediction has many np.nan, find it's network or cost issue                                                                          labels=flat_labels))


brain()
print("ok")

# I tensorflow/core/common_runtime/gpu/gpu_device.cc:975] Creating TensorFlow device (/gpu:0) -> (device: 0, name: Tesla K80, pci bus id: 0000:00:04.0)
# W tensorflow/core/common_runtime/bfc_allocator.cc:217] Ran out of memory trying to allocate 135.19MiB. The caller indicates that this is not a failure, but may mean that there could be performance gains if more memory is available.
# ('np.unique(predictions[...,0], return_counts=True) :', (array([ 0.23332419,  0.23743248,  0.2397621 , ...,  0.62915611,
#         0.62994802,  0.64970905], dtype=float32), array([1, 1, 1, ..., 1, 1, 1])))
# 2017-05-05 15:24:47,289 Verification error= 52.6%, loss= 0.9379
# 2017-05-05 15:24:47,290 Start optimization
# ('np.unique(predictions[...,0], return_counts=True) :', (array([ 0.5       ,  0.50011408,  0.50039601, ...,  0.94864899,
#         0.94919705,  0.94945931], dtype=float32), array([91,  1,  1, ...,  1,  1,  1])))
# 2017-05-05 15:25:04,404 Iter 0, Minibatch Loss= 0.4555, Training Accuracy= 0.9977, Minibatch error= 100.0%
# ('np.unique(predictions[...,0], return_counts=True) :', (array([ 0.73392671,  0.74132067,  0.75588918, ...,  0.9980306 ,
#         0.9980647 ,  0.99811184], dtype=float32), array([1, 1, 1, ..., 1, 1, 1])))
# 2017-05-05 15:26:22,735 Iter 5, Minibatch Loss= 0.2007, Training Accuracy= 0.9737, Minibatch error= 100.0%
# 2017-05-05 15:27:24,425 Epoch 0, Average loss: 0.3612, learning rate: 0.2000
# W tensorflow/core/common_runtime/bfc_allocator.cc:217] Ran out of memory trying to allocate 135.19MiB. The caller indicates that this is not a failure, but may mean that there could be performance gains if more memory is available.
# ('np.unique(predictions[...,0], return_counts=True) :', (array([ 0.75722975,  0.76508588,  0.78238547, ...,  0.99951386,
#         0.99951911,  0.99952328], dtype=float32), array([4, 4, 4, ..., 1, 1, 1])))
# 2017-05-05 15:27:33,090 Verification error= 100.0%, loss= 0.1699
# ('np.unique(predictions[...,0], return_counts=True) :', (array([ 0.76957798,  0.77723551,  0.79478973, ...,  0.99972779,
#         0.9997291 ,  0.99973017], dtype=float32), array([1, 1, 1, ..., 1, 1, 1])))
# 2017-05-05 15:27:50,470 Iter 10, Minibatch Loss= 0.1375, Training Accuracy= 0.9966, Minibatch error= 100.0%
