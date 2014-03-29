'''
http://opencvpython.blogspot.com/2012/06/hi-this-article-is-tutorial-which-try.html
box = cv2.cv.BoxPoints(rect)
'''


import numpy
import cv2
import os, sys
path = os.path.abspath(os.path.join(
        os.path.dirname(__file__), '../../projects/font_number_binary'))
if not path in sys.path:
    sys.path.insert(1, path)
import cv2_helper


ORIGINAL_IMAGE_NAME = 'original.jpg'
# 0 is black, white is 255
# large is brighter, less is darker.

# a good example
# http://stackoverflow.com/questions/16538774/dealing-with-contours-and-bounding-rectangle-in-opencv-2-4-python-2-7

'''
    notice, the point in the pic_arr, like [478, 128], 
    the first one is the y, 
    the second one is the x.
    Don't get them reversely.
'''

def find_max_square(pic_array):
    '''
        notice: the threshold_value is the key, if it directly impact the binary matrix.
    '''
    threshold_value = int(pic_array.mean()*0.7)

    not_use,threshed_matrix = cv2.threshold(pic_array,threshold_value,255,1)
    # findContours has the side effect, it will change the pic_arr
    contours,not_use = cv2.findContours(threshed_matrix.copy(),cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)

    def get_approximated_contour(contour):
        perimeter = cv2.arcLength(contour,True)
        return cv2.approxPolyDP(contour,0.01*perimeter,True)

    contours = map(get_approximated_contour, contours)
    squares = filter(is_almost_square, contours)
    square_perimeter_arr = [cv2.arcLength(i,True) for i in squares]
    return squares[square_perimeter_arr.index(max(square_perimeter_arr))]


def get_next_two_points(contour, start_index):
    if start_index+2 > len(contour):
        raise "Index is out of the length of contour."
    return contour[start_index:start_index+2]

def is_almost_square(contour, accuracy=0.001):
    '''
        The accuracy is the key, and cannot larger than 0.001
    '''    
    if len(contour)!=4:
        return False
    perimeter = cv2.arcLength(contour, True)
    area_from_perimeter = (perimeter / 4) ** 2
    real_area = cv2.contourArea(contour)
    # area_from_perimeter.pp()
    # real_area.pp()
    if (1-accuracy) * area_from_perimeter < real_area < (1+accuracy) * area_from_perimeter:
        return True
    return False

def cal_squre_area(contour):
    '''
        calculate the square area values,
        return the start_row_index, end_row_index, start_col_index, end_col_index.
        It can be used like: pic_array[start_row_index:end_row_index, start_col_index:end_col_index]
        The square must be horizonal.
    '''
    points_count = 4
    flat_arr = contour.flatten('F')
    col_indexs = flat_arr[0: points_count]
    col_indexs.sort()
    row_indexs = flat_arr[points_count: points_count*2]
    row_indexs.sort()
    return row_indexs[1], row_indexs[2], col_indexs[1], col_indexs[2]

def cal_split_ragion(start_row_index, end_row_index, start_col_index, end_col_index, 
    split_num=9, modified_percent=0.15):
    '''
        firstlt row, then col
    '''
    step = int((end_row_index - start_row_index) / 9)
    modifer = int(step*modified_percent)
    # return [(i,j) for i in range(split_num) for j in range(split_num)]
    result = [(start_row_index+i*step+modifer, start_row_index+(i+1)*step-modifer, 
        start_col_index+j*step+modifer, start_col_index+(j+1)*step-modifer) 
        for i in range(split_num) for j in range(split_num)]
    return result



