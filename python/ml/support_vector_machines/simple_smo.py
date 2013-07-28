# sequential minimal optimization (SMO)
# John C. Platt, "Using Analytic QP and Sparseness 
# to Speed Training of Support Vector Machines"

from functional_style import *
from operator import itemgetter
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

def smoSimple(dataMatIn, classLabels, C, tolerance, max_count):
    dataMatrix = mat(dataMatIn)
    labelMat = mat(classLabels).transpose()
    b = 0; m,n = shape(dataMatrix)
    alphas = mat(zeros((m,1)))
    no_change_count = 0
    while (no_change_count < max_count):
        alphaPairsChanged = 0
        for i in range(m):
            fXi = float(multiply(alphas,labelMat).T*\
                   (dataMatrix*dataMatrix[i,:].T)) + b
            Ei = fXi - float(labelMat[i])
            if ((labelMat[i]*Ei < -tolerance) and (alphas[i] < C)) or \
                    ((labelMat[i]*Ei > tolerance) and \
                    (alphas[i] > 0)):
                j = selectJrand(i,m)
                fXj = float(multiply(alphas,labelMat).T*\
                        (dataMatrix*dataMatrix[j,:].T)) + b
                Ej = fXj - float(labelMat[j])
                alphaIold = alphas[i].copy();
                alphaJold = alphas[j].copy();
                if (labelMat[i] != labelMat[j]):
                    L = max(0, alphas[j] - alphas[i])
                    H = min(C, C + alphas[j] - alphas[i])
                else:
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                if L==H: print "L==H"; continue
                eta = 2.0 * dataMatrix[i,:]*dataMatrix[j,:].T - \
                        dataMatrix[i,:]*dataMatrix[i,:].T - \
                        dataMatrix[j,:]*dataMatrix[j,:].T
                if eta >= 0: print "eta>=0"; continue
                alphas[j] -= labelMat[j]*(Ei - Ej)/eta
                alphas[j] = clipAlpha(alphas[j],H,L)
                if (abs(alphas[j] - alphaJold) < 0.00001): 
                    print "j not moving enough"; continue
                alphas[i] += labelMat[j]*labelMat[i]*\
                        (alphaJold - alphas[j])
                b1 = b - Ei- labelMat[i]*(alphas[i]-alphaIold)*\
                        dataMatrix[i,:]*dataMatrix[i,:].T - \
                        labelMat[j]*(alphas[j]-alphaJold)*\
                        dataMatrix[i,:]*dataMatrix[j,:].T
                b2 = b - Ej- labelMat[i]*(alphas[i]-alphaIold)*\
                        dataMatrix[i,:]*dataMatrix[j,:].T - \
                        labelMat[j]*(alphas[j]-alphaJold)*\
                        dataMatrix[j,:]*dataMatrix[j,:].T
                if (0 < alphas[i]) and (C > alphas[i]): b = b1
                elif (0 < alphas[j]) and (C > alphas[j]): b = b2
                else: b = (b1 + b2)/2.0
                alphaPairsChanged += 1
                print "no_change_count: %d i:%d, pairs changed %d" % \
                                  (no_change_count,i,alphaPairsChanged)
        if (alphaPairsChanged == 0): no_change_count += 1
        else: no_change_count = 0
        print "iteration number: %d" % no_change_count
    return b,alphas

if __name__ == '__main__':
    from minitest import *

    with test_case("simple smo"):
        tself = get_test_self()
        tself.dataset, tself.labels = get_dataset_from_file(
            "test_set.dataset")
        with test("smo"):
            smoSimple(tself.dataset, tself.labels, 0.6, 0.001, 1)