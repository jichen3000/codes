def kth_largest_with_sort(the_list, k):
    return sorted(the_list,reverse=True)[k-1]

def insert_to_ordered_large_and_limited_size(the_list, max_size, value):
    inserted = False
    for index in range(len(the_list)):
        if the_list[index] < value:
            the_list.insert(index, value)
            inserted = True
            break
    if not inserted and  max_size > len(the_list):
        the_list.append(value)
    if inserted and len(the_list) > max_size:
        the_list.pop()
    return the_list

def kth_largest_with_insert(the_list,k):
    largest_list = []
    for i in the_list:
        insert_to_ordered_large_and_limited_size(largest_list, k, i)
    return largest_list[-1]

if __name__ == '__main__':
    from minitest import *

    unique_list = range(5)
    with test(kth_largest_with_sort):
        kth_largest_with_sort(unique_list,2).must_equal(3)
        pass

    with test(insert_to_ordered_large_and_limited_size):
        the_list = []
        max_size = 2
        insert_to_ordered_large_and_limited_size(
                the_list, max_size, 1)
        the_list.must_equal([1])
        insert_to_ordered_large_and_limited_size(
                the_list, max_size, 5)
        the_list.must_equal([5,1])
        insert_to_ordered_large_and_limited_size(
                the_list, max_size, 6)
        the_list.must_equal([6,5])
        insert_to_ordered_large_and_limited_size(
                the_list, max_size, 4)
        the_list.must_equal([6,5])
        insert_to_ordered_large_and_limited_size(
                the_list, max_size, 7)
        the_list.must_equal([7,6])
        pass

    with test(kth_largest_with_insert):
        kth_largest_with_insert(unique_list,2).must_equal(3)
        