if __name__ == '__main__':
    from minitest import *

    gray_pic = cv2.imread(ORIGINAL_IMAGE_NAME, 0)
    gray_area_pic = gray_pic[400:1100,50:700]
    color_pic = cv2.imread(ORIGINAL_IMAGE_NAME)
    color_area_pic = color_pic[400:1100,50:700]

    with test("show how to use threshold"):
        threshold_value = int(gray_area_pic.mean())-50
        # http://docs.opencv.org/modules/imgproc/doc/miscellaneous_transformations.html?highlight=threshold#threshold
        result_threshold_value,threshed_matrix = cv2.threshold(gray_area_pic,threshold_value,255,0)
        int(result_threshold_value).must_equal(threshold_value)

        # it will show the pic only have the points of white and black colors.
        black_count = numpy.count_nonzero(threshed_matrix)
        white_count = numpy.count_nonzero(255-threshed_matrix)
        row_count, col_count = threshed_matrix.shape
        (row_count*col_count).must_equal(black_count+white_count)

        # show_pic(threshed_matrix)

    with test("arcLength"):
        ''' Calculates a contour perimeter or a curve length.
            curve - Input vector of 2D points, stored in std::vector or Mat.
            closed - Flag indicating whether the curve is closed or not  
            (its first and last vertices are connected). 
        '''
        points = numpy.array([ [[393,   1]],
                               [[393,   2]],
                               [[394,   2]],
                               [[394,   1]]])
        perimeter = cv2.arcLength(points,True)
        perimeter.must_equal(4)
        contour = numpy.array([[[ 1,  1]],
                               [[ 1,  401]],
                               [[ 401, 401]],
                               [[ 401, 1]]])
        cv2.arcLength(contour, True).must_equal(1600)
        # it shows, how to get the line length
        contour = numpy.array([[[ 1,  1]],
                               [[ 1,  401]]])
        cv2.arcLength(contour, False).must_equal(400)

    with test("contourArea"):
        contour = numpy.array([[[ 1,  1]],
                               [[ 1,  401]],
                               [[ 401, 401]],
                               [[ 401, 1]]])
        cv2.contourArea(contour).must_equal(160000)
        contour = numpy.array([[[ 1,  1]],
                               [[ 1,  501]],
                               [[ 401, 401]],
                               [[ 401, 1]]])
        cv2.contourArea(contour).must_equal(180000)

    with test("approxPolyDP"):
        ''' Approximates a polygonal curve(s) with the specified precision
            epsilon - Parameter specifying the approximation accuracy
            closed -
        '''
        cv2.approxPolyDP(points,0.01*perimeter,True).must_equal(points, numpy.allclose)

    with test("is_almost_square"):
        contour = numpy.array([[[ 1,  1]],
                               [[ 1,  401]],
                               [[ 401, 401]],
                               [[ 401, 1]]])
        is_almost_square(contour).must_equal(True)
        contour = numpy.array([[[ 1,  1]],
                               [[ 1,  501]],
                               [[ 401, 401]],
                               [[ 401, 1]]])
        is_almost_square(contour).must_equal(False)
        contour = numpy.array([[[ 671,  421]],
                               [[  78,  426]],
                               [[  85, 1016]],
                               [[ 675, 1012]]])
        is_almost_square(contour).must_equal(True)
        contour = numpy.array([[[ 671,  421]],
                               [[  128,  426]],
                               [[  85, 1016]],
                               [[ 675, 1012]]])
        is_almost_square(contour).must_equal(False)
    with test("get some point from contour"):
        contour = numpy.array([[[ 1,  1]],
                               [[ 1,  401]],
                               [[ 401, 401]],
                               [[ 401, 1]]])
        get_next_two_points(contour,1).must_equal(contour[1:3], numpy.allclose)
        get_next_two_points(contour,2).must_equal(contour[2:4], numpy.allclose)
        # get_next_two_points(contour,3).must_equal(contour[3:5], numpy.allclose)

    with test("cal_squre_area"):
        contour = numpy.array([[[ 671,  421]],
                               [[  78,  426]],
                               [[  85, 1016]],
                               [[ 675, 1012]]])
        cal_squre_area(contour).must_equal((426, 1012, 85, 671))

    with test("cal_split_ragion"):
        indexs = (426, 1012, 85, 671)
        ragion_indexs = cal_split_ragion(*indexs)
        ragion_indexs[0:9].must_equal(
            [(435, 482, 94, 141),
             (435, 482, 159, 206),
             (435, 482, 224, 271),
             (435, 482, 289, 336),
             (435, 482, 354, 401),
             (435, 482, 419, 466),
             (435, 482, 484, 531),
             (435, 482, 549, 596),
             (435, 482, 614, 661)])
        ragion_indexs.size().must_equal(81)

    with test("boundingRect x, y, width, height"):
        contour = numpy.array([[[ 1,  1]],
                               [[ 1,  401]],
                               [[ 401, 401]],
                               [[ 401, 1]]])
        cv2.boundingRect(contour).must_equal((1, 1, 401, 401))
        contour = numpy.array([[[ 675,  425]],
                               [[  85,  425]],
                               [[  85, 1015]],
                               [[ 675, 1015]]])
        cv2.boundingRect(contour).must_equal((85, 425, 591, 591))
        contour = numpy.array([[[ 671,  421]],
                               [[  78,  426]],
                               [[  85, 1016]],
                               [[ 675, 1012]]])
        cv2.boundingRect(contour).must_equal((78, 421, 598, 596))

    with test("x, y"):
        contour = numpy.array([[[ 10,  1]],
                               [[ 10,  401]],
                               [[ 401, 401]],
                               [[ 401, 1]]])
        # cv2_helper.show_contours_in_pic(color_pic, [contour])

    with test("find_max_square"):
        max_square = find_max_square(gray_pic)
        max_square.must_equal(numpy.array([[[ 671,  421]],
                               [[  78,  426]],
                               [[  85, 1016]],
                               [[ 675, 1012]]]), numpy.allclose)
        (cv2.arcLength(max_square,True) > 2300).must_equal(True)
        pass

    # with test("show max square in full pic"):
    #     current_pic_array = color_pic
    #     cv2.drawContours(current_pic_array,[max_square],-1,(0,255,255),1)
    #     show_pic(current_pic_array)

    # with test("show max square in area pic"):
    #     current_pic_array = color_area_pic
    #     area_max_square = find_max_square(gray_area_pic)
    #     cv2.drawContours(current_pic_array,[area_max_square],-1,(0,255,255),1)
    #     show_pic(current_pic_array)

    with test("show number pic"):
        not_use,current_pic_array = cv2.threshold(gray_area_pic,255,0,0)
        area_max_square = find_max_square(gray_area_pic)
        indexs = cal_squre_area(area_max_square)
        ragion_indexs_arr = cal_split_ragion(*indexs)
        for cur_indexs in ragion_indexs_arr:
            current_pic_array[cur_indexs[0]:cur_indexs[1],cur_indexs[2]:cur_indexs[3]] = \
                gray_area_pic[cur_indexs[0]:cur_indexs[1],cur_indexs[2]:cur_indexs[3]]
        # cur_indexs = ragion_indexs_arr[3]
        # current_pic_array[cur_indexs[0]:cur_indexs[1],cur_indexs[2]:cur_indexs[3]] = \
        #     gray_area_pic[cur_indexs[0]:cur_indexs[1],cur_indexs[2]:cur_indexs[3]]
        # show_pic(current_pic_array)
