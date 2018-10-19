from numpy import *

def load_dataset(filename, delim='\t'):
    with open(filename) as fr:
        string_arr = [line.strip().split(delim) for line in fr.readlines()] 
    data_arr = [map(float,line) for line in string_arr]
    return mat(data_arr)

def pca(dataMat, topNfeat=9999999):
    meanVals = mean(dataMat, axis=0)
    meanRemoved = dataMat - meanVals
    covMat = cov(meanRemoved, rowvar=0)
    eigVals,eigVects = linalg.eig(mat(covMat))
    # eigVals.p()
    eigValInd = argsort(eigVals)
    eigValInd = eigValInd[:-(topNfeat+1):-1]
    # eigVects.p()
    redEigVects = eigVects[:,eigValInd]
    # redEigVects.p()
    lowDDataMat = meanRemoved * redEigVects
    reconMat = (lowDDataMat * redEigVects.T) + meanVals
    return lowDDataMat, reconMat

def choose_n_features(dataMat):
    meanVals = mean(dataMat, axis=0)
    meanRemoved = dataMat - meanVals
    covMat = cov(meanRemoved, rowvar=0)
    eigVals,eigVects = linalg.eig(mat(covMat))
    eigVals.p()
    sum_value = sum(eigVals)
    cal_sum = 0
    no_features = 0
    for value in eigVals:
        cal_sum += value
        no_features += 1
        if cal_sum >= 0.95 * sum_value:
            break
    return no_features


def replaceNanWithMean(datMat):
    numFeat = shape(datMat)[1]
    for i in range(numFeat):
        meanVal = mean(datMat[nonzero(~isnan(datMat[:,i].A))[0],i])
        datMat[nonzero(isnan(datMat[:,i].A))[0],i] = meanVal
    return datMat

def draw_points(data_mat, reconMat):
    import matplotlib.pyplot as plt
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(data_mat[:,0].flatten().A[0], 
        data_mat[:,1].flatten().A[0],
        marker='^', s=90)
    ax.scatter(reconMat[:,0].flatten().A[0], 
        reconMat[:,1].flatten().A[0],
        marker='o', s=50, c='red')
    plt.show()

if __name__ == '__main__':
    from minitest import *

    with test("pca"):
        data_mat = load_dataset('testset.dataset')
        # data_mat.p()
        lowDDataMat, reconMat = pca(data_mat, 1)
        # lowDDataMat.p()
        # reconMat.p()
        # draw_points(data_mat, reconMat)
        pass

    with test(""):
        data_mat = load_dataset('secom.dataset', ' ')
        data_mat = replaceNanWithMean(data_mat)
        choose_n_features(data_mat).p()
        pass

