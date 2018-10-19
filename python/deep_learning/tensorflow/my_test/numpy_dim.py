
import numpy as np

def gen_index_array(the_shape):
    the_shape = (2,3,4)
    index_array = np.zeros(the_shape)
    for column in the_shape:
        for cur_index in range(the_shape[column]):

def ff():
    index_array = np.zeros((2,3))
    for i in range(2):
        for j in range(3):
            index_array[i,j] = (i+1)*10+(j+1)

    aa = np.zeros((2,3,4))
    for i in range(2):
        for j in range(3):
            for k in range(4):
                aa[i,j,k] = (i+1)*100+(j+1)*10+(k+1)

    bb = np.zeros((2,3,4))
    for i in range(2):
        bb[i,:,:] = (i+1)*100 + bb[i,:,:]
    for j in range(3):
        bb[:,j,:] = (j+1)*10 + bb[:,j,:]
    for k in range(4):
        bb[:,:,k] = (k+1)*1 + bb[:,:,k]
