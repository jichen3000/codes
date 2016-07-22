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

    def insert(self, point):
        if(not self.boundary.is_contains(point)):
            return False
        self.cum_size += 1
        self.update_center_of_mass(point)

        if (self.is_leaf and self.contain_point == None):
            self.contain_point = point
            return True

        # Don't add duplicates for now (this is not very nice)
        duplicate = point == self.contain_point
        if(duplicate):
            return True

        if(self.is_leaf):
            self.subdivide()

        for child in self.children:
            if child.insert(point):
                return True


        return False

    def subdivide(self):
        divided_boundarys = self.boundary.divide()
        self.children = [SpNode.create_from_boundary(self, cur_boundary)
                for cur_boundary in divided_boundarys]

        self.move_contain_point_to_children()

        self.is_leaf = False

    def move_contain_point_to_children(self):
        for child in self.children:
            if child.insert(self.contain_point):
                break
        self.contain_point = None

    def update_center_of_mass(self, point):
        mult1 = float(self.cum_size-1)/self.cum_size
        mult2 = 1.0/self.cum_size
        for index in range(self.dimension):
            self.center_of_mass[index] *= mult1
            self.center_of_mass[index] += mult2 * point[index]



    def fill(self, points):
        self.point_size = len(points)
        self.dimension = len(points[0])

        self.boundary = Boundary.create_from_points(points)
        self.center_of_mass = [0.0] * self.dimension


        [self.insert(cur_point) for cur_point in points]
        return self

    @classmethod
    def create_from_boundary(cls, parent, boundary):
        new_node = cls()
        new_node.parent = parent
        new_node.dimension = len(boundary.center)
        new_node.boundary = boundary
        new_node.center_of_mass = [0.0] * new_node.dimension
        return new_node

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
        the_tree.pp()
