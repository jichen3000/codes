import random
def gen_sample_tuple_list(count=15):
    return random.sample(zip(range(count), range(100,100+count)), 
        count)

from functools import partial
import operator

if __name__ == '__main__':
    print gen_sample_tuple_list()
    random_list = [
        (11, 111), (0, 100), (5, 105), (1, 101), (9, 109), 
        (3, 103), (14, 114), (6, 106), (10, 110), (13, 113), 
        (4, 104), (8, 108), (7, 107), (12, 112), (2, 102)]

    print map(operator.itemgetter(1), random_list)

    # print filter(partial(operator.gt, operator.itemgetter(1)))
    print filter(lambda entry: entry[0] > 6, random_list)
    print operator.itemgetter(0)(random_list[0])
    print sorted(random_list, key=operator.itemgetter(0),
        reverse=True)