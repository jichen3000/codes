# https://gist.github.com/ksimonyan/211839e770f7b538e2d8#file-readme-md

# http://caffe.berkeleyvision.org/tutorial/layers.html
import caffe
from caffe import layers as L, params as P


def vgg_16(lmdb_path, batch_size, mean_file_path):
    the_param = [dict(lr_mult=1,decay_mult=1),dict(lr_mult=2,decay_mult=0)]

    # our version of LeNet: a series of linear and simple nonlinear transformations
    n = caffe.NetSpec()

    n.data, n.label = L.Data(batch_size=batch_size, backend=P.Data.LMDB, source=lmdb_path,
            transform_param=dict(mirror=True,crop_size=227,mean_file=mean_file_path), 
            ntop=2)
    
    n.conv1_1 = L.Convolution(n.data, num_output=64, kernel_size=3, pad=1)
    n.relu1_1 = L.ReLU(n.conv1_1, in_place=True)
    n.conv1_2 = L.Convolution(n.relu1_1, num_output=64, kernel_size=3, pad=1)
    n.relu1_2 = L.ReLU(n.conv1_2, in_place=True)
    n.pool1 = L.Pooling(n.relu1_2, kernel_size=2, stride=2, pool=P.Pooling.MAX)

    n.conv2_1 = L.Convolution(n.pool1, num_output=128, kernel_size=3, pad=1)
    n.relu2_1 = L.ReLU(n.conv2_1, in_place=True)
    n.conv2_1 = L.Convolution(n.relu2_1, num_output=128, kernel_size=3, pad=1)
    n.relu2_2 = L.ReLU(n.conv2_1, in_place=True)
    n.pool2 = L.Pooling(n.relu2_2, kernel_size=2, stride=2, pool=P.Pooling.MAX)

    n.conv3_1 = L.Convolution(n.pool2, num_output=256, kernel_size=3, pad=1)
    n.relu3_1 = L.ReLU(n.conv3_1, in_place=True)
    n.conv3_2 = L.Convolution(n.relu3_1, num_output=256, kernel_size=3, pad=1)
    n.relu3_2 = L.ReLU(n.conv3_2, in_place=True)
    n.conv3_3 = L.Convolution(n.relu3_2, num_output=256, kernel_size=3, pad=1)
    n.relu3_3 = L.ReLU(n.conv3_3, in_place=True)
    n.pool3 = L.Pooling(n.relu3_3, kernel_size=2, stride=2, pool=P.Pooling.MAX)

    n.conv4_1 = L.Convolution(n.pool3, num_output=512, kernel_size=3, pad=1)
    n.relu4_1 = L.ReLU(n.conv4_1, in_place=True)
    n.conv4_2 = L.Convolution(n.relu4_1, num_output=512, kernel_size=3, pad=1)
    n.relu4_2 = L.ReLU(n.conv4_2, in_place=True)
    n.conv4_3 = L.Convolution(n.relu4_2, num_output=512, kernel_size=3, pad=1)
    n.relu4_3 = L.ReLU(n.conv4_3, in_place=True)
    n.pool4 = L.Pooling(n.relu4_3, kernel_size=2, stride=2, pool=P.Pooling.MAX)

    n.conv5_1 = L.Convolution(n.pool4, num_output=512, kernel_size=3, pad=1)
    n.relu5_1 = L.ReLU(n.conv5_1, in_place=True)
    n.conv5_2 = L.Convolution(n.relu5_1, num_output=512, kernel_size=3, pad=1)
    n.relu5_2 = L.ReLU(n.conv5_2, in_place=True)
    n.conv5_3 = L.Convolution(n.relu5_2, num_output=512, kernel_size=3, pad=1)
    n.relu5_3 = L.ReLU(n.conv5_3, in_place=True)
    n.pool5 = L.Pooling(n.relu5_3, kernel_size=2, stride=2, pool=P.Pooling.MAX)


    n.fc6 =   L.InnerProduct(n.pool5, num_output=4096)
    n.relu6 = L.ReLU(n.fc6, in_place=True)
    n.drop6 = L.Dropout(n.relu6, in_place=True, dropout_ratio=0.5)

    n.fc7 =   L.InnerProduct(n.drop6, num_output=4096)
    n.relu7 = L.ReLU(n.fc7, in_place=True)
    n.drop7 = L.Dropout(n.relu7, in_place=True, dropout_ratio=0.5)

    # this changes for dog and cat
    n.fc8 =   L.InnerProduct(n.drop7, num_output=2)
    # if has_accuracy:
    #     n.accuracy = L.Accuracy(n.fc8, n.label)

    n.loss =  L.SoftmaxWithLoss(n.fc8, n.label)
    
    return n.to_proto()



if __name__ == '__main__':
        from minitest import *
    
        with test(vgg_16):
            train_proto = vgg_16('train_lmdb', 256, "mean_file.binary").pp()   
            print type(train_proto)
            # test_proto = lenet('test_lmdb', 50, "mean_file.binary").pp()   