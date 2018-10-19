

from collections import OrderedDict
from lasagne.layers import InputLayer, ConcatLayer, ReshapeLayer, DimshuffleLayer, NonlinearityLayer, DropoutLayer, Upscale2DLayer, Upscale3DLayer, BatchNormLayer
from lasagne.layers.dnn import Conv3DDNNLayer as ConvLayer, Pool3DDNNLayer as PoolLayer
import lasagne
from lasagne.init import HeNormal

def build_UNet(n_input_channels=1, BATCH_SIZE=None, num_output_classes=2, pad='same', nonlinearity=lasagne.nonlinearities.elu, input_dim=(128, 128), depth=32, base_n_filters=32, kernel_size=3, do_dropout=False):
    net = OrderedDict()
    net['input'] = InputLayer((BATCH_SIZE, n_input_channels, depth, input_dim[0], input_dim[1]))

    net['contr_1_1'] = BatchNormLayer(ConvLayer(net['input'], base_n_filters, kernel_size, nonlinearity=nonlinearity, pad=pad, W=HeNormal(gain="relu")))    
    # net['contr_1_1'] = ConvLayer(net['input'], base_n_filters, kernel_size, nonlinearity=nonlinearity, pad=pad, W=HeNormal(gain="relu"))
    net['contr_1_2'] = ConvLayer(net['contr_1_1'], base_n_filters*2, kernel_size, nonlinearity=nonlinearity, pad=pad) #64
    net['pool1'] = PoolLayer(net['contr_1_2'], 2)

    net['contr_2_1'] = ConvLayer(net['pool1'], base_n_filters*2, kernel_size, nonlinearity=nonlinearity, pad=pad) #64
    net['contr_2_2'] = ConvLayer(net['contr_2_1'], base_n_filters*4, kernel_size, nonlinearity=nonlinearity, pad=pad) #128
    net['pool2'] = PoolLayer(net['contr_2_2'], 2)
 
    net['contr_3_1'] = ConvLayer(net['pool2'], base_n_filters*4, 3, nonlinearity=nonlinearity, pad=pad) #128
    net['contr_3_2'] = ConvLayer(net['contr_3_1'], base_n_filters*8, kernel_size, nonlinearity=nonlinearity, pad=pad) #256
    l=net['pool3'] = PoolLayer(net['contr_3_2'], 2)

    # the paper does not really describe where and how dropout is added. Feel free to try more options
    if do_dropout:
        l = DropoutLayer(l, p=0.4)

    net['encode_1'] = ConvLayer(l, base_n_filters*8, kernel_size, nonlinearity=nonlinearity, pad=pad) #256
    net['encode_2'] = ConvLayer(net['encode_1'], base_n_filters*16, kernel_size, nonlinearity=nonlinearity, pad=pad) #512
    net['upscale1'] = Upscale3DLayer(net['encode_2'], 2)


    net['concat1'] = ConcatLayer([net['upscale1'], net['contr_3_2']], cropping=(None, None, "center", "center"))
    net['expand_1_1'] = ConvLayer(net['concat1'], base_n_filters*8, kernel_size, nonlinearity=nonlinearity, pad=pad)
    net['expand_1_2'] = ConvLayer(net['expand_1_1'], base_n_filters*8, kernel_size, nonlinearity=nonlinearity, pad=pad)
    net['upscale2'] = Upscale3DLayer(net['expand_1_2'], 2)

    net['concat2'] = ConcatLayer([net['upscale2'], net['contr_2_2']], cropping=(None, None, "center", "center"))
    net['expand_2_1'] = ConvLayer(net['concat2'], base_n_filters*4, kernel_size, nonlinearity=nonlinearity, pad=pad)
    net['expand_2_2'] = ConvLayer(net['expand_2_1'], base_n_filters*4, kernel_size, nonlinearity=nonlinearity, pad=pad)
    net['upscale3'] = Upscale3DLayer(net['expand_2_2'], 2)
  
    net['concat3'] = ConcatLayer([net['upscale3'], net['contr_1_2']], cropping=(None, None, "center", "center"))
    net['expand_3_1'] = ConvLayer(net['concat3'], base_n_filters*2, kernel_size, nonlinearity=nonlinearity, pad=pad)
    net['expand_3_2'] = ConvLayer(net['expand_3_1'], base_n_filters*2, kernel_size, nonlinearity=nonlinearity, pad=pad)


    net['output_segmentation'] = ConvLayer(net['expand_3_2'], num_output_classes, 1, nonlinearity=None)
    
    
    net['dimshuffle'] = DimshuffleLayer(net['output_segmentation'], (1, 0, 2, 3, 4))
    net['reshapeSeg'] = ReshapeLayer(net['dimshuffle'], (num_output_classes, -1))
    print "net['reshapeSeg'] ", net['reshapeSeg'].output_shape

    net['dimshuffle2'] = DimshuffleLayer(net['reshapeSeg'], (1, 0))
    net['output_flattened'] = NonlinearityLayer(net['dimshuffle2'], nonlinearity=lasagne.nonlinearities.softmax)

    return net

