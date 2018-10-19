# sequential minimal optimization (SMO)
# John C. Platt, "Using Analytic QP and Sparseness 
# to Speed Training of Support Vector Machines"

# radial bias function,
# mapping from one feature space to another feature space.
# inner products.
# One great thing about the SVM optimization is that all 
# operations can be written in terms of inner products. 
# Inner products are two vectors multiplied together to 
# yield a scalar or single number.

# kernel trick or kernel substation.
# A popular kernel is the radial bias function, which we'll introduce next.

from functional_style import *

from functools import partial
from operator import itemgetter, gt, lt
from numpy import *
import random

def get_dataset_from_file(filename):
    with open(filename) as datafile:
        words = [line.strip().split('\t') for line in datafile]
    dataset = [ [float(cell) for cell in row[:-1]] for row in words]
    labels = map(comb(itemgetter(-1), float), words)
    return dataset, labels

# select a value from 0 to m, but not equal the value of i
def selectJrand(i,m):
    j=i
    while (j==i):
        j = int(random.uniform(0,m))
    return j

# reset a value according to a range from low_value to hight_value
def clipAlpha(aj,hight_value,low_value):
    if aj > hight_value:
        aj = hight_value
    if aj < low_value:
        aj = low_value
    return aj

class optStruct:
    def __init__(self,dataMatIn, classLabels, C, toler):
        self.X = dataMatIn
        self.labelMat = classLabels
        self.C = C
        self.tol = toler
        self.m = shape(dataMatIn)[0]
        self.alphas = mat(zeros((self.m,1)))
        self.b = 0 
        self.eCache = mat(zeros((self.m,2)))

def calcEk(oS, k):
    fXk = float(multiply(oS.alphas,oS.labelMat).T*\
          (oS.X*oS.X[k,:].T)) + oS.b
    Ek = fXk - float(oS.labelMat[k])
    return Ek

def selectJ(i, oS, Ei):
    maxK = -1; maxDeltaE = 0; Ej = 0
    oS.eCache[i] = [1,Ei]
    validEcacheList = nonzero(oS.eCache[:,0].A)[0] 
    # oS.eCache.pp()
    # validEcacheList.pp()
    if (len(validEcacheList)) > 1:
        for k in validEcacheList:
            if k == i: continue
            Ek = calcEk(oS, k)
            deltaE = abs(Ei - Ek)
            if (deltaE > maxDeltaE):
                maxK = k; maxDeltaE = deltaE; Ej = Ek
        return maxK, Ej
    else:
        j = selectJrand(i, oS.m)
        Ej = calcEk(oS, j)
    return j, Ej

def updateEk(oS, k):
    Ek = calcEk(oS, k)
    oS.eCache[k] = [1,Ek]

def innerL(i, oS):
    Ei = calcEk(oS, i)
    if ((oS.labelMat[i]*Ei < -oS.tol) and (oS.alphas[i] < oS.C)) or\
       ((oS.labelMat[i]*Ei > oS.tol) and (oS.alphas[i] > 0)):
        j,Ej = selectJ(i, oS, Ei)
        alphaIold = oS.alphas[i].copy()
        alphaJold = oS.alphas[j].copy()
        if (oS.labelMat[i] != oS.labelMat[j]):
            L = max(0, oS.alphas[j] - oS.alphas[i])
            H = min(oS.C, oS.C + oS.alphas[j] - oS.alphas[i])
        else:
            L = max(0, oS.alphas[j] + oS.alphas[i] - oS.C)
            H = min(oS.C, oS.alphas[j] + oS.alphas[i])
        if L==H: print "L==H"; return 0
        eta = 2.0 * oS.X[i,:]*oS.X[j,:].T - oS.X[i,:]*oS.X[i,:].T - \
                oS.X[j,:]*oS.X[j,:].T
        if eta >= 0: print "eta>=0"; return 0
        oS.alphas[j] -= oS.labelMat[j]*(Ei - Ej)/eta
        oS.alphas[j] = clipAlpha(oS.alphas[j],H,L)
        updateEk(oS, j)
        if (abs(oS.alphas[j] - alphaJold) < 0.00001):
             print "j not moving enough"; return 0
        oS.alphas[i] += oS.labelMat[j]*oS.labelMat[i]*\
        (alphaJold - oS.alphas[j])
        updateEk(oS, i)
        b1 = oS.b - Ei- oS.labelMat[i]*(oS.alphas[i]-alphaIold)*\
             oS.X[i,:]*oS.X[i,:].T - oS.labelMat[j]*\
             (oS.alphas[j]-alphaJold)*oS.X[i,:]*oS.X[j,:].T
        b2 = oS.b - Ej- oS.labelMat[i]*(oS.alphas[i]-alphaIold)*\
             oS.X[i,:]*oS.X[j,:].T - oS.labelMat[j]*\
             (oS.alphas[j]-alphaJold)*oS.X[j,:]*oS.X[j,:].T
        if (0 < oS.alphas[i]) and (oS.C > oS.alphas[i]): oS.b = b1
        elif (0 < oS.alphas[j]) and (oS.C > oS.alphas[j]): oS.b = b2
        else: oS.b = (b1 + b2)/2.0
        return 1
    else: return 0

