import tensorflow as tf
import numpy

    # (_, m_sym) = tensor.nlinalg.eig(tensor.dot(y_sym.T, y_sym))
    # result_sym = tensor.dot(y_sym, m_sym[:,0:no_dims])


if __name__ == '__main__':
    from minitest import *
    inject(numpy.allclose, 'must_close')

    with test("mean"):
        input_value = numpy.array([[3.,4], [5.,6], [6.,7]])
        mean_numpy = numpy.mean(input_value,1)
        mean_numpy.must_close([3.5, 5.5, 6.5])

        mean_tensor = tf.reduce_mean(input_value,1)
        with tf.Session() as sess:
            mean_tensorflow = sess.run(mean_tensor)
        mean_tensorflow.must_close(mean_numpy)

    with test("tile"):
        count = 2
        input_value = numpy.array([2,3,4])
        tile_numpy = numpy.tile(input_value,(count,1))
        tile_numpy.must_close([
            [2, 3, 4],
            [2, 3, 4]
        ])

        tile_tensor = tf.tile(input_value,[count])
        tile_tensor = tf.reshape(tile_tensor,[count, input_value.shape[0]])
        with tf.Session() as sess:
            tile_tensorflow = sess.run(tile_tensor)
            # tile_tensorflow = sess.run(tf.reshape(tile_tensor,[2,3]))
            # tile_tensorflow.p()
        tile_tensorflow.must_close(tile_numpy)

    with test("dot array"):
        input_value = numpy.array([2,3,4])
        input2_value = numpy.array([1,2,3])
        dot_numpy = numpy.dot(input_value, input2_value.T)
        dot_numpy.must_close(20)

        input_tensor = tf.Variable(input_value)
        input2_tensor = tf.Variable(input2_value)
        dot_tensor = input_tensor * input2_tensor
        with tf.Session() as sess:
            sess.run(tf.initialize_all_variables())
            dot_tensorflow = sess.run(dot_tensor)
        dot_tensorflow.must_close([2,6,12])

    with test("dot matrix"):
        input_value = numpy.matrix(numpy.arange(6).reshape(2,3))
        input2_value = numpy.matrix(numpy.arange(6).reshape(3,2))
        dot_numpy = numpy.dot(input_value, input2_value)
        dot_numpy.must_close([
            [10, 13],
            [28, 40]
        ])

        # normally it's int64
        input_tensor = tf.Variable(tf.to_int32(input_value))
        input2_tensor = tf.Variable(tf.to_int32(input2_value))
        # input2_tensor = tf.Variable(input2_value)
        dot_tensor = tf.matmul(input_tensor, input2_tensor)
        with tf.Session() as sess:
            sess.run(tf.initialize_all_variables())
            dot_tensorflow = sess.run(dot_tensor)
        dot_tensorflow.must_close(dot_numpy)

    with test("numpy.linalg.eig"):
        input_value = numpy.diag((1, 2, 3))
        eigenvalues, eigenvectors = numpy.linalg.eig(input_value)
        eigenvalues.must_close([1,2,3])
        eigenvectors.must_close(numpy.eye(3))

        input_tensor = tf.Variable(tf.cast(input_value,tf.float32))
        eigen_tensor = tf.self_adjoint_eig(input_tensor)
        with tf.Session() as sess:
            sess.run(tf.initialize_all_variables())
            eigen_tensorflow = sess.run(eigen_tensor)
        eigen_tensorflow[0,].must_close(eigenvalues)
        eigen_tensorflow[1:4,].must_close(eigenvectors)



    with test("add, same as matrix"):
        input_value = numpy.diag((1, 2, 3))
        add_one = input_value + 3
        add_one.must_close([
            [4, 3, 3],
            [3, 5, 3],
            [3, 3, 6]
        ])

        add_vector = input_value + numpy.arange(3)
        add_vector.must_close([
            [1, 1, 2],
            [0, 3, 2],
            [0, 1, 5]
        ])

        add_matrix = input_value + numpy.ones([3,3])
        add_matrix.must_close([
            [ 2,  1,  1],
            [ 1,  3,  1],
            [ 1,  1,  4]
        ])

        input_tensor = tf.Variable(input_value)
        add_one_tensor = input_tensor+3
        add_vector_tensor = input_tensor + tf.constant(numpy.arange(3))
        add_matrix_tensor = input_tensor + tf.cast(tf.constant(numpy.ones([3,3])), tf.int64)
        with tf.Session() as sess:
            sess.run(tf.initialize_all_variables())
            add_one_tensorflow = sess.run(add_one_tensor)
            add_vector_tensorflow = sess.run(add_vector_tensor)
            add_matrix_tensorflow = sess.run(add_matrix_tensor)
        add_one_tensorflow.must_close(add_one)
        add_vector_tensorflow.must_close(add_vector)
        add_matrix_tensorflow.must_close(add_matrix)

    with test("multiply"):
        input_value = numpy.arange(6).reshape(2,3)
        multiply_numpy = numpy.multiply(input_value, input_value)
        multiply_numpy.must_close([
            [ 0,  1,  4],
            [ 9, 16, 25]
        ])

        input_tensor = tf.Variable(input_value)
        multiply_tensor = input_tensor * input_tensor
        with tf.Session() as sess:
            sess.run(tf.initialize_all_variables())
            multiply_tensorflow = sess.run(multiply_tensor)
        multiply_tensorflow.must_close(multiply_numpy)

    with test("square"):
        input_value = numpy.arange(6).reshape(2,3)
        square_numpy = numpy.square(input_value)
        square_numpy.must_close([
            [ 0,  1,  4],
            [ 9, 16, 25]
        ])

        input_tensor = tf.Variable(input_value)
        square_tensor = tf.square(input_tensor)
        with tf.Session() as sess:
            sess.run(tf.initialize_all_variables())
            square_tensorflow = sess.run(square_tensor)
        square_tensorflow.must_close(square_numpy)

    with test("sum"):
        input_value = numpy.arange(6).reshape(2,3)
        sum_numpy = numpy.sum(input_value)
        sum0_numpy = numpy.sum(input_value,0)
        sum1_numpy = numpy.sum(input_value,1)
        sum_numpy.must_close(15)
        sum0_numpy.must_close([3, 5, 7])
        sum1_numpy.must_close([ 3, 12])

        input_tensor = tf.Variable(input_value)
        sum_tensor = tf.reduce_sum(input_tensor)
        sum0_tensor = tf.reduce_sum(input_tensor,0)
        sum1_tensor = tf.reduce_sum(input_tensor,1)
        with tf.Session() as sess:
            sess.run(tf.initialize_all_variables())
            sum_tensorflow = sess.run(sum_tensor)
            sum0_tensorflow = sess.run(sum0_tensor)
            sum1_tensorflow = sess.run(sum1_tensor)
        sum_tensorflow.must_close(sum_numpy)
        sum0_tensorflow.must_close(sum0_numpy)
        sum1_tensorflow.must_close(sum1_numpy)




        # num[range(n), range(n)] = 0;
        # Q = numpy.maximum(Q, 1e-12);

        # gains = (gains + 0.2) * ((dY > 0) != (iY > 0)) + (gains * 0.8) * ((dY > 0) == (iY > 0));

        # transpose
    with test("assign part of a matrix"):
        # IndexedSlices
        n = 3
        input1_value = numpy.arange(n*n).reshape(n,n)
        input1_value[range(n), range(n)] = input1_value[range(n), range(n)] + 11
        input1_value.p()

        input_value = numpy.arange(n*n).reshape(n,n)
        input_tensor = tf.to_int32(tf.Variable(input_value))
        indices = [[0,0],[1,1],[2,2]]
        values = [11] * n
        delta = tf.SparseTensor(indices, values, [n,n])
        delta1 = tf.gather_nd(input_tensor, [0,1])
        item_tensor = input_tensor + tf.sparse_tensor_to_dense(delta)
                
        sess = tf.Session()
        sess.run(tf.initialize_all_variables())
        item_tensorflow = sess.run(item_tensor)
        dd = sess.run(delta1)
        sess.close()
        item_tensorflow.p()
        dd.p()

