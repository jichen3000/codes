## wget https://www.dropbox.com/s/h4no2pm970im82k/data.npy
## wget https://www.dropbox.com/s/2vjan6mbcf2fsit/target.npy

import os 
import minitest
import numpy as np
import lasagne
import theano.tensor as T
import theano
from sklearn.metrics import roc_auc_score
import time

import Unet

def get_data_set():
    CUR_DIR = os.getcwd()
    data_path = CUR_DIR.replace("work","data")
    data_path.p()

    origin_data = np.load(os.path.join(data_path,"data.npy")).astype('float32')
    origin_labels = np.load(os.path.join(data_path,"target.npy")).astype('uint8')

    all_labels = origin_labels
    all_labels[all_labels>0]=1

    all_data = origin_data
    mean = np.mean(all_data)  # mean for data centering
    # notice, this is different with 3d_net
    std = np.std(all_data)  # std for data normalization

    all_data -= mean
    all_data /= std

    return all_data[0:200], all_labels[0:200], all_data[200:], all_labels[200:]

train_data, train_labels, valid_data, valid_labels = get_data_set()

BATCH_SIZE = 1
PATCH_SIZE = 128
net = Unet.build_UNet(n_input_channels=1, BATCH_SIZE=BATCH_SIZE, num_output_classes=2, pad='same',
         nonlinearity=lasagne.nonlinearities.elu, input_dim=(PATCH_SIZE, PATCH_SIZE),depth=128,
         base_n_filters=24,kernel_size=3, do_dropout=True)

#Point network's output layer to output_layer_for_loss parameter parameter for later use
output_layer_for_loss = net["output_flattened"]


#Some sanity check to see shape information for specific layers' outputs
print "Net output shape", net['output_segmentation'].output_shape
print "output_layer_for_loss", output_layer_for_loss.output_shape

#Class distribution between the two classes
class_frequencies = np.array([np.sum(train_labels == 0) ,
                              np.sum(train_labels == 1)  ])

# We are taking the log here because we want the net to focus more on the foreground pixels but not too much (otherwise
# it would not be penalized enough for missclassifying terrain pixels which results in too many false positives)
class_weights = np.log(class_frequencies[[1,0]])
class_weights = class_weights / np.sum(class_weights) * 2.
class_weights = class_weights.astype(np.float32)


#Tensors
x_sym = T.TensorType('float32',(False,)*5) ('inputs') #Input tensor (i.e. images)
seg_sym = T.ivector() #Target tensor (i.e. segmented images)
w_sym = T.vector() #Weight tensor for initializtion (i.e. see class_weights above)

#Add some weight decay for more regulization to the loss function
l2_loss = lasagne.regularization.regularize_network_params(output_layer_for_loss, lasagne.regularization.l2) * 1e-4
#This is prediction function
prediction_train = lasagne.layers.get_output(output_layer_for_loss, x_sym, deterministic=False)
# This is the main loss function. We could use a binary loss but I stuck with categorical crossentropy so that less code has to be changed if your
# application has more than two classes
loss_train = lasagne.objectives.categorical_crossentropy(prediction_train, seg_sym)
# We multiply our loss by a weight map. In this example the weight map only increases the loss for foreground pixels and
# decreases the loss for other pixels. We do this to ensure that the network puts more focus on getting the foreground right
loss_train *= w_sym
loss_train = loss_train.mean()
loss_train += l2_loss

#This is the accuracy function
acc_train = T.mean(T.eq(T.argmax(prediction_train, axis=1), seg_sym), dtype=theano.config.floatX)


#Repeat the same code for the testing phase. This phase is deterministic. The parameters (i.e. weights, biases) do not update during test phase

#This is prediction function
prediction_test = lasagne.layers.get_output(output_layer_for_loss, x_sym, deterministic=True)
# This is the main loss function. We could use a binary loss but I stuck with categorical crossentropy so that less code has to be changed if your
# application has more than two classes
loss_test = lasagne.objectives.categorical_crossentropy(prediction_test, seg_sym)
# We multiply our loss by a weight map. In this example the weight map only increases the loss for foreground pixels and
# decreases the loss for other pixels. We do this to ensure that the network puts more focus on getting the foreground right
loss_test *= w_sym
loss_test = loss_test.mean()
loss_test += l2_loss

#This is the accuracy function
acc_test = T.mean(T.eq(T.argmax(prediction_test, axis=1), seg_sym), dtype=theano.config.floatX)

#Use params to point to the network parameters
params = lasagne.layers.get_all_params(output_layer_for_loss, trainable=True)

#Learning rate has to be a shared variable because we decrease it with every epoch
learning_rate = theano.shared(np.float32(0.001))

