from numpy import *
from svd import *

def load_data_mat():
    return matrix([[4, 4, 0, 2, 2],
        [4, 0, 0, 3, 3],
        [4, 0, 0, 1, 1],
        [1, 1, 1, 2, 0],
        [2, 2, 2, 0, 0],
        [1, 1, 1, 0, 0],
        [5, 5, 5, 0, 0]])
def load_data_mat2():
    return matrix([
        [2, 0, 0, 4, 4, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 4, 0],
        [3, 3, 4, 0, 3, 0, 0, 2, 2, 0, 0],
        [5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 5, 0, 0, 5, 0],
        [4, 0, 4, 0, 0, 0, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 5, 0, 0, 5, 0],
        [0, 0, 0, 3, 0, 0, 0, 0, 4, 5, 0],
        [1, 1, 2, 1, 1, 2, 1, 0, 4, 5, 0]])
# Euclidian distance
def eclud_similarity(inA,inB):
    return 1.0/(1.0 + linalg.norm(inA - inB))

# Pearson correlation
def pearson_similarity(inA,inB):
    if len(inA) < 3 : return 1.0
    return 0.5+0.5*corrcoef(inA, inB, rowvar = 0)[0][1]

# cosine similarity
def cos_similarity(inA,inB):
    num = float(inA.T*inB)
    denom = linalg.norm(inA)*linalg.norm(inB)
    return 0.5+0.5*(num/denom)

# The data matrix is assumed to be organized like figures 14.1 and 14.2 
# with users as the row and items as the columns.
def standEst(dataMat, user, simMeas, item):
    n = shape(dataMat)[1]
    simTotal = 0.0; ratSimTotal = 0.0
    for j in range(n):
        userRating = dataMat[user,j]
        if userRating == 0: continue
        overLap = nonzero(logical_and(dataMat[:,item].A>0, \
                                      dataMat[:,j].A>0))[0]
        # dataMat[:,item].p()
        # dataMat[:,j].p()
        # overLap.p()
        if len(overLap) == 0: similarity = 0
        else: 
            # dataMat[overLap, item].p()
            similarity = simMeas(dataMat[overLap,item], \
                                   dataMat[overLap,j])
            # similarity.p()
        #print 'the %d and %d similarity is: %f' % (item, j, similarity)
        simTotal += similarity
        ratSimTotal += similarity * userRating
    if simTotal == 0: return 0
    else: return ratSimTotal/simTotal

def recommend(dataMat, user, N=3, simMeas=cos_similarity, 
        estMethod=standEst):
    # dataMat.p()
    # dataMat[user,:].A.p()
    # nonzero(dataMat[user,:].A==0).p()
    unratedItems = nonzero(dataMat[user,:].A==0)[1]
    if len(unratedItems) == 0: 
        return 'you rated everything' 
    itemScores = []
    for item in unratedItems:
        estimatedScore = estMethod(dataMat, user, simMeas, item)
        itemScores.append((item, estimatedScore))
    return sorted(itemScores, \
        key=lambda jj: jj[1], reverse=True)[:N]


def svdEst(dataMat, user, simMeas, item):
    n = shape(dataMat)[1]
    simTotal = 0.0; ratSimTotal = 0.0
    U,Sigma,VT = linalg.svd(dataMat)
    features = choose_features(Sigma, 0.9)
    sig_n = mat(eye(features)*Sigma[:features])
    xformedItems = dataMat.T * U[:,:features] * sig_n.I
    for j in range(n):
        userRating = dataMat[user,j]
        if userRating == 0 or j==item: continue
        similarity = simMeas(xformedItems[item,:].T,\
                             xformedItems[j,:].T)
        print 'the %d and %d similarity is: %f' % (item, j, similarity)
        simTotal += similarity
        ratSimTotal += similarity * userRating
    if simTotal == 0: return 0
    else: return ratSimTotal/simTotal

if __name__ == '__main__':
    from minitest import *

    with test("similarity"):
        data_mat = mat(load_example_data())
        # data_mat[:, 0].p()
        eclud_similarity(data_mat[:, 0], data_mat[:, 4]).must_equal(
            0.1336766024, allclose)
        eclud_similarity(data_mat[:, 0], data_mat[:, 0]).must_equal(
            1, allclose)
        pearson_similarity(data_mat[:, 0], data_mat[:, 4]).must_equal(
            0.23768619407595826, allclose)
        pearson_similarity(data_mat[:, 0], data_mat[:, 0]).must_equal(
            1, allclose)
        cos_similarity(data_mat[:, 0], data_mat[:, 4]).must_equal(
            0.54724555912615336, allclose)
        cos_similarity(data_mat[:, 0], data_mat[:, 0]).must_equal(
            1, allclose)

    with test("recommend"):
        data_mat = load_data_mat()
        recommend(data_mat, 2).must_equal(
            [(2, 2.5), (1, 2.0243290220056256)])
        pass

    with test("recommend"):
        data_mat2 = load_data_mat2()
        recommend(data_mat, 1, estMethod=svdEst).must_equal(
            [(2, 3.4177569186592374), (1, 3.3307171545585641)])
        pass