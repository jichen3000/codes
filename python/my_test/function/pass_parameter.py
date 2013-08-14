'''

http://stackoverflow.com/questions/986006/python-how-do-i-pass-a-variable-by-reference

How to pass parameters in the Python.

the parameter passed in is actually a reference to a variable 
(but the reference is passed by value)
some data types are mutable, but others aren't

If you pass a mutable object into a method, 
the method gets a reference to that same object and 
you can mutate it to your heart's delight, 
but if you rebind the reference in the method, 
the outer scope will know nothing about it, and after you're done, 
the outer reference will still point at the original object.

'''

from minitest import *

with test_case("How to pass parameters"):

    with test("try_to_change_list_contents"):
        def try_to_change_list_contents(the_list):
            the_list.append('four')

        outer_list = ['one', 'two', 'three']
        try_to_change_list_contents(outer_list)
        outer_list.must_equal(['one', 'two', 'three', 'four'])
        # print outer_list.__hash__
        # dir(outer_list).p()

    with test("try_to_change_list_reference"):
        def try_to_change_list_reference(the_list):
            the_list = ['and', 'we', 'can', 'not', 'lie']

        outer_list = ['one', 'two', 'three']
        try_to_change_list_reference(outer_list)
        outer_list.must_equal(['one', 'two', 'three'])

    with test("try_to_change_hash_contents"):
        def try_to_change_hash_contents(the_hash):
            the_hash['left'] = 100

        outer_hash = {'left':1, 'right':2}
        try_to_change_hash_contents(outer_hash)
        outer_hash.must_equal({'left':100, 'right':2})
