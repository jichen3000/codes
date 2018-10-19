import heap
class MaxPriorityQueue(object):
    def __init__(self, the_list):
        self.max_heap = heap.build_max_heap(the_list)
        self.heap_size = len(the_list)

    def get_max(self):
        return self.max_heap[0]

    def pop_max(self):
        if self.heap_size == 0:
            raise "heap underflow"
        max_value = self.max_heap[0]
        self.max_heap[0] = self.max_heap[self.heap_size-1]
        self.heap_size -= 1
        heap.max_heapify(self.max_heap, 0)
        return max_value

    def increase_key(self, index, new_value):
        if new_value < self.max_heap[index]:
            raise "new value is smaller than current value"
        self.max_heap[index] = new_value
        i = index
        while i > 0 and self.max_heap[heap.heap_parent(i)] < self.max_heap[i]:
            self.max_heap[heap.heap_parent(i)],self.max_heap[i] = self.max_heap[i],self.max_heap[heap.heap_parent(i)]
            i = heap.heap_parent(i)
        return new_value

    def insert(self, the_value):
        self.heap_size += 1
        if self.heap_size > len(self.max_heap):
            self.max_heap.append(the_value)
        else:
            self.max_heap[self.heap_size-1] = the_value
        return self.increase_key(self.heap_size-1, the_value)

    def __repr__(self):
        return str(self.max_heap)

if __name__ == '__main__':
    from minitest import *

    with test("get_max"):
        the_list = [4,1,3,2,16,9,10,14,8,7]
        pq = MaxPriorityQueue(the_list)
        pq.get_max().must_equal(16)

    with test("pop_max"):
        the_list = [4,1,3,2,16,9,10,14,8,7]
        pq = MaxPriorityQueue(the_list)
        str(pq).must_equal(str([16, 14, 10, 8, 7, 9, 3, 2, 4, 1]))
        pq.pop_max().must_equal(16)
        pq.pop_max().must_equal(14)
        str(pq).must_equal(str([10, 8, 9, 4, 7, 1, 3, 2, 1, 1]))

    with test("increase_key"):
        the_list = [4,1,3,2,16,9,10,14,8,7]
        pq = MaxPriorityQueue(the_list)
        str(pq).must_equal(str([16, 14, 10, 8, 7, 9, 3, 2, 4, 1]))
        pq.increase_key(1,15)
        str(pq).must_equal(str([16, 15, 10, 8, 7, 9, 3, 2, 4, 1]))
        pq.increase_key(9,12)
        str(pq).must_equal(str([16, 15, 10, 8, 12, 9, 3, 2, 4, 7]))
        pq.increase_key(9,17)
        str(pq).must_equal(str([17, 16, 10, 8, 15, 9, 3, 2, 4, 12]))

    with test("increase_key"):
        the_list = [4,1,3,2,16,9,10,14,8,7]
        pq = MaxPriorityQueue(the_list)
        str(pq).must_equal(str([16, 14, 10, 8, 7, 9, 3, 2, 4, 1]))
        pq.insert(18)
        str(pq).must_equal(str([18, 16, 10, 8, 14, 9, 3, 2, 4, 1, 7]))
        pq.insert(0)
        str(pq).must_equal(str([18, 16, 10, 8, 14, 9, 3, 2, 4, 1, 7, 0]))
        pq.insert(11)
        str(pq).must_equal(str([18, 16, 11, 8, 14, 10, 3, 2, 4, 1, 7, 0, 9]))

