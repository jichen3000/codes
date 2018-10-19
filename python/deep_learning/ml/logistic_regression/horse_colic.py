from gradient_ascent import *
from operator import itemgetter, ne, truth
from functional_style import comb
import numpy

def get_dataset_from_file(filename):
    with open(filename) as datafile:
        words = [line.strip().split('\t') for line in datafile]
    dataset = [ [float(cell) for cell in row[:-1]] for row in words]
    labels = map(comb(itemgetter(-1), float), words)
    return dataset, labels



def horse_colic(training_dataset, training_labels, test_dataset, test_labels):
    weights = stochastic_gradient_ascent(training_dataset, training_labels, 500) 
    classify_func = partial(classify, weights = weights)
    compute_labels = map(classify_func, test_dataset)
    compare_result = map(ne, compute_labels, test_labels)
    error_count = sum(filter(truth, compare_result))
    error_rate = float(error_count)/ len(test_labels)
    print "the error rate of this test is: %f" % error_rate
    return error_rate

def multiTest():
    training_dataset, training_labels = get_dataset_from_file('horse_colic_training.dataset')
    test_dataset, test_labels = get_dataset_from_file('horse_colic_test.dataset')
    run_func = partial(horse_colic, training_dataset, training_labels, test_dataset, test_labels)

    numTests = 10; errorSum=0.0
    for k in range(numTests):
        errorSum += run_func()
    print "after %d iterations the average error rate is:%f" % (numTests, errorSum/float(numTests))

if __name__ == '__main__':
    from minitest import *
    with test_case("horse_colic"):
        with test("multiTest"):
            multiTest()
            pass

        with test("get_dataset_from_file"):
            dataset, labels = get_dataset_from_file('horse_colic_test.dataset')
            dataset[0].size().must_equal(21)
