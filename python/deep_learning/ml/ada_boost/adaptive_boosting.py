
from numpy import *

def get_simple_dataset():
    dataset = [[ 1. ,  2.1],
        [ 2. , 1.1], [ 1.3, 1. ], [1., 1.], [2., 1.]]
    labels = [1.0, 1.0, -1.0, -1.0, 1.0]
    return dataset,labels

def stumpClassify(dataMatrix,dimen,threshVal,threshIneq):
    retArray = ones((shape(dataMatrix)[0],1))
    if threshIneq == 'lt':
        retArray[dataMatrix[:,dimen] <= threshVal] = -1.0
    else:
        retArray[dataMatrix[:,dimen] > threshVal] = -1.0
    return retArray

def buildStump(dataArr,classLabels,D):
    dataMatrix = mat(dataArr); labelMat = mat(classLabels).T
    m,n = shape(dataMatrix)
    numSteps = 10.0; bestStump = {}
    bestClasEst = mat(zeros((m,1))) 
    minError = inf
    for i in range(n):
        rangeMin = dataMatrix[:,i].min(); rangeMax = dataMatrix[:,i].max();
        stepSize = (rangeMax-rangeMin)/numSteps
        for j in range(-1,int(numSteps)+1):
            for inequal in ['lt', 'gt']:
                threshVal = (rangeMin + float(j) * stepSize)
                predictedVals = \
                        stumpClassify(dataMatrix,i,threshVal,inequal)
                errArr = mat(ones((m,1)))
                errArr[predictedVals == labelMat] = 0
                weightedError = D.T*errArr
                # print "split: dim %d, thresh %.2f, thresh ineqal: \
                # %s, the weighted error is %.3f" %\
                #    (i, threshVal, inequal, weightedError)
                if weightedError < minError:
                    minError = weightedError
                    bestClasEst = predictedVals.copy()
                    bestStump['dim'] = i
                    bestStump['thresh'] = threshVal
                    bestStump['ineq'] = inequal
    return bestStump,minError,bestClasEst

def adaBoostTrainDS(dataArr,classLabels,numIt=40):
    weakClassArr = []
    m = shape(dataArr)[0]
    D = mat(ones((m,1))/m)
    aggClassEst = mat(zeros((m,1)))
    for i in range(numIt):
        bestStump,error,classEst = buildStump(dataArr,classLabels,D)
        # error.p()
        # print "D:",D.T
        alpha = float(0.5*log((1.0-error)/max(error,1e-16)))
        bestStump['alpha'] = alpha
        # alpha.p()
        weakClassArr.append(bestStump)
        # print "classEst: ",classEst.T
        expon = multiply(-1*alpha*mat(classLabels).T,classEst)
        # expon.p()
        # exp(expon).p()
        D = multiply(D,exp(expon))
        D = D/D.sum()
        aggClassEst += alpha*classEst
        # print "aggClassEst: ",aggClassEst.T
        # sign(aggClassEst).p()
        aggErrors = multiply(sign(aggClassEst) !=
            mat(classLabels).T,ones((m,1)))
        errorRate = aggErrors.sum()/m
        print "total error: ",errorRate,"\n"
        if errorRate == 0.0: break
    return weakClassArr, aggClassEst

def adaClassify(datToClass,classifierArr):
    dataMatrix = mat(datToClass)
    m = shape(dataMatrix)[0]
    aggClassEst = mat(zeros((m,1)))
    for classifier in classifierArr:
        classEst = stumpClassify(dataMatrix,classifier['dim'],\
                                 classifier['thresh'],\
                                 classifier['ineq'])
        # classEst.p()
        aggClassEst += classifier['alpha']*classEst
        # aggClassEst.p()
        # print aggClassEst
    return sign(aggClassEst)

if __name__ == '__main__':
    from minitest import *

    with test_case("adaptive boosting"):
        with test("buildStump"):
            D = mat(ones((5,1))/5)
            dataset, labels = get_simple_dataset()
            # buildStump(dataset, labels, D).p()

            pass

        with test("adaBoostTrainDS"):
            classifierArr, aggClassEst = adaBoostTrainDS(dataset, labels,9)
            classifierArr.p()
            pass

        with test("adaClassify"):
            adaClassify([3, 0], classifierArr).p()
            pass