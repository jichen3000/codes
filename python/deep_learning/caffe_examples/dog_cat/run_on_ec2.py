import time
import os
import caffe
from caffe import layers as L, params as P
from caffe.proto import caffe_pb2

import lmdb

import cv2
import glob
import random
import numpy as np

IMAGE_WIDTH = 227
IMAGE_HEIGHT = 227
def transform_img(img, img_width=IMAGE_WIDTH, img_height=IMAGE_HEIGHT):
    #Histogram Equalization
    img[:, :, 0] = cv2.equalizeHist(img[:, :, 0])
    img[:, :, 1] = cv2.equalizeHist(img[:, :, 1])
    img[:, :, 2] = cv2.equalizeHist(img[:, :, 2])

    #Image Resizing
    img = cv2.resize(img, (img_width, img_height), interpolation = cv2.INTER_CUBIC)

    return img 

def make_datum(img, label):
    #image is numpy.ndarray format. BGR instead of RGB
    return caffe_pb2.Datum(
        channels=3,
        width=IMAGE_WIDTH,
        height=IMAGE_HEIGHT,
        label=label,
        data=np.rollaxis(img, 2).tostring())

def write_to_lmdb(lmdb_path, the_data):
    in_db = lmdb.open(lmdb_path, map_size=int(1e12))
    with in_db.begin(write=True) as in_txn:
        for in_idx, img_path in enumerate(the_data):
            if in_idx % 6 != 0:
                continue
            img = cv2.imread(img_path, cv2.IMREAD_COLOR)
            img = transform_img(img, img_width=IMAGE_WIDTH, img_height=IMAGE_HEIGHT)
            if 'cat' in img_path:
                label = 0
            else:
                label = 1
            datum = make_datum(img, label)
            in_txn.put('{:0>5d}'.format(in_idx), datum.SerializeToString())
            #print '{:0>5d}'.format(in_idx) + ':' + img_path
    in_db.close() 

def gen_lmdbs():
    DATA_PATH = "./data"
    train_data_path = os.path.join(DATA_PATH,'train')
    test_data_path = os.path.join(DATA_PATH,'test1')    

    random.seed(2)
    all_train_data = [img_path for img_path in glob.glob(train_data_path+"/*jpg")]
    test_data = [img_path for img_path in glob.glob(test_data_path+"/*jpg")]
    # len(all_train_data).p()
    # all_train_data[0].p()
    # len(all_train_data).p()
    #Shuffle train_data
    random.shuffle(all_train_data)
    # all_train_data[0].p()
    validation_count = len(all_train_data) / 5
    train_data = all_train_data[0:len(all_train_data)-validation_count]
    validation_data = all_train_data[len(all_train_data)-validation_count:]

    train_lmdb_path = os.path.join(DATA_PATH,'train.lmdb')
    validation_lmdb_path = os.path.join(DATA_PATH,'validation.lmdb')
    write_to_lmdb(train_lmdb_path, train_data)
    write_to_lmdb(validation_lmdb_path, validation_data)

