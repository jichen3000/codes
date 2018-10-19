# http://caffe.berkeleyvision.org/tutorial/layers.html
import caffe
from caffe import layers as L, params as P


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


if __name__ == '__main__':
        from minitest import *
    
        with test(alex_net_1):
            train_proto = alex_net_1('train_lmdb', 256, "mean_file.binary").pp()   
            print type(train_proto)
            # test_proto = lenet('test_lmdb', 50, "mean_file.binary").pp()   