import tensorflow as tf
import numpy

    # (_, m_sym) = tensor.nlinalg.eig(tensor.dot(y_sym.T, y_sym))
    # result_sym = tensor.dot(y_sym, m_sym[:,0:no_dims])

def _pixel_wise_softmax_2(output_map):
    # this will cause, result has np.nan
    exponential_map = tf.exp(output_map)
    sum_exp = tf.reduce_sum(exponential_map, -1, keep_dims=True)
    tensor_sum_exp = tf.tile(sum_exp, tf.stack(
            [1]*(exponential_map.shape.ndims-1)+[exponential_map.shape[-1]]))
    return tf.div(exponential_map,tensor_sum_exp)


if __name__ == '__main__':
    from minitest import *
    inject(numpy.allclose, 'must_close')
    only_test("softmax")

    with test("softmax"):
        input_value = numpy.array([
                [
                    [3.,6.], 
                    [5.,5.], 
                    [2.,6.]
                ],
                [
                    [1.,4.], 
                    [5.,5.], 
                    [1.,7.]
                ],
                [
                    [1.,4.], 
                    [5.,5.], 
                    [4.,4.]
                ],
                [
                    [4.,8.], 
                    [5.,1.1e+30], 
                    [1.1e+30,1.1e+30]
                ]
                ])
        x = input_value
        exp_x = numpy.exp(x)
        softmax_numpy = exp_x / numpy.sum(exp_x, -1).reshape(4,3,1)
        softmax_numpy.pp()

        softmax_tensor = tf.nn.softmax(input_value)
        softmax_tensor1 = _pixel_wise_softmax_2(input_value)
        with tf.Session() as sess:
            softmax_tensorflow = sess.run(softmax_tensor)
            softmax_tensorflow1 = sess.run(softmax_tensor1)
        softmax_tensorflow.pp()
        softmax_tensorflow1.pp()

        