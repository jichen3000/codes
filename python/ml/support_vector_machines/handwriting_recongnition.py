import os
from numpy import *

from rbf_smo import *

IMG_SIZE = 32

def img_to_vector(filename):
    with open(filename) as data_file:
        result = [int(line[index]) for line in data_file 
            for index in range(IMG_SIZE)]
    return result

def get_label_from_filename(filename):
    # filename.p()
    return filename.split('_')[0]

def get_label_and_data(pathname,filename):
    return get_label_from_filename(filename), img_to_vector(os.path.join(
            pathname, filename))

def filter_filenames_with_num(pathname,start_with_number):
    '''
        return list of list of the file names under the path.
        Like:
            [ ['0_0.dataset', ... '0_99.dataset'],
                ...
              ['9_0.dataset', ... '9_99.dataset'] ]
    '''
    num_str = str(start_with_number)
    return [filename for filename in os.listdir(pathname) if filename.startswith(num_str)] 


def get_handwriting_dataset(pathname):
    filenames = filter_filenames_with_num(pathname,9)+filter_filenames_with_num(pathname,1)
    label_and_data_list = [get_label_and_data(pathname, filename) 
        for filename in filenames]
    # label_and_data_list = [get_label_and_data(pathname, filename) 
    #     for filename in os.listdir(pathname)]
    labels, dataset = zip(*label_and_data_list)
    return array(dataset), to_binary_labels(labels)

def to_binary_labels(labels):
    return [-1 if label=='9' else 1 for label in labels]

def testDigits(kTup=('rbf', 10)):
    dataArr,labelArr = get_handwriting_dataset('../k_nearest_neighbours/training_digits')
    # dataArr,labelArr = get_handwriting_dataset('../../projects/font_number_binary/number_images')
    datMat=mat(dataArr)
    labelMat = mat(labelArr).transpose() 
    datMat.shape.pp()
    labelMat.shape.pp()
    # dataArr,labelArr = loadImages('trainingDigits')
    b,alphas = smoP(dataArr, labelArr, 200, 0.0001, 10000, kTup) 
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
    print "the training error rate is: %f" % (float(errorCount)/m) 

    # dataArr,labelArr = get_handwriting_dataset('../k_nearest_neighbours/test_digits')
    # # dataArr,labelArr = loadImages('testDigits')
    # errorCount = 0
    # datMat=mat(dataArr); labelMat = mat(labelArr).transpose()
    # m,n = shape(datMat)
    # for i in range(m):
    #     kernelEval = kernelTrans(sVs,datMat[i,:],kTup)
    #     predict=kernelEval.T * multiply(labelSV,alphas[svInd]) + b
    #     if sign(predict)!=sign(labelArr[i]): errorCount += 1
    # print "the test error rate is: %f" % (float(errorCount)/m)
    
# def loadImages(dirName):
#     from os import listdir
#     hwLabels = []
#     trainingFileList = listdir(dirName)
#     m = len(trainingFileList)
#     trainingMat = zeros((m,1024))
#     for i in range(m):
#         fileNameStr = trainingFileList[i]
#         fileStr = fileNameStr.split('.')[0]
#         # fileStr.p()
#         classNumStr = int(fileStr.split('_')[0])
#         if classNumStr == 9: hwLabels.append(-1)
#         else: hwLabels.append(1)
#         trainingMat[i,:] = img_to_vector('%s/%s' % (dirName, fileNameStr))
#     return trainingMat, hwLabels

if __name__ == '__main__':
    from minitest import *
    with test_case("handwriting"):
        with test("get_handwriting_dataset"):
            # dataset1, labels1 = loadImages('../k_nearest_neighbours/test_digits')
            dataset, labels = get_handwriting_dataset('../k_nearest_neighbours/test_digits')
            # dataset.must_equal(dataset1, key=allclose)
            # labels.must_equal(labels1)
            pass

        with test("testDigits"):
            testDigits()