#Use adam optimizer to update the parameters based on loss and learning rate
updates = lasagne.updates.adam(loss_train, params, learning_rate=learning_rate)

#Create a convenience function get_segmentation to get the segmentation
seg_output = lasagne.layers.get_output(net["output_segmentation"], x_sym, deterministic=True)
get_segmentation = theano.function([x_sym], seg_output)


#This is the training function. It takes 3 inputs: x_sym, seg_sym, w_sym and it outputs loss, acc_train and it calls updates to update the network
train_fn = theano.function([x_sym, seg_sym, w_sym], [loss_train, acc_train], updates=updates, allow_input_downcast=True)

#This is the testing/validation function. It takes 3 inputs: x_sym, seg_sym, w_sym and it outputs loss_test, acc
val_fn = theano.function([x_sym, seg_sym, w_sym], [loss_test, acc_test],  allow_input_downcast=True)

#We need this for calculating the AUC score
get_class_probas = theano.function([x_sym], prediction_test)

print "Started experiment"

def batch_generator(data, target, BATCH_SIZE, shuffle=False):
    if shuffle:
        np.random.seed(123)
        while True:
            ids = np.random.choice(len(data), BATCH_SIZE)
            yield data[ids], target[ids]
    else:
        for idx in range(0, len(data), BATCH_SIZE):
            ids = slice(idx, idx + BATCH_SIZE)
            yield data[ids], target[ids]
            

N_EPOCHS = 10
N_BATCHES_PER_EPOCH = 1
# N_BATCHES_PER_EPOCH = 100
test_count = 1
# test_count = 20
start_time = time.time()

for epoch in range(N_EPOCHS):
    train_generator = batch_generator(train_data, train_labels, BATCH_SIZE, shuffle=True)

    epoch_start_time = time.time()
    #Training phase
    losses_train = []
    n_batches = 0
    accuracies_train = []
    for data, label in train_generator:
        label_flat = label.ravel()
        loss, acc = train_fn(data.astype(np.float32), label_flat,class_weights[label_flat])
        losses_train.append(loss)
        accuracies_train.append(acc)
        n_batches += 1
        if n_batches >= N_BATCHES_PER_EPOCH:
            break
    print "epoch: ", epoch, "\ntrain accuracy: ", np.mean(accuracies_train), " train loss: ", np.mean(losses_train)
    epoch_end_time = time.time()
    print('%s took %0.3f ms' % ("epoch train", (epoch_end_time-epoch_start_time)*1000.0))

    losses_val = []
    accuracies_val = []
    auc_val = []
    dice = []
    test_index = 0
    #Testing phase
    validation_generator = batch_generator(valid_data, valid_labels, BATCH_SIZE, shuffle=False)
    for data, label in validation_generator:
        label_flat = label.ravel()
        loss, acc = val_fn(data.astype(np.float32), label_flat, class_weights[label_flat])
        losses_val.append(loss)
        accuracies_val.append(acc)
        auc_val.append(roc_auc_score(label_flat, get_class_probas(data)[:, 1]))
        test_index += 1
        if test_index >= test_count:
            break
    print "val accuracy: ", np.mean(accuracies_val), " val loss: ", np.mean(losses_val), "auc: ", np.mean(auc_val)
    learning_rate *= 0.2
    epoch_end_time = time.time()
    print('%s took %0.3f ms' % ("epoch valid", (time.time()-epoch_end_time)*1000.0))
    # save trained parameters after each epoch so that we get a snapshot of the network
    # import cPickle
    # with open("UNet_params_ep%03.0f.pkl"%epoch, 'w') as f:
    #     cPickle.dump(lasagne.layers.get_all_param_values(output_layer_for_loss), f)

now_time = time.time()
print('%s took %0.3f ms' % ("all", (now_time-start_time)*1000.0))
# all took 238109.098 ms


prediction_test_fn = theano.function([x_sym], [prediction_test],  allow_input_downcast=True) 
validation_generator = batch_generator(valid_data, valid_labels, BATCH_SIZE, shuffle=False)
cur_data, cur_label = validation_generator.next()  
label_flat = cur_label.ravel()
prediction_value, = prediction_test_fn(cur_data)

np.unique(prediction_value[...,0], return_counts=True)

# In [19]: np.sum(prediction_value[...,0] > 0.5)
# Out[19]: 88433

# In [20]: np.sum(prediction_value[...,0] <= 0.5)
# Out[20]: 2008719

# In [21]: np.sum(label_flat > 0.5)
# Out[21]: 34973

# In [22]: np.sum(label_flat <= 0.5)
# Out[22]: 2062179

