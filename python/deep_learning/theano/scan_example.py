# coding=utf-8
import numpy
import theano.tensor as T
from theano import function
import theano
from theano.ifelse import ifelse

import itertools

if __name__ == '__main__':
    from minitest import *
    inject(numpy.allclose, 'must_close')

    # http://deeplearning.net/software/theano/library/scan.html#lib-scan
    # conclusion
    # the fn arguments came from the below
    # sequences(每次只取一个值用， 可以通过外面传入，也可以定义好)
    # then outputs_info(上一次的计算结果，outputs_info为None表示没有，这时，没有第一个)
    # then non_sequence
    # sequences，non_sequence中的参数名，必须和theano.function中的一致
    # 参数的名字和sequences、non_sequence的名字没有关系
    # 不直观
    # 官方的例子没有按照顺序来组织，也没有说的非常清楚，必须要猜测，很费时间
    # hard point is the fn arguments, and the relationship with theano.function's arguments
    # 合理的顺序：
    # 1. outputs_info and sequences
    # 1.1 how outputs_info initializes. (you need to asign its value)
    # 1.2 return value, will be the list of outputs_info
    # 2. sequences and outputs_info is None
    # 3. non_sequence and n_steps with sequences outputs_info and is None.
    # 4. outputs_info, sequences, non_sequence and describe the fn arguments
    # 5. updates

    # scan performance:
    # minimizing scan usage
    # 

    # theano's cons:
    # 1. it requires the type of variable, let python become the static
    # 2. hard to debug, you can just get the symbol, not the real value. 
    #   因为是延时计算，开始生成symbol的graph, 直到最好取值时才会进行真实的计算。

    # theano 本质上是一种DSL

    with test("scan arguments, sequences"):
        x_sym = T.ivector()
        def scan_fn(cur_item):
            return cur_item

        result, updates = theano.scan(fn=scan_fn,
                                      outputs_info=None,
                                      sequences=x_sym)
        cur_f = theano.function([x_sym],result)
        cur_f([0,1,2]).must_close([0,1,2])

    with test("scan arguments, sequences and outputs_info"):
        x_sym = T.ivector()
        def scan_fn(cur_item,prior_result):
            return T.set_subtensor(
                    prior_result[cur_item], cur_item)

        result, updates = theano.scan(fn=scan_fn,
                                      outputs_info=T.zeros_like(x_sym),
                                      sequences=x_sym)
        cur_f = theano.function([x_sym],result)
        cur_f([0,1,2]).must_close(
                [  [0, 0, 0],
                   [0, 1, 0],
                   [0, 1, 2]])

    with test("scan arguments, sequences, outputs_info and non_sequences"):
        x_sym = T.ivector()
        y_sym = T.ivector()
        def scan_fn(cur_item,prior_result,y_vector):
            return T.set_subtensor(
                    prior_result[cur_item], y_vector[cur_item])

        result, updates = theano.scan(fn=scan_fn,
                                      sequences=x_sym,
                                      outputs_info=T.zeros_like(x_sym),
                                      non_sequences=y_sym)
        cur_f = theano.function([x_sym,y_sym],result)
        cur_f([0,1,2],[7,8,9]).must_close(
                [  [7, 0, 0],
                   [7, 8, 0],
                   [7, 8, 9]])

    with test("scan arguments with taps"):
        x_sym = T.matrix()
        n_sym = T.iscalar()

        results, updates = theano.scan(
                lambda x_tm2, x_tm1: x_tm2+x_tm1,
                n_steps=n_sym, 
                outputs_info=[dict(initial=x_sym, taps=[-2, -1])])
        compute_seq2 = theano.function(inputs=[x_sym, n_sym], outputs=results)

        # the initial value must be able to return x[-2]
        x = numpy.zeros((2, 2), dtype=theano.config.floatX) 
        x[1, 1] = 1
        n = 4
        compute_seq2(x, n).must_close(
                [  [ 0.,  1.],
                   [ 0.,  2.],
                   [ 0.,  3.],
                   [ 0.,  5.]])


    # with test("scan arguments, with taps"):
    #     u = T.ivector()
    #     x0 = numpy.ones([10,10],dtype=numpy.int32)
    #     # x0 = T.ones_like(u)
    #     # x0 = T.ones_like(u)
    #     y0 = T.zeros_like(u)
    #     # y0 = T.ivector()
    #     w = T.ivector()

    #     def scan_fn(u_tm3, u_t, x_tm1, y_tm1):
    #         x_t = T.set_subtensor(
    #                 x_tm1[u_t], u_tm3)
    #         y_t = T.set_subtensor(
    #                 y_tm1[u_tm3], u_t)
    #         # y_t = T.set_subtensor(
    #         #         y_tm1[u_t], y_tm1[u_tm3])
    #         return [x_t, y_t]
    #         # return x_t

    #     # ([x_vals, y_vals], updates) = theano.scan(
    #     #         fn=scan_fn,
    #     #         sequences=dict(input=u, taps=[-3,-0]),
    #     #         outputs_info=[dict(initial=x0, taps=[-3,-1]), y0],
    #     #         strict=True)
    #     # cur_f = theano.function([u],[x_vals, y_vals])
    #     # x_result, y_result = cur_f(range(10))
    #     # x_result.must_close([0])
    #     # y_result.must_close([0])
    #     ([x_vals, y_vals], updates) = theano.scan(
    #             fn=scan_fn,
    #             sequences=dict(input=u, taps=[-3,-0]),
    #             outputs_info=[dict(initial=x0, taps=[-2]),y0])
    #             # outputs_info=x0)
    #             # outputs_info=x0,
    #             # non_sequences=w)
    #     cur_f = theano.function([u],[x_vals, y_vals])
    #     x_result, y_result = cur_f(range(10))
    #     x_result.must_close([0])
    #     y_result.must_close([0])


    # with test("Simple loop with accumulation"):
    #     k = T.iscalar("k")
    #     A = T.vector("A")

    #     # Symbolic description of the result
    #     # fn parameters: first is prior_result, or the initial one
    #     # others are the non_sequences arguments.
    #     result, updates = theano.scan(fn=lambda prior_result, A: prior_result*A,
    #                                   outputs_info=T.ones_like(A),
    #                                   non_sequences=A,
    #                                   n_steps=k)

    #     # We only care about A**k, but scan has provided us with A**1 through A**k.
    #     # Discard the values that we don't care about. Scan is smart enough to
    #     # notice this and not waste memory saving them.
    #     final_result = result[-1]

    #     # compiled function that returns A**k
    #     # no need updates in this  case
    #     power = theano.function(inputs=[A,k], outputs=final_result, updates=updates)

    #     power(range(10),2).must_close(
    #             [0., 1., 4., 9.,16.,25.,36.,49.,64.,81.])

    #     power1 = theano.function(inputs=[A,k], outputs=result, updates=updates)
    #     power1(range(10),2).must_close(
    #             [[  0.,   1.,   2.,   3.,   4.,   5.,   6.,   7.,   8.,   9.],
    #             [  0.,   1.,   4.,   9.,  16.,  25.,  36.,  49.,  64.,  81.]])


    # with test("Iterating over the first dimension of a tensor: Calculating a polynomial"):
    #     coefficients = theano.tensor.vector("coefficients")
    #     x = T.scalar("x")

    #     max_coefficients_supported = 10000

    #     # Generate the components of the polynomial
    #     # there is no accumulation of results, we can set outputs_info to None
    #     components, updates = theano.scan(
    #             fn=lambda coefficient, power, free_variable: coefficient * (free_variable ** power),
    #             outputs_info=None,
    #             sequences=[coefficients, theano.tensor.arange(max_coefficients_supported)],
    #             non_sequences=x)
    #     # Sum them up
    #     polynomial = components.sum()

    #     # Compile a function
    #     calculate_polynomial = theano.function(inputs=[coefficients, x], outputs=polynomial)

    #     # Test
    #     test_coefficients = numpy.asarray([1, 0, 2], dtype=numpy.float32)
    #     test_value = 3
    #     calculate_polynomial(test_coefficients, test_value).must_close(
    #             19)
    #     (1.0 * (3 ** 0) + 0.0 * (3 ** 1) + 2.0 * (3 ** 2)).must_close(
    #             19)
    #     numpy.sum(test_coefficients * test_value ** numpy.asarray(range(3))).must_close(
    #             19)

    # with test("Simple accumulation into a scalar, ditching lambda"):
    #     up_to = T.iscalar("up_to")

    #     # define a named function, rather than using lambda
    #     def accumulate_by_adding(arange_val, sum_to_date):
    #         # import ipdb; ipdb.set_trace()
    #         return sum_to_date + arange_val
    #     seq = T.arange(up_to)

    #     # An unauthorized implicit downcast from the dtype of 'seq', to that of
    #     # 'T.as_tensor_variable(0)' which is of dtype 'int8' by default would occur
    #     # if this instruction were to be used instead of the next one:
    #     # outputs_info = T.as_tensor_variable(0)
    #     outputs_info = T.as_tensor_variable(numpy.asarray(0, seq.dtype))
    #     scan_result, scan_updates = theano.scan(fn=accumulate_by_adding,
    #                                             outputs_info=outputs_info,
    #                                             sequences=seq)
    #     triangular_sequence = theano.function(inputs=[up_to], outputs=scan_result)

    #     # test
    #     some_num = 15
    #     triangular_sequence(some_num).must_close(
    #             [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105])
    #     [n * (n + 1) // 2 for n in range(some_num)].must_close(
    #             [0, 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, 66, 78, 91, 105])

    # with test("Another simple example"):
    #     location = T.imatrix("location")
    #     values = T.vector("values")
    #     output_model = T.matrix("output_model")

    #     def set_value_at_position(a_location, a_value, output_model):
    #         zeros = T.zeros_like(output_model)
    #         zeros_subtensor = zeros[a_location[0], a_location[1]]
    #         return T.set_subtensor(zeros_subtensor, a_value)

    #     result, updates = theano.scan(fn=set_value_at_position,
    #                                   outputs_info=None,
    #                                   sequences=[location, values],
    #                                   non_sequences=output_model)

    #     assign_values_at_positions = theano.function(
    #             inputs=[location, values, output_model], outputs=result)

    #     # test
    #     test_locations = numpy.asarray([[1, 1], [2, 3]], dtype=numpy.int32)
    #     test_values = numpy.asarray([42, 50], dtype=numpy.float32)
    #     test_output_model = numpy.zeros((5, 5), dtype=numpy.float32)
    #     assign_values_at_positions(test_locations, test_values, test_output_model).must_close(
    #             [  [[  0.,   0.,   0.,   0.,   0.],
    #                 [  0.,  42.,   0.,   0.,   0.],
    #                 [  0.,   0.,   0.,   0.,   0.],
    #                 [  0.,   0.,   0.,   0.,   0.],
    #                 [  0.,   0.,   0.,   0.,   0.]],

    #                [[  0.,   0.,   0.,   0.,   0.],
    #                 [  0.,   0.,   0.,   0.,   0.],
    #                 [  0.,   0.,   0.,  50.,   0.],
    #                 [  0.,   0.,   0.,   0.,   0.],
    #                 [  0.,   0.,   0.,   0.,   0.]]])

    # with test("updates"):
    #     a = theano.shared(1)
    #     values, scan_updates = theano.scan(lambda: {a: a+1}, n_steps=10)
    #     var_b = a
    #     var_c = scan_updates[a]
    #     f = theano.function([], [var_b, var_c], updates=scan_updates)

    #     result_b,result_c = f()
    #     result_b.must_close(1)
    #     result_c.must_close(11)
    #     a.get_value().must_close(11)

    #     a1 = theano.shared(1)
    #     values, scan_updates1 = theano.scan(lambda: {a1: a1+1}, n_steps=10)
    #     var_b1 = a1
    #     var_c1 = scan_updates1[a1]
    #     f1 = theano.function([], [var_b1, var_c1])

    #     result_b1,result_c1 = f1()
    #     result_b1.must_close(1)
    #     result_c1.must_close(11)
    #     # since in the theano.function, there is no updates,
    #     # so the updates in theano.scan, would not impact the shared value.
    #     # 说明在theano.scan's updates不直接影响share varialbe
    #     # 在theano.function才会影响
    #     a1.get_value().must_close(1)

    # with test("Using shared variables - Gibbs sampling"):
    #     W_values = numpy.ones([2,2])
    #     bvis_values = 0.1
    #     bhid_values = 0.8
    #     W = theano.shared(W_values) # we assume that ``W_values`` contains the
    #                                 # initial values of your weight matrix

    #     bvis = theano.shared(bvis_values)
    #     bhid = theano.shared(bhid_values)

    #     trng = T.shared_randomstreams.RandomStreams(1234)

    #     # with explicit use of the shared variables (W, bvis, bhid)
    #     def OneStep(vsample, W, bvis, bhid) :
    #         hmean = T.nnet.sigmoid(theano.dot(vsample, W) + bhid)
    #         hsample = trng.binomial(size=hmean.shape, n=1, p=hmean)
    #         vmean = T.nnet.sigmoid(theano.dot(hsample, W.T) + bvis)
    #         return trng.binomial(size=vsample.shape, n=1, p=vmean,
    #                              dtype=theano.config.floatX)

    #     sample = theano.tensor.vector()

    #     # with the shared variables passed as non_sequences
    #     # best practice, for performance
    #     # using strict=True, to have theano check all shared var in the non_sequences
    #     values, updates = theano.scan(OneStep, 
    #             outputs_info=sample, 
    #             non_sequences=[W, bvis, bhid],
    #             n_steps=10,
    #             strict=True)

    #     gibbs10 = theano.function([sample], values[-1], updates=updates)        
    #     gibbs10([0,1]).must_close([1,1])
        
    with test("Conditional ending of Scan"):
        def power_of_2(previous_power, max_value):
            return previous_power*2, theano.scan_module.until(previous_power*2 > max_value)

        max_value = T.scalar()
        values, _ = theano.scan(power_of_2,
                                outputs_info = T.constant(1.),
                                non_sequences = max_value,
                                n_steps = 1024)

        f = theano.function([max_value], values)

        f(45).must_close([2, 4, 8,16,32,64])

    with test("generate matrix"):
        def scan_fn(cur_step, x_sym):
            return x_sym[cur_step] + cur_step
        x_sym = T.matrix()
        steps_sym = T.ivector()
        result, _ = theano.scan(scan_fn,
                outputs_info = None,
                non_sequences = x_sym,
                sequences = steps_sym)
        f = theano.function([steps_sym, x_sym],result)

        n = 3
        x0 = numpy.eye(3)
        steps = range(n)

        f(steps, x0).must_close([
            [ 1.,  0.,  0.],
            [ 1.,  2.,  1.],
            [ 2.,  2.,  3.]
        ])
    with test("generate matrix equally"):
        # the_result = theano.shared(numpy.zeros((3,3)))
        x_sym = T.matrix()
        n = 3
        x0 = numpy.eye(3)
        result_sym = [x_sym[cur_step] + cur_step for cur_step in range(n)]
        
        import ipdb; ipdb.set_trace()
        f = theano.function([x_sym],result_sym)
        the_result = f(x0)
        numpy.matrix(the_result).must_close([
            [ 1.,  0.,  0.],
            [ 1.,  2.,  1.],
            [ 2.,  2.,  3.]
        ])




    # not work
    # with test("generate matrix by cells"):
    #     k = 0
    #     def scan_fn(indexs, x):
    #         return ifelse(T.lt(x[indexs], 1), -1, 2)
    #     x_sym = T.matrix()
    #     indexs_sym = T.imatrix()
    #     result, _ = theano.scan(scan_fn,
    #             outputs_info = None,
    #             non_sequences = x_sym,
    #             sequences = indexs_sym)
    #     f = theano.function([indexs_sym, x_sym],result)

    #     n = 3
    #     x0 = numpy.eye(n)
    #     i0 = itertools.product(range(n),range(n))
    #     f(list(i0), x0).must_close([
    #         [ 1.,  0.,  0.],
    #         [ 1.,  2.,  1.],
    #         [ 2.,  2.,  3.]
    #     ])

    with test("outputs_info"):
        def scan_fn(cur_step, x_sym):
            x_sym = T.set_subtensor(x_sym[cur_step], cur_step+1)
            return x_sym
        x_sym = T.matrix()
        steps_sym = T.ivector()
        result, _ = theano.scan(scan_fn,
                outputs_info = [x_sym],
                sequences = steps_sym)
        f = theano.function([steps_sym, x_sym],result)

        n = 3
        x0 = numpy.eye(3)
        steps = range(n)

        f(steps, x0)[-1].must_close([
            [ 1.,  1.,  1.],
            [ 2.,  2.,  2.],
            [ 3.,  3.,  3.]
        ])


    with test("using update, not result"):
        # define shared variables
        k = theano.shared(0)
        n_sym = T.iscalar("n_sym")

        results, updates = theano.scan(lambda:{k:(k + 1)}, n_steps=n_sym)
        accumulator = theano.function([n_sym], [], updates=updates, allow_input_downcast=True)

        k.get_value().must_close(0)
        accumulator(5)
        k.get_value().must_close(5)
        results.must_equal(None)

    with test("using update for matrix, save memory"):
        x_sym = theano.shared(numpy.eye(3))
        def scan_fn(cur_step):
            # x_sym = T.set_subtensor(x_sym[cur_step], cur_step+1)
            # x_sym[cur_step]= cur_step+1
            # return {x_sym:x_sym}
            new_x_sym = T.set_subtensor(x_sym[cur_step], cur_step+1)
            return {x_sym:new_x_sym}
            # return {x_sym: T.set_subtensor(x_sym[cur_step], cur_step+1)}
            # return {x_sym: (x_sym[cur_step]+1)}
            # return [(x_sym, (x_sym+1))]
        # x_sym = T.matrix()
        steps_sym = T.ivector()
        result, updates = theano.scan(scan_fn,
                outputs_info = None,
                sequences = steps_sym)
        f = theano.function([steps_sym], result, updates=updates, allow_input_downcast=True)

        n = 3
        # x0 = numpy.eye(3)
        steps = range(n)

        f(steps)
        # x_sym.get_value().p()
        x_sym.get_value().must_close([
            [ 1.,  1.,  1.],
            [ 2.,  2.,  2.],
            [ 3.,  3.,  3.]
        ])

