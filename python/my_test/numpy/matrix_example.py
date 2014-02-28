from numpy import *


if __name__ == '__main__':
    from minitest import *

    # array([[ 0.,  1.,  2.],
    #        [ 3.,  4.,  5.]])
    arr23 = arange(6.0).reshape((2,3))
    # array([[ 0.,  1.],
    #        [ 2.,  3.],
    #        [ 4.,  5.]])
    arr32 = arange(6.0).reshape((3,2))

    # matrix([[ 0.,  1.,  2.],
    #         [ 3.,  4.,  5.]])
    mat23 = mat(arr23)
    # matrix([[ 0.,  1.],
    #        [ 2.,  3.],
    #        [ 4.,  5.]])
    mat32 = mat(arr32)

    with test("matric.*"):
        (mat23 * mat32).must_equal(matrix([[ 10.,  13.],[ 28.,  40.]]), allclose)

    with test("matric.T"):
        mat23.T.must_equal(
            matrix([[ 0.,  3.],
                    [ 1.,  4.],
                    [ 2.,  5.]]), allclose)

    with test("multiply"):
        multiply(arr23, arr23[0,:]).must_equal(
            array([[  0.,   1.,   4.],
                   [  0.,   4.,  10.]]), allclose)

    with test("A"):
        mat23.A.must_equal(
            array([[ 0.,  1.,  2.],
                   [ 3.,  4.,  5.]]), allclose)       

    with test("get first col"):
        mat23[:,0].must_equal(
            matrix([[ 0.],
                    [ 3.]]), allclose)  

    with test("nonzero"):
        nonzero([1,2,0,0,1,0,2,0]).must_equal(
            (array([0, 1, 4, 6]),), allclose)

        arr = array([[1,0],[2,3]])
        arr.nonzero().must_equal(
            (array([0, 1, 1]), array([0, 0, 1])), allclose)

        # this will show why nonzero result is so weird.
        arr[arr.nonzero()].must_equal(array([1, 2, 3]), allclose)

        # nonBoundIs = nonzero((self.alphas.A > 0) * (self.alphas.A < self.edge_threshold))[0]
        arr = array([[10], [20], [0], [0], [15], [16], [0]])
        nonzero(arr>0)[0].must_equal(
            (array([0, 1, 4, 5]),), allclose)
        nonzero((arr > 0) * (arr < 16))[0].must_equal(
            (array([0, 4]),), allclose)
    with test("matirc.transport"):
        pass
