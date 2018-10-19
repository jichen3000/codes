# http://blog.csdn.net/lenbow/article/details/52181159

import tensorflow as tf
import numpy


if __name__ == '__main__':
    from minitest import *
    inject(numpy.allclose, 'must_close')
    only_test("range_input_producer with array")



    with test("queue"):
        the_list = range(10,20)
        the_queue = tf.FIFOQueue(3, "float32")
        init_values = the_queue.enqueue_many(([1,2],))
        x = the_queue.dequeue()
        y = x * 10
        q_inc = the_queue.enqueue(the_list.pop(0))

        with tf.Session() as sess:
            init_values.run().must_equal(None)
            y.eval().must_equal(10.0)
            q_inc.run().must_equal(None)
            y.eval().must_equal(20.0)
            q_inc.run().must_equal(None)
            # always get the first one
            y.eval().must_equal(100.0)
            q_inc.run().must_equal(None)
            y.eval().must_equal(100.0)
            q_inc.run().must_equal(None)
            y.eval().must_equal(100.0)

    with test("range_input_producer"):
        epoch_size = 10
        i = tf.train.range_input_producer(epoch_size, shuffle=False).dequeue()

        # must use Supervisor to start threads
        sv = tf.train.Supervisor(logdir="/tmp")
        with sv.managed_session() as sess:
            sess.run(i).must_equal(0)
            sess.run(i).must_equal(1)
            sess.run(i).must_equal(2)

    with test("range_input_producer with data"):
        epoch_size = 10
        the_list = range(10,20)
        i = tf.train.range_input_producer(epoch_size, shuffle=False).dequeue()
        slice_1 = tf.strided_slice(the_list, [i], [i+2])

        # must use Supervisor to start threads
        sv = tf.train.Supervisor(logdir="/tmp")
        with sv.managed_session() as sess:
            sess.run(slice_1).must_close([10,11])
            sess.run(slice_1).must_close([11,12])

    with test("range_input_producer with array"):
        the_array = numpy.array(range(200)).reshape(20,10)
        the_array.shape.p()
        the_array.p()
        step_number = 5
        i = tf.train.range_input_producer(2, shuffle=False).dequeue()
        slice_1 = tf.strided_slice(the_array, [0, i*step_number], [20, (i+1)*step_number])

        # must use Supervisor to start threads
        sv = tf.train.Supervisor(logdir="/tmp")
        with sv.managed_session() as sess:
            sess.run(slice_1).p()
            sess.run(slice_1).p()



