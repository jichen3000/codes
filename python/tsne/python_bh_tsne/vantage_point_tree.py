import numpy
import heapq

def cal_distance(first, second):
    # maybe can remove the sqrt
    return numpy.sqrt(numpy.sum((first - second) ** 2))

def gen_distance_fun(origin):
    def internal(other):
        return cal_distance(origin,other)
    return internal

# notice, the range is [start_index, end_index),
# so end_index - 1 is true last index
def nth_element_by_indexes(points, indexes, start_index, nth_index, end_index, distance_fun):
    distances = [distance_fun(points[indexes[i]]) for i in range(start_index, end_index)]
    # distances.p()
    part_indexes = numpy.argpartition(distances, nth_index-start_index )
    old_indexes = indexes[start_index:end_index]
    for i in range(start_index, end_index):
        indexes[i] = old_indexes[part_indexes[i-start_index]]
    return indexes

class VpNode(object):
    def __init__(self, index, threshold=None):
        self.index = index
        self.threshold = threshold
        self.left = None
        self.right = None
    def __repr__(self):
        return "VpNode(index={0},threshold={1})".format(self.index,self.threshold)

    def __str__(self):
        return self.__repr__()

class VpTree(object):
    def __init__(self, points, indexes=None):
        # super(Boundary, self).__init()
        self.points = points
        self.indexes = indexes if indexes != None else range(len(self.points))
        self.root = self.build(0, len(points))

    def get_list_with_layer_and_pos(self, is_depth_first=True):
        pop_pos = -1 if is_depth_first else 0
        result = []
        acc = [(self.root, 0, "root", 0)]
        while len(acc) > 0:
            the_node, layer, pos, layer_pos = acc.pop(pop_pos)
            result.append((the_node, layer, pos, layer_pos))
            if is_depth_first:
                if the_node.right != None:
                    acc.append((the_node.right,layer+1,"right", layer_pos*2+1))
                if the_node.left != None:
                    acc.append((the_node.left,layer+1,"left", layer_pos*2+0))
            else:
                if the_node.left != None:
                    acc.append((the_node.left,layer+1,"left", layer_pos*2+0))
                if the_node.right != None:
                    acc.append((the_node.right,layer+1,"right", layer_pos*2+1))
        return result

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        acc = self.get_list_with_layer_and_pos(True)
        msg = "VpTree:\n"
        # acc.p()
        for the_node, layer, pos, layer_pos  in acc:
            msg +=  "  " * layer +pos+":"+str(layer_pos)+":"+ str(the_node) + "\n"
            # msg += str(the_node)
        return msg

    def build(self, lower, upper):
        # (lower, upper).p()
        if (upper == lower):
            return None
        new_node = VpNode(self.indexes[lower])

        if (upper > lower + 1):
            # random_index = numpy.random.randint(lower, upper)
            # if lower != random_index:
            #     self.indexes[random_index], self.indexes[lower] =
            #             self.indexes[lower], self.indexes[random_index]

            median = (upper + lower) / 2
            # median.p()

            # self.indexes.p()
            self.indexes = nth_element_by_indexes(self.points, self.indexes,
                    lower + 1, median, upper,
                    gen_distance_fun(self.points[new_node.index]))
            # self.indexes.p()

            new_node.threshold = cal_distance(self.points[new_node.index],
                    self.points[self.indexes[median]])
            new_node.left = self.build(lower+1, median)
            new_node.right = self.build(median, upper)

        return new_node

    def search(self, target_point, count):
        # target_point.p()
        self.tau = float("inf")
        the_heap = []
        self.search_in_nodes(self.root, target_point, count, the_heap)
        distances = []
        indexes = []
        for i in range(count):
            item=heapq.heappop(the_heap)
            distances.append(0 - item[0])
            indexes.append(item[1])
        # 'the_heap :', [(48.0, 1), (27.0, 6), (12.0, 7), (3.0, 8), (0.0, 9)]
        distances.reverse()
        indexes.reverse()
        return (distances, indexes)

    def search_in_nodes(self, the_node, target_point, count, the_heap):
        if the_node == None:
            return

        # the_node.index.p()
        # self.points[the_node.index].p()
        distance = cal_distance(self.points[the_node.index], target_point)

        if(distance < self.tau):
            if(len(the_heap) == count):
                heapq.heappushpop(the_heap, (0-distance, the_node.index))
                self.tau = 0 - the_heap[0][0]
                # the_heap.p()
            else:
                heapq.heappush(the_heap, (0-distance, the_node.index))
                # the_heap.p()

        if(the_node.left == None and the_node.right == None):
            return

        if(distance < the_node.threshold):
            self.search_in_nodes(the_node.left, target_point, count, the_heap)
            if (self.tau + distance >= the_node.threshold):
                self.search_in_nodes(the_node.right, target_point, count, the_heap)
        else:
            self.search_in_nodes(the_node.right, target_point, count, the_heap)
            if (self.tau >= distance - the_node.threshold):
                self.search_in_nodes(the_node.left, target_point, count, the_heap)



