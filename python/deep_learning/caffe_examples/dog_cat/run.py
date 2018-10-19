import time
import os
import caffe
from caffe import layers as L, params as P
from caffe.proto import caffe_pb2

# all conv layers use half num_output
def alex_net_1_half(lmdb_path, batch_size, mean_file_path, has_accuracy=False):
    the_param = [dict(lr_mult=1,decay_mult=1),dict(lr_mult=2,decay_mult=0)]

    # our version of LeNet: a series of linear and simple nonlinear transformations
    n = caffe.NetSpec()

    n.data, n.label = L.Data(batch_size=batch_size, backend=P.Data.LMDB, source=lmdb_path,
            transform_param=dict(mirror=True,crop_size=227,mean_file=mean_file_path), 
            ntop=2)
    
    n.conv1 = L.Convolution(n.data, num_output=32, kernel_size=11, stride=4, 
            weight_filler=dict(type='gaussian',std=0.01),
            bias_filler=dict(type='constant',value=0),
            param=the_param)
    n.relu1 = L.ReLU(n.conv1, in_place=True)
    n.pool1 = L.Pooling(n.relu1, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.norm1 = L.LRN(n.pool1, local_size=5, alpha=0.0001, beta=0.75)

    n.conv2 = L.Convolution(n.norm1, num_output=96, kernel_size=5, pad=2, #group=2,
            weight_filler=dict(type='gaussian',std=0.01),
            bias_filler=dict(type='constant',value=0),
            param=the_param)
    n.relu2 = L.ReLU(n.conv2, in_place=True)
    n.pool2 = L.Pooling(n.relu2, kernel_size=3, stride=2, pool=P.Pooling.MAX)
    n.norm2 = L.LRN(n.pool2, local_size=5, alpha=0.0001, beta=0.75)

    # why this conv3 is not group=2
    n.conv3 = L.Convolution(n.norm2, num_output=192, kernel_size=3, pad=1,
            weight_filler=dict(type='gaussian',std=0.01),
            bias_filler=dict(type='constant',value=0),
            param=the_param)
    n.relu3 = L.ReLU(n.conv3, in_place=True)

    n.conv4 = L.Convolution(n.relu3, num_output=192, kernel_size=3, pad=1, #group=2,
            weight_filler=dict(type='gaussian',std=0.01),
            bias_filler=dict(type='constant',value=0),
            param=the_param)
    n.relu4 = L.ReLU(n.conv4, in_place=True)

    n.conv5 = L.Convolution(n.relu4, num_output=128, kernel_size=3, pad=1, #group=2,
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
    train_lmdb_path = os.path.join(DATA_PATH,'train.lmdb')
    validation_lmdb_path = os.path.join(DATA_PATH,'validation.lmdb')
    mean_binary_path = os.path.join(DATA_PATH,'mean.binaryproto')

    train_proto = str(alex_net_1_half(train_lmdb_path, 256, mean_binary_path))
    # print train_proto
    validation_proto = str(alex_net_1_half(validation_lmdb_path, 50, mean_binary_path))

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

    # start = time.time()
    # caffe.set_device(0)
    # caffe.set_mode_gpu()
    # solver.step(1)
    # end = time.time()
    # print "time:",end-start

def gen_solver_vgg_16():
    solver = caffe_pb2.SolverParameter()
    solver.train_net= "train_vgg_16.prototxt"
    solver.test_net.extend(["validation_vgg_16.prototxt"])
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

def main_vgg_16():
    solver_proto_str = gen_solver_vgg_16()
    solver_proto_path = 'solver_vgg_16.prototxt'
    write_to_file(solver_proto_path, solver_proto_str);

    solver = None  # ignore this workaround for lmdb data (can't instantiate two solvers on the same data)
    solver = caffe.SGDSolver(solver_proto_path)

    # each output is (batch size, feature dim, spatial dim)
    aa = [(k, v.data.shape) for k, v in solver.net.blobs.items()]
    print aa

# main_vgg_16()
# alex_net need 3.4G memory
# vgg_16 need 6G memory

# main(), step(1) 77s
main()
print "ok"