import numpy

# def gen_comparator(origin):
#     def internal(first, second):
#         return cal_distance(origin,first) > cal_distance(origin,second)
#     return internal
#
def cal_distance(first, second):
    return numpy.sum((first - second) ** 2)

def gen_distance_fun(origin):
    def internal(other):
        return cal_distance(origin,other)
    return internal

# notice, the range is [start_index, end_index),
# so end_index - 1 is true last index
def nth_element_by_indexs(points, indexs, start_index, nth_index, end_index, distance_fun):
    distances = [distance_fun(points[indexs[i]]) for i in range(start_index, end_index)]
    # distances.p()
    part_indexs = numpy.argpartition(distances, nth_index-start_index )
    # part_indexs.p()
    old_indexs = indexs[start_index:end_index]
    for i in range(start_index, end_index):
        indexs[i] = old_indexs[part_indexs[i-start_index]]
    return indexs

if __name__ == '__main__':
    from minitest import *

    inject(numpy.allclose, 'must_close')

    # with test(nth_element):
    #     numpy.random.seed(2)
    #     points = numpy.random.randint(0,10, (10,2))
    #     indexs = range(points.shape[0])

    with test(cal_distance):
        numpy.random.seed(2)
        points = numpy.random.randint(0,10, (10,2))
        points[0].must_close([8,8])
        points[1].must_close([6,2])
        cal_distance(points[0],points[1]).must_equal(40)

    # with test(gen_comparator):
    #     numpy.random.seed(2)
    #     points = numpy.random.randint(0,10, (10,2))
    #     points[0].must_close([8,8])
    #     points[1].must_close([6,2])
    #     points[2].must_close([8,7])
    #     the_comparator = gen_comparator(points[0])
    #     the_comparator(points[1],points[2]).must_true()

    with test(nth_element_by_indexs):
        D = 3
        N = 10
        points = numpy.ones([N,D])
        for i in range(N): points[i] = points[i] * i
        indexs = [6, 0, 3, 5, 7, 8, 4, 1, 2, 9]
        # distances with 0
        # [40, 1, 85, 25, 25, 26, 20, 26, 53]
        #  1,  2,  3,  4,  5,  6,  7,  8,  9
        indexs1 = nth_element_by_indexs(points,indexs, 1, 5, 10,
                gen_distance_fun(points[indexs[0]]))
        indexs1.must_close([6, 4, 8, 5, 7, 9, 3, 1, 2, 0])

        # [32, 34, 37, 45]
        # indexs = [0, 2, 7, 5, 4, 8, 6, 1, 3, 9]
        # indexs2 = nth_element_by_indexs(points,indexs, 6, 7, 10,
        #         gen_distance_fun(points[indexs[5]]))
        # indexs2.p()
        # # indexs1.must_close([0, 2, 7, 5, 4, 8, 6, 1, 3, 9])
