'''
    this version copied from the book, and I've tested it with the data,
    the result is perfect.
'''

import os
from numpy import *
from rbf_smo_original import *

IMG_SIZE = 32


def img2vector(filename):
    returnVect = zeros((1,1024))
    fr = open(filename)
    for i in range(IMG_SIZE):
        lineStr = fr.readline()
        for j in range(IMG_SIZE):
            returnVect[0,IMG_SIZE*i+j] = int(lineStr[j])
    return returnVect

# def img2vector(filename):
#     with open(filename) as data_file:
#         result = [int(line[index]) for line in data_file 
#             for index in range(IMG_SIZE)]
#     return result


def filter_filenames_with_nums(pathname,start_with_numbers):
    '''
        return list of list of the file names under the path.
        Like:
            [ ['0_0.dataset', ... '0_99.dataset'],
                ...
              ['9_0.dataset', ... '9_99.dataset'] ]
    '''
    num_strs = map(str, start_with_numbers)
    # num_str = str(start_with_number)
    return [filename for filename in os.listdir(pathname) 
        for num_str in num_strs if filename.startswith(num_str)] 

def loadImages(dirName):
    # from os import listdir
    hwLabels = []
    # trainingFileList = os.listdir(dirName)
    # this place has been changed.
    trainingFileList = filter_filenames_with_nums(dirName, (9, 1))
    trainingFileList.size().pp()

    m = len(trainingFileList)
    trainingMat = zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        if classNumStr == 9: hwLabels.append(-1)
        else: hwLabels.append(1)
        trainingMat[i,:] = img2vector('%s/%s' % (dirName, fileNameStr))
    return trainingMat, hwLabels

def testDigits(kTup=('rbf', 20)):
    # cur_pic_path = '../../projects/font_number_binary/number_images'
    pic_path = '../k_nearest_neighbours'
    training_pic_path = os.path.join(pic_path,'training_digits')
    test_pic_path = os.path.join(pic_path,'test_digits')
    # training_pic_path = '../../projects/font_number_binary/number_images'

    dataArr,labelArr = loadImages(training_pic_path)
    # dataArr.shape.pp()
    
    b,alphas = smoP(dataArr, labelArr, 200, 0.0001, 1000, kTup) 
    datMat=mat(dataArr); labelMat = mat(labelArr).transpose() 
    datMat.shape.pp()
    labelMat.shape.pp()

    svInd=nonzero(alphas.A>0)[0]
    sVs=datMat[svInd]
    labelSV = labelMat[svInd];
    print "there are %d Support Vectors" % shape(sVs)[0]
    m,n = shape(datMat)
    errorCount = 0
    for i in range(m):
        kernelEval = kernelTrans(sVs,datMat[i,:],kTup)
        predict=kernelEval.T * multiply(labelSV,alphas[svInd]) + b
        if sign(predict)!=sign(labelArr[i]): errorCount += 1
    print "the training error rate is: %f, (%f/%f)" % (float(errorCount)/m, errorCount, m) 
    dataArr,labelArr = loadImages(test_pic_path)
    errorCount = 0
    datMat=mat(dataArr); labelMat = mat(labelArr).transpose()
    m,n = shape(datMat)
    for i in range(m):
        kernelEval = kernelTrans(sVs,datMat[i,:],kTup)
        predict=kernelEval.T * multiply(labelSV,alphas[svInd]) + b
        if sign(predict)!=sign(labelArr[i]): errorCount += 1
    print "the test error rate is: %f, (%f/%f)" % (float(errorCount)/m, errorCount, m)   

if __name__ == '__main__':
    from minitest import *
    testDigits()    