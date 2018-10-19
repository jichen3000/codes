import numpy as np

# import operator
# import functools

# def multiply_all(the_list):
#     return functools.reduce(operator.mul, the_list, 1)

def gen_cur_weights_2d(weights, input_shape, cur_indexs):
    new_weights = weights
    for k in range(0, cur_indexs[0]):
        new_weights = np.insert(new_weights, k, 0, axis=0)
    for k in range(weights.shape[0]+cur_indexs[0], input_shape[0]):
        new_weights = np.insert(new_weights, k, 0, axis=0)
    for k in range(0, cur_indexs[1]):
        new_weights = np.insert(new_weights, k, 0, axis=1)
    for k in range(weights.shape[1]+cur_indexs[1], input_shape[1]):
        new_weights = np.insert(new_weights, k, 0, axis=1)
    return new_weights

def cal_output_shape_for_convolution(input_shape, weights_shape):
    return [i-w+1 for i, w in zip(input_shape, weights_shape)]

def cal_output_shape_for_transposed(input_shape, weights_shape):
    return [i+w-1 for i, w in zip(input_shape, weights_shape)]

# no zero padding, unit strides
def gen_full_weights_2d(weights, input_shape):
    full_weights = []
    output_shape = cal_output_shape_for_convolution(input_shape, weights.shape)
    for i in range(output_shape[0]):
        for j in range(output_shape[1]):
            full_weights.append(gen_cur_weights_2d(weights,
                    input_shape,(i,j)).flatten())
    return np.array(full_weights)

def convolute_2d(input_array, weights):
    # input_shape = input_array.shape
    full_weights = gen_full_weights_2d(weights, input_array.shape)
    output_array = np.dot(full_weights,input_array.flatten())
    output_shape = cal_output_shape_for_convolution(input_array.shape, weights.shape)
    return output_array.reshape(output_shape)

def transposed_convolute_2d(input_array, weights):
    output_shape = cal_output_shape_for_transposed(input_array.shape, weights.shape)
    full_weights = gen_full_weights_2d(weights, output_shape)
    # full_weights_inv = np.linalg.pinv(full_weights)
    output_array = np.dot(full_weights.T,input_array.flatten())
    return output_array.reshape(output_shape)

def pad_2d(input_array, padding_numbers):
    padding_array = input_array
    for k in range(padding_numbers[0]):
        padding_array = np.insert(padding_array, padding_array.shape[0], 0, axis=0)
        padding_array = np.insert(padding_array, k, 0, axis=0)
    for k in range(padding_numbers[1]):
        padding_array = np.insert(padding_array, padding_array.shape[1], 0, axis=1)
        padding_array = np.insert(padding_array, k, 0, axis=1)
    return padding_array

def transposed_convolute_2d_by_direct_full_convolute(input_array, weights):
    padding_numbers = [i-1 for i in weights.shape]
    full_padding_input_array = pad_2d(input_array, padding_numbers)
    # full_padding_input_array.pp()
    output_shape = cal_output_shape_for_convolution(full_padding_input_array.shape, weights.shape)
    full_weights = gen_full_weights_2d(weights, full_padding_input_array.shape)
    full_weights.shape.pp()
    # full_weights_inv = np.linalg.pinv(full_weights)
    output_array = np.dot(full_weights,full_padding_input_array.flatten())
    output_array.shape.pp()
    return output_array.reshape(output_shape)


