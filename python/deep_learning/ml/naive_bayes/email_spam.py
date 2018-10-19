import numpy
import os

from bayes_common import *

def file_parse(filename):
    with open(filename) as datafile:
        words = text_parse(datafile.read())
    return words

def test_parse_on_path(pathname):
    return [file_parse(os.path.join(pathname, filename))
        for filename in os.listdir(pathname)]

def run_evaluate(spam_docs, normal_docs, test_each_count):

    datasets = dispatch_training_and_test_dataset(
        spam_docs, normal_docs, test_each_count)

    vocabs = create_vocab_list(spam_docs + normal_docs)

    return evaluate(vocabs,
        datasets['test']['docs'], datasets['test']['classes'], 
        datasets['training']['docs'], datasets['training']['classes'])


if __name__ == '__main__':
    from minitest import *

    with test_case("email spam"):
        with test("file_parse"):
            words = file_parse('ham/6.dataset')
            len(words).must_equal(198)
            words[:4].must_equal(['hello', 'since', 'you', 'are'])
            words[195:].must_equal(['changes', 'google', 'groups'])

        with test("run_evaluate"):
            test_each_count = 5
            run_evaluate(test_parse_on_path('spam'),
                test_parse_on_path('ham'), 
                test_each_count).must_equal((1,10))