# all conv layers use half num_output
def alex_net_1(lmdb_path, batch_size, mean_file_path, has_accuracy=False):
    the_param = [dict(lr_mult=1,decay_mult=1),dict(lr_mult=2,decay_mult=0)]

    # our version of LeNet: a series of linear and simple nonlinear transformations
    n = caffe.NetSpec()

    n.data, n.label = L.Data(batch_size=batch_size, backend=P.Data.LMDB, source=lmdb_path,
            transform_param=dict(mirror=True,crop_size=227,mean_file=mean_file_path), 
            ntop=2)
    
    n.conv1 = L.Convolution(n.data, num_output=96, kernel_size=11, stride=4, 
            weight_filler=dict(type='gaussian',std=0.01),
            bias_filler=dict(type='constant',value=0),
            param=the_param)
    n.relu1 = L.ReLU(n.conv1, in_place=True)
    n.pool1 = L.Pooling(n.relu1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.norm1 = L.LRN(n.pool1, local_size=5, alpha=0.0001, beta=0.75)

    n.conv2 = L.Convolution(n.norm1, num_output=256, kernel_size=5, pad=2, group=2,
            weight_filler=dict(type='gaussian',std=0.01),
            bias_filler=dict(type='constant',value=0),
            param=the_param)
    n.relu2 = L.ReLU(n.conv2, in_place=True)
    n.pool2 = L.Pooling(n.relu2, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.norm2 = L.LRN(n.pool2, local_size=5, alpha=0.0001, beta=0.75)

    # why this conv3 is not group=2
    n.conv3 = L.Convolution(n.norm2, num_output=384, kernel_size=3, pad=1,
            weight_filler=dict(type='gaussian',std=0.01),
            bias_filler=dict(type='constant',value=0),
            param=the_param)
    n.relu3 = L.ReLU(n.conv3, in_place=True)

    n.conv4 = L.Convolution(n.relu3, num_output=384, kernel_size=3, pad=1, group=2,
            weight_filler=dict(type='gaussian',std=0.01),
            bias_filler=dict(type='constant',value=0),
            param=the_param)
    n.relu4 = L.ReLU(n.conv4, in_place=True)

    n.conv5 = L.Convolution(n.relu4, num_output=256, kernel_size=3, pad=1, group=2,
            weight_filler=dict(type='gaussian',std=0.01),
            bias_filler=dict(type='constant',value=0),
            param=the_param)
    n.relu5 = L.ReLU(n.conv5, in_place=True)
    n.pool5 = L.Pooling(n.relu5, kernel_size=3, stride=2, pool=P.Pooling.MAX)

    n.fc6 =   L.InnerProduct(n.pool5, num_output=4096,
            weight_filler=dict(type='gaussian',std=0.005),
            bias_filler=dict(type='constant',value=1),
            param=the_param)
    n.relu6 = L.ReLU(n.fc6, in_place=True)
    n.drop6 = L.Dropout(n.relu6, in_place=True, dropout_ratio=0.5)

    n.fc7 =   L.InnerProduct(n.drop6, num_output=4096,
            weight_filler=dict(type='gaussian',std=0.005),
            bias_filler=dict(type='constant',value=1),
            param=the_param)
    n.relu7 = L.ReLU(n.fc7, in_place=True)
    n.drop7 = L.Dropout(n.relu7, in_place=True, dropout_ratio=0.5)

    n.fc8 =   L.InnerProduct(n.drop7, num_output=2,
            weight_filler=dict(type='gaussian',std=0.01),
            bias_filler=dict(type='constant',value=0),
            param=the_param)
    if has_accuracy:
        n.accuracy = L.Accuracy(n.fc8, n.label)
    n.loss =  L.SoftmaxWithLoss(n.fc8, n.label)
    
    return n.to_proto()


def alex_net_deploy():
    the_param = [dict(lr_mult=1,decay_mult=1),dict(lr_mult=2,decay_mult=0)]

    # our version of LeNet: a series of linear and simple nonlinear transformations
    n = caffe.NetSpec()

    n.data = L.Input(
            input_param=dict(shape=dict(dim=[1,3,227,227])))
    
    n.conv1 = L.Convolution(n.data, num_output=96, kernel_size=11, stride=4, 
            weight_filler=dict(type='gaussian',std=0.01),
            bias_filler=dict(type='constant',value=0),
            param=the_param)
    n.relu1 = L.ReLU(n.conv1, in_place=True)
    n.pool1 = L.Pooling(n.relu1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.norm1 = L.LRN(n.pool1, local_size=5, alpha=0.0001, beta=0.75)

    n.conv2 = L.Convolution(n.norm1, num_output=256, kernel_size=5, pad=2, group=2,
            weight_filler=dict(type='gaussian',std=0.01),
            bias_filler=dict(type='constant',value=0),
            param=the_param)
    n.relu2 = L.ReLU(n.conv2, in_place=True)
    n.pool2 = L.Pooling(n.relu2, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.norm2 = L.LRN(n.pool2, local_size=5, alpha=0.0001, beta=0.75)

    # why this conv3 is not group=2
    n.conv3 = L.Convolution(n.norm2, num_output=384, kernel_size=3, pad=1,
            weight_filler=dict(type='gaussian',std=0.01),
            bias_filler=dict(type='constant',value=0),
            param=the_param)
    n.relu3 = L.ReLU(n.conv3, in_place=True)

    n.conv4 = L.Convolution(n.relu3, num_output=384, kernel_size=3, pad=1, group=2,
            weight_filler=dict(type='gaussian',std=0.01),
            bias_filler=dict(type='constant',value=0),
            param=the_param)
    n.relu4 = L.ReLU(n.conv4, in_place=True)

    n.conv5 = L.Convolution(n.relu4, num_output=256, kernel_size=3, pad=1, group=2,
            weight_filler=dict(type='gaussian',std=0.01),
            bias_filler=dict(type='constant',value=0),
            param=the_param)
    n.relu5 = L.ReLU(n.conv5, in_place=True)
    n.pool5 = L.Pooling(n.relu5, kernel_size=3, stride=2, pool=P.Pooling.MAX)

    n.fc6 =   L.InnerProduct(n.pool5, num_output=4096,
            weight_filler=dict(type='gaussian',std=0.005),
            bias_filler=dict(type='constant',value=1),
            param=the_param)
    n.relu6 = L.ReLU(n.fc6, in_place=True)
    n.drop6 = L.Dropout(n.relu6, in_place=True, dropout_ratio=0.5)

    n.fc7 =   L.InnerProduct(n.drop6, num_output=4096,
            weight_filler=dict(type='gaussian',std=0.005),
            bias_filler=dict(type='constant',value=1),
            param=the_param)
    n.relu7 = L.ReLU(n.fc7, in_place=True)
    n.drop7 = L.Dropout(n.relu7, in_place=True, dropout_ratio=0.5)

    n.fc8 =   L.InnerProduct(n.drop7, num_output=2,
            weight_filler=dict(type='gaussian',std=0.01),
            bias_filler=dict(type='constant',value=0),
            param=the_param)
    n.prob =  L.Softmax(n.fc8)
    
    return n.to_proto()





def write_to_file(the_path, the_content):
    with open(the_path,'w') as the_f:
        the_f.write(the_content)
    return the_content

def gen_solver():
    solver = caffe_pb2.SolverParameter()
    solver.train_net= "train.prototxt"
    solver.test_net.extend(["validation.prototxt"])
    solver.test_iter.extend([1000])
    solver.test_interval= 1000
    solver.base_lr= 0.001
    solver.lr_policy= "step"
    solver.gamma= 0.1
    # solver.stepsize= 2500
    solver.stepsize= 500
    solver.display= 50
    # solver.max_iter= 40000
    solver.max_iter= 10000
    solver.momentum= 0.9
    solver.weight_decay= 0.0005
    solver.snapshot= 2000
    solver.snapshot_prefix= "snapshots"
    solver.solver_mode= solver.GPU
    return str(solver)

def main():
    DATA_PATH = "./data"
    gen_lmdbs()
    train_lmdb_path = os.path.join(DATA_PATH,'train.lmdb')
    validation_lmdb_path = os.path.join(DATA_PATH,'validation.lmdb')
    mean_binary_path = os.path.join(DATA_PATH,'mean.binaryproto')

    train_proto = str(alex_net_1(train_lmdb_path, 256, mean_binary_path))
    # print train_proto
    validation_proto = str(alex_net_1(validation_lmdb_path, 50, mean_binary_path, True))

    train_proto_path = 'train.prototxt'
    validation_proto_path = 'validation.prototxt'

    write_to_file(train_proto_path, train_proto)
    write_to_file(validation_proto_path, validation_proto);

    solver_proto_str = gen_solver()
    solver_proto_path = 'solver.prototxt'
    write_to_file(solver_proto_path, solver_proto_str);

    solver = None  # ignore this workaround for lmdb data (can't instantiate two solvers on the same data)
    solver = caffe.SGDSolver(solver_proto_path)

    # each output is (batch size, feature dim, spatial dim)
    aa = [(k, v.data.shape) for k, v in solver.net.blobs.items()]
    print aa

    start = time.time()
    caffe.set_device(0)
    caffe.set_mode_gpu()
    solver.step(1)
    end = time.time()
    print "time:",end-start



# main_vgg_16()
# alex_net need 3.4G memory
# vgg_16 need 6G memory

# main(), step(1) 77s
main()
# print str(alex_net_deploy())

print "ok"