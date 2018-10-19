import tensorflow as tf
import numpy


if __name__ == '__main__':
    from minitest import *
    inject(numpy.allclose, 'must_close')
    only_test("tf.nn.embedding_lookup")



    with test("convert_to_tensor"):
        input_value = numpy.array([[3.,4], [5.,6], [6.,7]])

        input_tensor = tf.convert_to_tensor(input_value, dtype=tf.float32)
        with tf.Session() as sess:
            input_tensorflow = sess.run(input_tensor)
        input_tensorflow.must_close(input_value)

    with test("tf.strided_slice"):
        # input_value = numpy.array([[[1, 1, 1], [2, 2, 2]],
        #     [[3, 3, 3], [4, 4, 4]],
        #     [[5, 5, 5], [6, 6, 6]]])

        # slice_1 = tf.strided_slice(input_value, [1, 0, 0], [3, 1, 3], [1, 1, 1])
        # with tf.Session() as sess:
        #     slice_1_value = sess.run(slice_1)
            # print(slice_1_value)


        input_value = range(10)
        slice_1 = tf.strided_slice(input_value, [1], [6], [2])
        with tf.Session() as sess:
            slice_1_value = sess.run(slice_1)
            slice_1_value.must_close([1,3,5])

    with test("tf.nn.embedding_lookup"):
        input_value = numpy.array(range(10))
        ids = [1,3,5]
        input_tensor = tf.convert_to_tensor(input_value, dtype=tf.float32)

        embedding_tensor = tf.nn.embedding_lookup(input_tensor,ids)
        with tf.Session() as sess:
            embedding_value = sess.run(embedding_tensor)
            embedding_value.must_close([1,3,5])
            # embedding_value.p()