def build_UNet_01(n_input_channels=1, BATCH_SIZE=None, num_output_classes=2, pad='same', nonlinearity=lasagne.nonlinearities.elu, input_dim=(128, 128), depth=32, base_n_filters=32, kernel_size=3, do_dropout=False):
    net = OrderedDict()
    net['input'] = InputLayer((BATCH_SIZE, n_input_channels, depth, input_dim[0], input_dim[1]))

    net['contr_1_1'] = BatchNormLayer(ConvLayer(net['input'], base_n_filters, kernel_size, nonlinearity=nonlinearity, pad=pad, W=HeNormal(gain="relu")))    
    net['contr_1_2'] = ConvLayer(net['contr_1_1'], base_n_filters*2, kernel_size, nonlinearity=nonlinearity, pad=pad) #64
    net['pool1'] = PoolLayer(net['contr_1_2'], 2)

    net['contr_2_1'] = ConvLayer(net['pool1'], base_n_filters*2, kernel_size, nonlinearity=nonlinearity, pad=pad) #64
    net['contr_2_2'] = ConvLayer(net['contr_2_1'], base_n_filters*4, kernel_size, nonlinearity=nonlinearity, pad=pad) #128
    net['pool2'] = PoolLayer(net['contr_2_2'], 2)
 
    net['contr_3_1'] = ConvLayer(net['pool2'], base_n_filters*4, 3, nonlinearity=nonlinearity, pad=pad) #128
    net['contr_3_2'] = ConvLayer(net['contr_3_1'], base_n_filters*8, kernel_size, nonlinearity=nonlinearity, pad=pad) #256
    l=net['pool3'] = PoolLayer(net['contr_3_2'], 2)

    # the paper does not really describe where and how dropout is added. Feel free to try more options
    if do_dropout:
        l = DropoutLayer(l, p=0.4)

    net['encode_1'] = ConvLayer(l, base_n_filters*8, kernel_size, nonlinearity=nonlinearity, pad=pad) #256
    net['encode_2'] = ConvLayer(net['encode_1'], base_n_filters*16, kernel_size, nonlinearity=nonlinearity, pad=pad) #512
    net['upscale1'] = Upscale3DLayer(net['encode_2'], 2)


    net['concat1'] = ConcatLayer([net['upscale1'], net['contr_3_2']], cropping=(None, None, "center", "center"))
    net['expand_1_1'] = ConvLayer(net['concat1'], base_n_filters*8, kernel_size, nonlinearity=nonlinearity, pad=pad)
    net['expand_1_2'] = ConvLayer(net['expand_1_1'], base_n_filters*8, kernel_size, nonlinearity=nonlinearity, pad=pad)
    net['upscale2'] = Upscale3DLayer(net['expand_1_2'], 2)

    net['concat2'] = ConcatLayer([net['upscale2'], net['contr_2_2']], cropping=(None, None, "center", "center"))
    net['expand_2_1'] = ConvLayer(net['concat2'], base_n_filters*4, kernel_size, nonlinearity=nonlinearity, pad=pad)
    net['expand_2_2'] = ConvLayer(net['expand_2_1'], base_n_filters*4, kernel_size, nonlinearity=nonlinearity, pad=pad)
    net['upscale3'] = Upscale3DLayer(net['expand_2_2'], 2)
  
    net['concat3'] = ConcatLayer([net['upscale3'], net['contr_1_2']], cropping=(None, None, "center", "center"))
    net['expand_3_1'] = ConvLayer(net['concat3'], base_n_filters*2, kernel_size, nonlinearity=nonlinearity, pad=pad)
    net['expand_3_2'] = ConvLayer(net['expand_3_1'], base_n_filters*2, kernel_size, nonlinearity=nonlinearity, pad=pad)


    net['output_segmentation'] = ConvLayer(net['expand_3_2'], num_output_classes, 1, nonlinearity=None)
    
    
    net['dimshuffle'] = DimshuffleLayer(net['output_segmentation'], (1, 0, 2, 3, 4))
    # net['reshapeSeg'] = ReshapeLayer(net['dimshuffle'], (num_output_classes, -1))
    # print "net['reshapeSeg'] ", net['reshapeSeg'].output_shape

    # net['dimshuffle2'] = DimshuffleLayer(net['reshapeSeg'], (1, 0))
    # net['output_flattened'] = NonlinearityLayer(net['dimshuffle2'], nonlinearity=lasagne.nonlinearities.softmax)

    return net

