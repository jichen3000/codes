from time import sleep
import json
import urllib2
import os.path

from numpy import *

from regression import *
from ridge_regress import *

def get_lego_json(setNum):
    filename = "lego_no%d.dataset.json" % setNum
    if os.path.exists(filename) and os.path.isfile(filename):
        with open(filename, 'r') as datafile:
            # "use file".p()
            json_file = datafile.read()
    else:
        # "use http".p()
        myAPIstr = 'AIzaSyDYF2fLxAjYuwMMeuFljacoWeeHkoJPJCM'
        searchURL = 'https://www.googleapis.com/shopping/search/v1/public/products?'+\
                    'key=%s&country=US&q=lego+%d&alt=json' % (myAPIstr, setNum)
        json_file = urllib2.urlopen(searchURL).read()
        with open(filename, 'w') as datafile:
            datafile.write(json_file)
    return json.loads(json_file)



def searchForSet(setNum, yr, numPce, origPrc):
    # sleep(10)
    retX = []
    retY = []
    retDict = get_lego_json(setNum)
    for currItem in retDict['items']:
        try:
            if currItem['product']['condition'] == 'new':
                newFlag = 1
            else: 
                newFlag = 0
            listOfInv = currItem['product']['inventories']
            for item in listOfInv:
                sellingPrice = item['price']
                if  sellingPrice > origPrc * 0.5:
                    # print "%d\t%d\t%d\t%f\t%f" %\
                    #     (yr,numPce,newFlag,origPrc, sellingPrice)
                    retX.append([1, yr, numPce, newFlag, origPrc])
                    retY.append(sellingPrice)
        except: 
            print 'problem with item %s' % currItem
    return retX, retY

def setDataCollect():
    tuple_lists = []
    tuple_lists.append(searchForSet(8288, 2006, 800, 49.99))
    tuple_lists.append(searchForSet(10030, 2002, 3096, 269.99))
    tuple_lists.append(searchForSet(10179, 2007, 5195, 499.99))
    tuple_lists.append(searchForSet(10181, 2007, 3428, 199.99))
    tuple_lists.append(searchForSet(10189, 2008, 5922, 299.99))
    tuple_lists.append(searchForSet(10196, 2009, 3263, 249.99))
    retX = []; retY = []
    for item in tuple_lists:
        # item.p()
        retX += item[0]
        retY += item[1]
    return retX, retY

def crossValidation(xArr,yArr,numVal=10):
    m = len(yArr)
    indexList = range(m)
    errorMat = zeros((numVal,30))
    for i in range(numVal):
        trainX=[]; trainY=[]
        testX = []; testY = []
        random.shuffle(indexList)
        for j in range(m):
            if j < m*0.9:
                trainX.append(xArr[indexList[j]])
                trainY.append(yArr[indexList[j]])
            else:
                testX.append(xArr[indexList[j]])
                testY.append(yArr[indexList[j]])
    wMat = ridgeTest(trainX,trainY)
    for k in range(30):
        matTestX = mat(testX); matTrainX=mat(trainX)
        meanTrain = mean(matTrainX,0)
        varTrain = var(matTrainX,0)
        matTestX = (matTestX-meanTrain)/varTrain
        yEst = matTestX * mat(wMat[k,:]).T + mean(trainY)
        errorMat[i,k]=regress_error(yEst.T.A,array(testY))
    meanErrors = mean(errorMat,0)
    minMean = float(min(meanErrors))
    bestWeights = wMat[nonzero(meanErrors==minMean)]
    xMat = mat(xArr); yMat=mat(yArr).T
    meanX = mean(xMat,0); varX = var(xMat,0)
    unReg = bestWeights/varX
    print "the best model from Ridge Regression is:\n",unReg 
    print "with constant term: ",\
          -1*sum(multiply(meanX,unReg)) + mean(yMat)

if __name__ == "__main__":
    from minitest import *

    with test_case("lego"):

        with test("searchForSet"):
            retX, retY = searchForSet(8288, 2006, 800, 49.99)
            pass

        with test("setDataCollect"):
            retX, retY = setDataCollect()
            retX.size().must_equal(retY.size())
            retX.pp()
            retY.pp()
            x_matrix, y_matrix = dataset_to_mat(retX, retY)
            standard_weight = standard_regress(x_matrix,y_matrix)
            # standard_weight.T.p()
            # x_matrix[0].p()
            # (x_matrix[0]*standard_weight).p()
            # y_matrix[0].p()

        with test("crossValidation"):
            crossValidation(retX, retY, 10)
            pass