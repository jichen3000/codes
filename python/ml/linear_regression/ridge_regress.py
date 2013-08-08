from regression import *

from numpy import *

def ridgeRegres(xMat,yMat,lam=0.2):
    xTx = xMat.T*xMat
    denom = xTx + eye(shape(xMat)[1])*lam
    if linalg.det(denom) == 0.0:
        print "This matrix is singular, cannot do inverse"
        return
    ws = denom.I * (xMat.T*yMat)
    return ws

def ridgeTest(xArr,yArr):
    xMat = mat(xArr); yMat=mat(yArr).T
    yMean = mean(yMat,0)
    yMat = yMat - yMean
    # yMean.p()
    xMeans = mean(xMat,0)
    xVar = var(xMat,0)
    # xVar.p()
    xMat = (xMat - xMeans)/xVar
    numTestPts = 30
    wMat = zeros((numTestPts,shape(xMat)[1]))
    for i in range(numTestPts):
        ws = ridgeRegres(xMat,yMat,exp(i-10))
        wMat[i,:]=ws.T
    return wMat

def draw_weights(weights):
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    weights.shape.p()
    # weights[-1].pp()
    ax.plot(weights)
    plt.show()

if __name__ == '__main__':
    from minitest import *

    with test_case("regression"):
        dataset, labels = get_dataset_from_file('abalone.dataset')

        with test("ridgeTest"):
            weights = ridgeTest(dataset, labels)
            weights[-1].must_equal([ -3.13618246e-06,   3.43488557e-04,   4.29265642e-04,
                    9.86279863e-04,   8.16188652e-05,   1.39858822e-04,
                    3.40121256e-04,   3.34847052e-04], 
                    allclose)
            # draw_weights(weights)
            pass

