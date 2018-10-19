import operator

from bayes_common import *

def feed_parse(feed_url):
    import feedparser
    content=feedparser.parse(feed_url)
    summaries = map(operator.itemgetter('summary'), content['entries'])

    # summaries = [entry['summary']
    #                 for entry in content['entries']]
    return map(text_parse, summaries)

def top_frequencies(words, vocabs=[], count=30):
    frequencies = map(words.count, vocabs)
    word_frequencies = [(word, freq) for freq, word 
        in zip(frequencies, vocabs) if freq>0]
    return sorted(word_frequencies, key=operator.itemgetter(1),
        reverse=True)[:count]

def get_stop_words(filename="stop_words.txt"):
    with open(filename) as data_file:
        words = data_file.read().split("\n")
    return words

def remove_subset(lst, sub_lst):
    return [x for x in lst if x not in sub_lst]

def modify_vocabs(vocabs, all_docs):
    print len(vocabs)
    vocabs = remove_subset(vocabs, get_stop_words())
    print len(vocabs)
    top_n_frequencies = top_frequencies(words_from_dataset(
        all_docs), vocabs, 70)
    top_n_words = map(operator.itemgetter(0), top_n_frequencies)
    return remove_subset(vocabs,top_n_words)

def run_evaluate(docs_1, docs_0, test_count):
    datasets = random_dispatch_training_and_test_dataset(
        docs_1, docs_0, test_count)

    all_docs = docs_1 + docs_0
    vocabs = create_vocab_list(all_docs)
    vocabs = modify_vocabs(vocabs, all_docs)

    return evaluate(vocabs,
        datasets['test']['docs'], datasets['test']['classes'], 
        datasets['training']['docs'], datasets['training']['classes'])


def get_city_top_words(docs_1, docs_0):
    all_docs = docs_1 + docs_0
    vocabs = create_vocab_list(all_docs)
    vocabs = modify_vocabs(vocabs, all_docs)

    from functools import partial
    # bag_vector_func = partial(words_to_bag_vector, 
    #     vocab_list=vocabs)
    bag_vector_func = partial(words_to_vector, 
        vocab_list=vocabs)


    training_matrix = map(bag_vector_func, all_docs)
    training_classes = [1] * len(docs_1) + [0] * len(docs_0)

    prob_0_vector, prob_1_vector, prob_1_class=train_naive_bayes(
        training_matrix,training_classes)

    def get_top_words(vocabs, prob_vector):
        top_words =  filter(lambda entry: entry[1] > -6.0, 
            zip(vocabs, prob_vector))
        top_words = sorted(top_words, key=operator.itemgetter(1),
            reverse=True)
        return top_words

    return get_top_words(vocabs, prob_1_vector), \
        get_top_words(vocabs, prob_0_vector)

if __name__ == '__main__':
    from minitest import *

    with test_case("city words"):
        tself = get_test_self()
        tself.vocabs = ['cute', 'love', 'help', 'garbage', 'food', 'is', 
                 'stop', 'flea', 'quit', 'worthless', 'licks', 'how', 
                 'please', 'to', 'take', 'has', 'posting', 'I', 'problems', 
                 'park', 'dalmation', 'not', 'him', 'buying', 'ate', 
                 'maybe', 'dog', 'stupid', 'so', 'mr', 'steak', 'my']

        with test("top_frequencies"):
            words = "I is buying food food food is is is is".split(" ")
            top_frequencies(words,tself.vocabs).must_equal(
                [('is', 5), ('food', 3), ('I', 1), ('buying', 1)])

        # with test("run_evaluate"):
        #     test_count = 20
            # run_evaluate(feed_parse('http://newyork.craigslist.org/stp/index.rss'),
            #     feed_parse('http://sfbay.craigslist.org/stp/index.rss'), 
        #         test_count).pp()

        with test("get_stop_words"):
            len(get_stop_words()).must_equal(174)

        with test("remove_subset"):
            remove_subset(range(10),(1,4,3,9,11)).must_equal(
                [0, 2, 5, 6, 7, 8])

        with test("get_city_top_words"):
            get_city_top_words(feed_parse('http://newyork.craigslist.org/stp/index.rss'),
                feed_parse('http://sfbay.craigslist.org/stp/index.rss')).pp()