if __name__ == '__main__':
    from minitest import *
    inject(np.allclose, 'must_close')

    with test(cal_output_shape_for_convolution):
        cal_output_shape_for_convolution((4,4),(3,3)).must_equal(
                [2,2])

    with test(gen_cur_weights_2d):
        weights = np.array([
                [ 0. ,  0.1,  0.2],
                [ 0.3,  0.4,  0.5],
                [ 0.6,  0.7,  0.8]
        ])
        gen_cur_weights_2d(weights, (4,4), (0,0)
                ).must_close(np.array([
                [ 0. ,  0.1,  0.2,  0. ],
                [ 0.3,  0.4,  0.5,  0. ],
                [ 0.6,  0.7,  0.8,  0. ],
                [ 0. ,  0. ,  0. ,  0. ]                
                ]))

        gen_cur_weights_2d(weights, (5,5), (1,0)
                # ).pp()
                ).must_close(np.array([
                [ 0. ,  0. ,  0. ,  0. ,  0. ],
                [ 0. ,  0.1,  0.2,  0. ,  0. ],
                [ 0.3,  0.4,  0.5,  0. ,  0. ],
                [ 0.6,  0.7,  0.8,  0. ,  0. ],
                [ 0. ,  0. ,  0. ,  0. ,  0. ]
        ]))

    with test(gen_full_weights_2d):
        weights = np.array([
                [ 0. ,  0.1,  0.2],
                [ 0.3,  0.4,  0.5],
                [ 0.6,  0.7,  0.8]
        ])
        gen_full_weights_2d(weights, (4,4)).must_close(np.array([
                [ 0. ,  0.1,  0.2,  0. ,  0.3,  0.4,  0.5,  0. ,  0.6,  0.7,  0.8,
                    0. ,  0. ,  0. ,  0. ,  0. ],
                [ 0. ,  0. ,  0.1,  0.2,  0. ,  0.3,  0.4,  0.5,  0. ,  0.6,  0.7,
                    0.8,  0. ,  0. ,  0. ,  0. ],
                [ 0. ,  0. ,  0. ,  0. ,  0. ,  0.1,  0.2,  0. ,  0.3,  0.4,  0.5,
                    0. ,  0.6,  0.7,  0.8,  0. ],
                [ 0. ,  0. ,  0. ,  0. ,  0. ,  0. ,  0.1,  0.2,  0. ,  0.3,  0.4,
                    0.5,  0. ,  0.6,  0.7,  0.8]
        ]))

    with test(convolute_2d):
        weights = np.array([
                [ 0. ,  0.1,  0.2],
                [ 0.3,  0.4,  0.5],
                [ 0.6,  0.7,  0.8]
        ])
        input_array = np.array([
            [ 0.    ,  0.0625,  0.125 ,  0.1875],
            [ 0.25  ,  0.3125,  0.375 ,  0.4375],
            [ 0.5   ,  0.5625,  0.625 ,  0.6875],
            [ 0.75  ,  0.8125,  0.875 ,  0.9375]
        ])
        convolute_2d(input_array, weights).must_close(np.array([
                [ 1.6125,  1.8375],
                [ 2.5125,  2.7375]
        ]))

    with test(transposed_convolute_2d):
        weights = np.array([
                [ 0. ,  0.1,  0.2],
                [ 0.3,  0.4,  0.5],
                [ 0.6,  0.7,  0.8]
        ])
        input_array = np.array([
                [ 1.6125,  1.8375],
                [ 2.5125,  2.7375]
        ])
        transposed_convolute_2d(input_array, weights).must_close(np.array([
                [ 0.     ,  0.16125,  0.50625,  0.3675 ],
                [ 0.48375,  1.4475 ,  2.3175 ,  1.46625],
                [ 1.72125,  4.0575 ,  4.9275 ,  2.83875],
                [ 1.5075 ,  3.40125,  3.92625,  2.19   ]
        ]))

    with test(pad_2d):
        input_array = np.array([
                [ 1.6125,  1.8375],
                [ 2.5125,  2.7375]
        ])
        pad_2d(input_array, (2,2)).must_close(np.array([
                [ 0.    ,  0.    ,  0.    ,  0.    ,  0.    ,  0.    ],
                [ 0.    ,  0.    ,  0.    ,  0.    ,  0.    ,  0.    ],
                [ 0.    ,  0.    ,  1.6125,  1.8375,  0.    ,  0.    ],
                [ 0.    ,  0.    ,  2.5125,  2.7375,  0.    ,  0.    ],
                [ 0.    ,  0.    ,  0.    ,  0.    ,  0.    ,  0.    ],
                [ 0.    ,  0.    ,  0.    ,  0.    ,  0.    ,  0.    ]
        ]))

    with test(transposed_convolute_2d_by_direct_full_convolute):
        # not same as transposed_convolute_2d, even their eig is different
        weights = np.array([
                [ 0. ,  0.1,  0.2],
                [ 0.3,  0.4,  0.5],
                [ 0.6,  0.7,  0.8]
        ])
        input_array = np.array([
                [ 1.6125,  1.8375],
                [ 2.5125,  2.7375]
        ])
        transposed_convolute_2d_by_direct_full_convolute(input_array, weights).must_close(np.array([
                [ 1.29   ,  2.59875,  2.25375,  1.1025 ],
                [ 2.81625,  5.5125 ,  4.6425 ,  2.19375],
                [ 1.57875,  2.9025 ,  2.0325 ,  0.82125],
                [ 0.5025 ,  0.79875,  0.27375,  0.     ]
        ]))



