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
        dstack(arr.nonzero()).must_equal(
            array([[[0, 0],
                    [1, 0],
                    [1, 1]]]), allclose)

        # this will show why nonzero result is so weird.
        arr[arr.nonzero()].must_equal(array([1, 2, 3]), allclose)

    with test("nonzero advanced"):
        arr = array([[10], [20], [0], [0], [15], [16], [0]])
        nonzero(arr>0)[0].must_equal(
            (array([0, 1, 4, 5]),), allclose)
        nonzero((arr > 0) * (arr < 16))[0].must_equal(
            (array([0, 4]),), allclose)



    with test("vectorize"):
        '''
            It is the fastest/most efficient way to apply to every of each cells the same function -f-,
            for a numpy array.
        '''
        arr = array([[10], [20], [3], [4], [15], [16], [0]])
        def binarize(cell, threshold=6):
            if cell > threshold:
                return 1
            else:
                return 0
        binarize_arr = vectorize(binarize)
        binarize_arr(arr).must_equal(
            array([[1], [1], [0], [0], [1], [1], [0]]), allclose)
        binarize_arr(arr, 14).must_equal(
            array([[0], [1], [0], [0], [1], [1], [0]]), allclose)


    with test("set sub area"):
        full_arr = zeros((5,5))
        arr = arange(9).reshape((3,3))+1
        full_arr[1:4,1:4] = arr
        full_arr.must_equal(
            array([[ 0.,  0.,  0.,  0.,  0.],
                   [ 0.,  1.,  2.,  3.,  0.],
                   [ 0.,  4.,  5.,  6.,  0.],
                   [ 0.,  7.,  8.,  9.,  0.],
                   [ 0.,  0.,  0.,  0.,  0.]]), allclose)

    with test("iterate with index"):
        arr =array([[1,2],[3,4],[5,6]])
        value_arr = [ (i, j, value) for (i, j), value in ndenumerate(arr)]
        value_arr.must_equal(
            [(0, 0, 1), (0, 1, 2), (1, 0, 3), (1, 1, 4), (2, 0, 5), (2, 1, 6)])

    with test("loadtxt"):
        # StringIO behaves like a file object
        from StringIO import StringIO   

        fake_file = StringIO("01\n10")
        arr = loadtxt(fake_file, dtype=int, ndmin=2)
        arr.must_equal(
            array([[ 1],
                   [10]]), allclose)

    with test("savetxt"):
        # from tempfile import TemporaryFile
        # outfile = TemporaryFile()
        ''' when I used the format like %10.5f, the loadtxt will report string cannot transfer float. '''
        fmt='%1d'; 
        delimiter=' '
        arr = arange(9).reshape((3,3))
        file_name = 'arr.dataset'
        arr[1,1] = -1
        savetxt(file_name, arr, fmt=fmt, delimiter=delimiter)

        # outfile.readlines().pp()
        brr = loadtxt(file_name, delimiter=delimiter)
        brr.must_equal(arr, allclose)
        brr.pp()
        # brr.must_equal

    with test("save with others"):

        pass
        
    with test("add tow"):
        arr1 = zeros((3,3))+1
        arr2 = zeros((3,3))+2
        arr3 = zeros((3,3))+3
        arr4 = zeros((3,3))+4
        arr12 = concatenate((arr1, arr2), axis=1)
        arr12.must_equal(
            array([[ 1.,  1.,  1.,  2.,  2.,  2.],
                   [ 1.,  1.,  1.,  2.,  2.,  2.],
                   [ 1.,  1.,  1.,  2.,  2.,  2.]]), allclose)
        arr34 = concatenate((arr3, arr4), axis=1)
        arr1234 = concatenate((arr12, arr34), axis=0)
        arr1234.must_equal(
            array([[ 1.,  1.,  1.,  2.,  2.,  2.],
                   [ 1.,  1.,  1.,  2.,  2.,  2.],
                   [ 1.,  1.,  1.,  2.,  2.,  2.],
                   [ 3.,  3.,  3.,  4.,  4.,  4.],
                   [ 3.,  3.,  3.,  4.,  4.,  4.],
                   [ 3.,  3.,  3.,  4.,  4.,  4.]]), allclose)
