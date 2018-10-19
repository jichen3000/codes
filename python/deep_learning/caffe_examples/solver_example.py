# http://itinerantbioinformaticist.blogspot.com/2015/12/how-to-parse-caffe-deployprototxt-file.html
# https://developers.google.com/protocol-buffers/docs/reference/python-generated?csw=1#fields

from caffe.proto import caffe_pb2

def gen_solver():
    solver = caffe_pb2.SolverParameter()
    solver.train_net= "train.prototxt"
    solver.test_net.extend(["validation.prototxt"])
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


if __name__ == '__main__':
    from minitest import *

    with test(gen_solver):
        print gen_solver()

