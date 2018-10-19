# coding=utf-8
import numpy
import theano.tensor as tensor
from theano import function
import theano

FLOATX = "float32"

if __name__ == '__main__':
    from minitest import *
    inject(numpy.allclose, 'must_close')

    with test("set range for cell"):
        x_sym = tensor.matrix()
        step_sym = tensor.ivector()
        
        result, _ = theano.scan(lambda cur_i, cur_row: tensor.set_subtensor(cur_row[cur_i], 0),
                sequences=[step_sym, x_sym],
                outputs_info=None)
        cur_f = theano.function([step_sym, x_sym],result)

        cur_f(range(3),numpy.ones([3,3])).must_close(
                [[ 0.,  1.,  1.],
                   [ 1.,  0.,  1.],
                   [ 1.,  1.,  0.]])

    with test("set range for cell1"):
        x_sym = tensor.matrix()

        x0 = numpy.ones([3,3])
        n = x0.shape[0]
        
        # result, _ = theano.scan(lambda cur_i, cur_row: tensor.set_subtensor(cur_row[cur_i], 0),
        #         sequences=[step_sym, x_sym],
        #         outputs_info=None)
        result = tensor.set_subtensor(x_sym[range(n),range(n)], 0)
        cur_f = theano.function([x_sym],result)

        cur_f(x0).must_close(
                [[ 0.,  1.,  1.],
                   [ 1.,  0.,  1.],
                   [ 1.,  1.,  0.]])

    with test("set with condition"):
        x0 = numpy.ones([3,3])
        x0[:,1] = -1

        y0 = numpy.zeros([3,3])
        y1 = (y0 + 0.2) * (x0 > 0)

        x_sym = tensor.matrix()
        y_sym = tensor.matrix()

        indexs = (x_sym>0).nonzero()
        result = tensor.set_subtensor(y_sym[indexs], y_sym[indexs]+0.2)
        cur_f = theano.function([x_sym, y_sym],result)

        cur_f(x0, y0).must_close(y1)
        y1.must_close([
            [ 0.2,  0. ,  0.2],
            [ 0.2,  0. ,  0.2],
            [ 0.2,  0. ,  0.2]
        ])

    with test("set with complex condition"):
        x0 = numpy.zeros([3,3]) - 1
        x0[:,1] = -1
        x1 = numpy.zeros([3,3]) - 1
        x1[1,:] = 1

        y0 = numpy.ones([3,3])
        y1 = (y0 + 0.2) * ((x0 > 0) != (x1 > 0)) + (y0 * 0.8) * ((x0 > 0) == (x1 > 0));

        xa_sym = tensor.matrix()
        xb_sym = tensor.matrix()
        y_sym = tensor.matrix()

        indexsa = tensor.neq((xa_sym>0), (xb_sym>0)).nonzero()
        indexsb = tensor.eq((xa_sym>0), (xb_sym>0)).nonzero()
        # indexsb = (xa_sym>0 == xb_sym >0).nonzero()
        resulta = tensor.set_subtensor(y_sym[indexsa], y_sym[indexsa]+0.2)
        resultb = tensor.set_subtensor(resulta[indexsb], resulta[indexsb]*0.8)
        cur_f = theano.function([xa_sym, xb_sym, y_sym],resultb)

        cur_f(x0, x1, y0).must_close(y1)
        y1.must_close([
            [ 0.8,  0.8,  0.8],
            [ 1.2,  1.2,  1.2],
            [ 0.8,  0.8,  0.8]
        ])


    # with test("set range for row"):
    #     x_sym = tensor.matrix()
    #     y_sym = tensor.matrix()
    #     step_sym = tensor.ivector()

    #     result, _ = theano.scan(lambda cur_i, x_sym,y_sym: tensor.set_subtensor(x_sym[cur_i,:], y_sym[cur_i,:]),
    #             sequences=[step_sym],
    #             outputs_info=None,
    #             non_sequences=[x_sym,y_sym])
    #     cur_f = theano.function([step_sym, x_sym, y_sym],result)

    #     cur_f(range(3),numpy.ones([3,3], dtype=FLOATX),numpy.eye(3, dtype=FLOATX)).pp()
