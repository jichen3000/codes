from theano import function, config, shared, sandbox
import theano.tensor as T
import numpy
import time

vlen = 10 * 30 * 768  # 10 x #cores x # threads per core
iters = 1000

rng = numpy.random.RandomState(22)
x = shared(numpy.asarray(rng.rand(vlen), config.floatX))
f = function([], T.exp(x))
print(f.maker.fgraph.toposort())
t0 = time.time()
for i in range(iters):
    r = f()
t1 = time.time()
print("Looping %d times took %f seconds" % (iters, t1 - t0))
print("Result is %s" % (r,))
if numpy.any([isinstance(x.op, T.Elemwise) for x in f.maker.fgraph.toposort()]):
    print('Used the cpu')
else:
    print('Used the gpu')

# run
# THEANO_FLAGS=mode=FAST_RUN,device=cpu,floatX=float32 python cpu_gpu_compare.py    
# THEANO_FLAGS=mode=FAST_RUN,device=gpu,floatX=float32 python cpu_gpu_compare.py    


# Using gpu device 0: GeForce GTX 660 (CNMeM is disabled, cuDNN 4007)
# [GpuElemwise{exp,no_inplace}(<CudaNdarrayType(float32, vector)>), HostFromGpu(GpuElemwise{exp,no_inplace}.0)]
# Looping 1000 times took 0.609864 seconds

# [Elemwise{exp,no_inplace}(<TensorType(float32, vector)>)]
# Looping 1000 times took 1.859757 seconds