import itertools

def product(*args, **kwds):
    pools  = map(tuple, args) * kwds.get('repeat', 1)
    acc = [[]]
    for cur_list  in pools:
        acc =  [x+[y] for x in acc for y in cur_list]
    for item in acc:
        yield tuple(item)

def permutations(the_list):
    acc  = [[]]
    for i in xrange(len(the_list)):
        acc =  [x+[j] for x in acc for j in xrange(len(the_list)) if j not in x]
    for item in acc:
        yield tuple(the_list[i] for i in item)


if __name__ == '__main__':
    from minitest import *

    # with test(product):
    #     la, lb = "abc","def"
    #     list(product(la, lb)).must_equal(list(itertools.product(la, lb)))
    #     list(product(la, repeat=2)).must_equal(list(itertools.product(la, repeat=2)))

    with test(permutations):
        ll = "1234"
        list(permutations(ll)).pp()
