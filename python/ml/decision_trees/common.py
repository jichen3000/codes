
from numpy import *
from pprint import pprint as pp

def gen_count_list(lst):
    # return [(value, lst.count(value)) for value in set(lst)]
    return map(lst.count, set(lst))

# input count_list will be the list of (value, count in the original list)
# count will be the size of original list
def calculate_shannon_entropy(count_list):
    total_count = sum(count_list)
    def calculate_shannon_item(item_count):
        # according to Shannon information theory
        probility = float(item_count)/total_count
        information_value = log2(probility)
        return probility * information_value * -1
    return sum(map(calculate_shannon_item, count_list))

def split_dataset(dataset, axis, value):
    return [ row[:axis] + row[axis+1:] for row in dataset
            if row[axis] == value]

def calcShannonEnt(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featVec in dataSet:
        currentLabel = featVec[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1
    shannonEnt = 0.0
    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log2(prob)
    return shannonEnt

def get_nth_column(list_list, index):
    return zip(*list_list)[index]


def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = split_dataset(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            current = prob * calcShannonEnt(subDataSet)
            newEntropy += current
            subDataSet.pp()
            current.pp()
            # newEntropy += prob * calculate_shannon_entropy(
            #     gen_count_list(get_nth_column(subDataSet, -1)))
        infoGain = baseEntropy - newEntropy
        if (infoGain > bestInfoGain):
            bestInfoGain = infoGain
            bestFeature = i
    return bestFeature

if __name__ == '__main__':
    from minitest import *

    with test_case("decision trees"):
        tself = get_test_self()
        tself.lst = ["a", "a", "f", "e", "c", "e", "b", "b", "e", "c"]
        tself.count_list = [2, 2, 2, 3, 1]
        # notice, dataset just list not the numpy.array
        tself.dataset = [
                [1, 1, 'yes'],
                [1, 1, 'yes'],
                [1, 0, 'no'],
                [0, 1, 'no'],
                [0, 1, 'no']]
        tself.labels = ['no surfacing','flippers']
        
        with test("gen_count_list"):
            gen_count_list(tself.lst).must_equal(tself.count_list)

        with test("get_nth_column"):
            get_nth_column(tself.dataset,-1).must_equal(('yes', 'yes', 'no', 'no', 'no'))

        with test("gen_count_list"):
            gen_count_list(tself.lst).must_equal(tself.count_list)

        with test("calculate_shannon_entropy"):
            calculate_shannon_entropy(tself.count_list).must_equal_with_func(
                2.24643934467, allclose)
            calculate_shannon_entropy([1,1]).must_equal_with_func(
                1.0, allclose)
            # calculate_shannon_entropy([2,0]).pp()
            # calculate_shannon_entropy([4,1]).pp()
            # calculate_shannon_entropy([3,2]).pp()
            # calcShannonEnt(tself.dataset).pp()
            # chooseBestFeatureToSplit(tself.dataset).pp()


        with test("split_dataset"):
            split_dataset(tself.dataset, 2, 'no').must_equal(
                [[1, 0], [0, 1], [0, 1]])


