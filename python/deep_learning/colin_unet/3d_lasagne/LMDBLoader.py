#!/usr/bin/env python
import os
import numpy as np
import lmdb
import caffe
import scipy.misc
from StringIO import StringIO
from PIL import Image

def read_lmdb(folder, height, width):
    env = lmdb.open(folder, readonly=True)
    datum = caffe.proto.caffe_pb2.Datum()
    count = 0

    inputs = []
    labels = []
    with env.begin() as txn:
        cursor = txn.cursor()
        for key, value in cursor:

            datum.ParseFromString(value)
            s = StringIO()
            s.write(datum.data)
            s.seek(0)
            
            image = np.array(Image.open(s))
            image = image.astype('float32')
            image = np.transpose(scipy.misc.imresize(image, size=(height, width)), (2,0,1))
                
            y = datum.label
            inputs.append(image)
            labels.append(y)
            count=count+1

    #Convert to numpy arrays for easier ingestion to deep nets
    inputs = np.asarray(inputs)
    labels = np.asarray(labels)

    return inputs,labels


#READ TRAINING IMAGES FOLDER
def read_lmdb_images(folder, height, width):
    count = 0
    env = lmdb.open(folder, readonly=True)
    inputs = []
    datum = caffe.proto.caffe_pb2.Datum()
    with env.begin() as txn:
        cursor = txn.cursor()
        for key, value in cursor:
            datum.ParseFromString(value)
            image = caffe.io.datum_to_array(datum)
            image = image.astype('float32')
            image = np.transpose(scipy.misc.imresize(image, size=(height, width)), (2,0,1))
            inputs.append(image)
            count=count+1
    #Convert to numpy arrays for easier ingestion to deep nets
    inputs = np.asarray(inputs)
    
    return inputs

#READ TRAINING IMAGES FOLDER
def read_lmdb_labels(folder):
    count = 0
    env = lmdb.open(folder, readonly=True)
    labels = []
    datum = caffe.proto.caffe_pb2.Datum()
    with env.begin() as txn:
        cursor = txn.cursor()
        for key, value in cursor:
            datum.ParseFromString(value)
            label = datum.float_data
            labels.append(label)
            count=count+1
    #Convert to numpy arrays for easier ingestion to deep nets
    labels = np.asarray(labels).astype(np.uint8)
    
    return labels

if __name__ == '__main__':
    read_lmdb_images()
    read_lmdb_labels()
