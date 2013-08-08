from regression import *

from numpy import *

def regularize_x(xMat):#regularize by columns
    inMat = xMat.copy()
    inMeans = mean(inMat,0)   #calc mean then subtract it off
    inVar = var(inMat,0)      #calc variance of Xi then divide by it
    inMat = (inMat - inMeans)/inVar
    return inMat

def regularize_y(yMat):
    yMean = mean(yMat,0)
    return yMat - yMean
# the benefit of this manner is that you can see which feature is import to you.
def stageWise(xMat,yMat,eps=0.01,numIt=100):
    yMat = regularize_y(yMat)
    xMat = regularize_x(xMat)
    m,n=shape(xMat)
    returnMat = zeros((numIt,n)) #testing code remove
    ws = zeros((n,1)); wsTest = ws.copy(); wsMax = ws.copy()
    for i in range(numIt):
        # print ws.T
        # ws.T.p()
        lowestError = inf;
        for j in range(n):
            for sign in [-1,1]:
                wsTest = ws.copy()
                wsTest[j] += eps*sign
                yTest = xMat*wsTest
                rssE = regress_error(yMat.A,yTest.A)
                if rssE < lowestError:
                    lowestError = rssE
                    wsMax = wsTest
        ws = wsMax.copy()
        returnMat[i,:]=ws.T
    return returnMat

if __name__ == '__main__':
    from minitest import *

    with test_case("regression"):
        xMat,yMat = get_matrix_from_file('abalone.dataset')

        with test("ridgeTest"):
            # ridge regress
            # [ -3.13618246e-06,   3.43488557e-04,   4.29265642e-04,
            #         9.86279863e-04,   8.16188652e-05,   1.39858822e-04,
            #         3.40121256e-04,   3.34847052e-04]
            weights = stageWise(xMat,yMat, eps=0.001,numIt=5000)
            weights[-1].must_equal([ 0.043, -0.011,  0.12 ,  0.022,  2.023, -0.963, -0.105,  0.187], allclose)
            pass

        with test("compare with standard regress"):
            x_matrix = regularize_x(xMat)
            y_matrix = regularize_y(yMat)
            stardard_weight = standard_regress(x_matrix,y_matrix).T
            stardard_weight.must_equal([ 0.0430442 , -0.02274163,  0.13214087,  0.02075182,  2.22403814,
                -0.99895312, -0.11725427,  0.16622915], allclose)
