import numpy
import theano
import theano.tensor as T
import time
import theano.sandbox.cuda.basic_ops as cuda
rng = numpy.random

N = 4000
feats = 784
D = (rng.randn(N, feats).astype(theano.config.floatX),
rng.randint(size=N,low=0, high=2).astype(theano.config.floatX))
training_steps = 10000

# Declare Theano symbolic variables
x = theano.shared(D[0], name="x")
y = theano.shared(D[1], name="y")
w = theano.shared(rng.randn(feats).astype(theano.config.floatX), name="w")
b = theano.shared(numpy.asarray(0., dtype=theano.config.floatX), name="b")
x.tag.test_value = D[0]
y.tag.test_value = D[1]

# Construct Theano expression graph
# p_1 = 1 / (1 + T.exp(-T.dot(x, w)-b)) # Probability of having a one
# prediction = p_1 > 0.5 # The prediction that is done: 0 or 1
# xent = -y*T.log(p_1) - (1-y)*T.log(1-p_1) # Cross-entropy
# cost = xent.mean() + 0.01*(w**2).sum() # The cost to optimize
# gw,gb = T.grad(cost, [w,b])

p_1 = 1 / (1 + T.exp(-T.dot(x, w)-b)) # Probability of having a one
prediction = p_1 > 0.5 # The prediction that is done: 0 or 1
xent = -y*T.log(p_1) - (1-y)*T.log(1-p_1) # Cross-entropy
# prediction = theano.Out(cuda.gpu_from_host(T.cast(p_1 > 0.5,theano.config.floatX)),borrow=True) # The prediction that is done: 0 or 1
# xent = cuda.gpu_from_host(T.cast(-y*T.log(p_1) - (1-y)*T.log(1-p_1),theano.config.floatX)) # Cross-entropy
cost = xent.mean() + 0.01*(w**2).sum() # The cost to optimize
gw,gb = T.grad(cost, [w,b])
# cost = cuda.gpu_from_host(xent.mean() + 0.01*(w**2).sum()) # The cost to optimize
# gw,gb = cuda.gpu_from_host(T.grad(cost, [w,b]))


# Compile expressions to functions
train = theano.function(
            inputs=[],
            outputs=[theano.Out(cuda.gpu_from_host(T.cast(prediction,theano.config.floatX)),borrow=True), 
                theano.Out(cuda.gpu_from_host(T.cast(xent,theano.config.floatX)),borrow=True)],
            updates=[(w, w-0.01*gw), (b, b-0.01*gb)],
            name = "train")
predict = theano.function(inputs=[], outputs=theano.Out(cuda.gpu_from_host(T.cast(prediction,theano.config.floatX)),borrow=True),
            name = "predict")

if any([x.op.__class__.__name__ in ['Gemv', 'CGemv', 'Gemm', 'CGemm'] for x in
        train.maker.fgraph.toposort()]):
    print('Used the cpu')
elif any([x.op.__class__.__name__ in ['GpuGemm', 'GpuGemv'] for x in
          train.maker.fgraph.toposort()]):
    print('Used the gpu')
else:
    print('ERROR, not able to tell if theano used the cpu or the gpu')
    print(train.maker.fgraph.toposort())
t0 = time.time()

for i in range(training_steps):
    pred, err = train()
predict_result = predict()
t1 = time.time()

print("target values for D")
print(D[1])

print("prediction on D")
print(predict_result)

print("Took %f seconds" % (t1 - t0))

# THEANO_FLAGS=mode=FAST_RUN,device=gpu,floatX=float32 python gpu_logistic.py    
# THEANO_FLAGS=mode=FAST_RUN,device=cpu,floatX=float32 python cpu_logistic.py    

# export CUDA_LAUNCH_BLOCKING=1
# THEANO_FLAGS=mode=FAST_RUN,device=gpu,floatX=float32,profile=True python gpu_logistic.py    
# THEANO_FLAGS=mode=FAST_RUN,device=cpu,floatX=float32,profile=True python cpu_logistic.py    

# export CUDA_LAUNCH_BLOCKING=0


