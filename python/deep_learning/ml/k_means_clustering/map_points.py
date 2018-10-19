from numpy import *
from k_means import *
from bisecting_k_means import *

# Spherical distance measure
def distSLC(vecA, vecB):
    a = sin(vecA[0,1]*pi/180) * sin(vecB[0,1]*pi/180)
    b = cos(vecA[0,1]*pi/180) * cos(vecB[0,1]*pi/180) * \
        cos(pi * (vecB[0,0]-vecA[0,0]) /180)
    return arccos(a + b)*6371.0

def clusterClubs(numClust=5):
    import matplotlib
    import matplotlib.pyplot as plt
    datList = []
    for line in open('places.dataset').readlines():
        lineArr = line.split('\t')
        datList.append([float(lineArr[4]), float(lineArr[3])])
    datMat = mat(datList)
    myCentroids, clustAssing = biKmeans(datMat, numClust, \
                                      distSLC)
    fig = plt.figure()
    rect=[0.1,0.1,0.8,0.8]
    scatterMarkers=['s', 'o', '^', '8', 'p', \
                    'd', 'v', 'h', '>', '<']
    axprops = dict(xticks=[], yticks=[])
    ax0=fig.add_axes(rect, label='ax0', **axprops) 
    imgP = plt.imread('Portland.dataset.png')
    ax0.imshow(imgP)
    ax1=fig.add_axes(rect, label='ax1', frameon=False) 
    for i in range(numClust):
        ptsInCurrCluster = datMat[nonzero(clustAssing[:,0].A==i)[0],:]
        markerStyle = scatterMarkers[i % len(scatterMarkers)]
        ax1.scatter(ptsInCurrCluster[:,0].flatten().A[0],\
                    ptsInCurrCluster[:,1].flatten().A[0],\
                   marker=markerStyle, s=90)
    ax1.scatter(myCentroids[:,0].flatten().A[0], 
        myCentroids[:,1].flatten().A[0], marker='+', s=300)
    plt.show()

if __name__ == '__main__':
    from minitest import *

    with test_case("map_points"):

        with test("clusterClubs"):
            clusterClubs()
