# index from 0
def heap_parent(index):
    return (index-1)/2
def heap_left(index):
    return index*2 + 1
def heap_right(index):
    return index*2 + 2

def max_heapify(the_list, index, heap_size=None):
    if heap_size == None:
        heap_size = len(the_list)
    # heap_size.p()
    left_index = heap_left(index)
    right_index = heap_right(index)
    # (left_index,right_index).p()
    if left_index < heap_size and the_list[left_index] > the_list[index]:
        largest_index = left_index
    else:
        largest_index = index
    if right_index < heap_size and the_list[right_index] > the_list[largest_index]:
        largest_index = right_index
    if largest_index != index:
        the_list[index],the_list[largest_index] = the_list[largest_index], the_list[index]
        max_heapify(the_list, largest_index, heap_size)

def build_max_heap(the_list):
    # len(the_list).p()
    heap_size = len(the_list)
    for i in xrange(len(the_list)/2-1,-1,-1):
        # i.p()
        max_heapify(the_list,i, heap_size)
        # the_list.p()
    return the_list

def heap_sort(the_list):
    build_max_heap(the_list)
    # the_list.p()
    heap_size = len(the_list)
    for i in xrange(len(the_list)-1,0,-1):
        the_list[0],the_list[i] = the_list[i],the_list[0]
        heap_size -= 1
        max_heapify(the_list,0,heap_size)
        # (i,heap_size,the_list).p()
    return the_list

if __name__ == '__main__':
    from minitest import *

    with test(max_heapify):
        the_list = [16,4,10,14,7,9,3,2,8,1]
        max_heapify(the_list, 1)
        the_list.must_equal([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])
        the_list = [4,1,3,2,16,9,10,14,8,7]
        max_heapify(the_list, 0)
        the_list.must_equal([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

    with test(build_max_heap):
        # the_list = [16,4,10,14,7,9,3,2,8,1]
        the_list = [4,1,3,2,16,9,10,14,8,7]
        build_max_heap(the_list)
        the_list.must_equal([16, 14, 10, 8, 7, 9, 3, 2, 4, 1])

    with test(heap_sort):
        the_list = [4,1,3,2,16,9,10,14,8,7]
        heap_sort(the_list).must_equal(
                [1, 2, 3, 4, 7, 8, 9, 10, 14, 16])
