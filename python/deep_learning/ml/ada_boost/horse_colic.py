from adaptive_boosting import *
from operator import itemgetter, ne, truth
from functional_style import comb
from numpy import *

def get_dataset_from_file(filename):
    with open(filename) as datafile:
        words = [line.strip().split('\t') for line in datafile]
    dataset = [ [float(cell) for cell in row[:-1]] for row in words]
    labels = map(comb(itemgetter(-1), float), words)
    return dataset, labels


def plotROC(predStrengths, classLabels):
    import matplotlib.pyplot as plt
    cur = (1.0,1.0)
    ySum = 0.0
    numPosClas = sum(array(classLabels)==1.0) 
    yStep = 1/float(numPosClas)
    xStep = 1/float(len(classLabels)-numPosClas) 
    sortedIndicies = predStrengths.argsort()
    fig = plt.figure()
    fig.clf()
    ax = plt.subplot(111)
    for index in sortedIndicies.tolist()[0]:
        if classLabels[index] == 1.0:
            delX = 0; delY = yStep;
        else:
            delX = xStep; delY = 0;
            ySum += cur[1]
        ax.plot([cur[0],cur[0]-delX],[cur[1],cur[1]-delY], c='b')
        cur = (cur[0]-delX,cur[1]-delY)
    ax.plot([0,1],[0,1],'b--')
    plt.xlabel('False Positive Rate')
    plt.ylabel('True Positive Rate') 
    plt.title('ROC curve for AdaBoost Horse Colic Detection System') 
    ax.axis([0,1,0,1])
    plt.show()
    print "the Area Under the Curve is: ",ySum*xStep


if __name__ == '__main__':
    from minitest import *
    with test_case("horse_colic"):
        with test("multiTest"):
            dataset, labels = get_dataset_from_file('horse_colic_training2.dataset')
            classifierArray, aggClassEst = adaBoostTrainDS(dataset, labels, 10)
            classifierArray.p()
            test_dataset, test_labels = get_dataset_from_file('horse_colic_test2.dataset')
            prediction10 = adaClassify(test_dataset,classifierArray)
            errArr=mat(ones((len(test_labels),1)))
            error_count = errArr[prediction10!=mat(test_labels).T].sum()
            error_count.p()
            error_rate = error_count/float(len(test_labels))
            error_rate.p()
            pass

        with test("plotROC"):
            aggClassEst.p()
            plotROC(aggClassEst.T, labels)
            pass


