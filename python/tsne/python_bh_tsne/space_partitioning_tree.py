import math
# import sys
import types
# import numpy
# DBL_MAX = sys.float_info.max
# DBL_MIN = sys.float_info.min

def list_all_equal(the_a, the_b):
    if type(the_a) == types.NoneType or type(the_b) == types.NoneType:
        return False;
    if len(the_a) != len(the_b):
        return False
    for i in range(len(the_a)):
        if the_a[i] != the_b[i]:
            return False
    return True


class Boundary(object):
    def __init__(self, center, half_widths):
        # super(Boundary, self).__init()
        self.center = center
        self.half_widths = half_widths

    def is_contains(self, point):
        for index in range(len(self.center)):
            if self.center[index] - self.half_widths[index] > point[index]:
                return False
            if self.center[index] + self.half_widths[index] < point[index]:
                return False
        return True

    def divide(self):
        dim_count = len(self.center)
        count = dim_count ** 2
        def inner(index):
            new_half_widths = [0.5*w for w in self.half_widths]
            new_center = self.center[:]
            div = 1
            for d_index in range(dim_count):
                if ((index/div) % 2 == 1):
                    new_center[d_index] -= new_half_widths[d_index]
                else:
                    new_center[d_index] += new_half_widths[d_index]
                div *= 2
            return Boundary(new_center, new_half_widths)

        return [inner(index) for index in range(count)]

    @classmethod
    def create_from_points(cls, points):
        point_size = len(points)
        dimension = len(points[0])
        means = [0.0] * dimension
        half_widths = [0.0] * dimension
        mins = [float("inf")] * dimension
        maxs = [-float("inf")] * dimension
        for cur_point in points:
            for index in range(dimension):
                means[index] += cur_point[index]
                if cur_point[index] > maxs[index]:
                    maxs[index] = cur_point[index]
                if cur_point[index] < mins[index]:
                    mins[index] = cur_point[index]
        for index in range(dimension):
            means[index] = means[index]/point_size
            half_widths[index] = max(maxs[index]-means[index],
                means[index]-mins[index]) + 1e-5

        return cls(means, half_widths)

    def __repr__(self):
        return "{0}({1},{2})".format(str(self.__class__)[8:-2],
                self.center,self.half_widths)

    def __eq__(self, other):
        return  self.center == other.center and \
                self.half_widths == other.half_widths

# space-partitioning tree
class SpNode(object):
    def __init__(self):
        # super(SpNode, self).__init__()
        self.cum_size = 0
        self.contain_point = None
        self.children = None
        self.center_of_mass = None
        self.is_leaf = True
        self.parent = None

        # self.buffs = None

    def insert(self, point):
        if(not self.boundary.is_contains(point)):
            return False
        self.cum_size += 1
        self.update_center_of_mass(point)

        if (self.is_leaf and type(self.contain_point) == types.NoneType):
            self.contain_point = point
            return True

        # Don't add duplicates for now (this is not very nice)
        # duplicate = point == self.contain_point
        duplicate = list_all_equal(point, self.contain_point)
        if(duplicate):
            return True

        if(self.is_leaf):
            self.subdivide()
            self.move_contain_point_to_children()

        for child in self.children:
            if child.insert(point):
                return True


        return False

    def subdivide(self):
        divided_boundarys = self.boundary.divide()
        self.children = [SpNode.create_from_boundary(self, cur_boundary)
                for cur_boundary in divided_boundarys]
        self.is_leaf = False

    def move_contain_point_to_children(self):
        for child in self.children:
            if child.insert(self.contain_point):
                break
        self.contain_point = None

    def update_center_of_mass(self, point):
        ''' calculate the center one by one point'''
        mult1 = float(self.cum_size-1)/self.cum_size
        mult2 = 1.0/self.cum_size
        for index in range(self.dimension):
            self.center_of_mass[index] *= mult1
            self.center_of_mass[index] += mult2 * point[index]



    def fill(self, points):
        # self.point_size = len(points)
        self.dimension = len(points[0])

        self.boundary = Boundary.create_from_points(points)
        self.center_of_mass = [0.0] * self.dimension


        [self.insert(cur_point) for cur_point in points]

        # self.buffs = [0.0] * self.dimension
        return self

    @classmethod
    def create_from_boundary(cls, parent, boundary):
        new_node = cls()
        new_node.parent = parent
        new_node.dimension = len(boundary.center)
        new_node.boundary = boundary
        new_node.center_of_mass = [0.0] * new_node.dimension
        return new_node

    def compute_non_edge_forces(self, points, point_index, theta, neg_f_item, sum_q):
        ''' Compute non-edge forces using Barnes-Hut algorithm
            for performance, it didn't return the values, but using references
        '''
        cur_point = points[point_index]
        if self.cum_size == 0 or (self.is_leaf and list_all_equal(cur_point, self.contain_point)):
            return

        dimension_range = range(len(self.center_of_mass))
        buffs = [cur_point[i] - self.center_of_mass[i] for i in dimension_range]
        D = 0
        # D = sys.float_info.min
        for i in dimension_range:
            D += buffs[i] * buffs[i]

        max_width = max(self.boundary.half_widths)
        if (self.is_leaf or (D>0 and max_width / math.sqrt(D) < theta)):
        # if (self.is_leaf or max_width / numpy.sqrt(D) < theta):
            D = 1.0 / (1.0 + D)
            mult = self.cum_size * D
            sum_q[0] += mult
            mult *= D
            for i in dimension_range:
                neg_f_item[i] += mult * buffs[i]
            # neg_f_item.p()
        else:
            for child in self.children:
                child.compute_non_edge_forces(points, point_index, theta,
                        neg_f_item, sum_q)


    def __str__(self, indent="  "):
        msg = repr(self.boundary)+","+str(self.contain_point)
        # msg.p()
        if self.children:
            msg += ("\n"+indent)+("\n"+indent).join(
                    [child.__str__(indent*2) for child in self.children])
        return msg

    def __repr__(self):
        return self.__str__()



