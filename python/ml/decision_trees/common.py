
from numpy import *
from pprint import pprint as pp
import operator

def gen_count_list(lst):
    # return [(value, lst.count(value)) for value in set(lst)]
    return map(lst.count, set(lst))

def split_dataset(dataset, axis, value):
    return [ row[:axis] + row[axis+1:] for row in dataset
            if row[axis] == value]

# def calcShannonEnt(dataSet):
#     numEntries = len(dataSet)
#     labelCounts = {}
#     for featVec in dataSet:
#         currentLabel = featVec[-1]
#         if currentLabel not in labelCounts.keys():
#             labelCounts[currentLabel] = 0
#         labelCounts[currentLabel] += 1
#     shannonEnt = 0.0
#     for key in labelCounts:
#         prob = float(labelCounts[key])/numEntries
#         shannonEnt -= prob * log2(prob)
#     return shannonEnt

def get_nth_column(list_list, index):
    return zip(*list_list)[index]

# input count_list will be the list of (value, count in the original list)
# count will be the size of original list
def calculate_shannon_entropy_for_count_list(count_list):
    total_count = sum(count_list)
    def calculate_shannon_item(item_count):
        # according to Shannon information theory
        probility = float(item_count)/total_count
        information_value = log2(probility)
        return probility * information_value * -1
    return sum(map(calculate_shannon_item, count_list))

def calculate_shannon_entropy_for_dataset(dataset):
    return calculate_shannon_entropy_for_count_list(
                gen_count_list(get_nth_column(dataset, -1)))

def calculate_shannon_entropy_for_split_dataset(dataset, column_index):
    def calculate_sub(value):
        sub_dataset = split_dataset(dataset, column_index, value)
        prob = len(sub_dataset)/float(len(dataset))
        return prob * calculate_shannon_entropy_for_dataset(sub_dataset)
    return sum(map(calculate_sub, set(get_nth_column(dataset, column_index))))

# dispatch method
def calculate_shannon_entropy(dataset_or_list, split_column_index=None):
    if not isinstance(dataset_or_list[0], list):
        return calculate_shannon_entropy_for_count_list(dataset_or_list)
    elif split_column_index == None:
        return calculate_shannon_entropy_for_dataset(dataset_or_list)
    else:
        return calculate_shannon_entropy_for_split_dataset(dataset_or_list, split_column_index)

# The first assumption is that it comes in the form of a list of lists, 
# and all these lists are of equal size. 
# The next assumption is that the last column in the data or the last item 
# in each instance is the class label of that instance.
def choose_best_feature_to_split(dataset):
    num_features = len(dataset[0]) - 1
    base_entropy = calculate_shannon_entropy(dataset)
    best_info_gain = 0.0
    best_feature = -1
    for i in range(num_features):
        new_entropy = calculate_shannon_entropy(dataset, split_column_index=i)
        infoGain = base_entropy - new_entropy
        if (infoGain > best_info_gain):
            best_info_gain = infoGain
            best_feature = i
    return best_feature


def most_common(lst):
    return max(set(lst), key=lst.count)

def copy_remove_index(lst, index):
    return lst[:index] + lst[index+1:]

def create_tree(dataset,labels):
    # Stop when all classes are equal
    class_list = get_nth_column(dataset, -1)
    if len(set(class_list)) == 1:
        return class_list[0]

    # When no more features, return majority
    if len(dataset[0]) == 1:
        return most_common(class_list)

    # fearture index just equals column index
    best_feature_index = choose_best_feature_to_split(dataset) 
    feature_values = get_nth_column(dataset, best_feature_index)

    sub_labels = copy_remove_index(labels, best_feature_index)
    sub_tree = {value : create_tree(split_dataset(dataset, best_feature_index, value),sub_labels) 
        for value in set(feature_values)}
    return {labels[best_feature_index] : sub_tree}


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
        tself.labels = ['no surfacing','flippers', 'fish']
        
        with test("gen_count_list"):
            gen_count_list(tself.lst).must_equal(tself.count_list)

        with test("get_nth_column"):
            get_nth_column(tself.dataset,-1).must_equal(('yes', 'yes', 'no', 'no', 'no'))

        with test("gen_count_list"):
            gen_count_list(tself.lst).must_equal(tself.count_list)

        with test("calculate_shannon_entropy"):
            calculate_shannon_entropy(tself.count_list).must_equal_with_func(
                2.24643934467, allclose)
            calculate_shannon_entropy([3,2]).must_equal_with_func(
                0.97095059445466858, allclose)
            calculate_shannon_entropy([1,1]).must_equal_with_func(
                1.0, allclose)
            calculate_shannon_entropy([1]).must_equal_with_func(
                0.0, allclose)
            calculate_shannon_entropy(tself.dataset).must_equal_with_func(
                0.97095059445466858, allclose)
            calculate_shannon_entropy(tself.dataset, split_column_index=0).must_equal_with_func(
                0.55097750043269367, allclose)
            # calculate_shannon_entropy([2,0]).pp()
            # calculate_shannon_entropy([4,1]).pp()
            # calculate_shannon_entropy([3,2]).pp()


        with test("split_dataset"):
            split_dataset(tself.dataset, 2, 'no').must_equal(
                [[1, 0], [0, 1], [0, 1]])

        with test("choose best "):
            choose_best_feature_to_split(tself.dataset).must_equal(0)

        with test("most common"):
            most_common(tself.count_list).must_equal(2)

        with test("create_tree"):
            create_tree(tself.dataset, tself.labels).must_equal(
                {'no surfacing': {0: 'no', 1: {'flippers': {0: 'no', 1: 'yes'}}}})

