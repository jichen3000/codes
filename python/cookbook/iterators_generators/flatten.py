from collections import Iterable

def flatten(items, ignore_types=(str, bytes)): 
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types): 
            # yield from flatten(x)
            for y in flatten(x):
                yield y
        else:
            yield x

if __name__ == '__main__':
    from minitest import *

    with test(flatten):
        items = [1, 2, [3, 4, [5, 6], 7], 8]
        list(flatten(items)).must_equal(
                [1, 2, 3, 4, 5, 6, 7, 8])
        pass