if __name__ == '__main__':
    from minitest import *

    # with test(Boundary.create_from_points):
    #     Boundary.create_from_points([(1,1),(5,5)]).must_equal(
    #             Boundary([3.0, 3.0],[2.00001, 2.00001]))

    # with test(Boundary.is_contains):
    #     boundary = Boundary([3.0, 3.0],[2.00001, 2.00001])
    #     boundary.is_contains([3.1, 4.1]).must_equal(True)
    #     boundary.is_contains([3.1, 5.1]).must_equal(False)

    # with test(Boundary.divide):
    #     boundary = Boundary([3.0, 3.0],[2.00001, 2.00001])
    #     boundary.divide().must_equal([
    #         Boundary([4.000005, 4.000005],[1.000005, 1.000005]),
    #         Boundary([1.999995, 4.000005],[1.000005, 1.000005]),
    #         Boundary([4.000005, 1.999995],[1.000005, 1.000005]),
    #         Boundary([1.999995, 1.999995],[1.000005, 1.000005])
    #     ])

    with test(SpNode):
        points = [(1,1),(3,3),(5,5),(7,7),(9,9)]
        the_tree = SpNode().fill(points)
        # import ipdb; ipdb.set_trace()
        # str(the_tree)
        # the_tree.pp()

    with test(SpNode.compute_non_edge_forces):
        points = [(1.0,1.0),(3.0,3.0),(5.0,5.0),(7.0,7.0),(9.0,9.0)]
        the_tree = SpNode().fill(points)
        point_index = 2
        theta = 0.2
        row_count = len(points)
        no_dims = len(points[0])
        neg_f = [[0. for j in range(no_dims)] for i in range(row_count)]
        sum_q = [0.0]
        the_tree.compute_non_edge_forces(points, point_index, theta,
                neg_f[point_index], sum_q)
        neg_f.must_equal([
                [0.0, 0.0],
                [0.0, 0.0],
                [-8.673617379884035e-19, -8.673617379884035e-19],
                [0.0, 0.0],
                [0.0, 0.0]])
        sum_q.must_equal([0.28282828282828276])

        point_index = 1
        the_tree.compute_non_edge_forces(points, point_index, theta,
                neg_f[point_index], sum_q)
        neg_f.must_equal([
                [0.0, 0.0],
                [-0.004799009387965188, -0.004799009387965188],
                [-8.673617379884035e-19, -8.673617379884035e-19],
                [0.0, 0.0],
                [0.0, 0.0]])
        sum_q.must_equal([0.5490521654905216])

    with test(SpNode.compute_non_edge_forces):
        import numpy
        points = numpy.array([(1.0,1.0),(3.0,3.0),(5.0,5.0),(7.0,7.0),(9.0,9.0)])
        the_tree = SpNode().fill(points)
        point_index = 2
        theta = 0.2
        row_count = len(points)
        no_dims = len(points[0])
        neg_f = [0.0 for i in range(row_count * no_dims)]
        neg_f = numpy.zeros((row_count, no_dims))
        sum_q = [0.0]
        # import ipdb; ipdb.set_trace()
        the_tree.compute_non_edge_forces(points, point_index, theta,
                neg_f[point_index], sum_q)
        neg_f.tolist().must_equal([
                [0.0, 0.0],
                [0.0, 0.0],
                [-8.673617379884035e-19, -8.673617379884035e-19],
                [0.0, 0.0],
                [0.0, 0.0]])
        sum_q.must_equal([0.28282828282828276])
