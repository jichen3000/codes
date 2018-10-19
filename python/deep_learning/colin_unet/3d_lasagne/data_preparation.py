import os
import sys
import fnmatch
import matplotlib.pyplot as plt
import numpy as np
sys.path.append("../../modelzoo/")
from generators import *
from multiprocessing.dummy import Pool
from urllib import urlretrieve
from PIL import Image
import skimage.io as io
from scipy.misc import imresize, imrotate

def load_mha(folder, width, height):
    folders = [os.path.join(folder,o) for o in os.listdir(folder) if os.path.isdir(os.path.join(folder,o))]
    
    data = np.zeros((len(folders), 1, 128, width, height),dtype=np.float32)
    target = np.zeros((len(folders), 1, 128, width, height), dtype=np.uint8)

        
    names = []

    ctr = 0
    for f in folders:
        subfolders = [os.path.join(f,o) for o in os.listdir(f) if os.path.isdir(os.path.join(f,o))]
        for imageFolder in subfolders:
            if "MR_Flair" in imageFolder:
                images_sat = [img for img in os.listdir(os.path.join(f,imageFolder,imageFolder)) if fnmatch.fnmatch(img, "*.mha*")]
                names.append(images_sat[0])
                img = io.imread(os.path.join(f,imageFolder,imageFolder,images_sat[0]),plugin='simpleitk')   
                
                images = np.zeros((len(img), width, height), dtype=np.uint8)

                for i in range (0,len(img)):
                    image = img[i][:][:].astype(np.int16)
                    image = imresize(image,size=(width,height), interp='nearest')
                    images[i] = image
                data[ctr][0]=images[20:155-7][:][:]
                
            if "3more" in imageFolder:
                images_sat = [img for img in os.listdir(os.path.join(f,imageFolder,imageFolder)) if fnmatch.fnmatch(img, "*.mha*")]
                img = io.imread(os.path.join(f,imageFolder,imageFolder,images_sat[0]),plugin='simpleitk')
                images = np.zeros((len(img), width, height), dtype=np.uint8)
                for i in range (0,len(img)):
                    image = img[i][:][:].astype(np.uint8)
                    image = imresize(image,size=(width,height), interp='nearest')
                    images[i] = image
                target[ctr][0]=images[20:155-7][:][:]
        ctr+=1
        
    return data, target, names
                
    

def load_data(folder, width, height):

    images_sat = [img for img in os.listdir(os.path.join(folder, "Images")) if fnmatch.fnmatch(img, "*.png*")]
    images_map = [img for img in os.listdir(os.path.join(folder, "Masks")) if fnmatch.fnmatch(img, "*.png*")]

    #assert(len(images_sat) == len(images_map))

    images_sat.sort()
    images_map.sort()

    data = np.zeros((len(images_sat), 1, width, height), dtype=np.uint8)
    target = np.zeros((len(images_map), 1, width, height), dtype=np.uint8)


    ctr = 0
    for sat_im, map_im in zip(images_sat, images_map):
        if sat_im == map_im:
            original_image = Image.open(os.path.join(folder, "Images", sat_im))
            original_image = original_image.convert('L')
            data[ctr,0] = original_image.resize((width,height))
            

            mask_image = Image.open(os.path.join(folder, "Masks", map_im))
            mask_image = mask_image.convert('L')
            target[ctr,0] = mask_image.resize((width,height))
            target[ctr,0] = target[ctr, 0]/255
            ctr += 1


    return data, target

def prepare_dataset(training_folder,validation_folder, testing_folder, width, height):
    try:
        print "Trying to load data..."
        print "Make sure your intensity images are in 0-255 range as well as the target ground truths at 0-1 range!"
        data_train, target_train = load_data(training_folder, width, height)
        data_valid, target_valid = load_data(testing_folder, width, height)
        data_test, target_test = load_data(validation_folder, width, height)

        # loading np arrays is much faster than loading the images one by one every time
        np.save("data_train.npy", data_train)
        np.save("target_train.npy", target_train)
        np.save("data_valid.npy", data_valid)
        np.save("target_valid.npy", target_valid)
        np.save("data_test.npy", data_test)
        np.save("target_test.npy", target_test)
    except:
        print "something went wrong! Couldn't prepare the data"

if __name__ == "__main__":
    prepare_dataset()