if __name__ == '__main__':
    from minitest import *
    inject(numpy.allclose, 'must_close')

    def zero_mean(data):
        return data-numpy.mean(data,0)

    with test(VpTree):
        D = 3
        N = 10
        points = numpy.ones([N,D])
        for i in range(N): points[i] = points[i] * i
        indexes = [6, 0, 3, 5, 7, 8, 4, 1, 2, 9]
        vp_tree = VpTree(points, indexes)
        vp_tree.indexes.must_equal([6, 4, 5, 7, 8, 9, 3, 2, 1, 0])

    with test(VpTree.search):
        D = 3
        N = 10
        points = numpy.ones([N,D])
        for i in range(N): points[i] = points[i] * i
        # indexes = [6, 0, 3, 5, 7, 8, 4, 1, 2, 9]
        indexes = None
        # points.p()
        # points = zero_mean(points)
        # points = points/numpy.max(points)
        # points.p()
        vp_tree = VpTree(points, indexes)
        # vp_tree.p()
        # vp_tree.indexes.must_equal([6, 4, 5, 7, 8, 9, 3, 2, 1, 0])
        distances, indexes = vp_tree.search(points[5],5)
        # distances.must_equal([12.0, 12.0, 3.0, 3.0, 0.0])
        indexes.must_equal([5, 6, 4, 7, 3])
        distances, indexes = vp_tree.search(points[9],5)
        # distances.must_equal([48.0, 27.0, 12.0, 3.0, 0.0])
        indexes.must_equal([9, 8, 7, 6, 5])
        # points.pp()
        # the_heap.must_equal([(12.0, 3), (12.0, 7), (3.0, 4), (3.0, 6), (0.0, 5)])

    with test("minus"):
        D = 3
        N = 10
        points = numpy.ones([N,D])
        for i in range(N): points[i] = points[i] * i
        # indexes = None
        indexes = [6, 0, 3, 5, 7, 8, 4, 1, 2, 9]
        # points.p()
        points = zero_mean(points)
        # points.p()
        vp_tree = VpTree(points, indexes)
        # vp_tree.p()
        distances, indexes = vp_tree.search(points[5],5)
        # distances.must_equal([12.0, 12.0, 3.0, 3.0, 0.0])
        indexes.must_equal([5, 6, 4, 7, 3])

    with test("compare with cpp"):
        D = 3
        N = 10
        points = numpy.ones([N,D])
        for i in range(N): points[i] = points[i] * i
        indexes = None
        # indexes = [6, 0, 3, 5, 7, 8, 4, 1, 2, 9]
        # points.p()
        points = zero_mean(points)
        # points.p()
        vp_tree = VpTree(points, indexes)
        # vp_tree.p()
        distances, indexes = vp_tree.search(points[2],7)
        # distances.must_equal([12.0, 12.0, 3.0, 3.0, 0.0])
        # indexes.must_equal([2, 3, 1, 4, 0, 5, 6])
        indexes.must_equal([2, 1, 3, 4, 0, 5, 6])
