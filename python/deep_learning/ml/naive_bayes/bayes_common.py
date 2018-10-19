# from chapter 4 of Machine Learning in Action

import numpy

def word_filter(word):
    return len(word) > 2 and not word.isdigit()

def text_parse(content):
    import re
    words = re.split(r'\W*', content)
    words = filter(word_filter ,words)
    words = map(type(words[0]).lower, words)
    return words


def create_vocab_list(dataset):
    all_set = set(item for sublist in dataset for item in sublist)
    return  list(all_set)

def words_from_dataset(dataset):
    return [item for sublist in dataset for item in sublist]

def words_to_vector(input_words, vocab_list):
    return map(list(set(input_words)).count, vocab_list)
    # word_vector = [0]*len(vocab_list)
    # for word in input_words:
    #     if word in vocab_list:
    #         word_vector[vocab_list.index(word)] = 1
    #     else: 
    #         print "the word: '%s' is not in my Vocabulary!" % word
    # return word_vector

def words_to_bag_vector(input_words, vocab_list=[]):
    return map(input_words.count, vocab_list)

def train_naive_bayes(train_matrix,classes):
    def matrix_filter_by_value(current_value):
        return [train_matrix[index] for index, value 
            in enumerate(classes) if value == current_value]

    def caculate_probability(value_matrix):
        row_sums = numpy.sum(value_matrix ,axis=0) # sum by row
        # modify for 0
        row_sums += numpy.ones(len(row_sums))
        all_sum = 2 + numpy.sum(value_matrix)
        return numpy.log(row_sums/float(all_sum))

    value_0_matrix = matrix_filter_by_value(0)
    value_1_matrix = matrix_filter_by_value(1)
    prob_1_class = sum(classes)/float(len(train_matrix)) 
    return caculate_probability(value_0_matrix),\
        caculate_probability(value_1_matrix),prob_1_class

def classify_naive_bayes(words_on_vector, 
        prob_0_vector=[], prob_1_vector=[], prob_1_class=0):
    p1 = sum(words_on_vector * prob_1_vector) + \
        numpy.log(prob_1_class)
    p0 = sum(words_on_vector * prob_0_vector) + \
        numpy.log(1.0 - prob_1_class)
    # print p1, p0
    if p1 > p0:
        return 1
    else:
        return 0

def dispatch_training_and_test_dataset(docs_1, docs_0, 
        test_each_count):
    test_docs = docs_1[:test_each_count] \
        + docs_0[:test_each_count]
    test_classes = [1] * test_each_count + [0] * test_each_count

    training_docs = docs_1[test_each_count:] \
        + docs_0[test_each_count:]
    training_classes = [1] * (len(docs_1) - test_each_count) \
        + [0] * (len(docs_0) - test_each_count)
    return {'test':{'docs':test_docs, 'classes':test_classes},
            'training': {'docs':training_docs, 'classes':training_classes}}

def random_dispatch_training_and_test_dataset(docs_1, docs_0, 
        test_count):
    import random
    all_docs = docs_1 + docs_0
    all_classes = [1] * len(docs_1) + [0] * len(docs_1)
    test_indexs = sorted(random.sample(
        range(len(all_docs)), test_count), reverse=True)
    test_docs = map(all_docs.pop, test_indexs)
    test_classes = map(all_classes.pop, test_indexs)
    training_docs = all_docs
    training_classes = all_classes
    return {'test':{'docs':test_docs, 'classes':test_classes},
            'training': {'docs':training_docs, 'classes':training_classes}}

def evaluate(vocabs, test_docs, test_classes, 
    training_docs, training_classes):

    from functools import partial
    # bag_vector_func = partial(words_to_bag_vector, 
    #     vocab_list=vocabs)
    bag_vector_func = partial(words_to_vector, 
        vocab_list=vocabs)

    test_matrix = map(bag_vector_func, test_docs)

    training_matrix = map(bag_vector_func, training_docs)

    prob_0_vector, prob_1_vector, prob_1_class=train_naive_bayes(
        training_matrix,training_classes)
    classify_func = partial(classify_naive_bayes,
        prob_0_vector=prob_0_vector,prob_1_vector=prob_1_vector,
        prob_1_class=prob_1_class)
    actual_test_classes = map(classify_func, test_matrix)
    print actual_test_classes
    print test_classes
    import operator
    error_count = [actual==expected for actual, expected 
        in zip(actual_test_classes, test_classes)].count(False)
    return error_count, len(test_docs)



