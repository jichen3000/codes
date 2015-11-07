import collections

class A(collections.Iterable):
    pass

import bisect
class SortedItems(collections.Sequence): 
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []
        
    # Required sequence methods
    def __getitem__(self, index): 
        return self._items[index]
    
    def __len__(self):
        return len(self._items)
        
    # Method for adding an item in the right location
    def add(self, item): 
        bisect.insort(self._items, item)


if __name__ == '__main__':
    from minitest import *

    with test(A):
        (lambda : A()).must_raise(TypeError,
                "Can't instantiate abstract class A with abstract methods __iter__")

    with test(SortedItems):
        items = SortedItems([5,1,3])
        list(items).must_equal([1,3,5])
        items.add(2)
        list(items).must_equal([1,2,3,5])
        isinstance(items, collections.Iterable).must_true()
        isinstance(items, collections.Sequence).must_true()
        isinstance(items, collections.Container).must_true()
        isinstance(items, collections.Sized).must_true()
        isinstance(items, collections.Mapping).must_false()