def smoP(dataMatIn, classLabels, C, toler, max_iteration, kTup=('lin', 0)): 
    oS = optStruct(mat(dataMatIn),mat(classLabels).transpose(),C,toler) 
    iter = 0
    entireSet = True
    alphaPairsChanged = 0
    while (iter < max_iteration) and ((alphaPairsChanged > 0) \
            or (entireSet)):
        alphaPairsChanged = 0
        if entireSet:
            for i in range(oS.m):
                alphaPairsChanged += innerL(i,oS)
            print "fullSet, iter: %d i:%d, pairs changed %d" %\
                    (iter,i,alphaPairsChanged)
            iter += 1
        else:
            nonBoundIs = nonzero((oS.alphas.A > 0) * (oS.alphas.A < C))[0]
            for i in nonBoundIs:
                alphaPairsChanged += innerL(i,oS)
                print "non-bound, iter: %d i:%d, pairs changed %d" % \
                        (iter,i,alphaPairsChanged)
            iter += 1
        if entireSet: entireSet = False
        elif (alphaPairsChanged == 0): entireSet = True
        print "iteration number: %d" % iter
    return oS.b,oS.alphas


def get_support_vectors(dataset, labels, alphas):
    # [item.pp() for item in zip(alphas, dataset, labels)]
    # return []
    return filter(lambda item: item[0]>0, 
        zip(alphas, dataset, labels))

def calcWs(dataArr, classLabels, alphas):
    dataMat = mat(dataArr)
    labelMat = mat(classLabels).transpose()
    m,n = shape(dataMat)
    w = zeros((n,1))
    for i in range(m):
        w += multiply(alphas[i]*labelMat[i],dataMat[i,:].T)
    return w

if __name__ == '__main__':
    from minitest import *

    with test_case("simple smo"):
        tself = get_test_self()
        tself.dataset, tself.labels = get_dataset_from_file(
            "test_set.dataset")
        tself.small_dataset = tself.dataset[:]
        tself.small_labels = tself.labels[:]
        tself.b_value = matrix([[-3.81666061]])[0,0]
        tself.alphas_list = matrix([[ 0.10356041,  0.25615675,  
            0.01420587,  0.34551129]]).tolist()[0]
        with test("get_support_vectors"):
            get_support_vectors(tself.dataset, tself.labels, 
                tself.alphas_list).must_equal(
                [(0.10356041, [3.542485, 1.977398], -1.0),
                 (0.25615675, [3.018896, 2.556416], -1.0),
                 (0.01420587, [7.55151, -1.58003], 1.0),
                 (0.34551129, [2.114999, -0.004466], -1.0)])

        with test("smo"):
            # smoP(tself.dataset, tself.labels, 0.6, 0.001, 1)
            b, tself.alphas = smoP(tself.small_dataset, tself.small_labels, 
                0.6, 0.001, 40)
            b.p()
            tself.alphas[tself.alphas>0].p()
            pass

        with test("calcWs"):
            calcWs(tself.dataset, tself.labels, tself.alphas).p()

