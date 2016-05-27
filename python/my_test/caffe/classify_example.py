# set up Python environment: numpy for numerical routines, and matplotlib for plotting
import numpy as np
import matplotlib.pyplot as plt
# display plots in this notebook

import os
import caffe
# import os
# os.getenv('CAFFE_ROOT')

# # The caffe module needs to be on the Python path;
# #  we'll add it here explicitly.
# import sys
# caffe_root = os.getenv('CAFFE_ROOT')  # this file should be run from {caffe_root}/examples (otherwise change this line)
# sys.path.insert(0, caffe_root + 'python')

def setup():
    %matplotlib osx

    # set display defaults
    plt.rcParams['figure.figsize'] = (10, 10)        # large images
    plt.rcParams['image.interpolation'] = 'nearest'  # don't interpolate: show square pixels
    plt.rcParams['image.cmap'] = 'gray'  # use grayscale output rather than a (potentially misleading) color heatmap


def load_net():
    caffe.set_mode_cpu()
    model_weights_path = os.path.join('big_data','bvlc_reference_caffenet.caffemodel')
    model_def_path = os.path.join('small_data','bvlc_reference_caffenet/deploy.prototxt')
    net = caffe.Net(model_def_path,      # defines the structure of the model
                model_weights_path,  # contains the trained weights
                caffe.TEST)     # use test mode (e.g., don't perform dropout)

    # load the mean ImageNet image (as distributed with Caffe) for subtraction
    mu_path = os.path.join('small_data','ilsvrc_2012_mean.npy')
    mu = np.load(mu_path)
    # average over pixels to obtain the mean (BGR) pixel values
    mu = mu.mean(1).mean(1)
    print 'mean-subtracted values:', zip('BGR', mu)

    # net.blobs['data'].data.shape
    # (10, 3, 227, 227)
    # create transformer for the input called 'data'
    transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})

    transformer.set_transpose('data', (2,0,1))  # move image channels to outermost dimension
    transformer.set_mean('data', mu)            # subtract the dataset-mean value in each channel
    transformer.set_raw_scale('data', 255)      # rescale from [0, 1] to [0, 255]
    transformer.set_channel_swap('data', (2,1,0))  # swap channels from RGB to BGR

def classify():
    # set the size of the input (we can skip this if we're happy
    #  with the default; we can also change it later, e.g., for different batch sizes)
    net.blobs['data'].reshape(50,        # batch size
                              3,         # 3-channel (BGR) images
                              227, 227)  # image size is 227x227

    # image_path = os.path.join('small_data', 'cat.jpg')
    image_path = os.path.join('big_data', 'bridge.jpg')
    image = caffe.io.load_image(image_path)
    transformed_image = transformer.preprocess('data', image)
    plt.imshow(image)

    # copy the image data into the memory allocated for the net
    net.blobs['data'].data[...] = transformed_image

    ### perform classification
    output = net.forward()

    output_prob = output['prob'][0]  # the output probability vector for the first image in the batch

    print 'predicted class is:', output_prob.argmax()

    # load ImageNet labels
    labels_path = os.path.join('big_data', 'synset_words.txt')
    labels = np.loadtxt(labels_path, str, delimiter='\t')

    print 'output label:', labels[output_prob.argmax()]

    # sort top five predictions from softmax output
    top_inds = output_prob.argsort()[::-1][:5]  # reverse sort and take five largest items

    print 'probabilities and labels:'
    zip(output_prob[top_inds], labels[top_inds])

def compare_to_gpu():
    %timeit net.forward()

    caffe.set_device(0)  # if we have multiple GPUs, pick the first one
    caffe.set_mode_gpu()
    net.forward()  # run once before timing to set up memory
    %timeit net.forward()

def show_intermediate_output():
    # for each layer, show the output shape
    #  (batch_size, channel_dim, height, width).
    # fc FullyConnected
    # conv  Convolution
    for layer_name, blob in net.blobs.iteritems():
        print layer_name + '\t' + str(blob.data.shape)    
    # data    (10, 3, 227, 227)
    # conv1   (10, 96, 55, 55)
    # pool1   (10, 96, 27, 27)
    # norm1   (10, 96, 27, 27)
    # conv2   (10, 256, 27, 27)
    # pool2   (10, 256, 13, 13)
    # norm2   (10, 256, 13, 13)
    # conv3   (10, 384, 13, 13)
    # conv4   (10, 384, 13, 13)
    # conv5   (10, 256, 13, 13)
    # pool5   (10, 256, 6, 6)
    # fc6 (10, 4096)
    # fc7 (10, 4096)
    # fc8 (10, 1000)
    # prob    (10, 1000)

    # (output_channels, input_channels, filter_height, filter_width)
    # and bias
    for layer_name, param in net.params.iteritems():
        print layer_name + '\t' + str(param[0].data.shape), str(param[1].data.shape)
    # conv1   (96, 3, 11, 11) (96,)
    # conv2   (256, 48, 5, 5) (256,)
    # conv3   (384, 256, 3, 3) (384,)
    # conv4   (384, 192, 3, 3) (384,)
    # conv5   (256, 192, 3, 3) (256,)
    # fc6 (4096, 9216) (4096,)
    # fc7 (4096, 4096) (4096,)
    # fc8 (1000, 4096) (1000,)

    # First we'll look at the first layer filters, conv1
    # the parameters are a list of [weights, biases]
    filters = net.params['conv1'][0].data
    vis_square(filters.transpose(0, 2, 3, 1),plt)

    # The first layer output, conv1 (rectified responses of the filters above, first 36 only)
    feat = net.blobs['conv1'].data[0, :36]
    vis_square(feat,plt)

    # The fifth layer after pooling, pool5
    feat = net.blobs['pool5'].data[0]
    vis_square(feat,plt)

    # The first fully connected layer, fc6 (rectified)
    feat = net.blobs['fc6'].data[0]
    plt.subplot(2, 1, 1)
    plt.plot(feat.flat)
    plt.subplot(2, 1, 2)
    _ = plt.hist(feat.flat[feat.flat > 0], bins=100)

    # The final probability output, prob
    feat = net.blobs['prob'].data[0]
    plt.figure(figsize=(15, 3))
    plt.plot(feat.flat)

def vis_square(data):
    """Take an array of shape (n, height, width) or (n, height, width, 3)
       and visualize each (height, width) thing in a grid of size approx. sqrt(n) by sqrt(n)"""
    
    # normalize data for display
    data = (data - data.min()) / (data.max() - data.min())
    
    # force the number of filters to be square
    n = int(np.ceil(np.sqrt(data.shape[0])))
    padding = (((0, n ** 2 - data.shape[0]),
               (0, 1), (0, 1))                 # add some space between filters
               + ((0, 0),) * (data.ndim - 3))  # don't pad the last dimension (if there is one)
    data = np.pad(data, padding, mode='constant', constant_values=1)  # pad with ones (white)
    
    # tile the filters into an image
    data = data.reshape((n, n) + data.shape[1:]).transpose((0, 2, 1, 3) + tuple(range(4, data.ndim + 1)))
    data = data.reshape((n * data.shape[1], n * data.shape[3]) + data.shape[4:])
    
    plt.imshow(data); plt.axis('off')

def main():
    setup()

