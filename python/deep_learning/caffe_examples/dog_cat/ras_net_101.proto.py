# https://github.com/KaimingHe/deep-residual-networks/blob/master/prototxt/ResNet-101-deploy.prototxt

import os
import caffe
from caffe import layers as L, params as P
from caffe.proto import caffe_pb2

def write_to_file(the_path, the_content):
    with open(the_path,'w') as the_f:
        the_f.write(the_content)
    return the_content

def ras_net_101(lmdb_path, batch_size, mean_file_path):

    # our version of LeNet: a series of linear and simple nonlinear transformations
    n = caffe.NetSpec()

    n.data, n.label = L.Data(batch_size=batch_size, backend=P.Data.LMDB, source=lmdb_path,
            transform_param=dict(mirror=True,crop_size=224,mean_file=mean_file_path), 
            ntop=2)
    
    n.conv1 = L.Convolution(n.data, num_output=64, kernel_size=7, pad=3, stride=2, bias_term=False)
    n.bn_conv1 = L.BatchNorm(n.conv1, in_place=True, use_global_stats=True)
    n.scale_conv1 = L.Scale(n.conv1, in_place=True, bias_term=True)
    n.conv1_relu = L.ReLU(n.conv1, in_place=True)
    n.pool1 = L.Pooling(n.conv1, kernel_size=3, stride=2, pool=P.Pooling.MAX)

    n.res2a_branch1 = L.Convolution(n.pool1, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn2a_branch1 = L.BatchNorm(n.res2a_branch1, in_place=True, use_global_stats=True)
    n.scale2a_branch1 = L.Scale(n.res2a_branch1, in_place=True, bias_term=True)

    n.res2a_branch2a = L.Convolution(n.pool1, num_output=64, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn2a_branch2a = L.BatchNorm(n.res2a_branch2a, in_place=True, use_global_stats=True)
    n.scale2a_branch2a = L.Scale(n.res2a_branch2a, in_place=True, bias_term=True)
    n.res2a_branch2a_relu = L.ReLU(n.res2a_branch2a, in_place=True)
    
    n.res2a_branch2b = L.Convolution(n.res2a_branch2a, num_output=64, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn2a_branch2b = L.BatchNorm(n.res2a_branch2b, in_place=True, use_global_stats=True)
    n.scale2a_branch2b = L.Scale(n.res2a_branch2b, in_place=True, bias_term=True)
    n.res2a_branch2b_relu = L.ReLU(n.res2a_branch2b, in_place=True)
    
    n.res2a_branch2c = L.Convolution(n.res2a_branch2b, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn2a_branch2c = L.BatchNorm(n.res2a_branch2c, in_place=True, use_global_stats=True)
    n.scale2a_branch2c = L.Scale(n.res2a_branch2c, in_place=True, bias_term=True)

    n.res2a = L.Eltwise(n.res2a_branch1, n.res2a_branch2c)
    n.res2a_relu = L.ReLU(n.res2a, in_place=True)
    
    n.res2b_branch2a = L.Convolution(n.res2a, num_output=64, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn2b_branch2a = L.BatchNorm(n.res2b_branch2a, in_place=True, use_global_stats=True)
    n.scale2b_branch2a = L.Scale(n.res2b_branch2a, in_place=True, bias_term=True)
    n.res2b_branch2a_relu = L.ReLU(n.res2b_branch2a, in_place=True)
    
    n.res2b_branch2b = L.Convolution(n.res2b_branch2a, num_output=64, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn2b_branch2b = L.BatchNorm(n.res2b_branch2b, in_place=True, use_global_stats=True)
    n.scale2b_branch2b = L.Scale(n.res2b_branch2b, in_place=True, bias_term=True)
    n.res2b_branch2b_relu = L.ReLU(n.res2b_branch2b, in_place=True)
    
    n.res2b_branch2c = L.Convolution(n.res2b_branch2b, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn2b_branch2c = L.BatchNorm(n.res2b_branch2c, in_place=True, use_global_stats=True)
    n.scale2b_branch2c = L.Scale(n.res2b_branch2c, in_place=True, bias_term=True)

    n.res2b = L.Eltwise(n.res2a, n.res2b_branch2c)
    n.res2b_relu = L.ReLU(n.res2b, in_place=True)

    n.res2c_branch2a = L.Convolution(n.res2b, num_output=64, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn2c_branch2a = L.BatchNorm(n.res2c_branch2a, in_place=True, use_global_stats=True)
    n.scale2c_branch2a = L.Scale(n.res2c_branch2a, in_place=True, bias_term=True)
    n.res2c_branch2a_relu = L.ReLU(n.res2c_branch2a, in_place=True)
    
    n.res2c_branch2b = L.Convolution(n.res2c_branch2a, num_output=64, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn2c_branch2b = L.BatchNorm(n.res2c_branch2b, in_place=True, use_global_stats=True)
    n.scale2c_branch2b = L.Scale(n.res2c_branch2b, in_place=True, bias_term=True)
    n.res2c_branch2b_relu = L.ReLU(n.res2c_branch2b, in_place=True)
    
    n.res2c_branch2c = L.Convolution(n.res2c_branch2b, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn2c_branch2c = L.BatchNorm(n.res2c_branch2c, in_place=True, use_global_stats=True)
    n.scale2c_branch2c = L.Scale(n.res2c_branch2c, in_place=True, bias_term=True)
    
    n.res2c = L.Eltwise(n.res2b, n.res2c_branch2c)
    n.res2c_relu = L.ReLU(n.res2c, in_place=True)

    n.res3a_branch1 = L.Convolution(n.res2c, num_output=512, kernel_size=1, pad=0, stride=2, bias_term=False)
    n.bn3a_branch1 = L.BatchNorm(n.res3a_branch1, in_place=True, use_global_stats=True)
    n.scale3a_branch1 = L.Scale(n.res3a_branch1, in_place=True, bias_term=True)

    n.res3a_branch2a = L.Convolution(n.res2c, num_output=128, kernel_size=1, pad=0, stride=2, bias_term=False)
    n.bn3a_branch2a = L.BatchNorm(n.res3a_branch2a, in_place=True, use_global_stats=True)
    n.scale3a_branch2a = L.Scale(n.res3a_branch2a, in_place=True, bias_term=True)
    n.res3a_branch2a_relu = L.ReLU(n.res3a_branch2a, in_place=True)

    n.res3a_branch2b = L.Convolution(n.res3a_branch2a, num_output=128, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn3a_branch2b = L.BatchNorm(n.res3a_branch2b, in_place=True, use_global_stats=True)
    n.scale3a_branch2b = L.Scale(n.res3a_branch2b, in_place=True, bias_term=True)
    n.res3a_branch2b_relu = L.ReLU(n.res3a_branch2b, in_place=True)
    
    n.res3a_branch2c = L.Convolution(n.res3a_branch2b, num_output=512, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn3a_branch2c = L.BatchNorm(n.res3a_branch2c, in_place=True, use_global_stats=True)
    n.scale3a_branch2c = L.Scale(n.res3a_branch2c, in_place=True, bias_term=True)

    n.res3a = L.Eltwise(n.res3a_branch1, n.res3a_branch2c)
    n.res3a_relu = L.ReLU(n.res3a, in_place=True)
    
    n.res3b1_branch2a = L.Convolution(n.res3a, num_output=128, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn3b1_branch2a = L.BatchNorm(n.res3b1_branch2a, in_place=True, use_global_stats=True)
    n.scale3b1_branch2a = L.Scale(n.res3b1_branch2a, in_place=True, bias_term=True)
    n.res3b1_branch2a_relu = L.ReLU(n.res3b1_branch2a, in_place=True)

    n.res3b1_branch2b = L.Convolution(n.res3b1_branch2a, num_output=128, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn3b1_branch2b = L.BatchNorm(n.res3b1_branch2b, in_place=True, use_global_stats=True)
    n.scale3b1_branch2b = L.Scale(n.res3b1_branch2b, in_place=True, bias_term=True)
    n.res3b1_branch2b_relu = L.ReLU(n.res3b1_branch2b, in_place=True)
    
    n.res3b1_branch2c = L.Convolution(n.res3b1_branch2b, num_output=512, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn3b1_branch2c = L.BatchNorm(n.res3b1_branch2c, in_place=True, use_global_stats=True)
    n.scale3b1_branch2c = L.Scale(n.res3b1_branch2c, in_place=True, bias_term=True)

    n.res3b1 = L.Eltwise(n.res3a, n.res3b1_branch2c)
    n.res3b1_relu = L.ReLU(n.res3b1, in_place=True)
    
    n.res3b2_branch2a = L.Convolution(n.res3b1, num_output=128, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn3b2_branch2a = L.BatchNorm(n.res3b2_branch2a, in_place=True, use_global_stats=True)
    n.scale3b2_branch2a = L.Scale(n.res3b2_branch2a, in_place=True, bias_term=True)
    n.res3b2_branch2a_relu = L.ReLU(n.res3b2_branch2a, in_place=True)

    n.res3b2_branch2b = L.Convolution(n.res3b2_branch2a, num_output=128, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn3b2_branch2b = L.BatchNorm(n.res3b2_branch2b, in_place=True, use_global_stats=True)
    n.scale3b2_branch2b = L.Scale(n.res3b2_branch2b, in_place=True, bias_term=True)
    n.res3b2_branch2b_relu = L.ReLU(n.res3b2_branch2b, in_place=True)
    
    n.res3b2_branch2c = L.Convolution(n.res3b2_branch2b, num_output=512, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn3b2_branch2c = L.BatchNorm(n.res3b2_branch2c, in_place=True, use_global_stats=True)
    n.scale3b2_branch2c = L.Scale(n.res3b2_branch2c, in_place=True, bias_term=True)

    n.res3b2 = L.Eltwise(n.res3b1, n.res3b2_branch2c)
    n.res3b2_relu = L.ReLU(n.res3b2, in_place=True)
    
    n.res3b3_branch2a = L.Convolution(n.res3b2, num_output=128, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn3b3_branch2a = L.BatchNorm(n.res3b3_branch2a, in_place=True, use_global_stats=True)
    n.scale3b3_branch2a = L.Scale(n.res3b3_branch2a, in_place=True, bias_term=True)
    n.res3b3_branch2a_relu = L.ReLU(n.res3b3_branch2a, in_place=True)

    n.res3b3_branch2b = L.Convolution(n.res3b3_branch2a, num_output=128, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn3b3_branch2b = L.BatchNorm(n.res3b3_branch2b, in_place=True, use_global_stats=True)
    n.scale3b3_branch2b = L.Scale(n.res3b3_branch2b, in_place=True, bias_term=True)
    n.res3b3_branch2b_relu = L.ReLU(n.res3b3_branch2b, in_place=True)
    
    n.res3b3_branch2c = L.Convolution(n.res3b3_branch2b, num_output=512, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn3b3_branch2c = L.BatchNorm(n.res3b3_branch2c, in_place=True, use_global_stats=True)
    n.scale3b3_branch2c = L.Scale(n.res3b3_branch2c, in_place=True, bias_term=True)

    n.res3b3 = L.Eltwise(n.res3b2, n.res3b3_branch2c)
    n.res3b3_relu = L.ReLU(n.res3b3, in_place=True)
    
    n.res4a_branch1 = L.Convolution(n.res3b3, num_output=1024, kernel_size=1, pad=0, stride=2, bias_term=False)
    n.bn4a_branch1 = L.BatchNorm(n.res4a_branch1, in_place=True, use_global_stats=True)
    n.scale4a_branch1 = L.Scale(n.res4a_branch1, in_place=True, bias_term=True)

    n.res4a_branch2a = L.Convolution(n.res3b3, num_output=256, kernel_size=1, pad=0, stride=2, bias_term=False)
    n.bn4a_branch2a = L.BatchNorm(n.res4a_branch2a, in_place=True, use_global_stats=True)
    n.scale4a_branch2a = L.Scale(n.res4a_branch2a, in_place=True, bias_term=True)
    n.res4a_branch2a_relu = L.ReLU(n.res4a_branch2a, in_place=True)

    n.res4a_branch2b = L.Convolution(n.res4a_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4a_branch2b = L.BatchNorm(n.res4a_branch2b, in_place=True, use_global_stats=True)
    n.scale4a_branch2b = L.Scale(n.res4a_branch2b, in_place=True, bias_term=True)
    n.res4a_branch2b_relu = L.ReLU(n.res4a_branch2b, in_place=True)
    
    n.res4a_branch2c = L.Convolution(n.res4a_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4a_branch2c = L.BatchNorm(n.res4a_branch2c, in_place=True, use_global_stats=True)
    n.scale4a_branch2c = L.Scale(n.res4a_branch2c, in_place=True, bias_term=True)

    n.res4a = L.Eltwise(n.res4a_branch1, n.res4a_branch2c)
    n.res4a_relu = L.ReLU(n.res4a, in_place=True)
    
    n.res4b1_branch2a = L.Convolution(n.res4a, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b1_branch2a = L.BatchNorm(n.res4b1_branch2a, in_place=True, use_global_stats=True)
    n.scale4b1_branch2a = L.Scale(n.res4b1_branch2a, in_place=True, bias_term=True)
    n.res4b1_branch2a_relu = L.ReLU(n.res4b1_branch2a, in_place=True)

    n.res4b1_branch2b = L.Convolution(n.res4b1_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4b1_branch2b = L.BatchNorm(n.res4b1_branch2b, in_place=True, use_global_stats=True)
    n.scale4b1_branch2b = L.Scale(n.res4b1_branch2b, in_place=True, bias_term=True)
    n.res4b1_branch2b_relu = L.ReLU(n.res4b1_branch2b, in_place=True)
    
    n.res4b1_branch2c = L.Convolution(n.res4b1_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b1_branch2c = L.BatchNorm(n.res4b1_branch2c, in_place=True, use_global_stats=True)
    n.scale4b1_branch2c = L.Scale(n.res4b1_branch2c, in_place=True, bias_term=True)

    n.res4b1 = L.Eltwise(n.res4a, n.res4b1_branch2c)
    n.res4b1_relu = L.ReLU(n.res4b1, in_place=True)
    
    n.res4b2_branch2a = L.Convolution(n.res4b1, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b2_branch2a = L.BatchNorm(n.res4b2_branch2a, in_place=True, use_global_stats=True)
    n.scale4b2_branch2a = L.Scale(n.res4b2_branch2a, in_place=True, bias_term=True)
    n.res4b2_branch2a_relu = L.ReLU(n.res4b2_branch2a, in_place=True)

    n.res4b2_branch2b = L.Convolution(n.res4b2_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4b2_branch2b = L.BatchNorm(n.res4b2_branch2b, in_place=True, use_global_stats=True)
    n.scale4b2_branch2b = L.Scale(n.res4b2_branch2b, in_place=True, bias_term=True)
    n.res4b2_branch2b_relu = L.ReLU(n.res4b2_branch2b, in_place=True)
    
    n.res4b2_branch2c = L.Convolution(n.res4b2_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b2_branch2c = L.BatchNorm(n.res4b2_branch2c, in_place=True, use_global_stats=True)
    n.scale4b2_branch2c = L.Scale(n.res4b2_branch2c, in_place=True, bias_term=True)

    n.res4b2 = L.Eltwise(n.res4b1, n.res4b2_branch2c)
    n.res4b2_relu = L.ReLU(n.res4b2, in_place=True)
    
    n.res4b3_branch2a = L.Convolution(n.res4b2, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b3_branch2a = L.BatchNorm(n.res4b3_branch2a, in_place=True, use_global_stats=True)
    n.scale4b3_branch2a = L.Scale(n.res4b3_branch2a, in_place=True, bias_term=True)
    n.res4b3_branch2a_relu = L.ReLU(n.res4b3_branch2a, in_place=True)

    n.res4b3_branch2b = L.Convolution(n.res4b3_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4b3_branch2b = L.BatchNorm(n.res4b3_branch2b, in_place=True, use_global_stats=True)
    n.scale4b3_branch2b = L.Scale(n.res4b3_branch2b, in_place=True, bias_term=True)
    n.res4b3_branch2b_relu = L.ReLU(n.res4b3_branch2b, in_place=True)
    
    n.res4b3_branch2c = L.Convolution(n.res4b3_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b3_branch2c = L.BatchNorm(n.res4b3_branch2c, in_place=True, use_global_stats=True)
    n.scale4b3_branch2c = L.Scale(n.res4b3_branch2c, in_place=True, bias_term=True)

    n.res4b3 = L.Eltwise(n.res4b2, n.res4b3_branch2c)
    n.res4b3_relu = L.ReLU(n.res4b3, in_place=True)
    
    n.res4b4_branch2a = L.Convolution(n.res4b3, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b4_branch2a = L.BatchNorm(n.res4b4_branch2a, in_place=True, use_global_stats=True)
    n.scale4b4_branch2a = L.Scale(n.res4b4_branch2a, in_place=True, bias_term=True)
    n.res4b4_branch2a_relu = L.ReLU(n.res4b4_branch2a, in_place=True)

    n.res4b4_branch2b = L.Convolution(n.res4b4_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4b4_branch2b = L.BatchNorm(n.res4b4_branch2b, in_place=True, use_global_stats=True)
    n.scale4b4_branch2b = L.Scale(n.res4b4_branch2b, in_place=True, bias_term=True)
    n.res4b4_branch2b_relu = L.ReLU(n.res4b4_branch2b, in_place=True)
    
    n.res4b4_branch2c = L.Convolution(n.res4b4_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b4_branch2c = L.BatchNorm(n.res4b4_branch2c, in_place=True, use_global_stats=True)
    n.scale4b4_branch2c = L.Scale(n.res4b4_branch2c, in_place=True, bias_term=True)

    n.res4b4 = L.Eltwise(n.res4b3, n.res4b4_branch2c)
    n.res4b4_relu = L.ReLU(n.res4b4, in_place=True)
    
    n.res4b5_branch2a = L.Convolution(n.res4b4, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b5_branch2a = L.BatchNorm(n.res4b5_branch2a, in_place=True, use_global_stats=True)
    n.scale4b5_branch2a = L.Scale(n.res4b5_branch2a, in_place=True, bias_term=True)
    n.res4b5_branch2a_relu = L.ReLU(n.res4b5_branch2a, in_place=True)

    n.res4b5_branch2b = L.Convolution(n.res4b5_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4b5_branch2b = L.BatchNorm(n.res4b5_branch2b, in_place=True, use_global_stats=True)
    n.scale4b5_branch2b = L.Scale(n.res4b5_branch2b, in_place=True, bias_term=True)
    n.res4b5_branch2b_relu = L.ReLU(n.res4b5_branch2b, in_place=True)
    
    n.res4b5_branch2c = L.Convolution(n.res4b5_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b5_branch2c = L.BatchNorm(n.res4b5_branch2c, in_place=True, use_global_stats=True)
    n.scale4b5_branch2c = L.Scale(n.res4b5_branch2c, in_place=True, bias_term=True)

    n.res4b5 = L.Eltwise(n.res4b4, n.res4b5_branch2c)
    n.res4b5_relu = L.ReLU(n.res4b5, in_place=True)
    
    n.res4b6_branch2a = L.Convolution(n.res4b5, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b6_branch2a = L.BatchNorm(n.res4b6_branch2a, in_place=True, use_global_stats=True)
    n.scale4b6_branch2a = L.Scale(n.res4b6_branch2a, in_place=True, bias_term=True)
    n.res4b6_branch2a_relu = L.ReLU(n.res4b6_branch2a, in_place=True)

    n.res4b6_branch2b = L.Convolution(n.res4b6_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4b6_branch2b = L.BatchNorm(n.res4b6_branch2b, in_place=True, use_global_stats=True)
    n.scale4b6_branch2b = L.Scale(n.res4b6_branch2b, in_place=True, bias_term=True)
    n.res4b6_branch2b_relu = L.ReLU(n.res4b6_branch2b, in_place=True)
    
    n.res4b6_branch2c = L.Convolution(n.res4b6_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b6_branch2c = L.BatchNorm(n.res4b6_branch2c, in_place=True, use_global_stats=True)
    n.scale4b6_branch2c = L.Scale(n.res4b6_branch2c, in_place=True, bias_term=True)

    n.res4b6 = L.Eltwise(n.res4b5, n.res4b6_branch2c)
    n.res4b6_relu = L.ReLU(n.res4b6, in_place=True)
        
    
    n.res4b7_branch2a = L.Convolution(n.res4b6, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b7_branch2a = L.BatchNorm(n.res4b7_branch2a, in_place=True, use_global_stats=True)
    n.scale4b7_branch2a = L.Scale(n.res4b7_branch2a, in_place=True, bias_term=True)
    n.res4b7_branch2a_relu = L.ReLU(n.res4b7_branch2a, in_place=True)

    n.res4b7_branch2b = L.Convolution(n.res4b7_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4b7_branch2b = L.BatchNorm(n.res4b7_branch2b, in_place=True, use_global_stats=True)
    n.scale4b7_branch2b = L.Scale(n.res4b7_branch2b, in_place=True, bias_term=True)
    n.res4b7_branch2b_relu = L.ReLU(n.res4b7_branch2b, in_place=True)
    
    n.res4b7_branch2c = L.Convolution(n.res4b7_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b7_branch2c = L.BatchNorm(n.res4b7_branch2c, in_place=True, use_global_stats=True)
    n.scale4b7_branch2c = L.Scale(n.res4b7_branch2c, in_place=True, bias_term=True)

    n.res4b7 = L.Eltwise(n.res4b6, n.res4b7_branch2c)
    n.res4b7_relu = L.ReLU(n.res4b7, in_place=True)
        
    
    n.res4b8_branch2a = L.Convolution(n.res4b7, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b8_branch2a = L.BatchNorm(n.res4b8_branch2a, in_place=True, use_global_stats=True)
    n.scale4b8_branch2a = L.Scale(n.res4b8_branch2a, in_place=True, bias_term=True)
    n.res4b8_branch2a_relu = L.ReLU(n.res4b8_branch2a, in_place=True)

    n.res4b8_branch2b = L.Convolution(n.res4b8_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4b8_branch2b = L.BatchNorm(n.res4b8_branch2b, in_place=True, use_global_stats=True)
    n.scale4b8_branch2b = L.Scale(n.res4b8_branch2b, in_place=True, bias_term=True)
    n.res4b8_branch2b_relu = L.ReLU(n.res4b8_branch2b, in_place=True)
    
    n.res4b8_branch2c = L.Convolution(n.res4b8_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b8_branch2c = L.BatchNorm(n.res4b8_branch2c, in_place=True, use_global_stats=True)
    n.scale4b8_branch2c = L.Scale(n.res4b8_branch2c, in_place=True, bias_term=True)

    n.res4b8 = L.Eltwise(n.res4b7, n.res4b8_branch2c)
    n.res4b8_relu = L.ReLU(n.res4b8, in_place=True)
        
    
    n.res4b9_branch2a = L.Convolution(n.res4b8, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b9_branch2a = L.BatchNorm(n.res4b9_branch2a, in_place=True, use_global_stats=True)
    n.scale4b9_branch2a = L.Scale(n.res4b9_branch2a, in_place=True, bias_term=True)
    n.res4b9_branch2a_relu = L.ReLU(n.res4b9_branch2a, in_place=True)

    n.res4b9_branch2b = L.Convolution(n.res4b9_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4b9_branch2b = L.BatchNorm(n.res4b9_branch2b, in_place=True, use_global_stats=True)
    n.scale4b9_branch2b = L.Scale(n.res4b9_branch2b, in_place=True, bias_term=True)
    n.res4b9_branch2b_relu = L.ReLU(n.res4b9_branch2b, in_place=True)
    
    n.res4b9_branch2c = L.Convolution(n.res4b9_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b9_branch2c = L.BatchNorm(n.res4b9_branch2c, in_place=True, use_global_stats=True)
    n.scale4b9_branch2c = L.Scale(n.res4b9_branch2c, in_place=True, bias_term=True)

    n.res4b9 = L.Eltwise(n.res4b8, n.res4b9_branch2c)
    n.res4b9_relu = L.ReLU(n.res4b9, in_place=True)
        
    
    n.res4b10_branch2a = L.Convolution(n.res4b9, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b10_branch2a = L.BatchNorm(n.res4b10_branch2a, in_place=True, use_global_stats=True)
    n.scale4b10_branch2a = L.Scale(n.res4b10_branch2a, in_place=True, bias_term=True)
    n.res4b10_branch2a_relu = L.ReLU(n.res4b10_branch2a, in_place=True)

    n.res4b10_branch2b = L.Convolution(n.res4b10_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4b10_branch2b = L.BatchNorm(n.res4b10_branch2b, in_place=True, use_global_stats=True)
    n.scale4b10_branch2b = L.Scale(n.res4b10_branch2b, in_place=True, bias_term=True)
    n.res4b10_branch2b_relu = L.ReLU(n.res4b10_branch2b, in_place=True)
    
    n.res4b10_branch2c = L.Convolution(n.res4b10_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b10_branch2c = L.BatchNorm(n.res4b10_branch2c, in_place=True, use_global_stats=True)
    n.scale4b10_branch2c = L.Scale(n.res4b10_branch2c, in_place=True, bias_term=True)

    n.res4b10 = L.Eltwise(n.res4b9, n.res4b10_branch2c)
    n.res4b10_relu = L.ReLU(n.res4b10, in_place=True)
        
    
    n.res4b11_branch2a = L.Convolution(n.res4b10, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b11_branch2a = L.BatchNorm(n.res4b11_branch2a, in_place=True, use_global_stats=True)
    n.scale4b11_branch2a = L.Scale(n.res4b11_branch2a, in_place=True, bias_term=True)
    n.res4b11_branch2a_relu = L.ReLU(n.res4b11_branch2a, in_place=True)

    n.res4b11_branch2b = L.Convolution(n.res4b11_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4b11_branch2b = L.BatchNorm(n.res4b11_branch2b, in_place=True, use_global_stats=True)
    n.scale4b11_branch2b = L.Scale(n.res4b11_branch2b, in_place=True, bias_term=True)
    n.res4b11_branch2b_relu = L.ReLU(n.res4b11_branch2b, in_place=True)
    
    n.res4b11_branch2c = L.Convolution(n.res4b11_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b11_branch2c = L.BatchNorm(n.res4b11_branch2c, in_place=True, use_global_stats=True)
    n.scale4b11_branch2c = L.Scale(n.res4b11_branch2c, in_place=True, bias_term=True)

    n.res4b11 = L.Eltwise(n.res4b10, n.res4b11_branch2c)
    n.res4b11_relu = L.ReLU(n.res4b11, in_place=True)
        
    
    n.res4b12_branch2a = L.Convolution(n.res4b11, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b12_branch2a = L.BatchNorm(n.res4b12_branch2a, in_place=True, use_global_stats=True)
    n.scale4b12_branch2a = L.Scale(n.res4b12_branch2a, in_place=True, bias_term=True)
    n.res4b12_branch2a_relu = L.ReLU(n.res4b12_branch2a, in_place=True)

    n.res4b12_branch2b = L.Convolution(n.res4b12_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4b12_branch2b = L.BatchNorm(n.res4b12_branch2b, in_place=True, use_global_stats=True)
    n.scale4b12_branch2b = L.Scale(n.res4b12_branch2b, in_place=True, bias_term=True)
    n.res4b12_branch2b_relu = L.ReLU(n.res4b12_branch2b, in_place=True)
    
    n.res4b12_branch2c = L.Convolution(n.res4b12_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b12_branch2c = L.BatchNorm(n.res4b12_branch2c, in_place=True, use_global_stats=True)
    n.scale4b12_branch2c = L.Scale(n.res4b12_branch2c, in_place=True, bias_term=True)

    n.res4b12 = L.Eltwise(n.res4b11, n.res4b12_branch2c)
    n.res4b12_relu = L.ReLU(n.res4b12, in_place=True)
        
    
    n.res4b13_branch2a = L.Convolution(n.res4b12, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b13_branch2a = L.BatchNorm(n.res4b13_branch2a, in_place=True, use_global_stats=True)
    n.scale4b13_branch2a = L.Scale(n.res4b13_branch2a, in_place=True, bias_term=True)
    n.res4b13_branch2a_relu = L.ReLU(n.res4b13_branch2a, in_place=True)

    n.res4b13_branch2b = L.Convolution(n.res4b13_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4b13_branch2b = L.BatchNorm(n.res4b13_branch2b, in_place=True, use_global_stats=True)
    n.scale4b13_branch2b = L.Scale(n.res4b13_branch2b, in_place=True, bias_term=True)
    n.res4b13_branch2b_relu = L.ReLU(n.res4b13_branch2b, in_place=True)
    
    n.res4b13_branch2c = L.Convolution(n.res4b13_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b13_branch2c = L.BatchNorm(n.res4b13_branch2c, in_place=True, use_global_stats=True)
    n.scale4b13_branch2c = L.Scale(n.res4b13_branch2c, in_place=True, bias_term=True)

    n.res4b13 = L.Eltwise(n.res4b12, n.res4b13_branch2c)
    n.res4b13_relu = L.ReLU(n.res4b13, in_place=True)
        
    
    n.res4b14_branch2a = L.Convolution(n.res4b13, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b14_branch2a = L.BatchNorm(n.res4b14_branch2a, in_place=True, use_global_stats=True)
    n.scale4b14_branch2a = L.Scale(n.res4b14_branch2a, in_place=True, bias_term=True)
    n.res4b14_branch2a_relu = L.ReLU(n.res4b14_branch2a, in_place=True)

    n.res4b14_branch2b = L.Convolution(n.res4b14_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4b14_branch2b = L.BatchNorm(n.res4b14_branch2b, in_place=True, use_global_stats=True)
    n.scale4b14_branch2b = L.Scale(n.res4b14_branch2b, in_place=True, bias_term=True)
    n.res4b14_branch2b_relu = L.ReLU(n.res4b14_branch2b, in_place=True)
    
    n.res4b14_branch2c = L.Convolution(n.res4b14_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b14_branch2c = L.BatchNorm(n.res4b14_branch2c, in_place=True, use_global_stats=True)
    n.scale4b14_branch2c = L.Scale(n.res4b14_branch2c, in_place=True, bias_term=True)

    n.res4b14 = L.Eltwise(n.res4b13, n.res4b14_branch2c)
    n.res4b14_relu = L.ReLU(n.res4b14, in_place=True)
        
    
    n.res4b15_branch2a = L.Convolution(n.res4b14, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b15_branch2a = L.BatchNorm(n.res4b15_branch2a, in_place=True, use_global_stats=True)
    n.scale4b15_branch2a = L.Scale(n.res4b15_branch2a, in_place=True, bias_term=True)
    n.res4b15_branch2a_relu = L.ReLU(n.res4b15_branch2a, in_place=True)

    n.res4b15_branch2b = L.Convolution(n.res4b15_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4b15_branch2b = L.BatchNorm(n.res4b15_branch2b, in_place=True, use_global_stats=True)
    n.scale4b15_branch2b = L.Scale(n.res4b15_branch2b, in_place=True, bias_term=True)
    n.res4b15_branch2b_relu = L.ReLU(n.res4b15_branch2b, in_place=True)
    
    n.res4b15_branch2c = L.Convolution(n.res4b15_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b15_branch2c = L.BatchNorm(n.res4b15_branch2c, in_place=True, use_global_stats=True)
    n.scale4b15_branch2c = L.Scale(n.res4b15_branch2c, in_place=True, bias_term=True)

    n.res4b15 = L.Eltwise(n.res4b14, n.res4b15_branch2c)
    n.res4b15_relu = L.ReLU(n.res4b15, in_place=True)
        
    
    n.res4b16_branch2a = L.Convolution(n.res4b15, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b16_branch2a = L.BatchNorm(n.res4b16_branch2a, in_place=True, use_global_stats=True)
    n.scale4b16_branch2a = L.Scale(n.res4b16_branch2a, in_place=True, bias_term=True)
    n.res4b16_branch2a_relu = L.ReLU(n.res4b16_branch2a, in_place=True)

    n.res4b16_branch2b = L.Convolution(n.res4b16_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4b16_branch2b = L.BatchNorm(n.res4b16_branch2b, in_place=True, use_global_stats=True)
    n.scale4b16_branch2b = L.Scale(n.res4b16_branch2b, in_place=True, bias_term=True)
    n.res4b16_branch2b_relu = L.ReLU(n.res4b16_branch2b, in_place=True)
    
    n.res4b16_branch2c = L.Convolution(n.res4b16_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b16_branch2c = L.BatchNorm(n.res4b16_branch2c, in_place=True, use_global_stats=True)
    n.scale4b16_branch2c = L.Scale(n.res4b16_branch2c, in_place=True, bias_term=True)

    n.res4b16 = L.Eltwise(n.res4b15, n.res4b16_branch2c)
    n.res4b16_relu = L.ReLU(n.res4b16, in_place=True)
        
    
    n.res4b17_branch2a = L.Convolution(n.res4b16, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b17_branch2a = L.BatchNorm(n.res4b17_branch2a, in_place=True, use_global_stats=True)
    n.scale4b17_branch2a = L.Scale(n.res4b17_branch2a, in_place=True, bias_term=True)
    n.res4b17_branch2a_relu = L.ReLU(n.res4b17_branch2a, in_place=True)

    n.res4b17_branch2b = L.Convolution(n.res4b17_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4b17_branch2b = L.BatchNorm(n.res4b17_branch2b, in_place=True, use_global_stats=True)
    n.scale4b17_branch2b = L.Scale(n.res4b17_branch2b, in_place=True, bias_term=True)
    n.res4b17_branch2b_relu = L.ReLU(n.res4b17_branch2b, in_place=True)
    
    n.res4b17_branch2c = L.Convolution(n.res4b17_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b17_branch2c = L.BatchNorm(n.res4b17_branch2c, in_place=True, use_global_stats=True)
    n.scale4b17_branch2c = L.Scale(n.res4b17_branch2c, in_place=True, bias_term=True)

    n.res4b17 = L.Eltwise(n.res4b16, n.res4b17_branch2c)
    n.res4b17_relu = L.ReLU(n.res4b17, in_place=True)
        
    
    n.res4b18_branch2a = L.Convolution(n.res4b17, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b18_branch2a = L.BatchNorm(n.res4b18_branch2a, in_place=True, use_global_stats=True)
    n.scale4b18_branch2a = L.Scale(n.res4b18_branch2a, in_place=True, bias_term=True)
    n.res4b18_branch2a_relu = L.ReLU(n.res4b18_branch2a, in_place=True)

    n.res4b18_branch2b = L.Convolution(n.res4b18_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4b18_branch2b = L.BatchNorm(n.res4b18_branch2b, in_place=True, use_global_stats=True)
    n.scale4b18_branch2b = L.Scale(n.res4b18_branch2b, in_place=True, bias_term=True)
    n.res4b18_branch2b_relu = L.ReLU(n.res4b18_branch2b, in_place=True)
    
    n.res4b18_branch2c = L.Convolution(n.res4b18_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b18_branch2c = L.BatchNorm(n.res4b18_branch2c, in_place=True, use_global_stats=True)
    n.scale4b18_branch2c = L.Scale(n.res4b18_branch2c, in_place=True, bias_term=True)

    n.res4b18 = L.Eltwise(n.res4b17, n.res4b18_branch2c)
    n.res4b18_relu = L.ReLU(n.res4b18, in_place=True)
        
    
    n.res4b19_branch2a = L.Convolution(n.res4b18, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b19_branch2a = L.BatchNorm(n.res4b19_branch2a, in_place=True, use_global_stats=True)
    n.scale4b19_branch2a = L.Scale(n.res4b19_branch2a, in_place=True, bias_term=True)
    n.res4b19_branch2a_relu = L.ReLU(n.res4b19_branch2a, in_place=True)

    n.res4b19_branch2b = L.Convolution(n.res4b19_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4b19_branch2b = L.BatchNorm(n.res4b19_branch2b, in_place=True, use_global_stats=True)
    n.scale4b19_branch2b = L.Scale(n.res4b19_branch2b, in_place=True, bias_term=True)
    n.res4b19_branch2b_relu = L.ReLU(n.res4b19_branch2b, in_place=True)
    
    n.res4b19_branch2c = L.Convolution(n.res4b19_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b19_branch2c = L.BatchNorm(n.res4b19_branch2c, in_place=True, use_global_stats=True)
    n.scale4b19_branch2c = L.Scale(n.res4b19_branch2c, in_place=True, bias_term=True)

    n.res4b19 = L.Eltwise(n.res4b18, n.res4b19_branch2c)
    n.res4b19_relu = L.ReLU(n.res4b19, in_place=True)
        
    
    n.res4b20_branch2a = L.Convolution(n.res4b19, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b20_branch2a = L.BatchNorm(n.res4b20_branch2a, in_place=True, use_global_stats=True)
    n.scale4b20_branch2a = L.Scale(n.res4b20_branch2a, in_place=True, bias_term=True)
    n.res4b20_branch2a_relu = L.ReLU(n.res4b20_branch2a, in_place=True)

    n.res4b20_branch2b = L.Convolution(n.res4b20_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4b20_branch2b = L.BatchNorm(n.res4b20_branch2b, in_place=True, use_global_stats=True)
    n.scale4b20_branch2b = L.Scale(n.res4b20_branch2b, in_place=True, bias_term=True)
    n.res4b20_branch2b_relu = L.ReLU(n.res4b20_branch2b, in_place=True)
    
    n.res4b20_branch2c = L.Convolution(n.res4b20_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b20_branch2c = L.BatchNorm(n.res4b20_branch2c, in_place=True, use_global_stats=True)
    n.scale4b20_branch2c = L.Scale(n.res4b20_branch2c, in_place=True, bias_term=True)

    n.res4b20 = L.Eltwise(n.res4b19, n.res4b20_branch2c)
    n.res4b20_relu = L.ReLU(n.res4b20, in_place=True)
        
    
    n.res4b21_branch2a = L.Convolution(n.res4b20, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b21_branch2a = L.BatchNorm(n.res4b21_branch2a, in_place=True, use_global_stats=True)
    n.scale4b21_branch2a = L.Scale(n.res4b21_branch2a, in_place=True, bias_term=True)
    n.res4b21_branch2a_relu = L.ReLU(n.res4b21_branch2a, in_place=True)

    n.res4b21_branch2b = L.Convolution(n.res4b21_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4b21_branch2b = L.BatchNorm(n.res4b21_branch2b, in_place=True, use_global_stats=True)
    n.scale4b21_branch2b = L.Scale(n.res4b21_branch2b, in_place=True, bias_term=True)
    n.res4b21_branch2b_relu = L.ReLU(n.res4b21_branch2b, in_place=True)
    
    n.res4b21_branch2c = L.Convolution(n.res4b21_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b21_branch2c = L.BatchNorm(n.res4b21_branch2c, in_place=True, use_global_stats=True)
    n.scale4b21_branch2c = L.Scale(n.res4b21_branch2c, in_place=True, bias_term=True)

    n.res4b21 = L.Eltwise(n.res4b20, n.res4b21_branch2c)
    n.res4b21_relu = L.ReLU(n.res4b21, in_place=True)
        
    
    n.res4b22_branch2a = L.Convolution(n.res4b21, num_output=256, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b22_branch2a = L.BatchNorm(n.res4b22_branch2a, in_place=True, use_global_stats=True)
    n.scale4b22_branch2a = L.Scale(n.res4b22_branch2a, in_place=True, bias_term=True)
    n.res4b22_branch2a_relu = L.ReLU(n.res4b22_branch2a, in_place=True)

    n.res4b22_branch2b = L.Convolution(n.res4b22_branch2a, num_output=256, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn4b22_branch2b = L.BatchNorm(n.res4b22_branch2b, in_place=True, use_global_stats=True)
    n.scale4b22_branch2b = L.Scale(n.res4b22_branch2b, in_place=True, bias_term=True)
    n.res4b22_branch2b_relu = L.ReLU(n.res4b22_branch2b, in_place=True)
    
    n.res4b22_branch2c = L.Convolution(n.res4b22_branch2b, num_output=1024, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn4b22_branch2c = L.BatchNorm(n.res4b22_branch2c, in_place=True, use_global_stats=True)
    n.scale4b22_branch2c = L.Scale(n.res4b22_branch2c, in_place=True, bias_term=True)

    n.res4b22 = L.Eltwise(n.res4b21, n.res4b22_branch2c)
    n.res4b22_relu = L.ReLU(n.res4b22, in_place=True)

    n.res5a_branch1 = L.Convolution(n.res4b22, num_output=2048, kernel_size=1, pad=0, stride=2, bias_term=False)
    n.bn5a_branch1 = L.BatchNorm(n.res5a_branch1, in_place=True, use_global_stats=True)
    n.scale5a_branch1 = L.Scale(n.res5a_branch1, in_place=True, bias_term=True)

    n.res5a_branch2a = L.Convolution(n.res4b22, num_output=512, kernel_size=1, pad=0, stride=2, bias_term=False)
    n.bn5a_branch2a = L.BatchNorm(n.res5a_branch2a, in_place=True, use_global_stats=True)
    n.scale5a_branch2a = L.Scale(n.res5a_branch2a, in_place=True, bias_term=True)
    n.res5a_branch2a_relu = L.ReLU(n.res5a_branch2a, in_place=True)

    n.res5a_branch2b = L.Convolution(n.res5a_branch2a, num_output=512, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn5a_branch2b = L.BatchNorm(n.res5a_branch2b, in_place=True, use_global_stats=True)
    n.scale5a_branch2b = L.Scale(n.res5a_branch2b, in_place=True, bias_term=True)
    n.res5a_branch2b_relu = L.ReLU(n.res5a_branch2b, in_place=True)
    
    n.res5a_branch2c = L.Convolution(n.res5a_branch2b, num_output=2048, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn5a_branch2c = L.BatchNorm(n.res5a_branch2c, in_place=True, use_global_stats=True)
    n.scale5a_branch2c = L.Scale(n.res5a_branch2c, in_place=True, bias_term=True)

    n.res5a = L.Eltwise(n.res5a_branch1, n.res5a_branch2c)
    n.res5a_relu = L.ReLU(n.res5a, in_place=True)
    
    n.res5b_branch2a = L.Convolution(n.res5a, num_output=512, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn5b_branch2a = L.BatchNorm(n.res5b_branch2a, in_place=True, use_global_stats=True)
    n.scale5b_branch2a = L.Scale(n.res5b_branch2a, in_place=True, bias_term=True)
    n.res5b_branch2a_relu = L.ReLU(n.res5b_branch2a, in_place=True)

    n.res5b_branch2b = L.Convolution(n.res5b_branch2a, num_output=512, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn5b_branch2b = L.BatchNorm(n.res5b_branch2b, in_place=True, use_global_stats=True)
    n.scale5b_branch2b = L.Scale(n.res5b_branch2b, in_place=True, bias_term=True)
    n.res5b_branch2b_relu = L.ReLU(n.res5b_branch2b, in_place=True)
    
    n.res5b_branch2c = L.Convolution(n.res5b_branch2b, num_output=2048, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn5b_branch2c = L.BatchNorm(n.res5b_branch2c, in_place=True, use_global_stats=True)
    n.scale5b_branch2c = L.Scale(n.res5b_branch2c, in_place=True, bias_term=True)

    n.res5b = L.Eltwise(n.res5a, n.res5b_branch2c)
    n.res5b_relu = L.ReLU(n.res5b, in_place=True)

    n.res5c_branch2a = L.Convolution(n.res5b, num_output=512, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn5c_branch2a = L.BatchNorm(n.res5c_branch2a, in_place=True, use_global_stats=True)
    n.scale5c_branch2a = L.Scale(n.res5c_branch2a, in_place=True, bias_term=True)
    n.res5c_branch2a_relu = L.ReLU(n.res5c_branch2a, in_place=True)

    n.res5c_branch2b = L.Convolution(n.res5c_branch2a, num_output=512, kernel_size=3, pad=1, stride=1, bias_term=False)
    n.bn5c_branch2b = L.BatchNorm(n.res5c_branch2b, in_place=True, use_global_stats=True)
    n.scale5c_branch2b = L.Scale(n.res5c_branch2b, in_place=True, bias_term=True)
    n.res5c_branch2b_relu = L.ReLU(n.res5c_branch2b, in_place=True)
    
    n.res5c_branch2c = L.Convolution(n.res5c_branch2b, num_output=2048, kernel_size=1, pad=0, stride=1, bias_term=False)
    n.bn5c_branch2c = L.BatchNorm(n.res5c_branch2c, in_place=True, use_global_stats=True)
    n.scale5c_branch2c = L.Scale(n.res5c_branch2c, in_place=True, bias_term=True)

    n.res5c = L.Eltwise(n.res5b, n.res5c_branch2c)
    n.res5c_relu = L.ReLU(n.res5c, in_place=True)

    n.pool5 = L.Pooling(n.res5c, kernel_size=7, stride=1, pool=P.Pooling.AVE)


    n.fc1000 =   L.InnerProduct(n.pool5, num_output=1000)
    # n.drop6 = L.Dropout(n.fc1000, in_place=True, dropout_ratio=0.5)


    n.loss =  L.SoftmaxWithLoss(n.fc1000, n.label)
    
    return n.to_proto()

def gen_solver(train_proto_path,validation_proto_path):
    solver = caffe_pb2.SolverParameter()
    solver.train_net= train_proto_path
    solver.test_net.extend([validation_proto_path])
    solver.test_iter.extend([1000])
    solver.test_interval= 1000
    solver.base_lr= 0.001
    solver.lr_policy= "step"
    solver.gamma= 0.1
    solver.stepsize= 2500
    solver.display= 50
    solver.max_iter= 40000
    solver.momentum= 0.9
    solver.weight_decay= 0.0005
    solver.snapshot= 5000
    solver.snapshot_prefix= "snapshots"
    solver.solver_mode= solver.GPU
    return str(solver)

def main_ras_net_101(train_proto_path,validation_proto_path):
    solver_proto_str = gen_solver(train_proto_path,validation_proto_path)
    solver_proto_path = 'solver_ras_net_101.prototxt'
    write_to_file(solver_proto_path, solver_proto_str);

    solver = None  # ignore this workaround for lmdb data (can't instantiate two solvers on the same data)
    solver = caffe.SGDSolver(solver_proto_path)

    # each output is (batch size, feature dim, spatial dim)
    aa = [(k, v.data.shape) for k, v in solver.net.blobs.items()]
    print aa


if __name__ == '__main__':
        from minitest import *
    
        with test(ras_net_101):
            DATA_PATH = "./data"
            mean_binary_path = os.path.join(DATA_PATH,'mean.binaryproto')
            train_lmdb_path = os.path.join(DATA_PATH,'train.lmdb')
            validation_lmdb_path = os.path.join(DATA_PATH,'validation.lmdb')            
            train_proto = ras_net_101(train_lmdb_path, 256, mean_binary_path)
            validation_proto = ras_net_101(validation_lmdb_path, 50, mean_binary_path)
            print type(train_proto)
            train_proto_path = "train_res_net_101.prototxt"
            validation_proto_path = "validation_res_net_101.prototxt"
            write_to_file(train_proto_path, str(train_proto))
            write_to_file(validation_proto_path, str(validation_proto))
            main_ras_net_101(train_proto_path,validation_proto_path)
            # 

