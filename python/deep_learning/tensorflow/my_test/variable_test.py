import tensorflow as tf
import numpy

if __name__ == '__main__':
    from minitest import *

    inject(numpy.allclose, 'must_close')

    with test("simple"):
        input_tensor = tf.Variable(tf.zeros([2]))
        with tf.Session() as sess:
            sess.run(tf.initialize_all_variables())
            result = sess.run(input_tensor)
            result.must_close([0,0])
    
    with test("placehold"):