if __name__ == '__main__':
    from minitest import *
    from functools import partial

    def create_dataset():
        posting_list=[['my', 'dog', 'has', 'flea', \
                       'problems', 'help', 'please'],
                      ['maybe', 'not', 'take', 'him', \
                       'to', 'dog', 'park', 'stupid'],
                      ['my', 'dalmation', 'is', 'so', 'cute', \
                       'I', 'love', 'him'],
                      ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                      ['mr', 'licks', 'ate', 'my', 'steak', 'how',\
                       'to', 'stop', 'him'],
                      ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
        #1 is abusive, 0 not
        class_vector = [0,1,0,1,0,1]
        return posting_list,class_vector

    def gen_classify_func(prob_0_vector, prob_1_vector, prob_1_class, 
            vocab_list):
        def classify_func(input_words):
            words_on_vector = words_to_vector(input_words, vocab_list)
            return classify_naive_bayes(
                words_on_vector, prob_0_vector, prob_1_vector, prob_1_class)
        return classify_func

    with test_case("bayes"):
        tself = get_test_self()
        tself.dataset, tself.classes = create_dataset()
        tself.vocab_list = create_vocab_list(tself.dataset)

        with test("words_from_dataset"):
            words_from_dataset(tself.dataset[:2]).must_equal(
                ['my', 'dog', 'has', 'flea', 'problems', 'help', 
                 'please', 'maybe', 'not', 'take', 'him', 'to', 
                  'dog', 'park', 'stupid'])
        with test("create_vocab_list"):
            create_vocab_list(tself.dataset).must_equal(
                ['cute', 'love', 'help', 'garbage', 'food', 'is', 
                 'stop', 'flea', 'quit', 'worthless', 'licks', 'how', 
                 'please', 'to', 'take', 'has', 'posting', 'I', 'problems', 
                 'park', 'dalmation', 'not', 'him', 'buying', 'ate', 
                 'maybe', 'dog', 'stupid', 'so', 'mr', 'steak', 'my'])

                # ['cute', 'love', 'help', 'garbage', 'quit', 'I', 
                #  'problems', 'is', 'park', 'stop', 'flea', 'dalmation', 
                #  'licks', 'food', 'not', 'him', 'buying', 'posting', 
                #  'has', 'worthless', 'ate', 'to', 'maybe', 'please', 
                #  'dog', 'how', 'stupid', 'so', 'take', 'mr', 'steak', 
                #  'my']

        with test("words_to_vector"):
            words_to_vector(tself.dataset[3], tself.vocab_list).must_equal(
                [0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 
                 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0])

        with test("words_to_bag_vector"):
            bag_vector = [0, 3, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 
                          0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                          0, 0, 0, 0, 0, 0, 0, 0]
            words_to_bag_vector("love food love love".split(" "), 
                tself.vocab_list).must_equal(bag_vector)
            bag_func = partial(words_to_bag_vector, 
                vocab_list=tself.vocab_list)
            bag_func("love food love love".split(" ")).must_equal(
                bag_vector)

        with test("train_naive_bayes"):
            vector_func = partial(words_to_vector, 
                vocab_list=tself.vocab_list)
            train_matrix = map(vector_func, tself.dataset)
            prob_0_vector, prob_1_vector, prob_1_class=train_naive_bayes(
                train_matrix,tself.classes)
            prob_0_vector.must_equal_with_func(numpy.array(
                  [-2.56494936, -2.56494936, -2.56494936, -3.25809654, -3.25809654,
                   -2.56494936, -2.56494936, -2.56494936, -3.25809654, -3.25809654,
                   -2.56494936, -2.56494936, -2.56494936, -2.56494936, -3.25809654,
                   -2.56494936, -3.25809654, -2.56494936, -2.56494936, -3.25809654,
                   -2.56494936, -3.25809654, -2.15948425, -3.25809654, -2.56494936,
                   -3.25809654, -2.56494936, -3.25809654, -2.56494936, -2.56494936,
                   -2.56494936, -1.87180218]), numpy.allclose)
            prob_1_vector.must_equal(numpy.array(
                  [-3.04452244, -3.04452244, -3.04452244, -2.35137526, -2.35137526,
                   -3.04452244, -2.35137526, -3.04452244, -2.35137526, -1.94591015,
                   -3.04452244, -3.04452244, -3.04452244, -2.35137526, -2.35137526,
                   -3.04452244, -2.35137526, -3.04452244, -3.04452244, -2.35137526,
                   -3.04452244, -2.35137526, -2.35137526, -2.35137526, -3.04452244,
                   -2.35137526, -1.94591015, -1.65822808, -3.04452244, -3.04452244,
                   -3.04452244, -3.04452244]), numpy.allclose)
            prob_1_class.must_equal(0.5)

        with test("classify_naive_bayes"):
            words = ['love', 'my', 'dalmation']
            words_on_vector = words_to_vector(words, tself.vocab_list)
            classify_naive_bayes(words_on_vector,
                prob_0_vector,prob_1_vector,prob_1_class).must_equal(0)

        with test("gen_classify_func"):
            classify_func = gen_classify_func(
                prob_0_vector,prob_1_vector,prob_1_class, tself.vocab_list)
            classify_func(['love', 'my', 'dalmation']).must_equal(0)
            classify_func(['stupid', 'garbage']).must_equal(1)

